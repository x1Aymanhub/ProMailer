# 📧 Script d'Envoi d'Email Professionnel

Ce projet est un script Python simple permettant d'envoyer des emails professionnels à plusieurs destinataires avec les éléments suivants :
- Un **contenu HTML personnalisé** lu depuis un fichier externe.
- Une **signature intégrée en inline** (affichée directement dans l'email).
- Un **CV au format PDF** en pièce jointe.
- Des **gestions d'erreurs** pour chaque étape critique.

## Exemple d'exécution

![Exemple d'exécution](picture/image.png)

## 🔧 Fonctionnalités principales

- ✅ Envoi d'emails via **Gmail SMTP** (avec mot de passe d'application).
- ✅ Gestion des **multiples destinataires**.
- ✅ Intégration de contenu **HTML dynamique**.
- ✅ Pièce jointe : **PDF en téléchargement direct** depuis le corps de l'email.
- ✅ Signature visuelle **intégrée en inline** (via `Content-ID`).

## 📁 Structure du projet

```
email_sender/
├── script_email.py         # Script d'envoi via SMTP Gmail
├── sendgrid_mail.py        # Script d'envoi via l'API SendGrid
├── config.env              # Variables sensibles pour SendGrid (clé API, emails...)
├── file.html               # Contenu HTML de l'email
├── CV_aliati_ayman.pdf     # CV envoyé en pièce jointe
├── picture/
│   └── signature.png       # Image de signature pour l'email
└── README.md               # Documentation du projet
```

- **script_email.py** : Envoi d'email via Gmail/SMTP, HTML, pièces jointes.
- **sendgrid_mail.py** : Envoi d'email via SendGrid, HTML, pièces jointes, configuration via `config.env`.
- **config.env** : Stocke la clé API SendGrid, l'expéditeur, les destinataires, le sujet.
- **file.html** : Modèle HTML de l'email.
- **CV_aliati_ayman.pdf** : CV à joindre à l'email.
- **picture/signature.png** : Image de signature insérée dans l'email.
- **README.md** : Ce fichier de documentation.

## ⚙️ Configuration requise

- Python 3.x
- Bibliothèques standard utilisées : `smtplib`, `email.mime.*`
- Gmail : Activer **l'authentification à deux facteurs** et générer un **mot de passe d'application**.

## 📌 Instructions d'utilisation

1. Installez Python si ce n'est pas déjà fait.
2. Configurez vos identifiants Gmail (`sender_email` et `app_password`) dans le script.
3. Ajoutez vos destinataires dans la liste `recipient_emails`.
4. Créez/modifiez le template HTML `file.html` selon vos besoins.
5. Placez votre image de signature dans `picture/signature.png`.
6. Mettez votre CV dans `cv.pdf`.
7. Exécutez le script :
   ```bash
   python .\send_email.py
   ```

## 🚀 Méthode SendGrid (API)

Ce projet propose aussi une méthode d'envoi d'email via l'API professionnelle SendGrid :

- Utilise le script `sendgrid_mail.py`.
- Les informations sensibles (clé API, expéditeur, destinataires, sujet) sont stockées dans `config.env`.
- Supporte l'envoi d'email HTML et de pièces jointes (PDF, etc.).
- Recommandé pour un usage professionnel et une meilleure délivrabilité.

**Utilisation :**
1. Configure le fichier `config.env` avec ta clé API SendGrid, l'adresse expéditeur validée, les destinataires et le sujet.
2. Lance le script :
   ```bash
   python .\sendgrid_mail.py
   ```

Voir la section "Exemple d'exécution" pour un aperçu du résultat.



   
