import random

from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    CreateView,
    UpdateView,
)
from django.shortcuts import get_object_or_404, redirect
from .forms import CheckForm

from .models import Card


class CardListViews(ListView):
    """ 
    Classe Genêrica para listar todos os cartões
    """
    model = Card
    queryset = Card.objects.all().order_by("caixa", "-data_de_criacao")

class CardCreateView(CreateView):
    """
    Classe genêrica para criar os cartões.
    """
    model = Card
    fields = ["questao", "resposta", "caixa"]
    seccess_url = reverse_lazy("card-create")

class CardUpdateView(CardCreateView, UpdateView):
    """
    Class genêrica para editar os cartões.
    
    Parar editar os cartões, está class 
    extende, os atributos da class CardCreateView
    mudando apenas a URL de sucesso
    """
    success_url = reverse_lazy("card-list")

class Caixas(CardListViews):
    """
    Esta class mostra o conteudo de uma caixa.
    
    Em vez de listar todos os devolve os cartões 
    onde o número da caixa cartões corresponde ao 
    num_caixa.
    """
    
    templates = "cards/caixa.html"
    form_class = CheckForm

    def get_queryset(self):
        return Card.objects.filter(caixa=self.kwargs["num_caixa"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_da_caixa"] = self.kwargs["num_caixa"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["id_do_cartao"])
            card. mover_cartao(form.cleaned_data["resposta"])

        return redirect(request.META.get("HTTP_REFERER"))
