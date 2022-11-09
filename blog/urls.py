from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', asosiy),
    path('ferrari/', ferrary),
    path('mercedes/', mersedes),
    path('bmw/', bmv),
    path('toyota/', toyota),
    path('lada/', lada),
    path('nissan/', nissan),
]
