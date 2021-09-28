from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

#HTML EMAIL REQUIRD STUFF

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import html
from django.utils.html import strip_tags

# Create your views here.
def sendanemail(request):
    if request.method == "post":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        # # print(to,content)
        # send_mail(
        #     #subject
        #     "testing",
        #     #msg
        #     content,
        #     #from email
        #     settings.EMAIL_HOST_USER,
        #     #rec list
        #     [to]
        #)
        #send the html mail
        html_content = render_to_string("email_template.html",{'title':'test email','content':content})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            #subject
            "testing",
            #content
            text_content,
            #from email
            settings.EMAIL_HOST_USER,
            #REC LIST
            [to]
        )
        email.attach_alternative(html_content,"text/html")
        email.send()

        return render(
            request,
            'email.html',
            {
                'title':'send an email'
            }
        )
    else:
        return render(
            request,
            'email.html',
            {
                'title':'send an email'
            }
        )