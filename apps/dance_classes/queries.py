from .models import DanceClass


def query_all_dance_classes():
    """
    Returns all `DanceClass` records.
    """
    
    return DanceClass.objects.all().order_by("date")
