from django.urls import path
from .views import UrlApiView, UrlView

urlpatterns = [
    path('api/v1/url', UrlApiView.as_view()),
    path('<str:short_path>', UrlView.as_view()),
]