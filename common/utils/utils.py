import os
import re
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from passlib.hash import pbkdf2_sha512


class Utils:

    @staticmethod
    def email_is_valid(email: str) -> bool:
        email_address_matcher = re.compile(r'^[\w-]+(@[\w-]+\.)+[\w]+$')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(password: str):
        return pbkdf2_sha512.hash(password)

    @staticmethod
    def check_password(password: str, hashed_password: str):
        return pbkdf2_sha512.verify(password, hashed_password)

    @staticmethod
    def send_mail(email: str, report_name: str, graph: str, f_name: str, l_name: str):
        message = MIMEMultipart('alternative')
        message['Subject'] = "Regarding Test Report"
        message['From'] = 'kusmakharpathak.sunway@gmail.com'
        message['To'] = email

        dir_path = "E:\\Python\\BreastCancer\\common\\docs"
        files = [report_name, graph]
        html = f"""\
        <html>
          <head></head>
          <body>
            <h1>Medical Report</h1>
            <p>Dear Patients<br>
               How are you?<br>
               Here is your medical report you can find in this email<br><br><b>Thank you.</b><br>{f_name} {l_name}
            </p>
          </body>
        </html>
        """

        message.attach(MIMEText(html, 'html'))

        for f in files:  # add files to the message
            file_path = os.path.join(dir_path, f)
            attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
            attachment.add_header('Content-Disposition', 'attachment', filename=f)
            message.attach(attachment)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('kusmakharpathak.sunway@gmail.com', 'yahoo123@')
        server.sendmail("kusmakharpathak.sunway@gmail.com", email, message.as_string())
        server.quit()


# Utils.send_mail('kusmakharpathak@outlook.com', 'Kusmakhar (9616695533).txt', 'Kusmakhar (9616695533).png', 'hell', 'test')
