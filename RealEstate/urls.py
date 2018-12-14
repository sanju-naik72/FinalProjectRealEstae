"""RealEstate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView

from appRE import views
from appRE.views import viewproperties

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.openHomePage),
    path('User/', views.openUserLogin),
    path('registerUser/',views.registerUser),

    path('checkUserLogin/', views.checkUserLogin),
    path('checkProfile/', views.checkProfile),

    path('updateProfile/', views.updateProfile),
    path('updatesave/', views.updatesave),
    path('deleteProperty/', views.deleteProperty),


    path('viewproperties/',viewproperties.as_view()),


    path('logout/', views.UserLogout),

    path('home/',views.openHomePage),
    path('about/',TemplateView.as_view(template_name="about-us.html")),
    path('blog/',TemplateView.as_view(template_name="blog.html")),
    path('agent/',TemplateView.as_view(template_name="agents.html")),
    path('elements/',TemplateView.as_view(template_name="elements.html")),
    path('properties/',TemplateView.as_view(template_name="properties.html")),
    path('single-blog/',TemplateView.as_view(template_name="single-blog.html")),
    path('contact/',TemplateView.as_view(template_name="contact.html")),



    path('addproperties/',views.addproperties),
    path('upropertysave/',views.upropertysave),
]
