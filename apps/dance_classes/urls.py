from django.urls import path

from .views import (
    DanceClassCreateListAPIView,
    DanceClassFullStackListView,
)


urlpatterns = [
    path("api", DanceClassCreateListAPIView.as_view(), name="dance-class-api"),
    path(
        "fullstack", DanceClassFullStackListView.as_view(), name="dance-class-fullstack"
    ),
]
