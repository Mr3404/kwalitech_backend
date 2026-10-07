from django.contrib import admin
from .models import *


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'unit')
    search_fields = ('name',)
    list_editable = ('price', 'unit')
    
    
class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    fields = ('name', 'description', 'assigned_to', 'status', 'start_date', 'end_date')
    readonly_fields = ('created_at',)
    show_change_link = True
    
    
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_mobile', 'location', 'address', 'received_date', 'status')
    search_fields = ('customer_name', 'customer_mobile', 'location', 'address')
    list_filter = ('status',)
    list_editable = ('status',)
    
    inlines = [TaskInline]


class TaskImageInline(admin.TabularInline):
    model = TaskImage
    extra = 0
    fields = ('image', 'uploaded_at')
    readonly_fields = ('uploaded_at',)
    show_change_link = True
    

class TaskResultImageInline(admin.TabularInline):
    model = TaskResultImage
    extra = 0
    fields = ('image', 'uploaded_at')
    readonly_fields = ('uploaded_at',)
    show_change_link = True
    
    
class TaskMaterialsInline(admin.TabularInline):
    model = TaskMaterial
    extra = 0

    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'request', 'assigned_to', 'status', 'start_date', 'end_date', 'created_at')
    search_fields = ('name', 'request__customer_name', 'assigned_to__username')
    list_filter = ('status',)
    list_editable = ('status','start_date', 'end_date')
    
    inlines = [TaskMaterialsInline, TaskImageInline, TaskResultImageInline]
    
    
@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'comment', 'created_at')
    search_fields = ('task__name', 'user__username', 'comment')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)