from rest_framework import serializers
from classes.models import Classroom


class ClassroomListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		exclude=['name']


class ClassroomDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields='__all__'


