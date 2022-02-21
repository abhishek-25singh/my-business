from django.conf.urls import include
from .views import CustomerViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
from django.urls import re_path as url

router = DefaultRouter()
router.register("customer", CustomerViewSet, basename="customer")
router.register("user", UserViewSet, basename="user")

urlpatterns = [
    url('', include(router.urls))
]
