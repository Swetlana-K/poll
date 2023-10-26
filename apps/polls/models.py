
from django.db import models
from django.contrib import admin

# Umfrage 
class Poll(models.Model):
    title = models.CharField(max_length=255)
    creator_name = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_timestamp = self.timestamp.strftime("%d-%m-%Y")
        return f"{self.title} - {formatted_timestamp} - {self.creator_name}"

    class Meta:
        app_label = 'polls'

# Vorschlag für einen bestimmten Tag und eine bestimmte Uhrzeit innerhalb einer Umfrage.
class DateOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    date_proposal = models.DateField()
    time_proposal = models.TimeField()

    def __str__(self):
        formatted_date_proposal = self.date_proposal.strftime("%d-%m-%Y")
        return f" Vorschlag zu Abstimmung {str(self.poll.title)} - {formatted_date_proposal}"
    
    class Meta:
        app_label = 'polls'    

# Eine einzelne Stimme oder Abstimmung in Bezug auf einen bestimmten Vorschlag in einer Umfrage.
class Vote(models.Model):
    RESPONSE_CHOICES = [
        ('ja', 'Ja'),
        ('nein', 'Nein'),
        ('vielleicht', 'Vielleicht'),
    ]

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voter_name = models.CharField(max_length=255)
    date_option = models.ForeignKey(DateOption, on_delete=models.CASCADE)
    response_choice = models.CharField(max_length=10, choices=RESPONSE_CHOICES)

    def __str__(self):
        return f"{self.voter_name} - {self.response_choice}"

    class Meta:
        app_label = 'polls'

#  Eine Inline-Klasse für das Vote-Modell, die in der Admin-Oberfläche angezeigt wird, eine Umfrage bearbeitet wird. 
class VoteInline(admin.TabularInline): 
    model = Vote
    extra = 1
      
# Eine Admin-Klasse für das Poll-Modell, die die Konfiguration für die Anzeige in der Django-Admin-Oberfläche enthält.
class PollAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator_name', 'timestamp']
    inlines = [VoteInline]  # Fügt die Inline-Klasse hinzu

# Eine Admin-Klasse für das Vote-Modell, die die Konfiguration für die Anzeige in der Django-Admin-Oberfläche enthält.
class VoteAdmin(admin.ModelAdmin):
    list_display = ['poll_title', 'date_option_datetime', 'voter_name', 'response_choice']

    def poll_title(self, obj):
        return obj.poll.title

    def date_option_datetime(self, obj):
        return f"{obj.date_option.date_proposal} {obj.date_option.time_proposal}"

