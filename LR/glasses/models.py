from django.db import models

class person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    username = models.CharField(max_length=150, unique=True)
    fullname = models.CharField(max_length=150, default="")
    email = models.EmailField(default="")
    phone = models.CharField(max_length=10, default="")  
    password = models.CharField(max_length=100, default="")
    confirmpassword = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
<<<<<<< HEAD
    otp=models.CharField(max_length=4,default='', null=True, blank=True)
    
    def __str__(self):
        return f"{self.username} {self.fullname} {self.email} {self.phone} {self.gender} {self.otp}"
=======
    country = models.CharField(max_length=10,default="")

    def __str__(self):
        return f"{self.username} {self.fullname} {self.email} {self.phone} {self.gender} {self.country}"
>>>>>>> 9ce8bb257e5a607b608763439900e8f6ff6be1f3
