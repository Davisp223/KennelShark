from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,  
)
from django.contrib.auth.decorators import login_required
from .models import Entry
from .filters import EntryFilter



#class EntryListView(LoginRequiredMixin, ListView):
    #model = Entry
    #template_name = 'ui/index.html'  # <app>/<model>_<viewtype>.html
    #context_object_name = "entries"
    #ordering = ['-date_out']

@login_required
def index(request):
    entry = Entry.objects.all()
    myFilter = EntryFilter(request.GET, queryset=entry)
    entry = myFilter.qs

    context = {'entry':entry, 'myFilter':myFilter,

    }
    return render(request, 'ui/index.html',context)
    
  

    


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    fields = [
        'kennel'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)





class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = [
        'First_Name','Last_Name','Name_of_animal','Type_of_animal','Sex','Age','Breed','Color','Groomer','Weight','DCV_DLX','GCD','Home','Cell','Work','Vet','Emer','DHLPP','Rabies','Bordetella','Remarks','Our_or_own_food','Food_Location','Feeding','Feeding2',
        'Meds','Rot','Starts','Ends','Mrn','Eve','Dosage'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin,  UpdateView):
    model = Entry
    fields = [
        'First_Name','Last_Name','Name_of_animal','Type_of_animal','Sex','Age','Breed','Color','Groomer','Weight','DCV_DLX','GCD','Home','Cell','Work','Vet','Emer','DHLPP','Rabies','Bordetella','Remarks','Our_or_own_food','Food_Location','Feeding','Feeding2',
        'Meds','Rot','Starts','Ends','Mrn','Eve','Dosage'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EntryBoardView(LoginRequiredMixin,  UpdateView):
    model = Entry
    fields = [
    'date_in','date_out','date_groom','Sex','Age','Groomer','Weight','DCV_DLX','GCD','Vet','Emer','DHLPP','Rabies','Bordetella','Remarks','Our_or_own_food','Food_Location','Feeding','Feeding2',
        'Meds','Rot','Starts','Ends','Mrn','Eve','Dosage'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EntryKennelView(LoginRequiredMixin,  UpdateView):
    model = Entry
    fields = [
    'Kennel','Food_Location'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EntrycheckinView(LoginRequiredMixin,  UpdateView):
    model = Entry
    fields = [
    'Checked_in'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class EntryDeleteView(LoginRequiredMixin,  DeleteView):
    model = Entry
    success_url = '/ui/'




