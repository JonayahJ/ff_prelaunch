# Generated by Django 3.2.3 on 2021-06-01 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech_exp', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('other', 'Other')], max_length=50)),
                ('tech_exp_text', models.CharField(blank=True, max_length=255)),
                ('tech_founder', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('other', 'Other')], max_length=50)),
                ('tech_founder_text', models.CharField(blank=True, max_length=255)),
                ('startup_stage', models.CharField(choices=[('no-proof', 'Have an idea, no proof of concept'), ('proof', 'Done proof of concept, not validated'), ('pre-rev', 'Pre-Revenue'), ('rev', 'Revenue'), ('val-comm', 'Validated and committed'), ('other', 'Other')], max_length=50)),
                ('startup_stage_text', models.CharField(blank=True, max_length=255)),
                ('startup_description', models.TextField(max_length=500)),
                ('access_freq', models.CharField(choices=[('always', 'Always'), ('often', 'Often'), ('occasionally', 'Occasionally'), ('rarely', 'Rarely'), ('never', 'Never'), ('other', 'Other')], max_length=50)),
                ('access_freq_text', models.CharField(blank=True, max_length=255)),
                ('tech_challenge', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50)),
                ('tech_challenge_description', models.TextField(max_length=500)),
                ('roadblocks', models.CharField(choices=[('tech-need', 'Articulating your technology needs'), ('advice', 'Having a single person of contact to give quality advice'), ('lack', 'Lack of resources/money'), ('deadlines', 'Meeting deadlines'), ('dev-agency', 'Working with a dev agency'), ('other', 'Other')], max_length=50)),
                ('roadblocks_text', models.CharField(blank=True, max_length=255)),
                ('timeline', models.CharField(choices=[('within-4w', 'Within 4 weeks'), ('within-1m', 'Within 1 month'), ('within-3m', 'Within 3 months'), ('within-6m', 'Within 6 months'), ('within-1y', 'Within 1 year'), ('other', 'Other')], max_length=50)),
                ('timeline_description', models.TextField(max_length=500)),
                ('subscriber_first_name', models.CharField(max_length=100)),
                ('subscriber_last_name', models.CharField(max_length=100)),
                ('subscriber_email', models.EmailField(max_length=100)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
