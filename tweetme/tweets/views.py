# standard
import random

# django
from django.shortcuts import Http404, HttpResponse, redirect, render
from django.http import JsonResponse
from django.conf import settings

# third_party
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# local
from .models import TweetModel
from .forms import TweetForm
from .serializers import TweetSerializer, TweetActionSerializer

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'tweets/home.html')

@api_view(['GET'])
def tweet_detail_view(request, tweet_id,  *args, **kwargs):
    qs = TweetModel.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({'message':f'Tweet not found'}, status=404)
    serializer = TweetSerializer(qs.first())
    return Response(serializer.data, status=200)

@api_view(['GET'])
def tweet_list_view(response, *args, **kwargs):
  qs = TweetModel.objects.all()
  serializer = TweetSerializer(qs, many=True)
  return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({'message':'Invalid Tweet'}, status=400)

@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    qs = TweetModel.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({'message':'Tweet not found'}, status=404)
    if not qs.first().user == request.user:
        return Response({'message':"You aren't authorized to delete this post"}, status=401)
    qs.first().delete()
    return Response({'message':'Tweet removed successfully.'}, status=200)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action_view(request, *args, **kwargs):
    # serializer = TweetActionSerializer(data=request.GET)
    serializer = TweetActionSerializer(data=request.POST)
    serializer.is_valid(raise_exception=True)
    tweet_id = serializer.data['id']
    if not TweetModel.id_exists(tweet_id):
        return Response({'message':'Tweet not found'}, status=404)
    obj = TweetModel.objects.filter(id=tweet_id).first()
    action = serializer.get('action')
    if action == 'like':
        obj.likes.add(request.user)
    elif action == 'unlike':
        obj.likes.remove(request.user)
    elif action == 'retweet':
        # Todo: Retweeting needs to be implemented.
        pass
    return Response({'message':'Tweet action success'}, status=200)