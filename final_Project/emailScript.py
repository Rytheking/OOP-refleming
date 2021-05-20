import smtplib
import ssl
from graphs import tempPlot, humPlot, vpdPlot
from plant import *
from datetime import date, timedelta
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

port = 465
email1 = "growtentmonitor@gmail.com"
password = "j!pPA7P4r0*O35U^"
context = ssl.create_default_context()


class Email:
    def __init__(self, fromAddr, toAddr, subject):
        self._message = MIMEMultipart()
        self._from = fromAddr
        self._to = toAddr
        self._subject = subject
        self._message['From'] = self._from
        self._message['To'] = self._to
        self._message["Subject"] = self._subject

    def sendEmail(self):
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(email1, password)
            server.sendmail(email1, self._to, self._message.as_string())

    def attachPNG(self, filename: str, contentID):
        with open(filename, 'rb') as f:
            attachment = MIMEBase('image', 'png', filename=filename)
            attachment.add_header('Content-Disposition',
                                  'attachment', filename=filename)
            attachment.add_header('X-Attachment-Id', '0')
            attachment.add_header('Content-ID', contentID)
            # read attachment file content into the MIMEBase object
            attachment.set_payload(f.read())
            # encode with base64
            encoders.encode_base64(attachment)
            # add MIMEBase object to MIMEMultipart object
            self._message.attach(attachment)


class dailyPlantUpdate(Email):
    def __init__(self, toAddr):
        self._today = date.today()
        self._yesterday = self._today-timedelta(days=1)
        folder = "./storage/"+str(self._yesterday)+"/"
        command = "mkdir "+folder
        os.system(command)
        temp_filename = folder+"tempPlot " + str(self._yesterday) + ".png"
        temp = tempPlot(temp_filename, self._yesterday, self._today)
        temp.savePicture(temp_filename)

        hum_filename = folder+"humPlot " + str(self._yesterday) + ".png"
        hum = humPlot(hum_filename, self._yesterday, self._today)
        hum.savePicture(hum_filename)

        vpd_filename = folder+"vpdPlot " + str(self._yesterday) + ".png"
        vpd = vpdPlot(vpd_filename, self._yesterday, self._today)
        vpd.savePicture(vpd_filename)
        image_title = folder+str(self._yesterday)+".png"
        command = "raspistill -o "+image_title
        os.system(command)
        self._subject = "Daily plant update from: " + str(self._yesterday)
        Email.__init__(self, email1, toAddr, self._subject)
        data = """\
            <html>
                <body>
                    <h1>Yesterday's Data</h1>
                </body>
            </html>
        """
        graphHTML = """\
            <html>
                <body>
                    <div style="display: inline-block">
                        <h2 style="text-align: center">Temperature Data</h2>
                        <img src='cid:0'>
                    </div>
                    <div style="display: inline-block">
                        <h2 style="text-align: center">Humdity Data</h2>
                        <img src='cid:1' style="display: inline-block">
                    </div>
                    <div style="display: inline-block">
                        <h2 style="text-align: center">VPD Data</h2>
                        <img src='cid:2' style="display: inline-block">
                    </div>
                    <div style="display: inline-block">
                        <h2 style="text-align: center">The tent this morning</h2>
                        <img src='cid:3' style="display: inline-block; width: 75%; height : 75%">
                    </div>
                </body>
            </html>
        """

        plant_information = "<p>Cultivar: " + \
            TK_Seed_3._cultivar._name+"</p><p>Age: "+str(TK_Seed_3._age)+"</p>"
        part1 = MIMEText(data, "html")
        part2 = MIMEText(graphHTML, "html")
        part3 = MIMEText(plant_information, "html")
        self._message.attach(part1)
        self._message.attach(part2)
        self.attachPNG(temp_filename, '<0>')
        self.attachPNG(hum_filename, '<1>')
        self.attachPNG(vpd_filename, '<2>')
        self.attachPNG(image_title, '<3>')
        self._message.attach(part3)


dailyUpdate = dailyPlantUpdate("ryanelliottfleming@gmail.com")
dailyUpdate.sendEmail()
