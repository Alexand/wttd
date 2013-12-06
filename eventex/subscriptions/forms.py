# coding:utf-8
from django import forms
from django.utils.translation import ugettext as _
class SubscriptionForm(forms.Form):
    name = forms.CharField(label=_('Nome'))
    email = forms.CharField(label=_('E-mail'))
    cpf = forms.EmailField(label=_('CPF'), max_length=11)
    phone = forms.CharField(label=_('Telefone'))