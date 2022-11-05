from django.db import models


class DanceClass(models.Model):
    """
    A SQL table that models dance classes.
    """

    teacher = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date = models.DateTimeField()
