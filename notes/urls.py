from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from . import views
app_name = "notes"

urlpatterns = [
    url(r'^$', login_required(views.NotesList.as_view()), name='index'),
    url(r'^login/$', login, {'template_name': 'notes/login.html'}, name='login'),
    url(r'^logout/$', login_required(logout), name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', login_required(views.profile), name='profile'),
    url(r'^create_note/$',login_required(views.CreateNote.as_view()), name="create_note"),
    url('^update_note/(?P<pk>[0-9]+)$', login_required(views.UpdateNote), name='update_note'),
    url(r'^delete_note/(?P<pk>[0-9]+)$', views.deleteNote, name='delete_note'),

]