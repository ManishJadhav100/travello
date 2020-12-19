from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination
from .models import News_post
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def index(request):
    dests = Destination.objects.all()

    posts = News_post.objects.all()


    mydict = {'dests': dests, 'posts': posts}
    return render(request, 'index.html', context=mydict)


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name + "'" + 's' + ' feedback',
            message,
            message_email,
            ['manishjadhav1200@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Your feedback received successfully')
        return render(request, 'contact.html', {})
    else:
        return render(request, 'contact.html', {})



def destinations(request):
    return render(request, 'destinations.html', {})


def news(request):
    return render(request, 'news.html', {})


def handler404(request, exception):
    data = {}
    return render(request, '404.html', status=404)


# def handler500(request, exception):
#     data = {}
#     return render(request, '500.html', status=404)


