from django import forms
from .models import Shop, Staff

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['shopName', 'location', 'telephone']  # Fields to be filled

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staffName', 'address', 'telephone', 'email','username', 'password']  # Fields to be filled