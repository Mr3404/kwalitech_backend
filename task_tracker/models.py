from django.db import models
from django.contrib.auth.models import User


class Material(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='materials_photos/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"
        
    def __str__(self):
        return self.name
    
    

class Request(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    received_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('received', 'Received'), ('in_progress', 'In Progress'), 
        ('completed', 'Completed'), ('cancelled', 'Cancelled'),
        ('inspected', 'Inspected')
        ], default='recieved')
    
    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"
        
    def __str__(self):
        return f"{self.address} - {self.status}"
    
    
    
class Task(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # materials = models.ManyToManyField(Material, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'), ('in_progress', 'In Progress'), 
        ('completed', 'Completed'), ('cancelled', 'Cancelled')
        ], default='pending')
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        
    def __str__(self):
        return f"Task: {self.name} for Request: {self.request.customer_name} - {self.status}"
    

class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='task_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Task Image"
        verbose_name_plural = "Task Images"
        
    def __str__(self):
        return f"Image for Task: {self.task.name}"
    

class TaskResultImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='result_images')
    image = models.ImageField(upload_to='task_result_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Task Result Image"
        verbose_name_plural = "Task Result Images"
        
    def __str__(self):
        return f"Result Image for Task: {self.task.name}"
    
    
class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Task Comment"
        verbose_name_plural = "Task Comments"
        
    def __str__(self):
        return f"Comment by {self.user.username if self.user else 'Unknown'} on Task: {self.task.name}"
    

class TaskMaterial(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = "Task Material"
        verbose_name_plural = "Task Materials"
        
    def __str__(self):
        return f"{self.quantity} of {self.material.name} for Task: {self.task.name}"