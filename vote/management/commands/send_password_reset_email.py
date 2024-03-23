from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.contrib.auth.forms import PasswordResetForm


class Command(BaseCommand):
    help = 'Emails password reset instructions to all users'

    def handle(self, *args, **kwargs):
        users = User.objects.filter(is_staff=False)
        for user in users:
            try:
                if user.email:
                    print("Sending email for reset to this email:", user.email)
                    form = PasswordResetForm({'email': user.email})
                    assert form.is_valid()
                    request = HttpRequest()
                    request.META['SERVER_NAME'] = '127:0:0:1'
                    request.META['SERVER_PORT'] = 8000
                    form.save(
                        request=request,
                        use_https=True,
                        from_email="alidehshini@gmail.com",
                        email_template_name='templates/password_reset_email.html'
                    )
            except Exception as e:
                print(e)
                continue

        return 'done'
