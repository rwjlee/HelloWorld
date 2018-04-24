from django.shortcuts import render, redirect
from apps.travel.models import User
from django.contrib import messages

def index(request):
    return render(request, 'travel/index.html')

def planes(request):
    return render(request, 'travel/planes.html')

def trains(request):
    return render(request, 'travel/trains.html')

def automobiles(request):
    return render(request, 'travel/automobiles.html')

def boats(request):
    return render(request, 'travel/boats.html')

def login(request):
    if request.method == 'POST':
        html_email = request.POST['html_email']
        html_password = request.POST['html_password']
        try:
            user = User.objects.get(email = html_email)
            if user.password == html_password:
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                return redirect('travel:index')
            else:
                messages.error(request, 'Invalid Login')
                return redirect('travel:login')

        except:
            messages.error(request, 'No such user')
            return redirect('travel:login')

    return render(request, 'travel/login.html')

def logout(request):
    request.session.clear()
    return redirect('travel:index')

def register(request):
    if 'user_id' not in request.session:
        return redirect('travel:index')

    if request.method == 'POST':
        if len(request.POST['html_password']) > 0 and request.POST['html_password']==request.POST['html_confirm']:
            try:
                user = User.objects.create(email = request.POST['html_email'], password = request.POST['html_password'])
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                
            except:
                messages.error(request, 'This is wrong')
                return redirect('travel:register')

        return redirect('travel:index')

    return render(request, 'travel/register.html')