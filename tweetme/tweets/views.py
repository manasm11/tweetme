from django.shortcuts import render, HttpResponse, Http404
from django.http import JsonResponse
from .models import TweetModel
from .forms import TweetForm
import random

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'tweets/home.html')

def tweet_detail_view(request, tweet_id,  *args, **kwargs):
    data = {'id':tweet_id}
    status = 200
    try:
        obj = TweetModel.objects.get(id=tweet_id)
        data['content'] = obj.content
    except :
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)

def tweet_list_view(response, *args, **kwargs):
  data = {
    'response':[{'id':x.id, 'content':x.content, 'isUser':False, 'likes':random.randint(0,999)} for x in TweetModel.objects.all()]
  }
  return JsonResponse(data)

def tweet_create_view(request, *args, **kwargs):
    template_name = "tweets/create.html"
    context = {}
    form = TweetForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TweetForm()
    context['form'] = form
    return render(request, template_name, context=context)
    
