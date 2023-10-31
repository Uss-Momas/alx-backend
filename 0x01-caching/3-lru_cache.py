#!/usr/bin/env python3
"""
3-lru_cache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching class
    """

    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """Overriding the put method from BaseCaching
        Args:
            - key: key value for the dictionairy
            - item: item being associated with the key
        """
        if key and item:
            ...

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
