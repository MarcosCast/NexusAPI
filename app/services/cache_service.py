import redis
from app.core.nexus_config import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

def set_cache(key: str, value: str, expire: int = 60):
    redis_client.setex(key, expire, value)

def get_cache(key: str):
    return redis_client.get(key)
