from rest_framework import serializers
from projects.serializers import *
from .models import Gallery
from projects.models import Projects

# from campaign.models import *

class GallerySerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Gallery
        fields = '__all__'


class GalleryReadSerializer(serializers.ModelSerializer):
    
    project = serializers.SerializerMethodField('proj_title', read_only=True)

    def proj_title(self, obj):
        project_instance = Projects.objects.get(id = obj.project.id)
        return ProjectsGallerySerializer(project_instance).data
    
    class Meta:
        model = Gallery
        fields = '__all__'


class GallerySerializer_slider(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['image']
