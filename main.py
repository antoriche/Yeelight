import yeelight
import color
import time

light = yeelight.Yeelight('192.168.0.196')
#light.toggle()
light.set_rgb(color.rgb(255,0,0))
time.sleep(1)
light.set_rgb(color.rgb(0,255,0))
time.sleep(1)
light.set_rgb(color.rgb(0,0,255))