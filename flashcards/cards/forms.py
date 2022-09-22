from django import forms

class CheckForm(forms.Form):
    id_do_cartao = forms.IntegerField(required=True)
    resposta = forms.BooleanField(required=False)