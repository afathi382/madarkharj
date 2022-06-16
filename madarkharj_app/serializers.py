from asyncore import write
import email
from lib2to3.pgen2 import token
from tkinter.ttk import Style
from unicodedata import name
from rest_framework import serializers
from django.contrib.auth.models import User
import django.contrib.auth.password_validation as validators
from .models import Comment, Factor, Group, Profile
from django.core.validators import validate_email
from rest_framework_simplejwt.tokens import RefreshToken



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


class UsereSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 
        
        

class GroupSerializer(serializers.ModelSerializer):
    # owner= ProfileSerializer(read_only=True)
    class Meta:
        model = Group
        fields = '__all__'   
        


