from domain.model.travel_distance import TravelDistance
from domain.ports.travel_distance import TravelDistanceInterface
from domain.utils.retry_with_backoff import retry_with_backoff
from adapters.google_maps.google_maps_factory import GoogleMapsFactory

class GoogleMapsTravelDistanceService(TravelDistanceInterface):

    def __init__(self):
        self.client = GoogleMapsFactory.get_instance()

    @retry_with_backoff(retries=3, backoff_in_seconds=1)
    def get_distance(self, origin: str, destination: str) -> TravelDistance:
        """
        Calculates the travel distance between the given origin and destination.

        Args:
            origin (str): The starting location.
            destination (str): The destination location.

        Returns:
            TravelDistance: An object representing the travel distance.
        """
        result = self.client.directions(origin=origin, destination=destination)
        distance = sum(int(step['distance']['value']) for step in result[0]['legs'][0]['steps'])

        route = TravelDistance(origin=origin, destination=destination, distance=distance)
        return route