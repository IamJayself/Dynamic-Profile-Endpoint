from django.contrib import admin
from django.urls import path
from api.views import me

urlpatterns = [
    path('admin/', admin.site.urls),
    path('me', me), 
]
