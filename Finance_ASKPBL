from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 rounded-xl border-2 border-pink-200 focus:outline-none focus:border-pink-400 bg-pink-50/50',
        'placeholder': 'Enter your password'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-xl border-2 border-pink-200 focus:outline-none focus:border-pink-400 bg-pink-50/50',
                'placeholder': 'Choose a username'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        # Use set_password to securely hash the password
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user