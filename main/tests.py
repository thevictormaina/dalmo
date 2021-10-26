from django.test import TestCase
from django.contrib.auth import get_user_model
from main.models import Moment
from django.utils import timezone

User = get_user_model()

# Create your tests here.
class MomentTestCase(TestCase):
    def setUp(self):
        self.user = User(username = "user", password = "password")
        self.user.save()
        self.moment = Moment(feeling = "happy", cause = "it's a great day", user = self.user)
        self.moment.save()

    def test_list_moments(self):
        """Test the list_moments classmethod method"""
        moments_all = Moment.list_moments()
        self.assertQuerysetEqual(moments_all, Moment.objects.all())

    def test_by_date(self):
        """Test if by_date method returns sorted dictionary of moments"""
        date = timezone.now().date()
        moment_dated = Moment.by_date()[0]
        m = { "date": date, "moments": Moment.objects.filter(date_added__date = date) }
        self.assertEqual(moment_dated['date'], m['date'])
        self.assertQuerysetEqual(moment_dated['moments'], m['moments'])