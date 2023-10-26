
from django.contrib import admin
from .models import Poll, DateOption, Vote, PollAdmin, VoteAdmin


admin.site.register(DateOption)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Poll, PollAdmin)





