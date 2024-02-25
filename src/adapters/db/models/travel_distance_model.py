from sqlalchemy import Column, String, Integer
from typing import Dict
from adapters.db.sql_alchemy_factory import db

class TravelDistanceModel(db.Model):
    """
    Represents a travel distance between two locations.
    """

    __tablename__ = 'travel_distance'

    id = Column(String(255), primary_key=True)
    origin = Column(String(255), nullable=False)
    destination = Column(String(255), nullable=False)
    distance = Column(Integer, nullable=False)
      

    def to_dict(self) -> Dict[str, str]:
        """
        Converts the TravelDistanceModel object to a dictionary.

        Returns:
            A dictionary representation of the TravelDistanceModel object.
        """
        return {
            "id": self.id,
            "origin": self.origin,
            "destination": self.destination,
            "distance": self.distance
        }
