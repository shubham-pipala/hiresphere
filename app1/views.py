from django.shortcuts import render,redirect # for rendering the html pages
from .models import *
from django.contrib.auth.hashers import check_password, make_password # for password hashing
from .models import *
import random   # for otp

# Candidate Registration
def register(request):
    if request.method == 'POST':
        if regi.objects.filter(email=request.POST['email']).exists():
            return render(request, 'user_registration.html', {'error': 'Email already registered!'})
        
        candidate = regi()
        candidate.name = request.POST['name']
        candidate.address = request.POST['address']
        candidate.email = request.POST['email']
        candidate.password = make_password(request.POST['password'])  
        candidate.phone = request.POST['phone']
        request.session['email'] = candidate.email
        cuser=candidate.name
        candidate.save()
        
        
        return render(request, 'home.html', {'message': 'Candidate registration successful!','registereduser':cuser})
    
    return render(request, 'user_registration.html')

# Company Registration
def cpregister(request):
    if request.method == 'POST':
        if cp_register.objects.filter(cp_email=request.POST['email']).exists():
            return render(request, 'cp-register.html', {'error': 'Email already registered!'})
        
        company = cp_register()
        company.cp_name = request.POST['name']
        company.cp_address = request.POST['address']
        company.cp_email = request.POST['email']
        company.cp_password = make_password(request.POST['password'])  
        
        company.cp_phone = request.POST['phone']
        company.cp_gst_no = request.POST['gstno']
        company.save()
        
        request.session['cp_email'] = company.cp_email
        return render(request, 'cp-register.html', {'message': 'Company registration successful!'})
    
    return render(request, 'cp-register.html')


#  Login
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        if cp_register.objects.filter(cp_email=email).exists():
            
            company = cp_register.objects.get(cp_email=email)
            if check_password(password, company.cp_password):

                cp_name = company.cp_name
                request.session['cp_email'] = company.cp_email
             
                return render(request,'home.html',{'cp':cp_name})
            else:
                return render(request, 'user_login.html', {'error': 'Invalid password for company account.'})
        
        elif regi.objects.filter(email=email).exists():
            print('yes')
            user = regi.objects.get(email=email)
            if check_password(password, user.password): 
                candidate = user.email
                request.session['email'] = user.email
                print(111111111111111111)
                return render(request,'home.html',{'candidate':candidate})
            else:
                return render(request, 'user_login.html', {'usererror': 'Invalid password for candidate account.'})
        
        
        
        
        # If email is not found in either table
        return render(request, 'user_login.html', {'emailerror':'Invalid email for candidate account.'})
    
    return render(request, 'user_login.html')


def home(request):
  
    return render(request, 'home.html')

def logout(request):
    if 'email' in request.session:
        del request.session['email']
    elif 'cp_email' in request.session:
        del request.session['cp_email']
    return redirect('home')

# Forget Password   # get all library rigarding mail 
   
from django.core.mail import send_mail 
def sendotp(request):
    if request.method == 'POST':
        email = request.POST['email']
        if regi.objects.filter(email=request.POST['email']).exists() or cp_register.objects.filter(cp_email=email).exists():# Get the email from the form
            otp = random.randint(1111, 9999)
            send_mail(
                        'This is OTP verification mail',
                        f'Your OTP: {otp}',
                        'prajapatiyash168@gmail.com',  # Sender email
                        [email],  # Receiver email
                        fail_silently=False
                    )
            request.session['OTP'] = otp 
            request.session['email'] = email 
            # return render(request, 'otpverify.html', {'email': email})
            return redirect('otpverify')
        else:
            return render(request,'sendotp.html',{'email':request.POST['email']})
    else:
        return render(request,'sendotp.html')

   

def otpverify(request):
    if request.method == 'POST':  
        enterdotp=int(request.POST['otp1'])
        if int(request.session['OTP']) == enterdotp:
            print('hello')

            # return render(request,'password.html',{'otpverify':'otp verified'})
            return redirect('password')
         
        else:
            return render(request, 'otpverify.html')
    else:
        return render(request, 'otpverify.html')
        
        


def password(request):
    if request.method == 'POST':
        password = request.POST['password']
        
        email = request.session['email']
        if regi.objects.filter(email=email).exists():
            print('11111')
            user = regi.objects.get(email=email)
            user.password = make_password(password)
            print('22222')

            user.save()
            print('33333')

            del request.session['OTP']
            del request.session['email']
            print('44444')
            return redirect('login')
        elif cp_register.objects.filter(cp_email=email).exists():
            company = cp_register.objects.get(cp_email=email)
            company.cp_password = make_password(password)
            company.save()
            del request.session['OTP']
            del request.session['email']
            return redirect('login')
    else:
            return render(request, 'password.html', {'error': 'Password and confirm password do not match!'})
    

    
  
          
            



