from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Hello from PrettyPrinted',
    'Hello there. This is an automated message.',
    'sininchicudo.38@gmail.com',
    ['haropap431@meogl.com'],
    fail_silently=False)

    return render(request, 'send/index.html')
