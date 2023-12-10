from django.urls import reverse
from rest_framework.test import APITestCase
from users.models import User
from atomic_habits.models import Habit


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test_user@app.com')
        self.user.set_password('1')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            location='test',
            time='00:00:00',
            action='test',
            is_nice_habit=False,
            periodicity=1,
            reward='test',
            time_to_complete=120,
            is_public=True,
        )

    def test_public_habits(self):
        response = self.client.get(reverse('atomic_habits:public_habits'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         [{
                             'owner': self.user.id,
                             'id': self.habit.id,
                             'location': self.habit.location,
                             'time': self.habit.time,
                             'action': self.habit.action,
                             'is_nice_habit': self.habit.is_nice_habit,
                             'related_habit': self.habit.related_habit,
                             'periodicity': self.habit.periodicity,
                             'reward': self.habit.reward,
                             'time_to_complete': self.habit.time_to_complete,
                             'is_public': self.habit.is_public,
                         }])

    def test_list_of_habits(self):
        response = self.client.get(reverse('atomic_habits:list_of_habits'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             'count': 1,
                             'next': None,
                             'previous': None,
                             'results': [
                                 {
                                     'id': self.habit.id,
                                     'owner': self.user.id,
                                     'location': self.habit.location,
                                     'time': self.habit.time,
                                     'action': self.habit.action,
                                     'is_nice_habit': self.habit.is_nice_habit,
                                     'periodicity': self.habit.periodicity,
                                     'related_habit': self.habit.related_habit,
                                     'reward': self.habit.reward,
                                     'time_to_complete': self.habit.time_to_complete,
                                     'is_public': self.habit.is_public,
                                 }
                             ]
                         })

    def test_show_habit(self):
        response = self.client.get(reverse('atomic_habits:show_habit', args=[self.habit.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             'id': self.habit.id,
                             'owner': self.user.id,
                             'location': self.habit.location,
                             'time': self.habit.time,
                             'action': self.habit.action,
                             'is_nice_habit': self.habit.is_nice_habit,
                             'periodicity': self.habit.periodicity,
                             'related_habit': self.habit.related_habit,
                             'reward': self.habit.reward,
                             'time_to_complete': self.habit.time_to_complete,
                             'is_public': self.habit.is_public,
                         })

    def test_create_a_habit(self):
        data = {
            'owner': self.user.id,
            'location': 'second_test',
            'time': '01:00:00',
            'action': 'second_test',
            'is_nice_habit': True,
            'periodicity': 1,
            'reward': '',
            'time_to_complete': 120,
            'is_public': True,
        }
        response = self.client.post(reverse('atomic_habits:create_a_habit'), data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Habit.objects.count(), 2)

    def test_edit_habit(self):
        data = {
            'owner': self.user.id,
            'location': 'Тестовое место изменён',
            'time': '18:00:00',
            'action': 'Тестовое действие изменён',
            'is_nice_habit': True,
            'periodicity': 1,
            'time_to_complete': 50,
            'is_public': True,
        }
        response = self.client.put(reverse('atomic_habits:edit_habit', args=[self.habit.id]), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             'owner': self.user.id,
                             'id': self.habit.id,
                             'location': data['location'],
                             'time': data['time'],
                             'action': data['action'],
                             'is_nice_habit': data['is_nice_habit'],
                             'related_habit': self.habit.related_habit,
                             'periodicity': data['periodicity'],
                             'reward': self.habit.reward,
                             'time_to_complete': data['time_to_complete'],
                             'is_public': data['is_public'],
                         })

    def test_delete_habit(self):
        response = self.client.delete(reverse('atomic_habits:delete_habit', args=[self.habit.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Habit.objects.count(), 0)
