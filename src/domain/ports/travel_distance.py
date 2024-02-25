
from abc import ABC, abstractmethod
from domain.model.travel_distance import TravelDistance

class TravelDistanceInterface(ABC):
    """Interface for calculating travel distance between two locations."""

    @abstractmethod
    def get_distance(self, origin: str, destination: str) -> TravelDistance:
        """Calculate the travel distance between the given origin and destination.

        Args:
            origin (str): The starting location.
            destination (str): The destination location.

        Returns:
            TravelDistance: The calculated travel distance.
        """
        pass # pragma: no cover