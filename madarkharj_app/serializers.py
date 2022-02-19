from asyncore import write
import email
from tkinter.ttk import Style
from unicodedata import name
from rest_framework import serializers
from django.contrib.auth.models import User
import django.contrib.auth.password_validation as validators
from .models import Comment, Factor, Group, Profile
from django.core.validators import validate_email

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','owner', 'factor', 'description', 'created', 'updated']
        


class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factor
        fields = '__all__'
     


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__' 
        
        

class GroupSerializer(serializers.ModelSerializer):
    # owner= ProfileSerializer(read_only=True)
    class Meta:
        model = Group
        fields = '__all__'   
        

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password= serializers.CharField(style={'input_type': 'confirm_password'}, write_only=True)
    class Meta:
        model = User
        fields =  ['username','password', 'confirm_password']
        
        extra_kwargs = {
            'password': {'write_only': True},
            
        }
        
    def validate(self, data):
        password=data['password']
        confirm_password=data['confirm_password']
        validators.validate_password(password=password)
        
        if password != confirm_password :
            raise serializers.ValidationError('confirm_password must match!')
        return data
    
    def validate_username(self, username):
        if validate_email(username) is not None:
            raise serializers.ValidationError("Invalid email")
        
        return username
    
    def create(self, validated_data):
        user_obj= User(username= validated_data['username'])
        user_obj.set_password(validated_data['password'])
        print(user_obj)
        user_obj.save()
        if Profile.objects.filter(email=validated_data['username']).exists():
            profile_obj=Profile.objects.get(email=validated_data['username'])
            setattr(profile_obj, 'user', user_obj)
            # profile_obj.set_user(user_obj)
            profile_obj.save()
        else:
            email= validated_data['username']
            profile_obj=Profile(email=email , name= email.split("@")[0])
            setattr(profile_obj, 'user', user_obj)
            # profile_obj.set_user(user_obj)
            profile_obj.save()
            
                    
        return user_obj

