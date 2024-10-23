"""This is a module that defines class cache as a first step to building our own cacheing
system"""
#!/usr/bin/python3
import redis # type: ignore
import uuid


class Cache:
    """Module defines cache and methods"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | int | float | bytes) -> str:
        randomKey = str(uuid.uuid4())
        # store input in _redis ande return key
        self._redis.set(randomKey, data)
        return randomKey
