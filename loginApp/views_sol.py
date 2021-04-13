from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, "index.html")

def register_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        User.objects.create(
            name = request.POST['name'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = pw_hash
        )
        messages.info(request, "User registered; log in now")
    return redirect('/')

def login_user(request):
    try:
        user = User.objects.get(email = request.POST['email'])
    except:
        messages.error(request, "Email address or password is incorrect")
        return redirect("/")
    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, "Email address or password is incorrect")
        return redirect("/")
    else:
        request.session['user_id'] = user.id
        request.session['user_email'] = user.email
        request.session['user_alias'] = user.alias
        return redirect('/books')

def logout(request):
    del request.session['user_id']
    del request.session['user_email']
    del request.session['user_alias']
    return redirect('/')

def single_user(request, user_id):
    user = User.objects.get(id = user_id)
    reviews = user.reviews.all()
    context = {
        'user': user,
        'reviews': reviews
    }
    return render(request, 'user.html', context)
