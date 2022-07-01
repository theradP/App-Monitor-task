from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import App, User


class SignUpForm(UserCreationForm):
	username = forms.CharField(
		label='',
		max_length=30,
		min_length=5,
		required=True,
		widget=forms.TextInput(
			attrs={
				"placeholder": "Username",
				"class": "form-control"
			}
		)
	)

	email = forms.EmailField(
		label='',
		max_length=255,
		required=True,
		widget=forms.EmailInput(
			attrs={
				"placeholder": "Email",
				"class": "form-control"
			}
		)
	)

	password1 = forms.CharField(
		label='',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "Password",
				"class": "form-control"
			}
		)
	)

	password2 = forms.CharField(
		label='',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "Confirm Password",
				"class": "form-control"
			}
		)
	)

	location = forms.CharField(
		label='',
		max_length=30,
		required=False,
		widget=forms.HiddenInput(
			attrs={
				"display": "none"
			}
		)
	)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'location')


class AppForm(forms.ModelForm):

	class Meta:
		model = App
		fields = '__all__'
		widgets = {
			'app_full_name': forms.Textarea(attrs={'cols': 30, 'rows': 1}),
			'app_name': forms.Textarea(attrs={'cols': 30, 'rows': 1}),
			'app_id': forms.Textarea(attrs={'cols': 30, 'rows': 1})
		}


class UserRoleForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('roles',)

	def save(self, commit=True):
		print(self.data.get('roles'))
		m = super(UserRoleForm, self).save(commit=False)
		print(m)
		print(m.__dict__)
		m.roles = self.data.get('roles')
		if commit:
			m.save()
		return m

