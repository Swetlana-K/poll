from django.test import TestCase
from django.urls import reverse
from apps.polls.models import Poll, DateOption, Vote

class PollViewsTest(TestCase):

    def setUp(self):
        # Erstelle Testdaten, die in den Tests verwendet werden
        self.poll = Poll.objects.create(title='Test Poll', creator_name='Test Creator')

    # Überprüft, ob die Startseite korrekt gerendert wird.
    def test_homepage_view(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'poll/home.html')

    # Überprüft, ob das Erstellen einer Umfrage erfolgreich ist.
    def test_create_poll_view(self):
        response = self.client.post(reverse('create_poll'), {'title': 'New Poll', 'creator_name': 'Max Mueller'})
        self.assertEqual(response.status_code, 302)  # Erwartete Umleitung nach dem Erstellen einer Umfrage
        self.assertEqual(Poll.objects.count(), 2)  # Zwei Umfragen (einschließlich der in setUp erstellten)

    # Überprüft, ob die Liste aller Umfragen korrekt gerendert wird.
    def test_view_polls_view(self):
        response = self.client.get(reverse('view_polls'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'poll/view_polls.html')
        self.assertIn(self.poll, response.context['polls'])  # Überprüfe, ob die erstellte Umfrage im Kontext vorhanden ist

    # Überprüft, ob das Abstimmen für eine Umfrage korrekt funktioniert.
    def test_vote_view(self):
        date_option = DateOption.objects.create(poll=self.poll, date_proposal='2023-01-01', time_proposal='12:00')
        response = self.client.post(reverse('vote', args=[self.poll.id]), {'voter_name': 'Anna', 'date_option_ids': [date_option.id], 'response_choice_' + str(date_option.id): 'ja'})
        self.assertEqual(response.status_code, 302)  # Erwartete Umleitung nach einer gültigen Abstimmung
        self.assertEqual(Vote.objects.count(), 1)  # Eine Stimme sollte in der Datenbank erstellt werden

    # Überprüft, ob die Detailansicht einer Umfrage korrekt gerendert wird.
    def test_view_poll_view(self):
        response = self.client.get(reverse('view_poll', args=[self.poll.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'poll/view_poll.html')
        self.assertEqual(self.poll, response.context['poll'])  # Überprüfe, ob die erstellte Umfrage im Kontext vorhanden ist
