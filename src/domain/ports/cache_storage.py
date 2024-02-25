
from abc import ABC, abstractmethod

class CacheStorageInterface(ABC):
    """
    Interface for cache storage.

    This interface defines the methods that should be implemented by a cache storage class.
    """

    @abstractmethod
    def get(self, key: str) -> str:
        """
        Retrieve the value associated with the given key from the cache.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            str: The value associated with the key, or None if the key does not exist in the cache.
        """
        pass # pragma: no cover

    @abstractmethod
    def set(self, key: str, value: str, expiration: int = 1) -> None:
        """
        Set the value associated with the given key in the cache.

        Args:
            key (str): The key to set the value for.
            value (str): The value to be stored in the cache.
            expiration (int, optional): The expiration time in seconds for the key-value pair. Defaults to 1 second.
        """
        pass # pragma: no cover

    