from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if user.check_password(password):
                raise forms.ValidationError('incorrect password')
            if not user.ist_active:
                raise forms.ValidationError('This user is not active')

        return super()

class UserSignupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # remove colon as label prefix in .html
        self.label_suffix = ""
        # self.fields['password'].widget.attrs.update(forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
        ]
