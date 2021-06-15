from django.urls import path

from .views import DogbookList, DogbookDetail


urlpatterns = [
    path("api/dogbooks/", DogbookList.as_view()),
    path("api/dogbooks/<int:pk>/", DogbookDetail.as_view()),
]
