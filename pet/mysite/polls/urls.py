from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'questions',views.QuestionSet)




app_name="polls"
urlpatterns = [
    path("",views.IndexView.as_view(), name = "index"),
    path ("<int:pk>/",views.DetailView.as_view(),name = "detail"),
    path("<int:pk>/results/",views.ResultsView.as_view() ,name = "results"),
    path("<int:question_id>/vote/",views.vote,name = "vote"), 
    path("mail/",views.mail, name = "email"),
    path ("file/",views.file_downloader,name="upload"),
    path ("view/",views.watchPhoto, name = "file"),
    path ("video/",views.video_upload, name = "video"),
    path ("watch",views.video_watch, name = "watch"),
    
    
    
    path("",include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
