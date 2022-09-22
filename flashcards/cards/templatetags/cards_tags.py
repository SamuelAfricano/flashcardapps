from django import template

from cards.models import CAIXAS, Card

register = template.Library()

@register.inclusion_tag("cards/box_links.html")
def link_das_caixas():
    caixas = []
    for num_caixa in CAIXAS:
        card_count = Card.objects.filter(caixa=num_caixa).count()
        caixas.append({
            "numero": num_caixa,
            "num_cartao": card_count,
        })

    return {"caixas": caixas}