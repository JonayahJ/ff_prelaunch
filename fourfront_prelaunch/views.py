from django.views.generic import TemplateView

# Create your views here.

class LandingPageView(TemplateView):
    template_name = "index.html"

class SurveyPageView(TemplateView):
    template_name = "survey.html"