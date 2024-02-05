from rest_framework import serializers
from .models import person
import random


class personSerializer(serializers.ModelSerializer):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    gender = serializers.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = person
        fields = [
            "username",
            "fullname",
            "email",
            "phone",
            "password",
            "confirmpassword",
            "gender",
            "country",
        ]

    def create(self, validated_data):
        gender = validated_data.pop("gender")
        validated_data["gender"] = gender.lower()
        return person.objects.create(**validated_data)


class forgetserializer(serializers.ModelSerializer):
   
    class Meta:
        model = person 
        fields = '__all__'
     