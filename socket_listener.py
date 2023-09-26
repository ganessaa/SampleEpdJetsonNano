import socket

def start_server():
    host = "127.0.0.1"
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((host, port))
      s.listen(1)
      print("Server started!")

      while True:
        c, _ = s.accept()
        while True:
          data = c.recv(1).decode("utf-8")
          if not data:
              break
          if str(data) == "0":
            drawText("Open")
          elif str(data) == "1":
            drawText("Close")
          else:
            drawText("")
        c.close()

import sys
import os
codedir = "/nvdli-nano/data/e-Paper/RaspberryPi_JetsonNano/python/"
fontdir = os.path.join(codedir, 'pic')
libdir = os.path.join(codedir, 'lib')

if os.path.exists(libdir):
  sys.path.append(libdir)

import logging
from waveshare_epd import epd1in54_V2
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.ERROR)

def drawText(txt):
  draw.rectangle((0, 0, 200, 200), fill = 255)
  draw.text((0, 0), txt, font = font, fill = 0)
  epd.displayPart(epd.getbuffer(image.rotate(90)))

def clearEpd():
  logging.info("Clear...")
  epd.init(0)
  epd.Clear(0xFF)

def sleepEpd():
  logging.info("Goto Sleep...")
  epd.sleep()

epd = epd1in54_V2.EPD()
clearEpd()
epd.init(1)

image = Image.new('1', (epd.width, epd.height), 255)
epd.displayPartBaseImage(epd.getbuffer(image))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(os.path.join(fontdir, 'Font.ttc'), 164)

if __name__ == "__main__":
  start_server()
