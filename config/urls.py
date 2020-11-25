"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from rideshare import views as rideshare_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rideshares/list/', rideshare_views.list_rideshares, name='list_rideshares.html'),
    path("", rideshare_views.home, name='home'),
    path('rideshares/add/',rideshare_views.add_rideshare,name='add_rideshare'),
    path('rideshares/booked/',rideshare_views.booked_ride,name='booked_rideshare'),
         

]

