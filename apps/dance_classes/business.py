from option import Result, Ok, Err

from rest_framework.exceptions import ValidationError

from .models import DanceClass


def create_dance_class(**kwargs) -> Result[str, Err]:
    """
    Create a `DanceClass` record.
    """

    if DanceClass.objects.filter(**kwargs).exists():
        return Err(ValidationError("`DanceClass` record already exists."))

    dance_class = DanceClass.objects.create(**kwargs)

    return Ok({"id":dance_class.id})


# def create_dance_class(**kwargs) -> Result[str, Err]:
#     """
#     A more explicit way to use these functions.
#     """

#     if DanceClass.objects.filter(
#         teacher=kwargs["teacher"],
#         location=kwargs["location"],
#         date=kwargs["date"],
#     ).exists():
#         return Err(ValidationError("`DanceClass` record already exists."))

#     dance_class = DanceClass.objects.create(
#         teacher=kwargs["teacher"],
#         location=kwargs["location"],
#         date=kwargs["date"],
#     )

#     return Ok(dance_class)
