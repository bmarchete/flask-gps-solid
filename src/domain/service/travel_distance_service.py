from domain.model.travel_distance import TravelDistance
from domain.ports.cache_storage import CacheStorageInterface
from domain.ports.travel_distance import TravelDistanceInterface
from domain.ports.travel_distance_repository import TravelDistanceRepositoryInterface
from domain.utils.retry_with_backoff import RetryLimitExceededException


class TravelDistanceServiceException(Exception):
    """Exception raised for errors in the TravelDistanceService.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="TravelDistanceService encountered an error"):
        self.message = message
        super().__init__(self.message)

class TravelDistanceService(TravelDistanceInterface):
    

    def __init__(self, travel_distance: TravelDistanceInterface = None, cache_storage: CacheStorageInterface = None, repository: TravelDistanceRepositoryInterface = None):
        self.travel_distance = travel_distance
        self.cache_storage = cache_storage
        self.travel_distance_repository = repository

    def _get_distance_from_cache(self, key) -> TravelDistance:
            print("Getting distance from cache")
            return self.cache_storage.get(key)
                
            
    def get_distance(self, origin, destination) -> TravelDistance:
            """
            Retrieves the travel distance between the given origin and destination.

            Args:
                origin (str): The origin location.
                destination (str): The destination location.

            Returns:
                TravelDistance: An object representing the travel distance between the origin and destination.
            """
            key = f"{origin}__{destination}"
            
            # This is where SOLID principles are hard to keep up with. The service should not be responsible for handling the cache.
            # A good solution would be to create a decorator that handles the cache. Another solution would be to create a separate class (CacheTravelDistanceService) that handles the cache.
            # Because of the overhead of creating a decorator or a separate class, sometimes it's acceptable to not follow this approach and keep the code simple.
            
            cached_distance = self._get_distance_from_cache(key)
            if cached_distance:
                result = TravelDistance(origin=origin, destination=destination, distance=cached_distance)
                return result
            
            try:
                result = self.travel_distance.get_distance(origin, destination)
                self.travel_distance_repository.create_travel_distance(result)
                self.cache_storage.set(key, result.distance, 60)

                return result

            except RetryLimitExceededException:
                result = self.travel_distance_repository.get_travel_distance(origin, destination)
                if result:
                    return result
                raise TravelDistanceServiceException
