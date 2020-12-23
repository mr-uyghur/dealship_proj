from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    # search_fields = Car.objects.values('model','city', 'year', 'body_style')
    model_search = Car.objects.values_list('model', flat = True).distinct()
    city_search = Car.objects.values_list('city', flat = True).distinct()
    year_search = Car.objects.values_list('year', flat = True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat = True).distinct()
    context = {
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        # 'search_fields': search_fields
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search': body_style_search,

    }

    return render(request, 'pages/home.html',context)

def about(request):
    teams = Team.objects.all()
    context = {
        'teams':teams,
    }
    return render(request,'pages/about.html', context)


def services(request):
    teams = Team.objects.all()
    context = {
        'teams':teams,
    }
    return render(request, 'pages/services.html',context)

def contact(request):
    # teams = Team.objects.all()
    # context = {
    #     'teams':teams,
    # }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = "You have a new message from Carzone website: " + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
                subject,
                message_body,
                'devuyghur1996@gmail.com',
                [admin_email],
                fail_silently=False,   
            )
        messages.success(request, "Thank you for contacting Carzone! We will get back to you as soon as we can.")
        return redirect('contact')
    return render(request, 'pages/contact.html')