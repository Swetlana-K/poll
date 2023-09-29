
from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User  

class Poll(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        formatted_timestamp = self.timestamp.strftime("%d-%m-%Y")  # Formatieren von Datum und  Uhrzeit ohne Sekunden
        return f"{self.title} - {formatted_timestamp}"


class DateOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    date_proposal = models.DateField()
    time_proposal = models.TimeField()
    
    
    def __str__(self):
        formatted_date_proposal = self.date_proposal.strftime("%d-%m-%Y") 
        return f" Vorschlag zu Abstimmung {str(self.poll.title)} - {formatted_date_proposal}"

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_option = models.ForeignKey(DateOption, on_delete=models.CASCADE)
    response_choice = models.CharField(max_length=10, choices=[('ja', 'ja'), ('nein', 'nein'), ('vielleicht', 'vielleicht')])

    def __str__(self):
        return f"{str(self.poll.title)} - {self.user} - {self.response_choice}"