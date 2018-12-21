from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index), 
    url(r'^signin$', views.signin), 
    url(r'^userdata$', views.userdata), 
    url(r'^createmember$', views.createmember), 
    url(r'^visits$', views.visits), 
    url(r'^visits_date$', views.visits_date), 
    url(r'^sales$', views.sales), 
    url(r'^sales_date$', views.sales_date), 
    url(r'^create_new_member$', views.create_new_member), 
    url(r'^update_member/(?P<user_id>\d+)$', views.update_member),
    url(r'^add_payment/(?P<user_id>\d+)$', views.add_payment),
    url(r'^update_member_account/(?P<user_id>\d+)$', views.update_member_account),
    url(r'^verify$', views.verify),
    url(r'^findemail$', views.findemail),
    url(r'^searchmember$', views.searchmember),
    url(r'^walkin_payment$', views.walkin_payment),
    url(r'^cafe_payment$', views.cafe_payment),
    url(r'^expenses$', views.expenses),
     url(r'^delete/(?P<user_id>\d+)$', views.delete),
    url(r'^logout$', views.logout)
]