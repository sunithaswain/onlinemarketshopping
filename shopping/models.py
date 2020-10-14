from django.db import models

# Create your models here.
class buying_model(models.Model):
	name = models.CharField(max_length=255, blank=True)
	email = models.CharField(max_length=255, blank=True)
	mobile=models.IntegerField(default=0)
	deliver_address=models.CharField(max_length=255, blank=True)
	password=models.CharField(max_length=255, blank=True)
class sellers_model(models.Model):
	name = models.CharField(max_length=255, blank=True)
	email = models.CharField(max_length=255, blank=True)
	password = models.CharField(max_length=255, blank=True)
	sellers_contact_address = models.CharField(max_length=255, blank=True)
	sellers_contact_number = models.IntegerField()
class products_model(models.Model):
	sellers_id = models.CharField(max_length=255, blank=True)
	product_name = models.CharField(max_length=255, blank=True)
	product_images = models.ImageField(upload_to = 'images/')
	product_details = models.CharField(max_length=255, blank=True)
class contact_model(models.Model):
	email = models.CharField(max_length=255, blank=True)
	query = models.CharField(max_length=255, blank=True)
	description = models.CharField(max_length=255, blank=True)