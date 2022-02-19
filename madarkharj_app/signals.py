from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .serializers import GroupSerializer, ProfileSerializer

from .models import Group, Group_Profiles


# @receiver(post_save, sender=Group)
# def create_group_profiles(sender, instance, created , **kwargs):
    
    
#     print(instance.owner)
#     if created :
#         print(created)
        
#         serializer = GroupSerializer(data=instance)  
#         # print(serializer.members)      
#         if serializer.is_valid():
#             print(serializer.owner)
#             print('-----')
#             print(serializer.members)
#             # serializer.save()
           
      
#         print(instance.members)
#         print('--------')
        
        
        
#     else:
#         pass
    


# post_save.connect(create_group_profiles, sender=Group)