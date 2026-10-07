from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from task_tracker.models import Request
from .serializers import *


class DashBoardView(APIView):
    def get(self, request):
        try:
            
            payload = {
                'requests': RequestListSerializer(Request.objects.filter(status='received'), many=True).data,
                'tasks': TaskListSerializer(Task.objects.filter(Q(start_date__date=timezone.localdate())), many=True).data,
            }
            return Response(payload, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RequestListAPIView(APIView):
    
    def get(self, request):
        try:
            requests = Request.objects.all()
            serializer = RequestListSerializer(requests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class RequestView(APIView):
    
    def get(self, request, pk):
        try:
            request = Request.objects.get(id=pk)
            serializer = RequestSerializer(request, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error: ': str(e)})
        
        
class TaskListView(APIView):
    def get(self, request):
        try:
            tasks = Task.objects.all()
            serializer = TaskListSerializer(tasks, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error: ': str(e)})
        
        
class TaskView(APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskDetailSerializer(task, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as e:
            return Response({'error: ': str(e)})