from django.shortcuts import render
from .serializers import ClassroomListSerializer, ClassroomDetailSerializer 
from classes.models import Classroom
from rest_framework.generics import (CreateAPIView,
	ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView,
	DestroyAPIView)



class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListSerializer


class ClassroomDetail(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field='id'
	lookup_url_kwarg='class_id'


class ClassroomCreate(CreateAPIView):
	serializer_class = ClassroomDetailSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)



class ClassroomUpdate(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'

class ClassroomDelete(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'






