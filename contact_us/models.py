from django.db import models
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 100)
	sender = forms.EmailField()
	message = forms.CharField()
	copy = forms.BooleanField(required = False)


class Contacts(models.Model):
	sub = models.CharField(max_length=200, default='')
	sender = models.CharField(max_length=200, default='')
	message = models.TextField(default='')
	name = models.CharField(max_length=60, default='')

	def __str__(self):
		return self.sub
