from django import forms
from listings.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class ContactUsForm(forms.Form):
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
