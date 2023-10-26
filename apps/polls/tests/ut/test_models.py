from django.test import TestCase
from apps.polls.models import Poll, DateOption, Vote
from django.utils import timezone
from datetime import date, time

class PollModelTests(TestCase):
    # Es erstellt ein Poll-Objekt mit einem Titel und einem Ersteller. Überprüft, ob der erstellte Poll die erwarteten Werte für Titel und Ersteller hat. Überprüft, ob das Attribut timestamp des Poll-Objekts ein Instanz von datetime aus dem timezone-Modul ist.
    def test_poll_creation(self):
        poll = Poll.objects.create(title='Test Poll', creator_name='Test Creator')
        self.assertEqual(poll.title, 'Test Poll')
        self.assertEqual(poll.creator_name, 'Test Creator')
        self.assertTrue(isinstance(poll.timestamp, timezone.datetime))

    # Es erstellt ein Poll-Objekt und ein DateOption-Objekt mit einem Datum und einer Zeit. Überprüft, ob das erstellte DateOption-Objekt das zugehörige Poll-Objekt referenziert. Überprüft, ob die Attribute date_proposal und time_proposal des erstellten DateOption-Objekts Instanzen von date bzw. time sind.
    def test_date_option_creation(self):
        poll = Poll.objects.create(title='Test Poll', creator_name='Test Creator')
        date_option = DateOption.objects.create(poll=poll, date_proposal=date.today(), time_proposal=time())
        self.assertEqual(date_option.poll, poll)
        self.assertTrue(isinstance(date_option.date_proposal, date))
        self.assertTrue(isinstance(date_option.time_proposal, time))

    #Es erstellt ein Poll-Objekt, ein DateOption-Objekt und ein Vote-Objekt mit einem Wähler, einer Auswahl und Verweisen auf das Poll- und DateOption-Objekt. Überprüft, ob das erstellte Vote-Objekt die erwarteten Werte für Wähler, Auswahl und Verweise auf das Poll- und DateOption-Objekt hat
    def test_vote_creation(self):
        poll = Poll.objects.create(title='Test Poll', creator_name='Test Creator')
        date_option = DateOption.objects.create(poll=poll, date_proposal=date.today(), time_proposal=time())
        vote = Vote.objects.create(poll=poll, voter_name='Test Voter', date_option=date_option, response_choice='ja')
        self.assertEqual(vote.poll, poll)
        self.assertEqual(vote.voter_name, 'Test Voter')
        self.assertEqual(vote.date_option, date_option)
        self.assertEqual(vote.response_choice, 'ja')
        
        