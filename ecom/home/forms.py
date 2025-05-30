from django import forms
from shop.models import Users_Product
from .models import Tweet

class UserProductForm(forms.ModelForm):
    class Meta:
        model = Users_Product
        fields = ['brand_name', 'title', 'desc', 'category', 'price', 'discounted_price', 'image','link']
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['username', 'comment', 'image']