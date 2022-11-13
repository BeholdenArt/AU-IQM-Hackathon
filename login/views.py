import smtplib
from email.message import EmailMessage

# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage as EM
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from hackathon import settings

from .tokens import generate_token

User = get_user_model()
# Create your views here.
def home(request):
    return redirect('news/')

def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        name = request.POST["name"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        if(pass1!=pass2):
            messages.error(request,"Password didn't match")
            return redirect('signup')
        if User.objects.filter(username=username):
            messages.error(request,"Username is already taken")
            return redirect('signup')
        if (len(username)>12):
            messages.error(request,"Username should be 12 character long")

        if not username.isalnum():
            messages.error(request,"Username should be alphanumeric")
        

        myUser = User.objects.create_user(username,email,pass1)
        myUser.first_name =name
        myUser.is_active = False
        myUser.save()

        # messages.success(request,"Your account has been successfully created")

        # Send the email
        msg = EmailMessage()
        msg.set_content("Hello "+ myUser.first_name+"!\n"+"Welcome to our NewsApp \n Thank You for signingup in our website \n We have also send you the confirmation link \n Thank You")
        msg['Subject'] = 'Thankyou for Registering'
        msg['From'] = "parthmodi019@gmail.com"
        msg['To'] = myUser.email
        s = smtplib.SMTP('smtp.gmail.com',587)

        s.starttls()
        s.login("parthmodi019@gmail.com", "vqmtigdadrufwzkx")
        s.send_message(msg)
        s.quit()

        #Email Address Confirmation
        current_site = get_current_site(request)
        email_subject = "Confirm Your Email for Login"
        message2 = render_to_string('email_confirmation.html',{
            'name':myUser.first_name,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(myUser.pk)),
            'token':generate_token.make_token(myUser)
        })
        # send_mail(email_subject,
        #     message2,
        #     "parthmodi019@gmail.com",
        #     [myUser.email])
        msg1 = EmailMessage()
        msg1.set_content(message2)
        msg1['Subject'] = email_subject
        msg1['From'] = "parthmodi019@gmail.com"
        msg1['To'] = myUser.email
        s1 = smtplib.SMTP('smtp.gmail.com',587)

        s1.starttls()
        s1.login("parthmodi019@gmail.com", "vqmtigdadrufwzkx")
        s1.send_message(msg1)
        s1.quit()
        return redirect('signin')
    else:
        return render(request,'login/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']
        user = authenticate(username = username,password = password)

        if user is not None:
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            fname = user.first_name
            print('-'*7, user.billing_plan)
            if user.billing_plan is not None: 
                return redirect('news/')
            else:
                return redirect('billing/0/0')
        else:
            messages.error(request,"Invalid Username or password")
            return redirect('signin')

    return render(request,'login/signin.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged out Successful")
    return redirect('news/')

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myUser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myUser =None

    if myUser is not None and generate_token.check_token(myUser,token):
        myUser.is_active=True
        myUser.save()
        messages.success(request,"Email is activated now you can login")
        return redirect('signin')

    else:
        return render(request,'activation_failed.html')

def forgot_password(request):
        email_subject = "Reset Password"
        if request.method =="POST" :
            email = request.POST['email']
            myUser = User.objects.all().filter(email = email)
            myUser = myUser.last()
            print(myUser)
            if myUser is None:
                messages.error(request,"Invalid Email")
                return render(request,"reset.html")
            message3 = render_to_string('reset_password.html',{
                'domain':'127.0.0.1:8000',
                'uid':urlsafe_base64_encode(force_bytes(myUser.pk)),
                'token':generate_token.make_token(myUser)
            })
            msg3 = EmailMessage()
            msg3.set_content(message3)
            msg3['Subject'] = email_subject
            msg3['From'] = "parthmodi019@gmail.com"
            msg3['To'] = myUser.email
            s2 = smtplib.SMTP('smtp.gmail.com',587)

            s2.starttls()
            s2.login("parthmodi019@gmail.com", "vqmtigdadrufwzkx")
            s2.send_message(msg3)
            s2.quit()

            return redirect('signin')
        return render(request,"reset.html")

def reset_password(request,uidb64,token):
    if request.method=="POST":
        pass1 = request.POST["new_pass1"]
        pass2 = request.POST["new_pass2"]
        if (pass1==pass2):
            uid = force_str(urlsafe_base64_decode(uidb64))
            myUser = User.objects.get(pk=uid)
            
            myUser.set_password(pass1)
            myUser.save()
            return redirect('signin')
        else:
            messages.error(request,"Password doesn't Match")
    return render(request,"new_password.html")

# @login_required(login_url='signup')
def billing(request, cost, duration):
    from newsapp.views import dashboard
    print(cost, duration)
    if cost == 0 and duration == 0:
        return render(request, 'login/payment.html')
    else:
        username = request.user.username
        username = User.objects.get(username= username)
        username.billing_plan = cost 
        username.duration = duration

        username.save()



        return dashboard(request)
