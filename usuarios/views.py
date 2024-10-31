from django.shortcuts import render
# app/views.py
from django.views.generic import TemplateView

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST

@require_POST
def logout_view(request):
    logout(request)
    return redirect('inicio')

class PerfilView(TemplateView):
    template_name="usuarios/perfil.html"

# Create your views here.
