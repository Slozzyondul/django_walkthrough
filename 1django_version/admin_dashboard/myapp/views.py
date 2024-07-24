from django.shortcuts import render, redirect

def avatar_screen(request):
    print(request.headers)
    return render (request, 'avatars.html', {})

# Create your views here.
