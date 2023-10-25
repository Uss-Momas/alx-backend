#!/usr/bin/env python3
"""
1-fifo_cache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching class
    """

    def __init__(self):
        """class constructor"""
        super().__init__()

    def put(self, key, item):
        """Overriding the put method from BaseCaching
        Args:
            - key: key value for the dictionairy
            - item: item being associated with the key
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]

    def get(self, key):
        """Overriding the get method from BaseCaching
        Args:
            - key: key containing the target value
        return:
            - the value associated with the key, or None if key doesnt exist
        """
        # if key is not None
        if key:
            return self.cache_data.get(key)
        return None
