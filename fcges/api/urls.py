from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from trading import views

app_name = 'trading'

router = DefaultRouter()

router.register(r'api/orders', views.OrderBlockViewSet, basename="trading")

swagger_view = get_swagger_view(title='Trading OrderBlock API')

urlpatterns = [
    re_path(r'^$', swagger_view),
]

urlpatterns += router.urls

