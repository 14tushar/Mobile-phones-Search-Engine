import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin

from urllib.parse import urlparse

from urllib.request import urlopen as ur
from bs4 import BeautifulSoup as bs
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('mobiles.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Mobile(
'id' INTEGER AUTO_INCREMENT PRIMARY KEY DEFAULT 1,
'name' TEXT,
'price' DECIMAL(8,2),
'rating' DECIMAL(2,1)
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Specs(
'id' TEXT,"In The Box" TEXT, "Model Number" TEXT, "Model Name" TEXT, "Color" TEXT, "Browse Type" TEXT, "SIM Type" TEXT, "Hybrid Sim Slot" TEXT, "Touchscreen" TEXT, "OTG Compatible" TEXT, "Sound Enhancements" TEXT, "Display Size" TEXT, "Resolution" TEXT, "Resolution Type" TEXT, "GPU" TEXT, "Display Colors" TEXT, "Other Display Features" TEXT, "Operating System" TEXT, "Processor Type" TEXT, "Processor Core" TEXT, "Primary Clock Speed" TEXT, "Operating Frequency" TEXT, "Internal Storage" TEXT, "RAM" TEXT, "Expandable Storage" TEXT, "Supported Memory Card Type" TEXT, "Memory Card Slot Type" TEXT, "Primary Camera Available" TEXT, "Primary Camera" TEXT, "Primary Camera Features" TEXT, "Secondary Camera Available" TEXT, "Secondary Camera" TEXT, "Secondary Camera Features" TEXT, "Flash" TEXT, "HD Recording" TEXT, "Full HD Recording" TEXT, "Video Recording" TEXT, "Video Recording Resolution" TEXT, "Frame Rate" TEXT, "Dual Camera Lens" TEXT, "Phone Book" TEXT, "Network Type" TEXT, "Supported Networks" TEXT, "Internet Connectivity" TEXT, "3G" TEXT, "Pre-installed Browser" TEXT, "Micro USB Port" TEXT, "Bluetooth Support" TEXT, "Bluetooth Version" TEXT, "Wi-Fi" TEXT, "Wi-Fi Hotspot" TEXT, "USB Connectivity" TEXT, "Audio Jack" TEXT, "Map Support" TEXT, "GPS Support" TEXT, "Smartphone" TEXT, "SIM Size" TEXT, "User Interface" TEXT, "Removable Battery" TEXT, "SMS" TEXT, "Graphics PPI" TEXT, "Sensors" TEXT, "Other Features" TEXT, "Important Apps" TEXT, "FM Radio" TEXT, "Audio Formats" TEXT, "Video Formats" TEXT, "Battery Capacity" TEXT, "Width" TEXT, "Height" TEXT, "Depth" TEXT, "Weight" TEXT, "Warranty Summary" TEXT, "Quick Charging" TEXT, "Display Type" TEXT, "Wi-Fi Version" TEXT, "Infrared" TEXT, "Secondary Clock Speed" TEXT, "USB Tethering" TEXT, "MMS" TEXT, "Video Call Support" TEXT, "Micro USB Version" TEXT, "Battery Type" TEXT, "3G Speed" TEXT, "GPRS" TEXT, "EDGE" TEXT, "GPRS Features" TEXT, "EDGE Features" TEXT, "Voice Input" TEXT, "SIM Access" TEXT, "Call Log Memory" TEXT, "Speaker Phone" TEXT, "Speed Dialing" TEXT, "WAP" TEXT, "WAP Version" TEXT, "Touchscreen Type" TEXT, "Predictive Text Input" TEXT, "User Memory" TEXT, "Supported Languages" TEXT, "Browser" TEXT, "FM Radio Recording" TEXT, "NFC" TEXT, "Keypad Type" TEXT, "Dual Battery" TEXT, "Business Phone" TEXT, "Image Editor" TEXT, "Call Wait/Hold" TEXT, "Conference Call" TEXT, "Hands Free" TEXT, "Call Divert" TEXT, "Call Timer" TEXT, "Social Networking Phone" TEXT, "Instant Message" TEXT, "Series" TEXT, "Phone Book Memory" TEXT, "SMS Memory" TEXT, "JAVA Support" TEXT, "Games" TEXT, "Optical Zoom" TEXT, "Call Records" TEXT, "Logs" TEXT, "Keypad" TEXT, "Music Player" TEXT, "Warranty Service Type" TEXT, "Digital Zoom" TEXT, "Mini USB Port" TEXT, "Mini HDMI Port" TEXT, "HD Game Support" TEXT, "Total Memory" TEXT, "Hot SWAP Support" TEXT, "Mini USB Version" TEXT, "TV Out" TEXT, "Mobile Tracker" TEXT, "Java Application" TEXT, "Ringtones Format" TEXT, "Domestic Warranty" TEXT, "International Warranty" TEXT, "Covered in Warranty" TEXT, "Talk Time" TEXT, "Upgradable Operating System" TEXT, "DLNA Support" TEXT, "Not Covered in Warranty" TEXT, "Additional Content" TEXT)''')

cur.execute('''SELECT * FROM Mobile ORDER BY id DESC LIMIT 1''')
idnew = int(cur.fetchone()[0]) + 1
conn.commit()
cur.close()
url1 = 'https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&page='
url2 = 'https://www.flipkart.com'
for i in range(1, 20):
    conn = sqlite3.connect('mobiles.sqlite')
    cur = conn.cursor()
    html1 = ur(url1+str(i), context=ctx).read()
    soup1 = bs(html1,'html.parser')
    lst1 = soup1.findAll('a',{'class':'_31qSD5'})
    for a in lst1:
        html1 = ur(url2+a['href'], context=ctx).read()
        soup1 = bs(html1, 'html.parser')
        lst2 = soup1.findAll('tr',{'class':'_3_6Uyw row'})
        specs1 = dict()
        for li in lst2:
            specs1[li.find(class_='_3-wDH3 col col-3-12').get_text()]=li.find(class_='_3YhLQA').get_text()
        if(specs1.get('Model Number',0)):    cur.execute('SELECT * FROM Specs WHERE "Model Number"=?', (specs1['Model Number'], ))
        if cur.fetchone():
            continue
        try:
            lst = re.findall('^\S(\S+),(\S+)',a.find(class_='_1vC4OE _2rQ-NK').get_text())[0]
            lst = lst[0]+lst[1]
        except:
            lst = re.findall('^\S(\S+)',a.find(class_='_1vC4OE _2rQ-NK').get_text())[0]
        mod = a.find(class_='_3wU53n').get_text()
        rate = float(a.find(class_='hGSR34 _2beYZw').get_text())
        cur.execute('INSERT INTO Mobile (id, name, price, rating) VALUES (?, ?, ?, ?)',(idnew, mod, lst, rate))
        sql1 = 'INSERT INTO Specs ("id'
        for key in specs1:
            sql1 = sql1 + '", "' + key
        sql1 = sql1 + '") VALUES ("'+str(idnew)
        for key in specs1:
            sql1 = sql1 + '","' + specs1[key]
        sql1 = sql1 + '")'
        cur.execute(sql1)
        print(str(idnew)+' rows inserted')
        idnew = idnew + 1
    conn.commit()
    cur.close()
