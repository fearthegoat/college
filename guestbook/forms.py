from django import forms

class CommentForm(forms.Form):
	name = forms.CharField(max_length=20, 
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
	comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}))

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True,
    	widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    name = forms.CharField(max_length=30, required=True,
    	widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    subject = forms.CharField(required=True, max_length=100,
    	widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))