from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.utils.html import escape

import resend


class ResendEmailBackend(BaseEmailBackend):

    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        resend.api_key = settings.RESEND_API_KEY

        sent_count = 0

        for message in email_messages:

            if not message.to:
                continue

            try:
                html_content = None

                # Use HTML alternative if Django supplied one
                for alternative in getattr(message, "alternatives", []):
                    content, mimetype = alternative

                    if mimetype == "text/html":
                        html_content = content
                        break

                # If there is no HTML version, convert plain text to simple HTML
                if not html_content:
                    html_content = (
                        "<pre style='font-family: Arial, sans-serif;'>"
                        + escape(message.body)
                        + "</pre>"
                    )

                params = {
                    "from": settings.RESEND_FROM_EMAIL,
                    "to": message.to,
                    "subject": message.subject,
                    "html": html_content,
                }

                result = resend.Emails.send(params)

                print("RESEND EMAIL SENT:", result)

                sent_count += 1

            except Exception as e:
                print(
                    "RESEND EMAIL ERROR:",
                    type(e).__name__,
                    str(e)
                )

                if not self.fail_silently:
                    raise

        return sent_count