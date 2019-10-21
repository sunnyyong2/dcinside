from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Feed(models.Model):
    content = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    image = ProcessedImageField(
        processors= [ResizeToFill(300,300)],
        format= 'JPEG',
        options= {'quality':90},
        upload_to='feeds'
    )
