from rest_framework import serializers
from task_tracker.models import *


class TaskMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskMaterial
        fields = '__all__'


class RequestListSerializer(serializers.ModelSerializer):
    tasks = serializers.IntegerField(source='tasks.count', read_only=True)
    class Meta:
        model = Request
        fields = ['id', 'customer_name', 'customer_mobile', 'location', 'address', 'received_date', 'status', 'tasks']
        
        
class TaskListSerializer(serializers.ModelSerializer):
    request = serializers.StringRelatedField()
    class Meta:
        model = Task
        fields = ['id', 'request', 'name', 'description', 'assigned_to', 'status', 'start_date', 'end_date', 'created_at']
        

class TaskDetailSerializer(serializers.ModelSerializer):
    task_materials = TaskMaterialsSerializer(many=True)
    class Meta:
        model = Task
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = Request
        fields = ['id', 'customer_name', 'customer_mobile', 'location', 'address', 'received_date', 'status', 'tasks']