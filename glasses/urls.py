from django.urls import path
from .views import RegisterView,LoginView,HomeView,ForgotView,OtpView,ResetView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', LoginView.as_view(), name='login'),    
    path('home/', HomeView.as_view(), name='home'),
    path('forgot/',ForgotView.as_view(),name='forgot'),
    path('otp/',OtpView.as_view(),name='otppage'),
    path('reset/',ResetView.as_view(),name='reset'),
]
