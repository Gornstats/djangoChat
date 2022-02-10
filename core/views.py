from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

from .forms import SignUpForm

def frontpage(request):
    return render(request, 'core/frontpage.html')

@user_passes_test(lambda u: not u.is_authenticated) # don't allow signup access to logged in users 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            return redirect('frontpage')
    else:
        form = SignUpForm()
        
    return render(request, 'core/signup.html', {'form': form})
