#!/usr/bin/env python3
"""
2-lifo_cache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching class
    """

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Overriding the put method from BaseCaching
        Args:
            - key: key value for the dictionairy
            - item: item being associated with the key
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # after adding the new item, the last added
                # element is in the second last position
                last_key = list(self.cache_data.keys())[-2]
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]

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
