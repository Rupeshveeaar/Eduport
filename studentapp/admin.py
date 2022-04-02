from django.contrib import admin
from .models import Course, CustomUser, Session_Year, Student,Staff,category,order,OrderItem
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# class UserModel(UserAdmin):
#     list_display = ['username', 'user_type']

class OrderItemTubleinLine(admin.TabularInline):
    models = OrderItem

class orderAdmin(admin.ModelAdmin):
    inLines = [OrderItemTubleinLine]

admin.site.register(CustomUser)    
admin.site.register(Course)    
admin.site.register(Session_Year)    
admin.site.register(Student)    
admin.site.register(Staff)
admin.site.register(category)    
admin.site.register(order,orderAdmin)    
admin.site.register(OrderItem)    





