from flask import jsonify
from flask_pydantic import validate
from adapters.api.dtos.travel_distance_query import TravelDistanceQuery
from adapters.cache.redis_cache_storage import RedisCacheStorage
from adapters.google_maps.services.google_maps_travel_distance_service import GoogleMapsTravelDistanceService
from domain.service.travel_distance_service import TravelDistanceService, TravelDistanceServiceException
from adapters.db.sql_alchemy_repositories import sqlAlchemyTravelDistanceRepository

@validate()
def get_travel_distance(query: TravelDistanceQuery):

    try:
        origin = query.origin
        destination = query.destination

        # Flask is not able to handle dependency injection by design. We have to create the service here until we setup a DI container.
        # Once the DI container is setup, the refactor is straightforward.
        g = TravelDistanceService(travel_distance=GoogleMapsTravelDistanceService(),cache_storage=RedisCacheStorage(prefix="travel_distance"),repository=sqlAlchemyTravelDistanceRepository)
        result = g.get_distance(origin, destination)
        return result.to_dict(), 200
       
    except TravelDistanceServiceException:
        return jsonify({"error": "We were not able to process your request"}), 401
    except Exception as e:
        print(e)
        return jsonify({"error": "Internal Server Error"}), 500
