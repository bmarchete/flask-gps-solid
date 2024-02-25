from typing import Any
from domain.ports.cache_storage import CacheStorageInterface
from adapters.cache.redis_factory import RedisFactory

class RedisCacheStorage(CacheStorageInterface):
    """
    RedisCacheStorage is a class that implements the CacheStorageInterface
    and provides methods for interacting with Redis cache.

    Args:
        prefix (str): Optional. Prefix to be added to cache keys.

    Attributes:
        redis_client: The Redis client used for cache operations.
        key_prefix (str): The prefix to be added to cache keys.

    """

    def __init__(self, prefix: str = ''):
        self.redis_client = RedisFactory.get_instance()
        self.key_prefix = prefix

    def get(self, key: str) -> str:
        """
        Retrieves the value associated with the given key from the Redis cache.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            str: The value associated with the key, or None if the key does not exist.

        """
        return self.redis_client.get(self.key_prefix + '__' + key)

    def set(self, key: str, value: Any, expiration: int = 60) -> None:
        """
        Sets the value associated with the given key in the Redis cache.

        Args:
            key (str): The key to set the value for.
            value (Any): The value to be stored in the cache.
            expiration (int): Optional. The expiration time in seconds for the cache entry.

        Returns:
            None

        """
        self.redis_client.setex(self.key_prefix + '__' + key, expiration, value)

    def delete(self, key: str) -> None:
        """
        Deletes the cache entry associated with the given key from the Redis cache.

        Args:
            key (str): The key to delete the cache entry for.

        Returns:
            None

        """
        self.redis_client.delete(self.key_prefix + '__' + key)

    