from django.shortcuts import render,redirect,get_object_or_404
from .models import Course
from .forms import CommentForm
from marketing.models import Signup
# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST("email")
        new_signup = Signup()
        new_signup.email=email
        new_signup.save()
    return render(request,'index.html')

def courses(request):
    return render(request,'courses.html')

def english(request):
    course_list = Course.objects.filter(categories__title='English')

    context = {
        'course_list':course_list
    }
    return render(request,'english.html',context)


def math(request):
    course_list = Course.objects.filter(categories__title='Math')

    context = {
        'course_list':course_list
    }
    return render(request,'math.html',context)

def course_detail(request,course_id):                            #we have come here w the help of reverse
    course = get_object_or_404(Course, id=course_id)  #this page would now help me to redirect to course deatil page and thus details can be used
    form = CommentForm(request.POST or None)
    if request.method == "POST" :
        if form.is_valid():
            form.instance.user = request.user
            form.instance.course = course                   #whichever user has loggged in we get the details of that
            form.save()
            return redirect('course_detail',course_id=course_id)
    context = {                                                  #we can see how we used reverse to redirect wout hardcoding urls anywhere
        'course':course,
        'form':form
    }
    return render(request,'course_detail.html',context)

def contact(request):
    return render(request,'contact.html')