from django.db import models
from django.core.exceptions import ValidationError
import random
from django.conf import settings

def _get_text_from_field(field):
    if isinstance(field, str):
        return field[:32]
    return str(field)

# Create your models here.
User = settings.AUTH_USER_MODEL

class TweetLikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('TweetModel', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if TweetLikeModel.objects.filter(user=self.user, tweet=self.tweet).exists():
            raise ValidationError('User already liked the tweet')
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class TweetModel(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='tweet_likes', through=TweetLikeModel, blank=True)

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
    @classmethod
    def id_exists(cls, id):
        return cls.objects.filter(id=id).exists()