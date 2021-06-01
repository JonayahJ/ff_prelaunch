from django.db import models
from datetime import datetime

# Create your models here.

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

class Survey(models.Model):
    # Q1
    tech_exp                        =   models.CharField(max_length=50, choices=YNO_CHOICES)
    tech_exp_text                   =   models.CharField(max_length=255, blank=True)
    # Q2
    tech_founder                    =   models.CharField(max_length=50, choices=YNO_CHOICES)
    tech_founder_text               =   models.CharField(max_length=255, blank=True)
    # Q3
    startup_stage                   =   models.CharField(max_length=50, choices=STARTUP)
    startup_stage_text              =   models.CharField(max_length=255, blank=True)
    # Q4
    startup_description             =   models.TextField(max_length=500)
    # Q5
    access_freq                     =   models.CharField(max_length=50, choices=ACCESS_FREQ)
    access_freq_text                =   models.CharField(max_length=255, blank=True)
    # Q6
    tech_challenge                  =   models.CharField(max_length=50, choices=TECH_CHALLENGE)
    tech_challenge_description      =   models.TextField(max_length=500)
    # Q7
    roadblocks                      =   models.CharField(max_length=50, choices=ROADBLOCKS)
    roadblocks_text                 =   models.CharField(max_length=255, blank=True)
    # Q8
    timeline                        =   models.CharField(max_length=50, choices=TIMELINE)
    timeline_text                   =   models.CharField(max_length=255, blank=True)
    # Q9
    subscriber_first_name           =   models.CharField(max_length=100)
    subscriber_last_name            =   models.CharField(max_length=100)
    subscriber_email                =   models.EmailField(max_length=100)
    # Other
    created_at                      =   models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.subscriber_email
