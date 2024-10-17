from rest_framework import serializers

from .models import Question,Video

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ("question_text","pub_date","answer")
        
class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ["title_video","url"]