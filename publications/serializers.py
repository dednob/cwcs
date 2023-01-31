from rest_framework import serializers
from projects.serializers import *
from .models import Publications
# from projects.models import Projects

# from campaign.models import *

class PublicationsSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Publications
        fields = '__all__'



