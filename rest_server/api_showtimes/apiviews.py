from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CinemaSerializer, ScreeningSerializer
from .models import Cinema, Screening


class CinemaList(generics.ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaView(APIView):

    def get_object(self, pk):
        try:
            return Cinema.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, id):
        cinema = self.get_object(id)
        serializer = CinemaSerializer(cinema, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, id):
        cinema = self.get_object(id)
        cinema.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        cinema = self.get_object(id)
        serializer = CinemaSerializer(cinema, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(seriaializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScreeningList(generics.ListAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer


class ScreeningView(APIView):

    def get_object(self, pk):
        try:
            return Screening.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, id):
        screening = self.get_object(id)
        serializer = ScreeningSerializer(screening, context={'request': request})
        return Response(serializer.data)

    def delete(self, id):
        screening = self.get_object(id)
        screening.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        screening = self.get_object(id)
        serializer = ScreeningSerializer(screening, data=request.data)
        if screening.is_valid():
            screening.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)