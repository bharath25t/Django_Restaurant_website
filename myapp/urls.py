from .views import *
from django.urls import path # type: ignore


urlpatterns=[
    path("about",about),
    path("home",home),
    path("service",service),
    path("contact",contact),
    path("forms",disp_form)

    # path("home",home)
]
