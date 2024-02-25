import googlemaps
from configuration.environment import env

class GoogleMapsFactory:
    __instance = None

    @staticmethod
    def get_instance():
        if GoogleMapsFactory.__instance is None:
            GoogleMapsFactory()
        return GoogleMapsFactory.__instance

    def __init__(self):
        if GoogleMapsFactory.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GOOGLE_MAPS_API_KEY = env.str('GOOGLE_MAPS_API_KEY', '')
            GoogleMapsFactory.__instance = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

