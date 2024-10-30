#!/usr/bin/env python3
"""Basic caching module implementing a simple key-value store.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Cache class that allows storing and retrieving items in a dictionary.
    Inherits from BaseCaching and provides basic cache operations.
    """
    
    def put(self, key, item):
        """Adds an item to the cache with the specified key.
        
        Args:
            key (str): The key under which to store the item.
            item (Any): The item to be stored in the cache.
        
        Note:
            If either key or item is None, the method does nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache by its key.
        
        Args:
            key (str): The key of the item to retrieve.
        
        Returns:
            Any: The item associated with the key, or None if the key is not found.
        """
        return self.cache_data.get(key, None)

