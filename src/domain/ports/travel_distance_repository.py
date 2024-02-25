
from abc import ABC, abstractmethod

from domain.model.travel_distance import TravelDistance

class TravelDistanceRepositoryInterface(ABC):
    """
    Interface for a travel distance repository.
    """

    @abstractmethod
    def create_travel_distance(self, travel_distance: TravelDistance) -> None:
        """
        Create a travel distance record.

        Args:
            travel_distance (TravelDistance): The travel distance object to be created.

        Returns:
            None
        """
        pass # pragma: no cover

    @abstractmethod
    def get_travel_distance(self, origin: str, destination: str) -> TravelDistance:
        """
        Get the travel distance between two locations.

        Args:
            origin (str): The origin location.
            destination (str): The destination location.

        Returns:
            TravelDistance: The travel distance object.
        """
        pass # pragma: no cover