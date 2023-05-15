from django.db import models
import email
from email.policy import default
from pyexpat import model
from re import T
from tkinter import CASCADE
from unittest import case
from django.db import models
from django.forms import EmailField
# Create your models here.

class Admin_mst_tbl(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Customer_mst_tbl(models.Model):
    fname=models.CharField(max_length=45)
    lname=models.CharField(max_length=45)
    email=models.EmailField(max_length=120,default="No mail Specified")
    password = models.CharField(max_length=8)
    address = models.CharField(max_length=256)
    contact = models.CharField(max_length=11)
    pincode  = models.IntegerField()
    referral_code = models.CharField(max_length=10)
    reward_points = models.IntegerField(default=0)

class Delivery_executive_tbl(models.Model):
    fname=models.CharField(max_length=45)
    lname=models.CharField(max_length=45)
    email=models.EmailField(max_length=120,default="No mail Specified")
    password = models.CharField(max_length=8)
    address = models.CharField(max_length=256)
    contact = models.CharField(max_length=11)
    age = models.IntegerField()
    gender = models.CharField(max_length=6,default="Male")
    assigned_pincode  = models.IntegerField()
    is_enabled = models.BooleanField(default=True)
    d_adhar_card = models.ImageField(upload_to="uploads/delivery_executive/addharcards",default="No adhar card")
    d_profile = models.ImageField(upload_to="uploads/delivery_executive/profiles",default="no profile img")


class Feeback_tbl(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback_desc = models.CharField(max_length=256)
    feedback_date = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer_mst_tbl,on_delete=models.CASCADE)
    reply_of_feedback = models.CharField(max_length=256)

class Franchise_tbl(models.Model):
    franchise_id = models.AutoField(primary_key=True)
    fname=models.CharField(max_length=45)
    lname=models.CharField(max_length=45)
    email=models.EmailField(max_length=120,default="No mail Specified")
    location = models.CharField(max_length=256)
    contact = models.CharField(max_length=11)
    available_capital = models.FloatField()
    experience =models.CharField(max_length=15)
    save_for_later = models.BooleanField(default=False)

class Service_mst_tbl(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=120)
    service_desc = models.CharField(max_length=256)
    price_per_unit = models.FloatField()
    discount_per_service = models.FloatField(default=10)
    is_enabled =models.BooleanField(default=True)
    service_img = models.ImageField(upload_to='uploads/services',default="noimg")
    urgent_charges = models.FloatField()

class Order_tbl(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer_mst_tbl,on_delete=models.CASCADE)
    service_id =models.ForeignKey(Service_mst_tbl,on_delete=models.CASCADE)
    units = models.IntegerField()
    is_urgent = models.BooleanField()
    order_status = models.IntegerField(default=0) #0-nothing 1-picked up
    # 2-under process 3-out for delivery 4-completed/delivered
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_executive_id = models.ForeignKey(Delivery_executive_tbl,on_delete=models.CASCADE)
    rewarded_discount = models.FloatField()
    net_bill = models.FloatField()
    payment_mode = models.CharField(max_length=20)
    


class Payment_tbl(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_status = models.IntegerField()
    order_id = models.ForeignKey(Order_tbl,on_delete=models.CASCADE)
    