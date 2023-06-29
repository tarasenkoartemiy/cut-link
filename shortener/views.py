from django.views import View
from rest_framework.generics import CreateAPIView
from .serializers import UrlSerializer


class UrlView(View):
    def get(self, request, short_path):
        pass


class UrlApiView(CreateAPIView):
    serializer_class = UrlSerializer
