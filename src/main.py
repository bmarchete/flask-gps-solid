from adapters.api.factory import create
from adapters.db.sql_alchemy_factory import SQLAlchemyConfig, db
from adapters.cache.redis_factory import RedisFactory
from adapters.google_maps.google_maps_factory import GoogleMapsFactory

app = create()
app.config.from_object(SQLAlchemyConfig)

db.init_app(app)

# Initiate Redis connection
RedisFactory.get_instance()

#Initiate Google Maps API
GoogleMapsFactory.get_instance()


# Migrate database based on registered
with app.app_context():
    db.create_all()


# Serve API at port 1911
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1911)
