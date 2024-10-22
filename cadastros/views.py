from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo, Atividade

from django.urls import reverse_lazy

class CampoCreate(CreateView):
    model = Campo
    fields = ['nome','descricao']
    template_name='cadastros/form.html'
    success_url = reverse_lazy('inicio') 

class AtividadeCreate(CreateView):
    model= Atividade
    fields = ['numero','descricao', 'pontos', 'detalhes', 'campo']
    template_name='cadastros/form.html'
    success_url = reverse_lazy('inicio')

    #####update view####

class CampoUpdate(UpdateView):
        model = Campo
        fields = ['nome','descricao']
        template_name='cadastros/form.html'
        success_url = reverse_lazy('inicio')

class AtividadeUpdate(UpdateView):
        model=Atividade
        fields = ['numero','descricao', 'pontos', 'detalhes', 'campo']
        template_name='cadastros/form.html'
        success_url = reverse_lazy('inicio')

     ######delete view########
 
class CampoDelete(DeleteView):
       model = Campo
       template_name='cadastros/form-excluir.html'
       success_url = reverse_lazy('inicio')

class AtividadeDelete(DeleteView):
       model=Atividade
       template_name='cadastros/form-excluir.html'       
       success_url = reverse_lazy('inicio')

#####lista######

class CampoList(ListView):
    model = Campo
    template_name = 'cadastros/listas/campo.html'     

class AtividadeList(ListView):
      model= Atividade
      template_name = 'cadastros/listas/atividade.html'      
    