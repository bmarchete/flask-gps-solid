from adapters.db.repositories.sql_alchemy_travel_distance_repository import SQLAlchemyTravelDistanceRepository
from adapters.db.sql_alchemy_factory import db

sqlAlchemyTravelDistanceRepository = SQLAlchemyTravelDistanceRepository(database=db)