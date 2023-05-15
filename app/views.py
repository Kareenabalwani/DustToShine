
from webbrowser import get
from django.shortcuts import redirect, render
from .models import *
from random import randint
from django.http import HttpResponseRedirect, HttpResponse
import datetime
import random
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'app/home.html')
#Admin  views Section

def adminloginpage(request):
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/login.html")

def admin_login(request):
    if request.method == "POST":
        uname = request.POST['username']
        password = request.POST['password']
        admin_details = Admin_mst_tbl.objects.get(username=uname)
        if admin_details:
            if admin_details.password==password:
                return redirect("admin_panel")
            else:
                msg = "Invalid Credentials !"
                return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/login.html",{'msg':msg})
        else:
            msg = "Invalid Admin details !"
            return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/login.html",{'msg':msg})
            
        
def admin(request):
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/index.html")

def manage_service_page(request):
    services = Service_mst_tbl.objects.all()
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/manage_services.html",{'services':services})

def add_delivery_executive_page(request):
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/add_delivery_executive.html")

def add_del_executive(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password']
        address = request.POST['address']
        contact= request.POST['contact']
        age= request.POST['age']
        gender = request.POST['gender']
        assigned_pincode = request.POST['assigned_pincode']
        d_adhar_card = request.FILES['d_adhar_card']
        d_profile = request.FILES['d_profile']
        boy = Delivery_executive_tbl.objects.filter(email=email)
        if boy:
            msg="Delivery Executive already Exist"
            return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/add_delivery_executive.html")
        else:
            if password==cpassword:
                Delivery_executive_tbl.objects.create(fname=fname,lname=lname,email=email,password=password,address=address,contact=contact,age=age,gender=gender,assigned_pincode=assigned_pincode,is_enabled=True,d_adhar_card=d_adhar_card,d_profile=d_profile)
                return redirect('manage_delivery_executive')
            else:
                msg="Password does not match !"
                return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/add_delivery_executive.html",{'msg':msg})



def add_service_page(request):
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/add_service.html")

def add_service(request):
    service_name = request.POST['service_name']
    service_desc = request.POST['service_desc']
    service_price = request.POST['service_price']
    service_discount = request.POST['service_discount']
    urgent_charges = request.POST['urgent_charges']
    is_enabled = request.POST['is_enabled']
    service_img = request.FILES['service_img']
    Service_mst_tbl.objects.create(service_name=service_name,service_desc=service_desc,price_per_unit=service_price,discount_per_service=service_discount,urgent_charges=urgent_charges,is_enabled=is_enabled,service_img=service_img)
    return HttpResponse("<script>alert('Added!')</script>")
    
    return render(request,'')

def change_status_admin(request):
    return render(request,"app/Admin-DeliveryExecuxtive/admin_panel/pages/samples/change_status_admin.html")

def manage_delivery_executive(request):
    boys = Delivery_executive_tbl.objects.all()
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/manage_delivery_ex.html",{'boys':boys})

def reply_feedback_page(request,pk):
    fb = Feeback_tbl.objects.get(pk=pk)
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/reply_feedback.html",{'fb':fb})

def reply_feedback(request):
    if request.method =="POST":
        feedback_id= request.POST['feedback_id']
        feedback_reply = request.POST['feedback_reply']
        fb=Feeback_tbl.objects.get(pk=feedback_id)
        fb.reply_of_feedback=feedback_reply
        fb.save()
        return redirect('view_feedback_page')
        


def update_delivery_executive_page(request,pk):
    boy = Delivery_executive_tbl.objects.get(pk=pk)
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/update_delivery_executive.html",{'boy':boy})

def update_delivery_executive(request):
    boy_id = request.POST['boy_id']
    boy = Delivery_executive_tbl.objects.get(id=boy_id)
    if request.method=="POST":
        boy.fname = request.POST['fname']
        boy.lname = request.POST['lname']
        boy.contact = request.POST['contact']
        boy.age = request.POST['age']
        if request.POST['password'] == request.POST['cpassword']:
            boy.password = request.POST['password']
        boy.save()
        return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/update_delivery_executive.html",{'boy':boy})

def disable_delivery_executive(request,pk):
    boy = Delivery_executive_tbl.objects.get(pk=pk)
    boy.is_enabled=0
    boy.save()
    return redirect("view_feedback_page")

def view_feeback_page(request):
    feedbacks=Feeback_tbl.objects.all()
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/view_feedback.html",{'feedbacks':feedbacks})

def view_franchise_page(request):
    saved_franchises=Franchise_tbl.objects.filter(save_for_later=True)
    unsaved_franchises=Franchise_tbl.objects.filter(save_for_later=False)
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/view_franchise.html",{'saved_franchises':saved_franchises,'unsaved_franchises':unsaved_franchises})


def save_franchise(request,pk):
    fb=Franchise_tbl.objects.get(pk=pk)
    fb.save_for_later=True
    fb.save()
    return redirect('view_franchise_page')

def unsave_franchise(request,pk):
    fb=Franchise_tbl.objects.get(pk=pk)
    fb.save_for_later=False
    fb.save()
    return redirect('view_franchise_page')


def view_orders(request):
    
    urgent_order = Order_tbl.objects.filter(is_urgent=1)
    n_order = Order_tbl.objects.filter(is_urgent=0)
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/view_orders.html",{'urgent_order':urgent_order,'n_order':n_order})


# users and visitors view

# def user_contact_page(request):
#     return render(request,"app/Visitor-Customer/contact.html")

# def user_franchise(request):
#     return render(request,"app/Visitor-Customer/franchise.html")
# users and visitors view section

# Visitor

def  visitor_home(request):
    return render(request,"app/Visitor-Customer/index.html")

def  visitor_about(request):
    return render(request,"app/Visitor-Customer/about.html")

def  visitor_signup_alert(request):
    return render(request,"app/Visitor-Customer/alert.html")

def  visitor_service_page(request):
    return render(request,"app/Visitor-Customer/uservice.html")

def  visitor_contact(request):
    return render(request,"app/Visitor-Customer/contact.html")

def  visitor_franchise(request):
    return render(request,"app/Visitor-Customer/franchise.html")

#  User

def  user_loginpage(request):
    return render(request,"app/Visitor-Customer/login.html")

def user_signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        contact= request.POST['contact']
        address = request.POST['address']
        pincode =request.POST['pincode']
        referral_code = randint(100000,999999)

        user = Customer_mst_tbl.objects.filter(email=email)

        if user:
            msg = "User already Exist!"
            return render(request,"app/Visitor-Customer/login.html",{'msg':msg})
        else:
            Customer_mst_tbl.objects.create(fname=fname,lname=lname,email=email,password=password,contact=contact,address=address,pincode=pincode,referral_code=referral_code)
            return render(request,"app/Visitor-Customer/login.html")
        

def user_login(request):
    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        user = Customer_mst_tbl.objects.get(email=email)
        if user:
            if password == user.password:
                request.session['id']=user.id
                request.session['email']=user.email
                request.session['name']=user.fname
                return redirect("visitor_home")
            else:
                msg = "Invalid Credentials!"
                return render(request,"app/Visitor-Customer/login.html",{'msg':msg})
        else:
            msg = "User Does not exist"
            return render(request,"app/Visitor-Customer/login.html",{'msg':msg})

def  user_change_pswd(request):
    user_id = request.session['id']
    user = Customer_mst_tbl.objects.get(id=user_id)
    if user:
        return render(request,"app/Visitor-Customer/changepass.html",{'user':user})
    

def forget_password_mail(request):    
    otp = random.randrange(1,100000)
    request.session['otpsession']=otp
    subject = "Verification mail"
    msg = f"DustToShine.io Password Recovery \n{otp}"
    frm = settings.EMAIL_HOST_USER
    to = request.session['email']
    send_mail(subject,msg,frm,[to])
    
    return redirect("new_password_page")

def new_password_page(request):
    return render(request,"app/Visitor-Customer/new_password.html")

def set_new_password1(request):
    otpsession=request.session['otpsession']
    if request.method=="POST":
        user_otp = request.POST['user_otp']
        user_password = request.POST['user_password']
        if otpsession == int(user_otp):
            return HttpResponse("Correct")
        else:
            return HttpResponse("Not match")

def set_new_password(request):
    otpsession=request.session['otpsession']
    if request.method=="POST":
        user_otp = request.POST['user_otp']
        user_password = request.POST['user_password']
        user_cpassword = request.POST['user_cpassword']
        if otpsession == int(user_otp):
            if user_password == user_cpassword:
                user = Customer_mst_tbl.objects.get(id=request.session['id'])
                if user:
                    user.password = user_password
                    user.save()
                    return redirect("visitor_home")
                else:
                    msg="user does not exist!"
                    return render(request,"app/Visitor-Customer/new_password.html",{'msg':msg})
            else:
                msg = "Password does not match !"
                return render(request,"app/Visitor-Customer/new_password.html",{'msg':msg})
        else:
            msg ="Invalid OTP !"
            return render(request,"app/Visitor-Customer/new_password.html",{'msg':msg})


def view_my_orders(request):
    orders = Order_tbl.objects.filter(customer_id_id=request.session['id'])
    return render(request,"app/Visitor-Customer/order.html",{'orders':orders})

def cancel_order(request):
    if request.method == "POST":
        order=request.POST['order_id']
        order = Order_tbl.objects.get(order_id=order)
        order.delete()
        return redirect("my_orders_page")
    
def user_contact_page(request):
    return render(request,"app/Visitor-Customer/ucontact.html")

def user_franchise(request):
    return render(request,"app/Visitor-Customer/ufranchise.html")

def new_franchise(request):
    if request.method == "POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        location=request.POST['location']
        contact=request.POST['contact']
        capital=request.POST['capital']
        experience=request.POST['experience']
        franchise = Franchise_tbl.objects.create(fname=fname,lname=lname,email=email,location=location,contact=contact,available_capital=capital,experience=experience)
        if franchise:
            return redirect("visitor_home")
        else:
            return redirect("franchise")
def  confirmation(request):
    return render(request,"app/Visitor-Customer/confirmation.html")


def next_to_pay(request,service):
    if request.method == "POST":
        request.session['sid'] = request.POST['service_id']
        request.session['qty'] = request.POST['quantity']
        request.session['is_urgent'] = request.POST['is_urgent']
        return render(request,"app/Visitor-Customer/checkout.html")
        
    else:
        return HttpResponse("<h1> Failed to Go Further !</h1>")
        
         
def  checkout_page(request,pk):
    user = Customer_mst_tbl.objects.get(pk=pk)
    service_id=request.session['sid']
    service = Service_mst_tbl.objects.get(pk=service_id)
    quantity = request.session['qty']
    is_urgent = request.session['is_urgent']
    rewarded_discount=0
    net_bill = int(int(quantity) * int(service.price_per_unit))
    delivery_ex_id=Delivery_executive_tbl.objects.get(assigned_pincode=user.pincode)
    order=Order_tbl.objects.create(units=quantity,is_urgent=is_urgent,order_status=0,net_bill=net_bill,rewarded_discount=rewarded_discount,customer_id_id=user.id,delivery_executive_id_id=delivery_ex_id.id,service_id_id=service_id)
    return render(request,"app/Visitor-Customer/confirmation.html")
    
        
#delivery panel
def d_panel_page(request):
    urgent_order=Order_tbl.objects.filter(delivery_executive_id_id=request.session['did'],is_urgent=1)

    #non urgent
    n_order=Order_tbl.objects.filter(delivery_executive_id_id=request.session['did'],is_urgent=0)
    

    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/d_panel.html",{'urgent_order':urgent_order,'n_order':n_order})
    


def d_panel_login_page(request):
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/d_login.html")

def d_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        boy_details = Delivery_executive_tbl.objects.get(email=email)
        if boy_details:
            if boy_details.password == password:
                request.session['did']=boy_details.id
                request.session['demail']=boy_details.email
                return redirect('d_panel_page')
            else:
                msg = "Invalid Credentials !"
                return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/d_login.html",{'msg':msg})
        else:
            msg = "Invalid Admin details !"
            return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/d_login.html",{'msg':msg})

def d_change_status_page(request,code):
    # code = request.GET.get('code')
    details= Order_tbl.objects.get(order_id=code)
    return render(request,"app/Admin-DeliveryExecutive/admin_panel/pages/samples/change_status_admin.html",{'details':details})

def change_status(request):
    if request.method == "POST":
        order=request.POST['order_id']
        order = Order_tbl.objects.get(order_id=order)
        order.order_status = request.POST['order_status']
        order.save()
        return redirect(d_panel_page)
    
    

def  user_home(request):
    return render(request,"app/Visitor-Customer/user.html")

def  user_services_page(request):
    services = Service_mst_tbl.objects.filter(is_enabled=1)
    return render(request,"app/Visitor-Customer/uservice.html",{'services':services})

def single_service_page(request,pk):
    service = Service_mst_tbl.objects.get(pk=pk)
    return render(request,"app/Visitor-Customer/swash.html",{'service':service})

def ucart_page(request,pk):
    service = Service_mst_tbl.objects.get(pk=pk)
    return render(request,"app/Visitor-Customer/ucart.html",{'service':service})


def  bag_service(request):
    return render(request,"app/Visitor-Customer/bag.html")

def  carpet_service(request):
    return render(request,"app/Visitor-Customer/carpet.html")

def  curtain_service(request):
    return render(request,"app/Visitor-Customer/curtain.html")

def  dry_clean_service(request):
    return render(request,"app/Visitor-Customer/dryc.html")

def  petrol_clean_service(request):
    return render(request,"app/Visitor-Customer/petrol.html")

def  shoe_clean_service(request):
    return render(request,"app/Visitor-Customer/shoe.html")

def  stain_service(request):
    return render(request,"app/Visitor-Customer/stain.html")

def  steam_press_service(request):
    return render(request,"app/Visitor-Customer/steam.html")

def  simple_wash_service(request):
    return render(request,"app/Visitor-Customer/swash.html")

def  user_cart(request):
    return render(request,"app/Visitor-Customer/ucart.html")

def  edit_profile_page(request):
    user = Customer_mst_tbl.objects.get(id=request.session['id'])
    if user:
        return render(request,"app/Visitor-Customer/ueditprofile.html",{'user':user})
    
def edit_profile(request):
        if request.method=="POST":
                uid = request.session['id']
                user = Customer_mst_tbl.objects.get(id=uid)
                if user:
                    contact = request.POST['contact']
                    user.fname= request.POST['fname']
                    user.lname = request.POST['lname']
                    user.address= request.POST['address']
                    user.pincode= request.POST['pincode']
                    user.contact= request.POST['contact']
                    user.save()
                    return render(request,'app/Visitor-customer/index.html')
                else:
                     return HttpResponse("<h1> Failed to Update !</h1>")
                     
                     
            
            
        