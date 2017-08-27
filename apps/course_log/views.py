from django.shortcuts import render, redirect
from .models import Course
from django.contrib.messages import error
from django.core.urlresolvers import reverse

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'course_log/index.html', context)

def add(request):
    errors = Course.objects.validate(request.POST)
    if len(errors) > 0:
        for tag, message in errors.iteritems():
            error(request, message, extra_tags=tag)
        return redirect('/')
    Course.objects.create(
        name=request.POST['name'],
        desc=request.POST['desc']
    )
    return redirect('/')

def remove(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'course_log/remove.html', context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect(reverse('home'))
