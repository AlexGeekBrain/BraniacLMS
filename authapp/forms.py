import os
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'age',
            'avatar',
        )

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 10 or age > 100:
            raise ValidationError('Пожалуйста, введите действительный возраст!')
        return age

    def clean_avatar(self):
        arg_as_str = 'avatar'
        if arg_as_str in self.changed_data and self.instance.avatar:
            if os.path.exists(self.instance.avatar.path):
                os.remove(self.instance.avatar.path)
        return self.cleaned_data.get(arg_as_str)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'age',
            'avatar',
        )

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 10 or age > 100:
            raise ValidationError('Пожалуйста, введите действительный возраст!')
        return age
