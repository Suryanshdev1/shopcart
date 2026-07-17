"""Forms for the shop application."""
from django import forms


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(
        initial=1,
        min_value=1,
        max_value=99,
        widget=forms.NumberInput(attrs={
            'class': 'form-control quantity-input',
            'min': '1',
            'max': '99',
        })
    )
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your message...'}))
