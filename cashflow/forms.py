from django import forms
# from django.core.exceptions import ValidationError
from .models import Status, Type, Categories, SubCategories, Transaction


class FormAddTransaction(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('title', 'status', 'operation_type', 'categories',
                  'subcategories', 'amount', 'comment',)
        localized_fields = ('amount',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'},),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'operation_type': forms.Select(attrs={'class': 'form-select'}),
            'categories': forms.Select(attrs={'class': 'form-select'}),
            'subcategories': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.TextInput(attrs={'class': 'form-control',
                                               'id': "amount",
                                               'name': "amount",
                                               'placeholder': "Например, 1500.50",
                                               'inputmode': 'decimal',
                                             'minlength': 1,
                                             'maxlength': 12 }),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'id': "comment", 'name': "comment"}),
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if not amount > 0:
            raise forms.ValidationError('Сумма должна быть больше нуля')
        return amount
