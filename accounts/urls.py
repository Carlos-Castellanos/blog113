from django.urls import path
from . import views


# from django.conf import settings


urlpatterns = [
    path("signup/", views.register_request, name="signup"),
    

]