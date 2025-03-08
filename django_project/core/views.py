from django.shortcuts import render
from services.models import Service
from post.models import Post
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    
    static_content = """
        <div class="inner">
        <h1>Hyperspace</h1>
        <p>
        Just another fine responsive site template designed by
        <a href="http://html5up.net">HTML5 UP</a><br />
        and released for free under the
        <a href="http://html5up.net/license">Creative Commons</a>.
        </p>
        <ul class="actions">
        <li><a href="#one" class="button scrolly">Learn more</a></li>
        </ul>
    </div>
    """

    featured_services = Service.objects.filter(is_featured=True)
    latest_posts = Post.objects.all()[:3]

    context = {
        "static_content": static_content,
        "featured_services": featured_services,
        "latest_posts": latest_posts,
    }

    return render(request, 'core/index.html', context)

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if not name or not email or not message:
            messages.error(request, "All fields are required!")
            return HttpResponseRedirect(reverse('index') + '#three')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Please enter a valid email address!")
            return HttpResponseRedirect(reverse('index') + '#three')

        subject = "Django Project Contact Form"
        message_body = f"Message from {name} - {email}: \n\n {message}"
        recipient_list = [settings.EMAIL_HOST_USER]

        try: 
            send_mail(subject, message_body, email, recipient_list)
        except Exception:
            messages.error(request, "Something went wrong. Please try again later.")
        else:
            messages.success(request, "We have received your email.")

    return HttpResponseRedirect(reverse('index') + '#three')
