from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from .models import Journal, Volume, Issue, Paper
from .serializers import JournalSerializer, VolumeSerializer, IssueSerializer, PaperSerializer
from .route_list import routes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


# The ModelViewSet covers both the list,update,create and delete
# ViewSet can only be used for views that have the same serializer and queryset
class JournalsViewSet(ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

# class ApiJournals(ListCreateAPIView):
#     queryset = Journal.objects.all()
#     serializer_class = JournalSerializer

# class ApiJournal(RetrieveUpdateDestroyAPIView):
#     queryset = Journal.objects.all()
#     serializer_class = JournalSerializer


class VolumeViewSet(ModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer

# class ApiVolumes(ListCreateAPIView):
#     queryset = Volume.objects.all()
#     serializer_class = VolumeSerializer

# class ApiVolume(RetrieveUpdateDestroyAPIView):
#     queryset = Volume.objects.all()
#     serializer_class = VolumeSerializer

