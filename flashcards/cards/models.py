from django.db import models

NUM_CAIXAS = 5
CAIXAS = range(1, NUM_CAIXAS + 1)

class Card(models.Model):
    """
    Esta class representa o modelo dos cartões.
    """
    questao  = models.CharField(max_length=140)
    resposta  = models.CharField(max_length=140)
    caixa = models.IntegerField(
        choices=zip(CAIXAS, CAIXAS),
        default=CAIXAS[0],
    )
    data_de_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.questao

    def mover_cartao(self, resposta):
        nova_caixa = self.caixa + 1 if resposta else CAIXAS[0]

        if nova_caixa in CAIXAS:
            self.caixa = nova_caixa
            self.save()

        return self
