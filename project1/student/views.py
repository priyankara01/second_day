from rest_framework import viewsets
from .serializers import StudentSerializers
from .models import Student


class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializers
    queryset = Student.objects.all()
    
    
