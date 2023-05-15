
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.user_loginpage,name="user_loginpage"),
#    ADMIN SECTION
   path("adminpanel/login",views.adminloginpage,name="admin_login_page"),
   path("adminpanel",views.admin,name="admin_panel"),
   path("adminlogin",views.admin_login,name="admin_login"), 
   path("samples/manage_services.html",views.manage_service_page,name="Manage services"),
   path("samples/add_delivery_executive.html",views.add_delivery_executive_page,name="add_delivery_executive_page"),
   path("samples/add_delivery_executive",views.add_del_executive,name="add_del_executive"),
   path("samples/add_service.html",views.add_service_page,name="add_services_page"),
   path("addservice",views.add_service,name="add_service"),
   path("samples/change_status_admin.html",views.change_status_admin,name="Change status | admin"),
   path("samples/manage_delivery_ex.html",views.manage_delivery_executive,name="manage_delivery_executive"),
   path("samples/reply_feedback.html/<int:pk>",views.reply_feedback_page,name="reply_feedback_page"),
   path("reply_feedback",views.reply_feedback,name="reply_feedback"),
   path("update_delivery_executive_page/<int:pk>",views.update_delivery_executive_page,name="update_delivery_executive_page"),
   path("update_delivery_executive",views.update_delivery_executive,name="update_delivery_executive"),
   path("disable_delivery_executive/<int:pk>",views.disable_delivery_executive,name="disable_delivery_executive"),
   path("samples/view_feedback.html",views.view_feeback_page,name="view_feedback_page"),
   path("samples/view_franchise.html",views.view_franchise_page,name="view_franchise_page"),
   path("save_franchise<int:pk>",views.save_franchise,name="save_franchise"),
   path("unsave_franchise<int:pk>",views.unsave_franchise,name="unsave_franchise"),
   path("samples/view_orders.html",views.view_orders,name="View Orders"),
    #user section
   path("franchise.html",views.user_franchise,name="franchise"),
   path("new_franchise",views.new_franchise,name="new_franchise"),
   # path("contact.html",views.user_contact_page,name="contact"),
   #  path
      # Visitor section
   path("index.html",views.visitor_home,name="visitor_home"),
   path("about.html",views.visitor_about,name="About page | Visitor"),
   path("alert.html",views.visitor_signup_alert,name="Signup_alert"),
   path("nservice.html",views.visitor_service_page,name="Service page | Visitor"),
   path("contact.html",views.visitor_contact,name="Contact page | Visitor"),
   path("franchise.html",views.visitor_franchise,name="Franchise page | visitor"),

   #user section
   path("login.html",views.user_loginpage,name="user_loginpage"),
   path("user_signup",views.user_signup,name="user_signup"),
   path("user_login",views.user_login,name="user_login"),
   path("changepass.html",views.user_change_pswd,name="change_password"),
   path("changepass_sendmail",views.forget_password_mail,name="change_password_send_mail"),
   path("new_password_page",views.new_password_page,name="new_password_page"),
   path("set_new_password",views.set_new_password,name="set_new_password"),
   path("ucontact.html",views.user_contact_page,name="contact | customer"),
   path("ufranchise.html",views.user_franchise,name="franchise | customer"),
   path("cart/confirmation.html",views.confirmation,name="Order confirmation"),
   path("PaymentPage/<int:service>",views.next_to_pay,name="next_to_pay"),
   path("cart/checkout/<int:pk>",views.checkout_page,name="checkout_page"),
   path("user.html",views.user_home,name="Home page | Customer"),
   path("services.html",views.user_services_page,name="user_services_page"),
   path("service/<int:pk>",views.single_service_page,name="single_service_page"),
   path("cart/<int:pk>",views.ucart_page,name="ucart_page"),
   path("bag.html",views.bag_service,name="Bag Cleaning"),
   path("carpet.html",views.carpet_service,name="Carpet Cleaning"),
   path("curtain.html",views.curtain_service,name="Curtain Cleaning"),
   path("dryc.html",views.dry_clean_service,name="Dry Cleaning"),
   path("petrol.html",views.petrol_clean_service,name="Petrol Wash"),
   path("shoe.html",views.shoe_clean_service,name="Shoe Cleaning"),
   path("stain.html",views.stain_service,name="Stain Removal"),
   path("steam.html",views.steam_press_service,name="Steam Press"),
   path("swash.html",views.simple_wash_service,name="Simple Wash"),
   path("ucart.html",views.user_cart,name="Cart"),
   path("ueditprofile.html",views.edit_profile_page,name="edit_profile_page"),
   path("edit_profile",views.edit_profile,name="edit_profile"),
   path("order.html",views.view_my_orders,name="my_orders_page"),
   path("cancel_order",views.cancel_order,name="cancel_order"),
   path("uabout.html",views.visitor_about,name="About page | customer"),
   #delivery panel 
   path("delivery_boy_panel",views.d_panel_page,name="d_panel_page"),
   path("delivery_boy_panel_login_page",views.d_panel_login_page,name="d_panel_login_page"),
   path("delivery_boy_panel_login",views.d_login,name="d_login"),
   path("samples/change_status_dboy.html/<int:code>",views.d_change_status_page,name="d_boy_change_status"),
   path("delivery_boy_change_status",views.change_status,name="change_status"),

]+ static  (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)








