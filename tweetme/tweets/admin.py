from django.contrib import admin
from tweets.models import TweetModel, TweetLikeModel
# Register your models here.


class TweetLikesAdmin(admin.TabularInline):
    model = TweetLikeModel

class TweetAdmin(admin.ModelAdmin):
    search_fields = ['content', 'user__username']
    list_display = ['__str__', 'user']
    inlines = [TweetLikesAdmin]
    class Meta:
        model = TweetModel

admin.site.register(TweetModel, TweetAdmin)