from fourfront_prelaunch.forms import SurveyForm
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect

# from . forms import SurveyForm

# Create your views here.

class LandingPageView(TemplateView):
    template_name = "index.html"

class SurveyPageView(TemplateView):
    template_name = "survey.html"

def survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")

    else:
        form = SurveyForm()
    
    return render(request, "survey.html", {
        "form": form
    })

def thank_you(request):
    return render(request, "thank_you.html")
