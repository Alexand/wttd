# coding: utf-8
from eventex.subscriptions.forms import SubscriptionForm
from django.test import TestCase

class SubscriptionFormTeste(TestCase):
    def test_has_fields(self):
        """
        Form must have 4 fields
        """
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)