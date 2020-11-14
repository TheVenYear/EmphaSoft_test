from django.forms import ModelForm

from user.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar', 'about')
