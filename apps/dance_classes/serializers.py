from rest_framework import serializers

from .models import DanceClass


class DanceClassSerializer(serializers.ModelSerializer):
    """
    Validates and converts request data into Python types.
    """

    class Meta:
        model = DanceClass
        fields = (
            "teacher",
            "location",
            "date",
        )


# class DanceClassSerializer(serializers.Serializer):
#     """
#     A more explicit way to write the serializer.
#     """

#     teacher = serializers.CharField(max_length=30)
#     location = serializers.CharField(max_length=30)
#     date = serializers.DateField()
