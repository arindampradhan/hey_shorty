from tastypie.authorization import Authorization
from .redis_resource import RedisResource
from .models import Url
import redis


class UrlResource(RedisResource):

    """Api resource for Url"""
    class Meta:
        resource_name = "url"
        list_allowed_methods = ["delete", "get", "post"]
        authorization = Authorization()
        object_class = Url


    def get_database(self):
        import redis
        return redis.StrictRedis(host='localhost', port=6379, db=0)
