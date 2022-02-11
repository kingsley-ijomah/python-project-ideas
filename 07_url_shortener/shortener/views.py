import random
import string

from django.shortcuts import get_object_or_404, redirect, render

from .models import URLs


def home(request):
    return render(request, "shortener/index.html")


def short(request):
    url = request.POST["url"]

    try:
        while True:
            # keep generating new url until it is unique
            shortURL = short_url()
            # keep trying until exception is thrown
            URLs.objects.get(shortURL=shortURL)
    except URLs.DoesNotExist:
        # now we are sure URL is unique, save it!
        URLs(shortURL=shortURL, longURL=url).save()

    return render(request, "shortener/index.html", context={"shortURL": shortURL})


def redirect_short_url(request, shortURL):
    url = get_object_or_404(URLs, shortURL=shortURL)
    return redirect(url.longURL)


def short_url():
    url = ""
    string_digits = string.ascii_letters + string.digits

    for i in range(7):
        url += random.choice(string_digits)

    return url
