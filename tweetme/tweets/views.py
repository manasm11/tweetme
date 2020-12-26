from django.shortcuts import Http404, HttpResponse, redirect, render
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
    'isUser':False,
    'response':[x.serialize() for x in TweetModel.objects.all()]
  }
  return JsonResponse(data)

def tweet_create_view(request, *args, **kwargs):
    template_name = "components/form.html"
    context = {}
    print("*****post data id ", request.POST)
    next_url = request.POST.get("next") or None
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # Play with onj
        obj.save()
        if request.is_ajax():
            print(obj)
            return JsonResponse(obj.serialize(), status=201)
        if next_url:
            return redirect("/")
        form = TweetForm()
    context['form'] = form
    return render(request, template_name, context=context)
    
