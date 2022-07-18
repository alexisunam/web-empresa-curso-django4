from ast import Try
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    contactForm = ContactForm()
    if request.method == "POST":
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Enviamos el correo y redireccionamos

            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["alexisduenasunam@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                # Todo a ido bien, redireccionamos ok
                print(request.path)
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no salio bien, redireccionamos fail
                return redirect(reverse('contact')+"?fail")

    return render(request, 'contact/contact.html', {'form': contactForm})