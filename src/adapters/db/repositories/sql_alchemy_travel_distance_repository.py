from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from adapters.db.models.travel_distance_model import TravelDistanceModel
from domain.model.travel_distance import TravelDistance
from domain.ports.travel_distance_repository import TravelDistanceRepositoryInterface

class SQLAlchemyTravelDistanceRepository(TravelDistanceRepositoryInterface):
    """
    Repository class for managing travel distance data using SQLAlchemy.
    """

    def __init__(self, database) -> None:
        self.database = database
        print(f"Initialized SQLAlchemyTravelDistanceRepository with database: {self.database}")


    def _generate_id(self, origin: str, destination: str) -> str:
        return f"{origin}__{destination}"

    def create_travel_distance(self, travel_distance: TravelDistance) -> None:

        try:
            with sessionmaker(bind=self.database.engine)() as session:
                id = self._generate_id(travel_distance.origin, travel_distance.destination)
                model = TravelDistanceModel(id=id, origin=travel_distance.origin, destination=travel_distance.destination, distance=travel_distance.distance)
                
                session.merge(model)
                session.commit()
        except SQLAlchemyError as e:
            print(f"Error occurred during create: {e}")
            raise e

    def get_travel_distance(self, origin: str, destination: str) -> TravelDistance:
            
        try:
            with sessionmaker(bind=self.database.engine)() as session:
                id = self._generate_id(origin, destination)
                model = session.query(TravelDistanceModel).get(id)
                if model:
                    return TravelDistance(id=model.id, origin=model.origin, destination=model.destination, distance=model.distance)
                return None
        except SQLAlchemyError as e:
            print(f"Error occurred during get_travel_distance: {e}")
            raise e