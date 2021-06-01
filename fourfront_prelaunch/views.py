from datetime import time
from fourfront_prelaunch.models import Survey
from fourfront_prelaunch.forms import SurveyForm
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Survey

from . forms import SurveyForm

# Create your views here.

class LandingPageView(TemplateView):
    template_name = "index.html"

def survey(request):
    if request.method == "POST":
        # form = SurveyForm(request.POST)

        # if form.is_valid():
        #     survey = Survey(
        tech_exp = request.POST["tech_exp"],
        tech_exp_text = request.POST["tech_exp_text"],
        tech_founder = request.POST["tech_founder"],
        tech_founder_text = request.POST["tech_founder_text"],
        startup_stage = request.POST["startup_stage"],
        startup_stage_text = request.POST["startup_stage"],
        startup_description = request.POST["startup_description"],
        access_freq = request.POST["access_freq"],
        access_freq_text = request.POST["access_freq_text"],
        tech_challenge = request.POST["tech_challenge"],
        tech_challenge_description = request.POST["tech_challenge_description"],
        roadblocks = request.POST["roadblocks"],
        roadblocks_text = request.POST["roadblocks_text"],
        timeline = request.POST["timeline"],
        timeline_description = request.POST["timeline_description"],
        subscriber_first_name = request.POST["subscriber_first_name"],
        subscriber_last_name = request.POST["subscriber_last_name"],
        subscriber_email = request.POST["subscriber_email"]

        survey = Survey(tech_exp=tech_exp, tech_exp_text=tech_exp_text, tech_founder=tech_founder, tech_founder_text=tech_founder_text, startup_stage=startup_stage, startup_stage_text=startup_stage_text, startup_description=startup_description, access_freq=access_freq, access_freq_text=access_freq_text, tech_challenge=tech_challenge, tech_challenge_description=tech_challenge_description, roadblocks=roadblocks, roadblocks_text=roadblocks_text, timeline=timeline, timeline_description=timeline_description, subscriber_first_name=subscriber_first_name, subscriber_last_name=subscriber_last_name, subscriber_email=subscriber_email)

        survey.save()
        return HttpResponseRedirect("/thank-you")
            # )
    #         survey.save()
    #         return HttpResponseRedirect("/thank-you")

    else:
        form = SurveyForm()
    
    return render(request, "survey.html", {
        "form": form
    })

def thank_you(request):
    return render(request, "thank_you.html")
