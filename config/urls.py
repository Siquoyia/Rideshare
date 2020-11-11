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
from rideshare import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', contacts_views.list_rideshare, name='list_rideshare'),
    path("", views.home, name='home')
    #path('rideshares/add/',rideshares_views.add_rideshare,name='add_rideshare'),
    #path('rideshares/<int:pk>/edit/',
         #rideshares_views.edit_rideshare,
         #name='edit_rideshare'),
    #path('rideshares/<int:pk>/delete/',
         #rideshares_views.delete_contact,
         #name='delete_rideshare'),
    #path('rideshares/<int:pk/', rideshares_views.rideshare_detail, name='rideshare_detail')     

]

