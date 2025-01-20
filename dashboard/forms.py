from django import forms
from .models import Staff, Shop, Item, Sales


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staffName', 'address', 'telephone', 'email', 'username', 'password']
        # widgets = {
        #     'password': forms.PasswordInput(),  # Render password as hidden input
        # }


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['shopName', 'location', 'telephone', 'staffAssigned']
       


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['itemName', 'unit']


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['item', 'shop', 'saleType', 'quantity', 'staff']
        widgets = {
            'saleType': forms.Select(choices=[('stock_supplied', 'Stock Supplied'), ('stock_balance', 'Stock Balance')]),
        }
