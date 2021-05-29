from django import forms
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect

YNO_CHOICES=[
    ("yes", "Yes"),
    ("no", "No"),
    ("other", "Other"),
]

STARTUP=[
    ("no-proof", "Have an idea, no proof of concept"),
    ("proof", "Done proof of concept, not validated"),
    ("pre-rev", "Pre-Revenue"),
    ("rev", "Revenue"),
    ("val-comm", "Validated and committed"),
    ("other", "Other"),
]

ACCESS_FREQ=[
    ("always", "Always"),
    ("often", "Often"),
    ("occasionally", "Occasionally"),
    ("rarely", "Rarely"),
    ("never", "Never"),
    ("other", "Other"),
]

TECH_CHALLENGE=[
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
]

ROADBLOCKS=[
    ("tech-need", "Articulating your technology needs"),
    ("advice", "Having a single person of contact to give quality advice"),
    ("lack", "Lack of resources/money"),
    ("deadlines", "Meeting deadlines"),
    ("dev-agency", "Working with a dev agency"),
    ("other", "Other"),
]

TIMELINE=[
    ("within-4w", "Within 4 weeks"),
    ("within-1m", "Within 1 month"),
    ("within-3m", "Within 3 months"),
    ("within-6m", "Within 6 months"),
    ("within-1y", "Within 1 year"),
    ("other", "Other"),
]

class SurveyForm(forms.Form):
    # Q1
    tech_exp                        =   forms.ChoiceField(widget=forms.RadioSelect, choices=YNO_CHOICES)
    tech_exp_text                   =   forms.CharField(max_length=100, required=False)
    # Q2
    tech_founder                    =   forms.ChoiceField(widget=forms.RadioSelect, choices=YNO_CHOICES)
    tech_founder_text               =   forms.CharField(max_length=100, required=False)
    # Q3
    startup_stage                   =   forms.ChoiceField(widget=forms.RadioSelect, choices=STARTUP)
    startup_stage_text              =   forms.CharField(max_length=100, required=False)
    # Q4
    startup_description             =   forms.CharField(widget=forms.Textarea, max_length=500)
    # Q5
    access_freq                     =   forms.ChoiceField(widget=forms.RadioSelect, choices=ACCESS_FREQ)
    access_freq_text                =   forms.CharField(max_length=100, required=False)
    # Q6
    tech_challenge                  =   forms.ChoiceField(widget=forms.RadioSelect, choices=TECH_CHALLENGE)
    tech_challenge_description      =   forms.CharField(widget=forms.Textarea, max_length=500)
    # Q7
    roadblocks                      =   forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=ROADBLOCKS)
    roadblocks_text                 =   forms.CharField(max_length=100, required=False)
    # Q8
    timeline                        =   forms.ChoiceField(widget=forms.RadioSelect, choices=TIMELINE)
    timeline_description            =   forms.CharField(widget=forms.Textarea, max_length=500)
    # Q9
    subscriber_first_name           =   forms.CharField(max_length=100)
    subscriber_last_name            =   forms.CharField(max_length=100)
    subscriber_email                =   forms.EmailField(widget=forms.EmailInput, min_length=10)

