from django.urls import path
from .views import LandingPageView

from . import views

urlpatterns = [
    path("", LandingPageView.as_view(), name="home"),
    path("survey", views.survey, name="survey"),
    path("thank-you", views.thank_you, name="thank-you"),

]