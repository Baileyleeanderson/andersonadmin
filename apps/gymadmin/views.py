# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
from django.utils import timezone
from datetime import date, datetime

def index(request):
    return render(request, "gymadmin/index.html")

def signin(request):
    if request.POST['username'] == "":
        messages.error(request, "Incorrect Username Or Password")
        request.session['id'] = "Wrong!"
        return redirect ("/")  
    if request.POST['password'] == "":
        messages.error(request, "Incorrect Username Or Password")
        request.session['id'] = "Wrong!"
        return redirect ("/")  
    username = request.POST['username']
    userpassword = request.POST['password']
    if (username == "andersonhealthclub"): 
            if ( userpassword == "Believe888!"):
                request.session['id'] = "1723andersonhealth!@#$%"
            return redirect ("/userdata") 
    else:
        messages.error(request, "Incorrect Username Or Password")
        request.session['id'] = "Wrong!"
        return redirect ("/")

def userdata(request):
    if (request.session['id'] != "1723andersonhealth!@#$%"):
        return redirect ("/")
    else:
        return render(request, "gymadmin/userdata.html")

def createmember(request):
    if (request.session['id'] != "1723andersonhealth!@#$%"):
        return redirect ("/")
    return render(request, "gymadmin/createmember.html")    

def visits(request):
    if (request.session['id'] != "1723andersonhealth!@#$%"):
        return redirect ("/") 
    request.session['visit_num'] = 0
    request.session['date'] = ""
    request.session['visits'] = "visits on"
    searchdate = datetime.today().date()
    all_visits = Visit.objects.all().filter(visit_date__contains=searchdate)
    for visit in all_visits:
        request.session['visit_num'] += 1

    context = {
        "all_visits" : all_visits,
        "date" : searchdate
    }
    return render(request, "gymadmin/visits.html",context)

def visits_date(request):
    request.session['visit_num'] = 0
    if (request.session['id'] != "1723andersonhealth!@#$%"):
        return redirect ("/") 

    searchdate = request.POST['searchdate']
    request.session['date'] = searchdate
    all_visits = Visit.objects.all().filter(visit_date__contains=searchdate)
    for visit in all_visits:
        request.session['visit_num'] += 1

    context = {
        "all_visits" : all_visits,
        "date" : searchdate
    }
    return render(request, "gymadmin/visits.html", context)

def create_new_member(request):
    if request.POST['firstname'] == "":
            messages.error(request, "Enter First Name")
            return redirect ("/createmember")
    if request.POST['lastname'] == "":
            messages.error(request, "Enter last Name")
            return redirect ("/createmember")
    if request.POST['email'] == "":
            messages.error(request, "Enter Email")
            return redirect ("/createmember")
    if request.POST['phone'] == "":
            messages.error(request, "Enter Phone #")
            return redirect ("/createmember")
    if request.POST['address'] == "":
            messages.error(request, "Enter Address")
            return redirect ("/createmember")
    if request.POST['birthday'] == "":
            messages.error(request, "Enter Date Of Birth")
            return redirect ("/createmember")
    if request.POST['datepaid'] == "":
            messages.error(request, "Enter Date Paid")
            return redirect ("/createmember")
    if request.POST['expiration'] == "":
            messages.error(request, "Enter Expiration")
            return redirect ("/createmember")
    if request.POST['card_number'] == "":
            messages.error(request, "Enter Users Card Number")
            return redirect ("/createmember")
    if request.POST['membership_type'] == "":
            messages.error(request, "Enter Users Membership Type")
            return redirect ("/createmember")
    else: 
        user = User.objects.create(
                first_name=request.POST['firstname'],
                last_name=request.POST['lastname'],
                email=request.POST['email'],
                phone_number=request.POST['phone'],
                address=request.POST['address'],
                birthday=request.POST['birthday'],
                date_paid=request.POST['datepaid'],
                contract_expiration_date=request.POST['expiration'],
                card_number=request.POST['card_number'],
                membership_type= request.POST['membership_type'],
                kids_club_member= request.POST['kids_club_member']
                )
        user.save()
        print("user " + user.first_name)
        return redirect ("/update_member/"+ str(user.id))

def update_member(request, user_id):
    if (request.session['id'] != "1723andersonhealth!@#$%"):
        return redirect ("/")
    user = User.objects.get(id=user_id)
    if (user.contract_expiration_date.date() < datetime.today().date()):
        color = "bigred"
        status = "CONTRACT EXPIRED"
        status_color = "bigred"
    else:
        color = "biggreen"
        status = "PAID"
        status_color = "biggreen"

    users_visits = user.visits.all()
    payments = user.payments.all()
    last_payment = user.payments.all().last
    date = datetime.today().date()
    context = {
            "user" : user,
            "users_visits" : users_visits,
            "payments" : payments,
            "last_payment" : last_payment,
            "color" : color,
            "status" : status,
            "status_color" : status_color,
            "date" : date
        }
    return render(request, "gymadmin/update_member.html", context)

def update_member_account(request, user_id):
    user = User.objects.get(id= user_id)
    user.first_name=request.POST['firstname']
    user.last_name=request.POST['lastname']
    user.email=request.POST['email']
    user.phone_number=request.POST['phone']
    user.address=request.POST['address']
    user.contract_expiration_date=request.POST['expiration']
    user.card_number=request.POST['card_number']
    user.membership_type=request.POST['membership_type']
    kids_club_member= request.POST['kids_club_member']
    user.save()
    return redirect ("/update_member/"+ str(user.id))    

def add_payment(request, user_id):
    user = User.objects.get(id= user_id)
    new_payment = Payments.objects.create(
            payment_date = request.POST['payment_date'],
            user_payment = user,
            desc = request.POST['desc'],
            amount = request.POST['amount']
        )
    return redirect ("/update_member/"+ str(user.id))

def verify(request):
    try:   
        card_number= request.POST["card_number"]
        user = User.objects.get(card_number= card_number)
        new_visit = Visit.objects.create(user_visit=user)
        new_visit.save()
        return redirect ("/update_member/"+ str(user.id))
    except:
        messages.error(request, "Invalid Card Number")
        return redirect("/userdata")

def findemail(request):
    try:   
        email= request.POST["email"]
        user = User.objects.get(email= email)
        return redirect ("/update_member/"+ str(user.id))
    except:
        messages.error(request, "Invalid Email")
        return redirect("/searchmember")

def searchmember(request):
    if (request.session['id'] != "1723andersonhealth!@#$%"):
        return redirect ("/")
    else:
        all_users = User.objects.all().order_by('contract_expiration_date')
        all_users_alpha = User.objects.all().order_by('last_name')
        context = {
                "all_users" : all_users,
                "all_users_alpha" : all_users_alpha
        }
        return render(request, "gymadmin/allmembers.html", context)

def sales(request):
    if (request.session['id'] != "1723andersonhealth!@#$%"):
        return redirect ("/")
    searchdate = datetime.today().date()
    walkins = Walkin.objects.all().filter(date__contains=searchdate)
    cafe_sales = Cafe.objects.all().filter(date__contains=searchdate)
    expenses = Expense.objects.all().filter(date__contains=searchdate)
    sub_total = 0
    for w in walkins:
        sub_total += w.amount
    for c in cafe_sales:
        sub_total += c.amount
    for e in expenses:
        sub_total -= e.amount 
    request.session['total'] = sub_total
    if sub_total <= 0:
        request.session.total_color = 'red'
    else:
        request.session.total_color = 'green'
    context = {
        "date" : searchdate,
        "walkins" : Walkin.objects.all().filter(date__contains=searchdate),
        "cafe_sales" : Cafe.objects.all().filter(date__contains=searchdate),
        "expenses" : Expense.objects.all().filter(date__contains=searchdate),
     }   
    return render(request, "gymadmin/sales.html", context) 

def sales_date(request):
    if (request.session['id'] != "1723andersonhealth!@#$%"):
        return redirect ("/")
    searchdate = request.POST['searchdate']
    walkins = Walkin.objects.all().filter(date__contains=searchdate)
    cafe_sales = Cafe.objects.all().filter(date__contains=searchdate)
    expenses = Expense.objects.all().filter(date__contains=searchdate)
    sub_total = 0
    for w in walkins:
        sub_total += w.amount
    for c in cafe_sales:
        sub_total += c.amount
    for e in expenses:
        sub_total -= e.amount 
    request.session['total'] = sub_total
    if sub_total <= 0:
        request.session.total_color = 'red'
    else:
        request.session.total_color = 'green'
    context = {
        "date" : searchdate ,
        "walkins" : Walkin.objects.all().filter(date__contains=searchdate),
        "cafe_sales" : Cafe.objects.all().filter(date__contains=searchdate),
        "expenses" : Expense.objects.all().filter(date__contains=searchdate),
     }   
    return render(request, "gymadmin/sales.html", context) 

def walkin_payment(request):
    if (request.session['id'] != "1723andersonhealth!@#$%"):
        return redirect ("/")
    searchdate = timezone.now()
    print("today " + str(searchdate))
    new_walkin_payment = Walkin.objects.create(
        last_name= request.POST['last_name'],
        membership_purchased= request.POST['membership_purchased'],
        amount= request.POST['amount'],
        date= searchdate )
    new_walkin_payment.save()
    print("saved date" + str(new_walkin_payment.date))
    return redirect("/sales")    

def cafe_payment(request):
    if (request.session['id'] != "1723andersonhealth!@#$%"):
        return redirect ("/")
    searchdate = timezone.now()
    new_cafe_payment = Cafe.objects.create(
        last_name= request.POST['last_name'],
        item_purchased= request.POST['item_purchased'],
        amount= request.POST['amount'],
        date= searchdate )
    new_cafe_payment.save()
    return redirect("/sales")    

def expenses(request):
    if (request.session['id'] != "1723andersonhealth!@#$%"):
        return redirect ("/")
    searchdate = timezone.now()
    new_expense = Expense.objects.create(
        expense_paid_for= request.POST['expense_paid_for'],
        note= request.POST['note'],
        amount= request.POST['amount'],
        date= searchdate )
    new_expense.save()
    return redirect("/sales")    

def delete(request, user_id):
    if (request.session['id'] != "1723andersonhealth!@#$%"):
        return redirect ("/")
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/searchmember')

def logout(request):
    request.session['id'] = ""
    request.session['visit_num'] = ""
    request.session['date'] = ""
    return redirect ("/")