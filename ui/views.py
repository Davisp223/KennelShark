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


#entries
class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'ui/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'entries'
    ordering = ['-date_posted']


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Entry = self.get_object()
        if self.request.user == Entry.author:
            return True
        return False


class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    success_url = '/ui/'

    def test_func(self):
        Entry = self.get_object()
        if self.request.user == Entry.author:
            return True
        return False