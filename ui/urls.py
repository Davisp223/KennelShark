from . import views
from django.urls import path
from ui import views as ui_views
from .views import (
    EntryListView,
    EntryDetailView,
    EntryCreateView,
    EntryUpdateView,
    EntryDeleteView,
    PrintView,


    
)
urlpatterns = [
    path('', EntryListView.as_view(), name='index'),
    

    #entry
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
    path('entry/<int:pk>/', PrintView.as_view(), name='entry-print'),
    path('entry/new/', EntryCreateView.as_view(), name='entry-create'),
    path('entry/<int:pk>/update/', EntryUpdateView.as_view(), name='entry-update'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry-delete'),

]
