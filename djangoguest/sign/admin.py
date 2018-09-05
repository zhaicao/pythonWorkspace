from django.contrib import admin
from sign.models import Event, Guest

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    """
    Event模型定义管理页面显示字段、搜索栏及过滤器
    """
    list_display = ['id', 'name', 'status', 'address', 'start_time']
    search_fields = ['name']
    list_filter = ['status']

class GuestAdmin(admin.ModelAdmin):
    """
    Guest模型定义管理页面显示字段、搜索栏及过滤器
    """
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname', 'phone']
    list_filter = ['sign']

admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
