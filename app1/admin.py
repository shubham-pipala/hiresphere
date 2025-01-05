from django.contrib import admin
from .models import *

# Register your models here.
class regi_admin(admin.ModelAdmin):
    list_display=['name','email','phone','address','password']

admin.site.register(regi,regi_admin)    



class cp_register_admin(admin.ModelAdmin):
    list_display=['cp_name','cp_email','cp_phone','cp_address','cp_password','cp_gst_no']

admin.site.register(cp_register,cp_register_admin)