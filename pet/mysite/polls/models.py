from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    answer = models.TextField (verbose_name="Enter you think", max_length=500,default="")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
class Persons (models.Model):
    name = models.CharField(max_length=300)
    message = models.TextField()

class FileManager(models.Model):
    title = models.CharField(max_length=200,default="")
    file = models.ImageField(upload_to='media/')
    
class Video(models.Model):
    title_video = models.CharField(verbose_name="Title Video",max_length=200)
    url = models.FileField(verbose_name="Video", upload_to="media/")
    