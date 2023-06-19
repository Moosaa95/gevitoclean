from django.urls import path
from .views import *


urlpatterns = [
    path("", LandingPageView.as_view(), name="index"),
    path("about", AboutPageView.as_view(), name="about"),
    path("contact", ContactPageView.as_view(), name="contact"),
    path("services", ServicePageView.as_view(), name="services"),
    path("trainings", TrainingPageView.as_view(), name="trainings"),
    path("service/<str:service_slug>/", ServiceDetailPageView.as_view(), name="service"),
    path("training/<str:training_slug>/", TrainingDetailPageView.as_view(), name="training"),
    # path("contact_form", ContactAPiView.as_view(), name="contact_form"),
]