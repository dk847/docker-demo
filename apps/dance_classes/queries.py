from .models import DanceClass


def query_all_dance_classes():
    return DanceClass.objects.all().order_by("date")
