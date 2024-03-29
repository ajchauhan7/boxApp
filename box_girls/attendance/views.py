from django.conf import settings

from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response


from .serializers import *

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer