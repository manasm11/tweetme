from django.db import models

def _get_text_from_field(field):
    # assert isinstance(field, None)
    print(type(field))
    return field[:32]

# Create your models here.
class TweetModel(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        if self.content:
            return _get_text_from_field(self.content)
        return _get_text_from_field(self.image)