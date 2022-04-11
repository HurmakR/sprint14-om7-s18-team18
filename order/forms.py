from django import forms
from .models import *


class AddOrderPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].label_from_instance = lambda obj: f'{obj.first_name} {obj.last_name} '
        self.fields['book'].label_from_instance = lambda obj: f'{obj.name} '



    class Meta:
        model = Order

        fields = ['user', 'book', 'plated_end_at', 'end_at']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'}),
            'plated_end_at': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'end_at': forms.SelectDateWidget(attrs={'class': 'form-control'}),
        }
        labels = {
            'user': 'Користувач',
            'book': 'Книга',
            'plated_end_at': 'Буде повернено',
            'end_at': 'Повернено',
        }
