from rest_framework import serializers

from .models import Comment, Factor, Group, Profile

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
        

