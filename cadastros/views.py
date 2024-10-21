from django.views.generic.edit import CreateView

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
