from . import models
from django.forms import ModelForm, TextInput


class CourseForm(ModelForm):
	class Meta:
		model = models.Course
		fields = ["title","ID_Pass"]
		widgets = {
			"title": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Введите имя'
			}),
			"ID_Pass": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Введите ID-Pass'
			})
		}
