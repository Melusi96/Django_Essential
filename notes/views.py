from django.shortcuts import render
from django.http import Http404

from .forms import NotesForm
from .models import Notes
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes' #redirects the user to other created notes
    form_class = NotesForm

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes' #redirects the user to other created notes
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    context_object_name = "note"
    template_name = 'notes/notes_delete.html'
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = '/admin'

    '''Displaying only the logged user data'''
    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    # template_name = "notes/notes_detail.html" #I don't know why it works without including this line