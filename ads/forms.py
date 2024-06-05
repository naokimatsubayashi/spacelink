from django import forms
from .models import Consumer

class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ['name', 'phone_number', 'email']
        labels = {
            'name': 'サービス利用者',
            'phone_number': '電話番号',
            'email': 'Email',
        }