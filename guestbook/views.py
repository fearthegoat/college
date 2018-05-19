from django.shortcuts import render, redirect
from .models import Comment
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	comments = Comment.objects.order_by('-date_added')
	
	context = {'comments' : comments}

	return render(request,'guestbook/index.html', context)

def sign(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
			new_comment.save()
			return redirect('index')
	else:
		form = CommentForm()

	context = {'form' : form}
	return render(request, 'guestbook/sign.html', context)

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
				send_mail(subject, message, from_email, ['admin@example.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('landingpage')
	return render(request, 'guestbook/landingpage.html',{'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')