from rest_framework import viewsets
from .models import Schedules
from .serializers import ScheduleSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedules.objects.all()
    serializer_class = ScheduleSerializer
