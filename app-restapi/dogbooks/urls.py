from django.urls import path

from .views import DogbookList


urlpatterns = [
    path("api/dogbooks/", DogbookList.as_view()),
]
