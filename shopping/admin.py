# Register your models here.
from django.contrib import admin
from .models import products_model
from django.contrib.auth.models import User
class Process2(admin.ModelAdmin):
    list_display= ('sellers_id','product_name','product_images','product_details')
admin.site.register(products_model, Process2)



