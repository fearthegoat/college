from django.shortcuts import render, redirect
from .models import College
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
import requests

def list(request):
	colleges = College.objects.order_by('conference')
	
	context = {'colleges' : colleges}

	return render(request,'guestbook/list.html', context)

def send_simple_message(subject, from_email, message, name):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox0328e6f54eef4bc99a0dd0c3911a574d.mailgun.org",
        auth=("api", "key-6f0f1b84092d075a462f048ffcfec2e8"),
        data={"from": "postmaster@sandbox0328e6f54eef4bc99a0dd0c3911a574d.mailgun.org",
              "to": ["gary_stewart98@hotmail.com"],
              "subject": subject,
              "text": name + ' ' + message})

def landingpage(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			name = form.cleaned_data['name']
			try:
				send_simple_message(subject, from_email, message, name)
				#send_mail(subject, message, from_email, ['usacitizen80@hotmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('landingpage')
	return render(request, 'guestbook/landingpage.html',{'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')