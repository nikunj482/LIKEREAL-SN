from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from .serializers import personSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from .models import person
from django.contrib import messages
import random
from django.core.mail import EmailMessage


class RegisterView(generics.CreateAPIView):
    serializer_class = personSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "register.html"

    def get(self, request):
        serializer = personSerializer()
        return render(request, self.template_name, {"serializer": serializer})

    def post(self, request):
        username = request.data.get("username")
        if person.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data.get("phone")
            password = serializer.validated_data.get("password")
            confirm_password = serializer.validated_data.get("confirmpassword")
<<<<<<< HEAD
            
            if len(phone) != 10 :
                messages.error(request,"phone number is not Valid")
=======

            if len(phone) != 10:
                messages.error(request, "phone number is not Valid")
>>>>>>> 9ce8bb257e5a607b608763439900e8f6ff6be1f3
                return redirect("register")

            if password != confirm_password:
                messages.error(request, "Passwords do not match")
                return redirect("register")
            serializer.save()
<<<<<<< HEAD
=======

>>>>>>> 9ce8bb257e5a607b608763439900e8f6ff6be1f3
            return redirect("login")
        return render(request, self.template_name, {"serializer": serializer})


class LoginView(generics.CreateAPIView):
    serializer_class = personSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "login.html"
<<<<<<< HEAD
    
=======

>>>>>>> 9ce8bb257e5a607b608763439900e8f6ff6be1f3
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = person.objects.filter(username=username).first()
            if user and user.password == password:
                messages.success(request, "Login successful")
                request.session["username"] = username
                return redirect("home")
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Please provide username and password")
<<<<<<< HEAD
            return render(request, self.template_name)
=======
        return render(request, self.template_name)
>>>>>>> 9ce8bb257e5a607b608763439900e8f6ff6be1f3


class ForgotView(generics.CreateAPIView):
<<<<<<< HEAD
    serializer_class=forgetserializer
=======
>>>>>>> 9ce8bb257e5a607b608763439900e8f6ff6be1f3
    renderer_classes = [TemplateHTMLRenderer]
    tempalte_name = "forgot.html"

    def get(self, request):
        return render(request, self.tempalte_name)

<<<<<<< HEAD
    def post(self,request):
        email=request.POST.get("email")
        print('email:',email)
        try:
            user=person.objects.filter(email=email)
            request.session["email"] = email
            print(user)
        except:
            return redirect('forgot')
        
        if user:
            otp = str(random.randint(1000,9999))
            request.session["otp"] = otp
            print("otp :", otp)
            email = EmailMessage(body=otp,to=[email])
            email.send()
            return redirect('otppage')
        else:
            messages.error(request, "Email Not Valid")
            return redirect('forgot')   
        
=======

>>>>>>> 9ce8bb257e5a607b608763439900e8f6ff6be1f3
class OtpView(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "otp.html"

    def get(self, request):
        return render(request, self.template_name)

<<<<<<< HEAD
    def post(self,request):
        enter_otp=request.POST.get('enter_otp')
        otp = request.session.get("otp")
        if otp != enter_otp:
            messages.error(request," Invalid OTP")
            return redirect('otppage')
        else:
            return redirect('reset')
=======
>>>>>>> 9ce8bb257e5a607b608763439900e8f6ff6be1f3

class ResetView(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "reset.html"
    
    def get(self, request):
        return render(request, self.template_name)
<<<<<<< HEAD

    def post(self, request):
        new_password = request.POST.get("new_password")
        confirmpassword = request.POST.get("confirm__password")
        print("new_password:",new_password)
        print("confirm_password:",confirmpassword)
        email= request.session.get("email")
        
        try:
            user=person.objects.filter(email=email)
        except:
            return redirect('forgot')
        
        if new_password != confirmpassword:
            messages.error(request,"password Does't match")
            return redirect('reset')
        user = request.user
        if user:
            user.set_password(new_password)
            user.save()
            return redirect('login')
        return render(request,self.template_name)
        
=======
    
    def Post(self, request):
        email = request.POST.get("email")
        


>>>>>>> 9ce8bb257e5a607b608763439900e8f6ff6be1f3
class HomeView(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "home.html"

    def get(self, request):
        return render(request, self.template_name)
