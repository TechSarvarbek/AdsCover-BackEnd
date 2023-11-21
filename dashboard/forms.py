from django import forms
from django.urls import reverse

from users.models import Users
from company.models import Company, Ad



class AdminUpdateForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput, required=False)

	class Meta:
		model = Users
		fields = ['email','first_name','last_name']

	def save(self, commit=True):
		user = super().save(commit=False)
		password = self.cleaned_data.get('password')
		if password:
			user.set_password(password)
		
		user.save()
		return user


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = ['email','password','first_name','last_name','telegram_name']
		

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ['user','ad','locations','name','website','launge','status']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		if 'user' in self.fields and 'ad' in self.fields:
			# user
			user = self.fields['user']
			user.widget = forms.widgets.TextInput()
			user.widget.attrs['readonly'] = True
			url = reverse('dashboard:user-update', args=[self.instance.user.id]) + f"?url={reverse('dashboard:company', args=[self.instance.id])}"
			user.widget.attrs['onclick'] = f"window.location.href='{url}'"

			# Ad
			ad = self.fields['ad']
			ad.widget = forms.widgets.TextInput()
			ad.widget.attrs['readonly'] = True
			url = reverse('dashboard:ad-update', args=[self.instance.ad.id]) + f"?url={reverse('dashboard:company', args=[self.instance.id])}"
			ad.widget.attrs['onclick'] = f"window.location.href='{url}'"

	
class AdForm(forms.ModelForm):
	class Meta:
		model = Ad
		fields = ('headline','description','ad_type','keywords','price','impressions','clicks',
				'click_rate','conversions','cost','cpc','cpa')

