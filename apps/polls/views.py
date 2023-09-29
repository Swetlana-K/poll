
from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, DateOption, Vote
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from collections import Counter

def homepage(request):
    return render(request, 'poll/home.html')


def create_poll(request):
    if request.method == 'POST':
        
        title = request.POST['title']

        poll = Poll.objects.create(title=title, user=request.user)

        date_proposals = request.POST.getlist('date_proposals[]')  
        time_proposals = request.POST.getlist('time_proposals[]')
        
        for date, time in zip(date_proposals, time_proposals):
            DateOption.objects.create(poll=poll, date_proposal=date, time_proposal=time)

        messages.success(request, 'Poll created successfully.')
        return redirect('view_polls') 

    return render(request, 'poll/create_poll.html')

def view_polls(request):
    polls = Poll.objects.all()
    return render(request, 'poll/view_polls.html', {'polls': polls})



def view_poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    votes = Vote.objects.filter(poll=poll)
    
    # Zählen der "Ja"-Stimmen
    total_yes_votes = votes.filter(response_choice='ja').count()
    
    # Zählen der Ergebnisse für alle Nutzer
    vote_choices = [vote.response_choice for vote in votes]
    vote_counts = Counter(vote_choices)
    
    return render(request, 'poll/view_poll.html', {'poll': poll, 'total_yes_votes': total_yes_votes, 'vote_counts': vote_counts})


def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

    if request.method == 'POST':
        # Überprüfen ob der Benutzer bereits abgestimmt hat
        user_has_voted = Vote.objects.filter(poll=poll, user=request.user).exists()

        if not user_has_voted:
            # Holen der ausgewählten Abstimmungsoption aus dem POST-Daten
            date_option_id = request.POST.get('date_option_id')
            response_choice = request.POST.get('response_choice_' + date_option_id)

            date_option = get_object_or_404(DateOption, pk=date_option_id)

            # Erstellen einer neue Abstimmung
            Vote.objects.create(poll=poll, user=request.user, date_option=date_option, response_choice=response_choice)

            messages.success(request, 'Ihre Abstimmung wurde erfasst.')
        else:
            messages.error(request, 'Sie haben bereits abgestimmt.')

        return redirect('view_polls')  # Weiterleitung zur Umfragenliste

    date_options = DateOption.objects.filter(poll=poll)
    return render(request, 'poll/vote.html', {'poll': poll, 'date_options': date_options})



