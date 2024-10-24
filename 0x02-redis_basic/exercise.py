#!/usr/bin/python3
"""This is a module that defines class cache as a first
step to building our own cacheing system"""
import uuid
import redis  # type: ignore


class Cache:
    """Module defines cache and methods"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | int | float | bytes) -> str:
        """method generates a random key and strores the data into redis"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
