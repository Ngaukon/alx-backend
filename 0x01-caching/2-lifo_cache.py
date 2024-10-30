#!/usr/bin/env python3
"""Last-In First-Out (LIFO) caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system that stores items up to a set limit, 
    discarding the most recent entry when the limit is exceeded.
    """
    
    def __init__(self):
        """Initializes the LIFO cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache; removes most recent if limit is reached."""
        if key is None or item is None:
            return
        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Retrieves an item by key."""
        return self.cache_data.get(key, None)
