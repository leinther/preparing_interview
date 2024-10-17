from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from django.urls import reverse
from django.db.models import F
from django.views import generic 
from django.utils import timezone
from .serializers import QuestionSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser



class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    
def vote (request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,"polls/detail.html",
            {"question": question,"error_message": "You didn't select a choice.",},)
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def mail (request):
    context = {}
    form = PersonsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect ("polls:email")
    context ["form"] = form
    return render (request,"polls/static/polls/images",context)


def file_downloader(request):
    #image = FileManager.objects.filter(pk=1)
    if request.POST or request.FILES:
        table = FileManager(file=request.FILES["file"],title=request.POST["title"])
        table.save()
        return redirect ("polls:file")
    return render(request,"polls/upload.html")


def watchPhoto(request):
    photo = FileManager.objects.all()
    return render (request, "polls/view.html",{"photo":photo}) 

def video_upload(request):
    if request.POST or request.FILES:
        video = Video (url = request.FILES["file"], title_video = request.POST["title"])
        video.save()
        return redirect ("polls:watch")
    return render(request,"polls/video.html")      


def video_watch(request):
    video = Video.objects.all()
    return render(request,"polls/youtube.html", {"video":video})

# API 

class QuestionSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
  
    
    
  
    
    
