from email.policy import default

from django.core.mail import send_mail
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from real_estate.settings.development import DEFAULT_FROM_EMAIL

from .models import Enquiry


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(request):
    data = request.data

    try:
        subject = data["subject"]
        name = data["name"]
        phone_number = data["phone_number"]
        message = data["message"]
        email = data["email"]
        from_email = data["email"]
        recipient_list = [DEFAULT_FROM_EMAIL]

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        enquiry = Enquiry(
            name=name,
            phone_number=phone_number,
            email=email,
            subject=subject,
            message=message,
        )
        enquiry.save()

        return Response({"success": "Your enquiry was successfully submmitted"})
    except:
        return Response({"fail": "Your enquiry was not send, please try again"})
