from django.db import models


class DanceClass(models.Model):
    """
    Modeling the SQL table
    """

    teacher = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date = models.DateTimeField()
