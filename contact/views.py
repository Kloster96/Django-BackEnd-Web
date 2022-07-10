from django.shortcuts import render, redirect
from django.urls import reverse
from pkg_resources import require
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Cafeteria: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "No-contestar@inbox.mailtrap.io",
                ["luciano.kloster@hotmail.com"],
                reply_to=[email]

            )
            try:
                email.send()
                # Algo no ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+ "?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+ "?fail")
    return render(request,"contact/contact.html", {'form': contact_form})