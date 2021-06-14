import django_filters
from django_filters import DateFilter
from .models import *

class EntryFilter(django_filters.FilterSet):
    class Meta:
        model = Entry
        fields = ['Name_of_animal', 'Last_Name','date_in','date_out','date_groom','Kennel','Food_Location','Meds','Checked_in']
       # exclude = ['First_Name']

