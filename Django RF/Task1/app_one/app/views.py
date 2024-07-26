from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Teacher, Student
from .serializers import TeacherSerializer, StudentSerializer

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello World'})

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer