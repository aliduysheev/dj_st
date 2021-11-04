from django.urls import path
from .views import SongsListView

urlpatterns = [
    path('songs-list/', SongsListView.as_view()),
]
