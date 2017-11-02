from django.db.models import *
from django.contrib.auth.models import User
from django.urls import reverse

class Note(Model):
    user = ForeignKey(User, unique=False)
    title = CharField(max_length=200)
    content = CharField(max_length=2000,blank=True )
    dateAndTime = DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return ("By: " + self.user.username + " | " + self.title + ": " + self.content + " Date: " +str(self.dateAndTime.date()) + " | Time: " + str(self.dateAndTime.time()))




