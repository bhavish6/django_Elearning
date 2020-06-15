from django.db import models
from django.contrib.auth import get_user_model
from tinymce import HTMLField
from django.urls import reverse

# Create your models here.

User = get_user_model()                                             #t's good future-proofing, in case you ever change the User model in your project. In real life, that's highly unlikely, but where it's *really important* to use get_user_model() is when you are writing reusable apps for distribution. If your app is intended to be dropped into any existing Django project, you have no idea what User model is in use by other people's projects.#
class Author(models.Model):                                          # This layer of abstraction makes it possible for re-usable apps that depend on some User model existing to work no matter what.class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)      #Cascade means when user is deleted ,delete the relationship
    profile_pic = models.ImageField()
    def __str__(self):
        return self.user.username



class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=20)
    Overview = models.TextField()
    Time = models.DateTimeField(auto_now_add=True)                      #automatically sets the field to now,current date used
    comment_count  = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)     #many to one relationship,this is child
    thumbnail = models.ImageField()
    content = HTMLField(null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):                      #Tells my model where the url of the particular model would exist
        return reverse('course_detail', kwargs={     #here, i pass the view name bec idw pass url hardcoding verytime,so it takes me to the url path which has the particular view
            'course_id':self.id
        })
    @property      #decorator used mostly buit in here
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)    #many to one relationship
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    course = models.ForeignKey('Course',related_name='comments',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
