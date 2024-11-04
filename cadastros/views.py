from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo, Atividade

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

class CampoCreate(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url = 'login' 
    model = Campo
    fields = ['nome','descricao']
    template_name='cadastros/form.html'
    success_url = reverse_lazy('listar-campos') 

class AtividadeCreate(LoginRequiredMixin, CreateView):
    login_url = 'login' 
    model= Atividade
    fields = ['numero','descricao', 'pontos', 'detalhes', 'campo']
    template_name='cadastros/form.html'
    success_url = reverse_lazy('inicio')

    #####update view####

class CampoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
        group_required = u"Administrador"
        login_url = 'login'      
        model = Campo
        fields = ['nome','descricao']
        template_name='cadastros/form-editar.html'
        success_url = reverse_lazy('listar-campos')

class AtividadeUpdate(LoginRequiredMixin, UpdateView):
        login_url = 'login' 
        model=Atividade
        fields = ['numero','descricao', 'pontos', 'detalhes', 'campo']
        template_name='cadastros/form.html'
        success_url = reverse_lazy('listar-atividades')

     ######delete view########
 
class CampoDelete(GroupRequiredMixin,DeleteView):
       group_required = u"Administrador"
       login_url = 'login' 
       model = Campo
       template_name='cadastros/form-excluir.html'
       success_url = reverse_lazy('listar-campos')

class AtividadeDelete(LoginRequiredMixin, DeleteView):
       login_url = 'login' 
       model=Atividade
       template_name='cadastros/form-excluir.html'       
       success_url = reverse_lazy('listar-atividades')

#####lista######

class CampoList(LoginRequiredMixin, ListView):
    model = Campo
    template_name = 'cadastros/listas/campo.html'  
    login_url = 'login'   

class AtividadeList(LoginRequiredMixin, ListView):
      login_url = 'login' 
      model= Atividade
      template_name = 'cadastros/listas/atividade.html'      
    