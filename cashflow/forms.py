from django import forms
# from django.core.exceptions import ValidationError
from .models import Status, Type, Categories, SubCategories, Transaction


class FormTransaction(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].empty_label = 'Выберите статус'
        self.fields['operation_type'].empty_label = 'Выберите тип'
        self.fields['categories'].empty_label = 'Выберите категорию'
        self.fields['subcategories'].empty_label = 'Выберите подкатегорию'

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if not amount > 0:
            raise forms.ValidationError('Сумма должна быть больше нуля')
        return amount


class FormStatus(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('name_status',)
        widgets = {
            'name_status': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FormType(forms.ModelForm):
    class Meta:
        model = Type
        fields = ('type_operation',)
        widgets = {
            'type_operation': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FormCategories(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('categories', 'type',)
        widgets = {
            'categories': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = 'Выберите тип'


class FormSubCategories(forms.ModelForm):
    class Meta:
        model = SubCategories
        fields = ('category', 'subcategories',)
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subcategories': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите тип'


class FormDate(forms.Form):
    user_date_start = forms.DateField(required=False, label="С", widget=forms.DateInput(attrs={'type': 'date', 'id': "date_picker_start"}, format='%Y-%m-%d'))
    user_date_end = forms.DateField(required=False, label="по", widget=forms.DateInput(attrs={'type': 'date', 'id': "date-picker_end"}, format='%Y-%m-%d'))
    def clean(self):
        date_start = self.cleaned_data.get('user_date_start')
        date_end = self.cleaned_data.get('user_date_end')
        if date_start and date_end is not None:
            if date_start > date_end:
                raise forms.ValidationError('date_start > date_end')

