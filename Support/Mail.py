import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import Support.CustomException as Except

class Mail:
    """
    Transmiterea mesajelor electronice

    Transmission of electronic messages
    """

    def __init__(self):
        """
        Initializarea datelor pentru transmiterea mesajului:
         - SMTPServer: Tipul serverului de transmitere (mail.ru, gmal.com)
         - email: addresa electronica expediator
         - password: parola expediator
         - send_to_email: addresa electronica destinatar
         - subject: subiectul mesajului
         - message: textul mesajului
         - file_location: calea catre fisierul atasat la mesaj

         Initialize the data for sending the message:
         - SMTPServer: Transmission server type (mail.ru, gmal.com)
         - email: sender's email address
         - password: the sender password
         - send_to_email: recipient's email address
         - subject: the subject of the message
         - message: the text of the message
         - file_location: the path to the file attached to the message
        """

        self.SMTPServer = 'Mail.ru'
        self.email = None
        self.password = None
        self.send_to_email = None
        self.subject = None
        self.message = None
        self.file_location = None

    def SendMail(self):
        """
        Transmiterea mesajului prin serverul indicat de utilizator in parametrul SMTPServer

        Transmission of the message through the server indicated by the user in the SMTPServer parameter
        """

        if self.SMTPServer == 'Mail.ru':
            self.MailRuSmtplib()
        elif self.SMTPServer == 'GMail.com':
            self.GMailSmtplib()
        else:
            print(self.SMTPServer + " server does not exist")

    def MailRuSmtplib(self):
        """
        Expedierea mesajului prin serverul mail.ru

        Sending the message through the mail.ru server
        """

        try:
            msg = MIMEMultipart()
            if self.email == None: raise Except.EMailIsNone
            if self.password == None: raise Except.PasswordIsNone
            if self.send_to_email == None: raise Except.ToEMailIsNone
            if self.subject == None: raise Except.SubjectIsNone
            if self.message == None: raise Except.MessageIsNone
            if self.file_location == None: raise Except.FileLocationIsNone
            msg['From'] = self.email
            msg['To'] = self.send_to_email
            msg['Subject'] = self.subject

            msg.attach(MIMEText(self.message, 'plain'))

            # Setup the attachment
            filename = os.path.basename(self.file_location)
            attachment = open(self.file_location, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            # Attach the attachment to the MIMEMultipart object
            msg.attach(part)

            server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
            server.login(self.email, self.password)
            text = msg.as_string()
            server.sendmail(self.email, self.send_to_email, text)
            server.quit()
        except Except.EMailIsNone:
            print('EMail None')
        except Except.PasswordIsNone:
            print("Password None")
        except Except.ToEMailIsNone:
            print("Email Receiver None")
        except Except.SubjectIsNone:
            print("Subject message None")
        except Except.MessageIsNone:
            print("Message None")
        except Except.FileLocationIsNone:
            print("Attachment file location None")
        except smtplib.SMTPAuthenticationError as ex:
            print(ex)
            print("Error Authentication")
        else:
            print("Message sent successfully")

    def GMailSmtplib(self):
        """
        Expedierea mesajului prin serverul Gmail.com

        Send the message through the Gmail.com server
        """

        try:
            msg = MIMEMultipart()
            if self.email == None: raise Except.EMailIsNone
            if self.password == None: raise Except.PasswordIsNone
            if self.send_to_email == None: raise Except.ToEMailIsNone
            if self.subject == None: raise Except.SubjectIsNone
            if self.message == None: raise Except.MessageIsNone
            if self.file_location == None: raise Except.FileLocationIsNone
            msg['From'] = self.email
            msg['To'] = self.send_to_email
            msg['Subject'] = self.subject
            msg.attach(MIMEText(self.message, 'plain'))

            # Setup the attachment
            filename = os.path.basename(self.file_location)
            attachment = open(self.file_location, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            # Attach the attachment to the MIMEMultipart object
            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(self.email, self.password)
            text = msg.as_string()
            server.sendmail(self.email, self.send_to_email, text)
            server.quit()
        except Except.EMailIsNone:
            print('EMail None')
        except Except.PasswordIsNone:
            print("Password None")
        except Except.ToEMailIsNone:
            print("Email Receiver None")
        except Except.SubjectIsNone:
            print( "Subject message None")
        except Except.MessageIsNone:
            print("Message None")
        except Except.FileLocationIsNone:
            print("Attachment file location None")
        except smtplib.SMTPAuthenticationError as ex:
            print(ex)
            print("Error Authentication")
        else:
            print("Message sent successfully")