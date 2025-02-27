"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static 


# Your views (Make sure these are imported)
from myapp.views import signup, loginpage, home, logoutpage, addemployee, viewemployee, deleteemployee, editemployee, updateemployee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signup, name='signup'),
    path('login', loginpage, name='login'),
    path('home', home, name='home'),
    path('logout', logoutpage, name='logout'),
    path('addemployee', addemployee, name='addemployee'),
    path('viewemployee', viewemployee, name='viewemployee'),
    path('deleteemployee/<int:empid>', deleteemployee, name='deleteemployee'),
    path('editemployee/<int:empid>', editemployee, name='editemployee'),
    path('updateemployee/<int:empid>', updateemployee, name='updateemployee'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

