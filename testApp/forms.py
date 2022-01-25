from django import forms
from testApp.models import UserProfile



class UserProfileForm(forms.ModelForm):


	class Meta():
		model = UserProfile
		exclude = [

			'phoneNumber',
			'profilePic',

		]