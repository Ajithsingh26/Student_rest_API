from rest_framework import viewsets
from . import models
from . import serializers

class StudentsViewset(viewsets.ModelViewSet):
    queryset = models.students.objects.all()
    serializer_class = serializers.StudentSerializer
