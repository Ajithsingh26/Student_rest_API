from django.conf.urls import include, url 
from django.contrib import admin
from .router import router
from django.urls import path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]