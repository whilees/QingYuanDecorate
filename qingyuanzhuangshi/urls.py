"""qingyuanzhuangshi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from rest_framework import routers
from supplier.views import *
from controller.views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'brand', BrandViewSet)
router.register(r'unit', UnitViewSet)
router.register(r'materialtype', MaterialTypeViewSet)
router.register(r'material', MaterialViewSet)
router.register(r'itemtype', ItemTypeViewSet)
router.register(r'client', ProjectViewSet)
router.register(r'project', ProjectViewSet)


urlpatterns = [
    url('controller/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
# urlpatterns = [
#     path('controller/', admin.site.urls),
#     path(r'^', include(router.urls)),
# ]
