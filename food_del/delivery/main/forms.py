from django import forms
from .models import Restaurant, Dish, Order

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['restaurant', 'name', 'price', 'image']
        widgets = {
            'restaurant': forms.Select(attrs={
                'class': 'form-select'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва страви'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ціна страви'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'restaurant', 'dishes', 'courier', 'status']
        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-select'
            }),
            'restaurant': forms.Select(attrs={
                'class': 'form-select'
            }),
            'dishes': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'size': 10
            }),
            'courier': forms.Select(attrs={
                'class': 'form-select'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
