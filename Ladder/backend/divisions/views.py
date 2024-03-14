from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .models import Division,TeamInDivision
from .serializers import DivisionSerializer,TeamInDivisionSerializer


class DivisionView(viewsets.ViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Division.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)
        
class TeamInDivisionView(viewsets.ViewSet):
    queryset = TeamInDivision.objects.all()
    serializer_class = TeamInDivisionSerializer