from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host ="smtp.gmail.com"
port = 587
username ="happy4evr2019@gmail.com"
password = "amna1234"
from_email = username
to_list = ["happy4evr2019@gmail.com", "ziagulzia@gmail.com"]
try:
	email_conn = smtplib.SMTP(host, port)
	email_conn.ehlo()
	email_conn.starttls()
	email_conn.login(username, password)
	the_msg = MIMEMultipart("alternative")
	the_msg['Subject'] = "Aoa There"
	the_msg["From"] = from_email
	#the_msg["To"] = to_list[0]
	plain_text = "Testng a message"
	html_txt = """\
	<html>
		<head>
			</head>
		<body>
			<p> Hey! <br>
				testing this email <b> message </b>. Made by <a href='http://joincfe.com'>Team CFE</a>
			</p?
		</body>
	</html>
	"""
	part_1 = MIMEText(plain_text, 'palin')
	part_2 = MIMEText(html_txt, 'html')
	the_msg.attach(part_1)
	the_msg.attach(part_2)
	email_conn.sendmail(from_email, to_list, the_msg.as_string())
	email_conn.quit()
except smtplib.SMTPExcept:
	print("error sending message")