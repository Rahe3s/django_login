from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from datetime import datetime




@login_required(login_url='login_page')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):   
    user_role = request.session.get('user_role', 'guest') 
    
    context = {
        'user_role': user_role,
        
    }
    return render(request, "home.html" , context    )



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['is_logged_in'] = True
            request.session['user_role'] = 'admin' if user.is_staff else 'user'
            response = redirect('home') 

            last_login_time = request.COOKIES.get('last_login_time')
            request.session['last_login_time'] = last_login_time or 'First time login'
            response.set_cookie('last_login_time', datetime.now().strftime('%Y-%m-%d %H:%M:%S'), max_age=30*24*60*60)
            
            return response
            
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login_page.html')


def logout_page(request):
    request.session.flush()
    logout(request)
    response = redirect('login_page')
    return response