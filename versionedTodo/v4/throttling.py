from django.core.cache import caches
from rest_framework.throttling import AnonRateThrottle, BaseThrottle 
import random

class RandomRateThrottle(BaseThrottle):
    def allow_request(self, request, view):
        return random.randint(1,10) != 1