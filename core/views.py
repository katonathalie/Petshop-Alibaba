from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
    template_name = 'home.html'
    return render(request, template_name)


def handle_page_not_found(request, *args, **kwargs):
    return redirect('/')