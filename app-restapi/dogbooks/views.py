from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Dogbook
from .serializers import DogbookSerializer


class DogbookList(APIView):
    def get(self, request, format=None):
        dogbooks = Dogbook.objects.all()
        serializer = DogbookSerializer(dogbooks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DogbookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogbookDetail(APIView):
    def get_object(self, pk):
        try:
            return Dogbook.objects.get(pk=pk)
        except Dogbook.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dogbook = self.get_object(pk)
        serializer = DogbookSerializer(dogbook)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dogbook = self.get_object(pk)
        serializer = DogbookSerializer(dogbook, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dogbook = self.get_object(pk)
        dogbook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
