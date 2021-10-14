from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Extend from default user model.
class User(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Moment(models.Model):
    feeling = models.CharField(max_length=50)
    cause = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moments')

    def save(self, *args, **kwargs):
        """Overriding default save method to save date and time instance is created."""
        if not self.id:
            self.date_added = timezone.now()
        return super(Moment, self).save(*args, *kwargs)

    def __str__(self):
        return f"Moment {self.id}: {self.feeling}"

class Entry(models.Model):
    class DayRating(models.IntegerChoices):
        """Integer choices for daily datings"""
        VERY_GOOD = 5, ('really good')
        GOOD = 4, ('good')
        NEUTRAL = 3, ('neutral')
        BAD = 2, ('bad')
        VERY_BAD = 1, ('really bad')

    rating = models.PositiveIntegerField(choices=DayRating.choices)
    sleep_time = models.DateTimeField()
    wake_time = models.DateTimeField()
    meals_amount = models.PositiveIntegerField()
    snacks = models.BooleanField(default=False)
    water_amount = models.PositiveIntegerField()

    class TidyRating(models.IntegerChoices):
        """Integer choices for tidiness datings"""
        VERY_TIDY = 5, ('really tidy')
        TIDY = 4, ('tidy')
        NEUTRAL = 3, ('neutral')
        UNTIDY = 2, ('untidy')
        VERY_UNTIDY = 1, ('really untidy')

    tidiness_rating = models.PositiveIntegerField(choices=TidyRating.choices)
    date_added = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')

    class Meta:
        verbose_name_plural = 'Entries'

    def save(self, *args, **kwargs):
        """Overriding default save method to save date and time instance is created."""
        if not self.id:
            self.date_added = timezone.now()
        return super(Entry, self).save(*args, *kwargs)

    def __str__(self):
        return f"Entry {self.id}: {self.date_added.strftime('%d %b %Y')}"

    @property
    def moments_from_this_day(self):
        """Returns all Moment instances from the same date as current Entry instance."""
        moments = Moment.objects.filter(date_added__date = self.date_added.date()).all()
        return moments