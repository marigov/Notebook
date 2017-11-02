from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib.auth import login, authenticate, update_session_auth_hash
from search_views.filters import BaseFilter
from search_views.views import SearchListView
from django.contrib import messages

from notes.models import Note
from .forms import CreateNoteForm,SignUpForm, NotesSearchForm


def index(request):
    return render(request, 'notes/index.html', {"notes": Note.objects.all()})


def profile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('notes:index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'notes/profile.html', {
        'form': form
    })


class CreateNote(FormView):
    template_name = 'notes/create_note.html'
    success_url = '/'
    form_class = CreateNoteForm

    def form_valid(self, form):
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        note = Note()
        note.title = title
        note.content = content
        note.user = self.request.user
        note.save()

        return super(CreateNote, self).form_valid(form)

def UpdateNote(request, pk):
    myNote = get_object_or_404(Note, pk = pk)
    form = CreateNoteForm(initial = {"title":myNote.title, "content": myNote.content})
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            myNote.title = form.cleaned_data['title']
            myNote.content = form.cleaned_data['content']
            myNote.save()
        return redirect("/")
    return render(request, 'notes/update_note.htmL', {'form':form, "note":myNote})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'notes/signup.html', {'form': form})


class NotesListFilter(BaseFilter):
    search_fields = {
        'search_text': ['title', 'content'],
    }

class NotesList(SearchListView):
    model = Note
    paginate_by = 5  # Generate pages of 30 elements in the table
    template_name = "notes/index.html"
    form_class = NotesSearchForm
    filter_class = NotesListFilter

def deleteNote(request, pk):
    noteDelete = get_object_or_404(Note, pk=pk).delete()
    return redirect('notes:index')
