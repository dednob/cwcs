import datetime
from django.db import models
import uuid
# from projects.models import Projects
# from campaign.models import Campaigns
# from areaofwork.models import Areaofwork


# Create your models here.
def generate_filename(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = "cwcspublications_%s.%s" % (uuid.uuid4(), extension)
    return new_filename


class Publications(models.Model):
    author_name = models.CharField(max_length=500, null = True, blank=True)
    # details = models.TextField(null=True, blank=True)
    # slug = models.SlugField(max_length=500, null=True, unique=True)
    pdf = models.FileField(upload_to=generate_filename, null=True)
    # project = models.ForeignKey(Projects, default=None, on_delete=models.CASCADE, related_name="gallery")
    


    
    
