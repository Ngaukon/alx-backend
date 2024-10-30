#!/usr/bin/env python3
"""Most Recently Used (MRU) caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system that stores items up to a limit, 
    discarding the most recently used entry if the limit is exceeded.
    """
    
    def __init__(self):
        """Initializes the MRU cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache; removes MRU item if limit is reached."""
        if key is None or item is None:
            return
        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", mru_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Retrieves an item by key and marks it as MRU."""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
