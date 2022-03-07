global animation

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT

#from luma.led_matrix.device import max7219
#from luma.core.interface.serial import spi, noop
#from luma.core.render import canvas
#from luma.core.virtual import viewport
#from luma.core.legacy import text, show_message
#from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

import random
import time
import datetime

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=90, blocks_arranged_in_reversed_order=False)
device.contrast(16)


now = datetime.datetime.now()


#print("Zu Welchem Zeitpunkt geht der countdown?")
#houres_in = int(input("Stunden: "))
#minutes_in = int(input("Minute: "))
#print("Countdown zur Uhrzeit: ", houres_in, ":", minutes_in)
#print("Derzeitige Zeit: ", now.hour, now.minute)

#future_date = datetime.datetime(2022,3,4,houres_in,minutes_in)
#paste_date = datetime.datetime.now
#diffrence = (future_date - paste_date)
#total_seconds = diffrence.total_seconds()
#print(total_seconds)seconds_until_complete

def draw(timer, over, animation):
    with canvas(device) as draw:
        print("Time: ", timer)
        print("ANimation: ", animation)
        if over == True:
            show_message(device, "Jetzt geh mor Heim und fahren mit dem RB80 ins Erzgebirge und tun dann sachen machen die sachen machen die sachen machen die sachen machen die sachen machen die sachen machen die sachen mache joa", fill="white", font=CP437_FONT)
            text(draw, (0,0), "Timer is over", fill="white", font=CP437_FONT)
            time.sleep(120)
        else:
            if animation <= 5:
                text(draw, (0,0), "We Zeit einfügen", fill="white", font=TINY_FONT)

            else:
                text(draw, (-12,0), timer, fill="white", font=TINY_FONT)
                animation = animation - 1
                return animation


def countdown(t,animation):

    """
    Countdown Timer
    """
    while t > -1:

        # Divmod takes only two arguments so
        # you'll need to do this for each time
        # unit you need to add
        animation = animation -1
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days, hours, mins, secs)
        time.sleep(1)
        t -= 1
        over = False
        if t <= 0:
            over = True
        draw(timer, over, animation)
        if animation <= 0:
            animation = 30


t = 17820
animation = 30

countdown(int(t), animation)
