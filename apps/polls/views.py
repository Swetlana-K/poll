
from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, DateOption, Vote  
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from collections import defaultdict

# Startseite der Anwendung
def homepage(request):
    return render(request, 'poll/home.html')

# Erstellt eine neue Umfrage basierend auf den Benutzereingaben.
def create_poll(request):
    if request.method == 'POST':
        title = request.POST['title']
        creator_name = request.POST['creator_name']  

        # Erstellen des Poll-Objekts und Zuweisen des Erstellernamens
        poll = Poll.objects.create(title=title, creator_name=creator_name)

        date_proposals = request.POST.getlist('date_proposals[]')
        time_proposals = request.POST.getlist('time_proposals[]')

        for date, time in zip(date_proposals, time_proposals):
            DateOption.objects.create(
                poll=poll, date_proposal=date, time_proposal=time)

        messages.success(request, 'Umfrage erfolgreich erstellt.')
        return redirect('view_polls')

    return render(request, 'poll/create_poll.html')

# Zeigt eine Liste aller Umfragen an.
def view_polls(request):
    polls = Poll.objects.all()
    return render(request, 'poll/view_polls.html', {'polls': polls})

#  Ermöglicht Benutzern das Abstimmen für eine bestimmte Umfrage.
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

    voter_name = request.POST.get('voter_name', '')

    if request.method == 'POST':
        date_option_ids = request.POST.getlist('date_option_ids')
        for date_option_id in date_option_ids:
            response_choice = request.POST.get(
                'response_choice_' + date_option_id)
            date_option = get_object_or_404(DateOption, pk=date_option_id)

            Vote.objects.create(poll=poll, voter_name=voter_name,
                                date_option=date_option, response_choice=response_choice)

        messages.success(request, 'Ihre Abstimmung wurde erfasst.')
        return redirect('view_poll', poll_id=poll.id)

    date_options = DateOption.objects.filter(poll=poll)
    return render(request, 'poll/vote.html', {'poll': poll, 'date_options': date_options, 'voter_name': voter_name})

#  Zeigt detaillierte Informationen zu einer bestimmten Umfrage an, einschließlich der Abstimmungsergebnisse. Erstellt Strukturen für die tabellarische Darstellung der Daten.
def view_poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

    # Voter-Namen für die Umfrage
    voter_names = Vote.objects.filter(
        poll=poll).values('voter_name').distinct()

    # Daten für die tabellarische Darstellung
    user_votes = defaultdict(dict)

    for voter_name in voter_names:
        votes_for_user = Vote.objects.filter(
            poll=poll, voter_name=voter_name['voter_name'])
        for vote in votes_for_user:
            user_votes[voter_name['voter_name']
                       ][vote.date_option] = vote.response_choice

    date_options = DateOption.objects.filter(poll=poll)
    
    creator_name = poll.creator_name

    date_choices = {}

    for date_option in date_options:
        votes_for_date = Vote.objects.filter(
            poll=poll, date_option=date_option)
        date_choices[date_option] = {
            vote.voter_name: vote.response_choice for vote in votes_for_date}

    voter_responses = {}

    for date_option, response_choices in date_choices.items():
        for voter_name, response_choice in response_choices.items():
            if voter_name not in voter_responses:
                voter_responses[voter_name] = {}

            voter_responses[voter_name][date_option] = response_choice
            
            
    date_choices_sum = {}

    for date_option in date_options:
        votes_for_date = Vote.objects.filter(
            poll=poll, date_option=date_option)
        date_choices_sum[date_option] = {
            'votes': {vote.voter_name: vote.response_choice for vote in votes_for_date},
            'sum_of_yes': sum(1 for vote in votes_for_date if vote.response_choice == 'ja')
        }
    
    return render(request, 'poll/view_poll.html', {'poll': poll, 'user_votes': user_votes, 'date_options': date_options, 'creator_name': creator_name, 'date_choices': date_choices, 'voter_responses': voter_responses, 'date_choices_sum': date_choices_sum, })
