from sys import exit as exiter
from SafeTrade.logging import LOGGER
from SafeTrade.config import REDIS_CACHE_TTL, REDIS_PORT, REDIS_URL

import redis
import json


class OrderHandler:
    def __init__(self, user_id):
        self.order_key = f"order:{user_id}"
        self.listed_order_key = f"listed_orders:{user_id}"
        self.redis_client = redis.StrictRedis(
            host=REDIS_URL, port=REDIS_PORT, decode_responses=True
        )

    async def set_order(self, data: dict):
        """
        setup an order for a user
        """
        serialized_data = json.dumps(data)

        self.redis_client.set(self.order_key, serialized_data)
        self.redis_client.expire(self.order_key, REDIS_CACHE_TTL)

    async def get_order(self):
        """
        get user orders
        """
        data = str(self.redis_client.get(self.order_key))
        return json.loads(data)

    async def update_order(self):
        """
        set order status to True
        it means the order has been completed
        """
        pass

    async def set_listed_order(self, data: dict):
        """
        setup listed cards for a user
        """
        serialized_data = json.dumps(data)

        self.redis_client.set(self.listed_order_key, serialized_data)
        self.redis_client.expire(self.listed_order_key, REDIS_CACHE_TTL)

    async def get_listed_order(self):
        """
        get users listed_orders
        """
        data = str(self.redis_client.get(self.listed_order_key))
        return json.loads(data)


async def check_redis_url(url: str, port: int) -> None:
    try:
        redis_client = redis.StrictRedis(
            host=url,
            port=port,
            decode_responses=True,
        )

        redis_client.client_id()
    except:
        LOGGER(__name__).error(  # type: ignore
            "Error in Establishing connection with Redis URL. Please enter valid url in the config section."
        )
        exiter(1)