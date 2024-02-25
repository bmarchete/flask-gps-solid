import redis
from configuration.environment import env

class RedisFactory:
    """
    A singleton class that provides a Redis connection instance.

    This class ensures that only one instance of Redis connection is created and
    provides a static method to retrieve the instance.

    Attributes:
        _instance (redis.StrictRedis): The singleton instance of Redis connection.

    Methods:
        get_instance(): Returns the singleton instance of Redis connection.

    Raises:
        Exception: If an attempt is made to create multiple instances of RedisFactory.

    """

    _instance = None

    @staticmethod
    def get_instance():
        """
        Returns the singleton instance of Redis connection.

        Returns:
            redis.StrictRedis: The singleton instance of Redis connection.

        """
        if RedisFactory._instance is None:
            RedisFactory()
        return RedisFactory._instance

    def __init__(self):
        """
        Initializes the RedisFactory instance.

        Raises:
            Exception: If an attempt is made to create multiple instances of RedisFactory.
            ValueError: If REDIS_HOST or REDIS_PORT environment variables are not set.

        """
        if RedisFactory._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            REDIS_HOST = env.str('REDIS_HOST', 'localhost')
            REDIS_PORT = env.int('REDIS_PORT', 6379)
            REDIS_PASSWORD = env.str('REDIS_PASSWORD', '')
            if not all([REDIS_HOST, REDIS_PORT]):
                raise ValueError("REDIS_HOST or REDIS_PORT not set.")

            RedisFactory._instance = redis.StrictRedis(
                host=REDIS_HOST,
                port=REDIS_PORT,
                password=REDIS_PASSWORD,
                decode_responses=True,
            )
            try:
                RedisFactory._instance.ping()
                print("Redis connection is good.")
            except redis.exceptions.ConnectionError:
                print("Unable to connect to Redis.")
