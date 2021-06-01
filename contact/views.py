from django.shortcuts import redirect, render
from .models import Survey
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

def survey(request):
    if request.method == 'POST':
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
        timeline_text = request.POST["timeline_text"],
        subscriber_first_name = request.POST["subscriber_first_name"],
        subscriber_last_name = request.POST["subscriber_last_name"],
        subscriber_email = request.POST["subscriber_email"]

        survey = Survey(
            tech_exp=tech_exp, 
            tech_exp_text=tech_exp_text, 
            tech_founder=tech_founder, 
            tech_founder_text=tech_founder_text, 
            startup_stage=startup_stage, 
            startup_stage_text=startup_stage_text, 
            startup_description=startup_description, 
            access_freq=access_freq, 
            access_freq_text=access_freq_text, 
            tech_challenge=tech_challenge, 
            tech_challenge_description=tech_challenge_description, 
            roadblocks=roadblocks, 
            roadblocks_text=roadblocks_text, 
            timeline=timeline, 
            timeline_text=timeline_text, 
            subscriber_first_name=subscriber_first_name, 
            subscriber_last_name=subscriber_last_name, 
            subscriber_email=subscriber_email)

        admin_info = User.objects.get(is_superuser = True)
        admin_email = admin_info.email
        send_mail(
            'You have a new survey waiting for you!',
            'A potential client or interested party submitted a survey on the prelaunch site.  Please login to the admin panel to see more details.',
            'support@fourfront.io',
            [admin_email],
            fail_silently=False,
        )

        survey.save()
        return redirect("/thank-you")