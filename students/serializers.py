from rest_framework import serializers
from .models import students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        # fields = ('name','id', 'tamil', 'english', 'maths','science','social', 'created_at', 'updated_at')
        fields = '__all__'