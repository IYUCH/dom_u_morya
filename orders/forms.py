from django import forms
from orders.models import Odrer


class OrderForm(forms.ModelForm):
    class Meta:
        model = Odrer
        fields = ['house', 'name', 'phone']
