from django.shortcuts import render
from django.conf import settings
from django.http import *
from django.template import Context
import random
from redishortener.models import Url
URL_LENGTH = getattr(settings, "SHORT_URL_GENERATOR_LEN", None)


def index(request):
    random = None
    if request.POST:
        url = request.POST['url']
        short_url = random_string(URL_LENGTH)
        flag = Url.objects.filter(short_url=short_url)
        # check if short flag is already , I know it higly impossible !! just
        # for testing
        while flag:
            short_url = random_string(URL_LENGTH)  # short
            short_url = str(short_url)
            flag = Url.objects.filter(short_url=short_url)
        Url(long_url=url, short_url=short_url).save()  # db save
        return render(request, "redishortener/shorten.html", locals())
    return render(request, "redishortener/index.html", locals())


def random_string(length):
    options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_%&@"
    return "".join([random.choice(options) for i in range(length)])


def follow(request, url=None):
    if request.path == '/':
        return render(request, 'redishortener/index.html')
    try:
        print request.path[1:]
        url_obj = Url.objects.filter(short_url=str(request.path)[1:])[0]
        print url_obj.long_url
        long_url = str(url_obj.long_url)
        return HttpResponseRedirect(long_url)
    except:
        return render(request, 'redishortener/notfound.html')
