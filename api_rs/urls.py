from django.urls import path
from api_rs.views import ChannelMetadata

urlpatterns = [   
 
   # internal chehk
   path('metadata', ChannelMetadata.as_view()),

]
