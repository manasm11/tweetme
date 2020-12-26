from django.db import models
import random

def _get_text_from_field(field):
    if isinstance(field, str):
        return field[:32]
    return str(field)

# Create your models here.
class TweetModel(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        if self.content:
            return _get_text_from_field(self.content)
        return _get_text_from_field(self.image)
    
    def serialize(self):
        return {
            "id": self.id,
            "content":self.content,
            "likes":random.randint(0,500),
        }