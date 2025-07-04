from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import base64
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis config.env
load_dotenv('config.env')

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
sender_email = os.getenv('SENDER_EMAIL')
recipient_emails = os.getenv('RECIPIENT_EMAILS').split(',')
subject = os.getenv('EMAIL_SUBJECT')

# Lire le contenu HTML depuis un fichier externe
with open("file.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Lire et encoder le PDF en base64
with open("CV_aliati_ayman.pdf", "rb") as pdf_file:
    pdf_data = pdf_file.read()
    encoded_pdf = base64.b64encode(pdf_data).decode()

attachment = Attachment(
    FileContent(encoded_pdf),
    FileName("CV_aliati_ayman.pdf"),
    FileType("application/pdf"),
    Disposition("attachment")
)

for recipient in recipient_emails:
    message = Mail(
        from_email=sender_email,
        to_emails=recipient,
        subject=subject,
        html_content=html_content
    )
    message.add_attachment(attachment)

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"✅ Email envoyé à {recipient} | Statut : {response.status_code}")
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi à {recipient} : {e}")