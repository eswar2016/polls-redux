from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers

from .models import Question, Choice


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

