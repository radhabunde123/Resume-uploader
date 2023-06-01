from django.contrib import admin
from .models import Create
# Register your models here.
@admin.register(Create)
class CreateModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'dob','gender','qualification','experience','city','email','mobile',
                 'profile_image','my_file']
