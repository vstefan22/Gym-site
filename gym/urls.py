from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('gym_app.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    

]