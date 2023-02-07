import psutil
from sys import *
import os
import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import schedule


# for text files
# Receivers - list of str (email addrs, Sender - str (email addr)
def SendEmail(Sender, Receivers, Subject, Message, AppPwd, File = None, Host = "smtp.gmail.com", Port = 465):
	msg = MIMEMultipart()
	msg["From"] = Header(Sender)
	# msg["To"] = Header(Receiver)
	msg['To'] = Header(", ".join(Receivers)) # multiple recipients
	msg["Subject"] = Header(Subject)
	msg.attach(MIMEText(Message, "html", "utf-8"))
	if File:
		AttachmentName = os.path.basename(File)
		Attachment = MIMEText(open(File, "rb").read(), "base64", "utf-8")
		Attachment["Content-Type"] = "application/octet-stream"
		Attachment["Content-Disposition"] = "attachment; filename=" + AttachmentName
		msg.attach(Attachment)

	Server = smtplib.SMTP_SSL(Host, Port)
	Server.login(Sender, AppPwd)
	Server.sendmail(Sender, Receivers, msg.as_string())
	Server.quit()
	print("Sent Email Successfully !!")



def LogProcessInfo(LogDir = "Logs"):
	print("Inside LogProcessInfo, current time is", datetime.datetime.now())
	if not os.path.exists(LogDir):
		try:
			# os.mkdirs(LogDir)
			os.makedirs(LogDir)
		except:
			pass

	Separator = "-" * 20
	NowTime = time.ctime()
	LogFileName = datetime.datetime.now().strftime("ProcessMonitorLog_%d-%m-%Y_%H-%M-%S.log") 
	LogFileAbsPath = os.path.join(LogDir, LogFileName)
	f = open(LogFileAbsPath, "w")
	f.write(Separator + "\n")
	f.write("Process Logger:"+ time.ctime() + "\n")

	ProcessList = list()
		# print(type(psutil.process_iter())) # <class 'generator'>
	for Process in psutil.process_iter():
		# print(type(process)) # <class 'psutil.Process'>
		# print(help(psutil.Process))
		try:
			ProcessInfo = Process.as_dict(attrs = ["pid", "name", "username"]) # returns dict containing asked attributes
			ProcessInfo["vms"] = Process.memory_info().vms / (1024 * 1024)
			# vms / rss returned will be in bytes, we converted it into MB
			# rss is the Resident Set Size, which is the actual physical memory the process is using
			# vms is the Virtual Memory Size which is the virtual memory that process is using
			ProcessList.append(ProcessInfo)
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
		# An orphan process is formed when it's parent dies while the process continues to execute, while zombie process is a process which has terminated but it's entry is there in the process table.

	for element in ProcessList:
		f.write("%s\n"%element)

	try:
		SendEmail("shruti.p109@gmail.com", ["spython188@gmail.com", "marvellousinfosystems@gmail.com"], "Process Monitor Log " + NowTime , "Hello, This is a scheduled (per minute) test mail.<br>Please find Process Monitor Log generated on <b>" + NowTime + "</b>.", "tzrioxmszzgauhxq", LogFileAbsPath)
	except Exception as ex:
		print("Error: ", str(ex))

	f.close()


def main():
	print("Current time is",datetime.datetime.now())
	schedule.every(1).minutes.do(LogProcessInfo)

	while(True):
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()