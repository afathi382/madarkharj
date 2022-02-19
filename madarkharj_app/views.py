
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.validators import validate_email
from django.db.models import Q

from .utils import factor_calculator, is_valid_uuid

from .serializers import CommentSerializer, FactorSerializer, GroupSerializer, ProfileSerializer, RegistrationSerializer

from .models import Comment, Factor, Group, Profile


# Create your views here.

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []
    
    # def get_queryset(self):
    #     factor_id=self.request.query_params['pk']
    #     print(factor_id)
        
    #     return get_object_or_404(Comment.objects.filter(factor=factor_id))
        
    


class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []
    
    





class Factor_Comments(APIView):
    
    permission_classes = []
    
    # get {"factor_id": "8927e8a0-ee37-4b22-91b5-440bac1a52e8"} and post comments of this factor
    def post(self, request):
                
        try:
            factor_id=request.data['factor_id']
            if not is_valid_uuid(factor_id):
                return Response('factor_id is not valid uuid', status=status.HTTP_400_BAD_REQUEST)  
            
        except:
            return Response('factor_id is required', status=status.HTTP_400_BAD_REQUEST)
        else:
            if Factor.objects.filter(pk=factor_id).exists():
                comments=Comment.objects.filter(factor=factor_id)
                serializer= CommentSerializer(comments, many= True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('factor does not exist', status=status.HTTP_404_NOT_FOUND)
        
    
    
class FactorListCreate(generics.ListCreateAPIView):
    queryset = Factor.objects.all()
    serializer_class = FactorSerializer
    permission_classes = []
    

class FactorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factor.objects.all()
    serializer_class = FactorSerializer
    permission_classes = []
    
    
    

class Group_Factors(APIView):
    
    permission_classes = []
    
    # get {"group_id": "4bf93138-450c-4d35-9d3d-7b5293abd4e6"} and post factors of this group
    def post(self, request):
                
        try:
            group_id=request.data['group_id']
            if not is_valid_uuid(group_id):
                return Response('group_id is not valid uuid', status=status.HTTP_400_BAD_REQUEST)  
            
        except:
            return Response('group_id is required', status=status.HTTP_400_BAD_REQUEST)
        else:
            if Group.objects.filter(pk=group_id).exists():
                factors=Factor.objects.filter(group=group_id)
                serializer= FactorSerializer(factors, many= True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('group does not exist', status=status.HTTP_404_NOT_FOUND)
        
    
    


class GroupListCreate(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = []
    
    def post(self, request):
        
        try:
            true_members=[]
            for member in request.data['members']:
                
                if is_valid_uuid(member): 
                    true_members.append(member)
                elif validate_email(member) is None:
                    if not Profile.objects.filter(email= member).exists():
                        serializer = ProfileSerializer(data={'name': member.split("@")[0],'email': member})
                        
                        if serializer.is_valid():
                            print(serializer)
                            serializer.save()
                            true_members.append(str(Profile.objects.get(email=member).id))
                    elif Profile.objects.filter(email= member).exists():
                        true_members.append(str(Profile.objects.get(email=member).id))
                    
                else:
                    return Response('member or email is not valid', status=status.HTTP_400_BAD_REQUEST) 
          
               
        except:
            return Response('member or email is not valid', status=status.HTTP_400_BAD_REQUEST)
        else:
            group_data=request.data
            group_data['members']= true_members
           
            serializer = GroupSerializer(data=group_data)        
            if serializer.is_valid():
               
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                  
       
        return Response(request.data) 
         
    


class GroupRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = []
    
    


class Profile_Groups(APIView):
    
    permission_classes = []
    
    # get {"profile_id": "bb40d81f-1a6c-40cb-99ee-a80cdc177a65"} and post groups of this profile
    def post(self, request):
                
        try:
            profile_id=request.data['profile_id']
            if not is_valid_uuid(profile_id):
                return Response('profile_id is not valid uuid', status=status.HTTP_400_BAD_REQUEST)  
            
        except:
            return Response('profile_id is required', status=status.HTTP_400_BAD_REQUEST)
        else:
            if Profile.objects.filter(pk=profile_id).exists():
                groups=Group.objects.filter(members=profile_id)
                serializer= GroupSerializer(groups, many= True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('profile does not exist', status=status.HTTP_404_NOT_FOUND)
        
    
 
 

class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = []
         
 
class ProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = []
    
    


class Profile_Group_amount(APIView):
    
    permission_classes = []
    
    def post(self, request):
                
        try:
            profile_id=request.data['profile_id']
            group_id=request.data['group_id']
            if not is_valid_uuid(profile_id):
                return Response('profile_id or group_id is not valid uuid', status=status.HTTP_400_BAD_REQUEST)  
            
        except:
            return Response('profile_id and group_id are required', status=status.HTTP_400_BAD_REQUEST)
        else:
            if (Profile.objects.filter(pk=profile_id).exists() and Group.objects.filter(pk=group_id).exists()):
                factors=Factor.objects.filter(Q(share_with__id= profile_id , group= group_id) | Q(owner= profile_id , group=group_id)).distinct()
                
                profile_in_group_amount= factor_calculator(factors=factors, profile_id=profile_id)                                         
                
                return Response(profile_in_group_amount, status=status.HTTP_200_OK)
            else:
                return Response('profile or group does not exist', status=status.HTTP_404_NOT_FOUND)
        


class Profile_amount(APIView):
    
    permission_classes = []
    
    def post(self, request):
                
        try:
            profile_id=request.data['profile_id']
            if not is_valid_uuid(profile_id):
                return Response('profile_id is not valid uuid', status=status.HTTP_400_BAD_REQUEST)  
            
        except:
            return Response('profile_id are required', status=status.HTTP_400_BAD_REQUEST)
        else:
            if Profile.objects.filter(pk=profile_id).exists():
                factors=Factor.objects.filter(Q(share_with__id= profile_id ) | Q(owner= profile_id)).distinct()
                
                profile_amount= factor_calculator(factors=factors, profile_id=profile_id)                                       
                
                return Response(profile_amount, status=status.HTTP_200_OK)
            else:
                return Response('profile does not exist', status=status.HTTP_404_NOT_FOUND)
            



class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = []
            
            
            

        
    
    
    
    
 