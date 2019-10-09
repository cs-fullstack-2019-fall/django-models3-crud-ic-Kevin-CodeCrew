from django.forms import ModelForm
from .models import ItemModel
from django.contrib.auth.models import User

class ItemForm(ModelForm):
    class Meta:
        model = ItemModel
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']