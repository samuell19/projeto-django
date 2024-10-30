from django.shortcuts import render
# app/views.py

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST

@require_POST
def logout_view(request):
    logout(request)
    return redirect('inicio')

# Create your views here.
