from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name='index'),
    path('News', views.News, name='News'),
    path('AlienwareDoc', views.DocA, name='AlienwareDoc'),
    path('BlogDoc', views.DocB, name='BlogDoc'),
    path('JourneyDoc', views.JourneyDoc, name='JourneyDoc'),
    path('AiDoc', views.AiDoc, name='AiDoc')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
