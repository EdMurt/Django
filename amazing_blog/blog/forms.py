from models import Post, comment
from django import forms

class PostForm(forms.ModelForm):
	mas = forms.CharField(widget = forms.Textarea(attrs={'cols':80,'rows':20}), required = False, min_length = 20)
 #El required es opc sirve para q el campo no sea  o no obligatorio
	class Meta:
		model = Post

class commentForm(forms.ModelForm):
	class Meta:
		model = comment
