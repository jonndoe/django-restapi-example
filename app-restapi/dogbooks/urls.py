from django.urls import path

from .views import DogbookDetail, DogbookList

urlpatterns = [
    path("api/dogbooks/", DogbookList.as_view()),
    path("api/dogbooks/<int:pk>/", DogbookDetail.as_view()),
]
