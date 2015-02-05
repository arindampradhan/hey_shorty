from tastypie.authorization import Authorization
from tastypie_redis.resources import RedisResource
from .models import Url


class UrlResource(RedisResource):

    """Api resource for Url"""
    class Meta:
        resource_name = "url"
        list_allowed_methods = ["delete", "get", "post"]
        authorization = Authorization()
        object_class = Url
