from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import DetailView, ListView

# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    # template_name = "notes/notes_detail.html" #I don't know why it works without including this line