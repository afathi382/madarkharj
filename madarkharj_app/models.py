from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.deletion import CASCADE




# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email=models.EmailField(null=False, blank=False)
    phone=models.CharField(max_length=11, null=True, blank=True)
    total_amount= models.FloatField(default=0, editable=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    
    
    
    def __str__(self):
        return self.name
    



class Group(models.Model):
    GROUP_TYPE_CHOICES = (
        ('apartment', 'apartment'),
        ('house', 'house'),
        ('trip', 'trip'),
        ('other', 'other'),
    )
    
    name = models.CharField(max_length=500)
    owner= models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='group_owner', null=True, blank=True)
    members= models.ManyToManyField(Profile)
    group_type= models.CharField(max_length=100, choices=GROUP_TYPE_CHOICES)
            
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.name


class Group_Profiles(models.Model):
    group= models.ForeignKey(Group, on_delete=models.CASCADE)
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount= models.FloatField(default=0)
      
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    

    

class Factor(models.Model):
    title = models.CharField(max_length=255)
    owner= models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='factor_owner', null=True, blank=True)
    price= models.FloatField(default=0)
    group= models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=False)
    share_with= models.ManyToManyField(Profile)   
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.title




class Comment(models.Model):
    owner= models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    factor= models.ForeignKey(Factor, on_delete=models.CASCADE, null=True, blank=True)
    description= models.TextField()   
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    
    


    
    
    







