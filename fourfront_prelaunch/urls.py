from django.urls import path
from .views import LandingPageView, SurveyPageView

urlpatterns = [
    path("", LandingPageView.as_view(), name="home"),
    path("survey", SurveyPageView.as_view(), name="survey"),
]