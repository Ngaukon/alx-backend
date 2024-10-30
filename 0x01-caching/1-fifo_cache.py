#!/usr/bin/env python3
"""First-In First-Out (FIFO) caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system that stores items up to a set limit, 
    removing the oldest entry when the limit is exceeded.
    """
    
    def __init__(self):
        """Initializes the FIFO cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache; removes oldest if limit is reached."""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by its key."""
        return self.cache_data.get(key, None)
