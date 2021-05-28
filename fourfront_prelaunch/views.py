from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

class LandingPageView(TemplateView):
    template_name = "index.html"

class SurveyPageView(TemplateView):
    template_name = "survey.html"

def survey(request):
    if request.method == "POST":
        subscriber_email = request.POST["subscribe_email"]
        print(subscriber_email)
        return HttpResponseRedirect("/thank-you")

    return render(request, "survey.html")

def thank_you(request):
    return render(request, "thank_you.html")
