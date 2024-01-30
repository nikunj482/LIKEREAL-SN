from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from .serializers import personSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from .models import person
from django.contrib import messages


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
            password = serializer.validated_data.get("password")
            confirm_password = serializer.validated_data.get("confirmpassword")

            if password != confirm_password:
                messages.error(request, "Passwords do not match")
                return redirect("register")

            serializer.save()
            messages.success(request, "Registration successful")
            return redirect("login")

        return render(request, self.template_name, {"serializer": serializer})
