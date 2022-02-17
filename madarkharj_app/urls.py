
from django.urls import path
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from .views import CommentListCreate, CommentRetrieveUpdateDestroy, Factor_Comments, FactorListCreate, FactorRetrieveUpdateDestroy, Group_Factors, GroupListCreate, GroupRetrieveUpdateDestroy, Profile_Groups, ProfileListCreate, ProfileRetrieveUpdateDestroy, calculator

urlpatterns = [
    
    # path('swagger-ui/', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='swagger-ui'),
    
    # path('swagger/' , schema_view),
     path('openapi/', get_schema_view(
        title="madarkharj API",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),
     
     path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    
    
    path('comment/', CommentListCreate.as_view()),
    path('comment/<pk>', CommentRetrieveUpdateDestroy.as_view()),
    path('factor_comments/', Factor_Comments.as_view()),
    
    
    path('factor/', FactorListCreate.as_view()),
    path('factor/<pk>', FactorRetrieveUpdateDestroy.as_view()),
    path('group_factors/', Group_Factors.as_view()),
    
    
    path('group/', GroupListCreate.as_view()),
    path('group/<pk>', GroupRetrieveUpdateDestroy.as_view()),
    path('profile_groups/', Profile_Groups.as_view()),
    
    
    path('profile/', ProfileListCreate.as_view()),
    path('profile/<pk>', ProfileRetrieveUpdateDestroy.as_view()),
    
    path('calc/', calculator ),
    
    
]