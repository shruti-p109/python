import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# for text files
# Receivers - list of str (email addrs), Sender - str (email addr)
def SendTxtAttachmentMail(Sender, Receivers, Subject, Message, AppPwd, Files = None, Host = "smtp.gmail.com", Port = 465):
	try:
		msg = MIMEMultipart()
		msg["From"] = Header(Sender)
		# msg["To"] = Header(Receivers)
		msg['To'] = Header(", ".join(Receivers)) # multiple recipients
		msg["Subject"] = Header(Subject)
		msg.attach(MIMEText(Message, "html", "utf-8"))

		if Files:
			for File in Files:
				AttachmentName = os.path.basename(File)
				Attachment = MIMEText(open(File, "rb").read(), "base64", "utf-8")
				Attachment["Content-Type"] = "application/octet-stream"
				Attachment["Content-Disposition"] = "attachment; filename=" + AttachmentName
				msg.attach(Attachment)

		Server = smtplib.SMTP_SSL(Host, Port)
		Server.login(Sender, AppPwd)
		Server.sendmail(Sender, Receivers, msg.as_string())
		Server.quit()
	except ValueError:
		return(False, "Failed to send email: Invalid datatype of input.")
	except Exception as ex:
		print()
		return(False, "Failed to send email: {}".format(str(ex)))

	return (True,)