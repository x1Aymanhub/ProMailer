import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import time
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Charger les variables d'environnement depuis config.env
load_dotenv('config.env')

# Paramètres du serveur SMTP (exemple avec Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = os.getenv('SENDER_EMAIL')
app_password = os.getenv('APP_PASSWORD')

# Liste des destinataires
recipient_emails = os.getenv('RECIPIENT_EMAILS').split(',')

# Contenu de l'emailS
subject = os.getenv('EMAIL_SUBJECT')

# Lire le contenu HTML depuis un fichier externe
with open("file.html", "r", encoding="utf-8") as f:
    body = f.read()

# Configuration du serveur SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, app_password)

# Boucle pour envoyer à chaque destinataire
for recipient in recipient_emails:
    msg = MIMEMultipart("alternative")  
    msg["From"] = sender_email
    msg["To"] = recipient
    msg["Subject"] = subject
    msg["Reply-To"] = sender_email
    msg["Message-ID"] = f"<{int(time.time())}.{recipient}@{sender_email.split('@')[1]}>"

    # Version texte simple
    text = "Bonjour,\nVeuillez trouver ci-joint mon CV et ma signature.\nCordialement."
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(body, "html")
    msg.attach(part1)
    msg.attach(part2)
    # Ajout de la signature en pièce jointe inline
    try:
        with open("picture/signature.png", "rb") as sig_file:
            sig_img = MIMEImage(sig_file.read())
            sig_img.add_header('Content-ID', '<signature>')
            sig_img.add_header('Content-Disposition', 'inline', filename="signature.png")
            msg.attach(sig_img)
    except Exception as e:
        print(f"Erreur lors de l'attachement de la signature : {e}")
    # Ajout du PDF en pièce jointe
    try:
        with open("CV_aliati_ayman.pdf", "rb") as pdf_file:
            pdf = MIMEApplication(pdf_file.read(), _subtype="pdf")
            pdf.add_header('Content-Disposition', 'attachment', filename="CV_aliati_ayman.pdf")
            msg.attach(pdf)
    except Exception as e:
        print(f"Erreur lors de l'attachement du PDF : {e}")
    try:
        server.sendmail(sender_email, recipient, msg.as_string())
        print(f"✅ Email envoyé à {recipient}")
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi à {recipient} : {e}")
    time.sleep(10)

server.quit()
print("Tous les emails ont été envoyés.")
