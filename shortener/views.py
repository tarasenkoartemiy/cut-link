from django.views import View
from rest_framework.generics import CreateAPIView
from .serializers import UrlSerializer
from .models import Url
from django.shortcuts import get_object_or_404, redirect
from django.core.cache import cache


class UrlView(View):
    def get(self, request, short_path):
        obj = get_object_or_404(Url, short_path=short_path)
        cache.get_or_set(short_path, 0, timeout=None)
        cache.incr(short_path)
        return redirect(obj.original_url)


class UrlApiView(CreateAPIView):
    serializer_class = UrlSerializer
