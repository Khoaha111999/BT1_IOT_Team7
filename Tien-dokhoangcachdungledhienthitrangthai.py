from gpiozero import LED, DistanceSensor
import time

sensor = DistanceSensor(echo=23, trigger=24)
led = LED(14)

while True:
    distance = sensor.distance * 100  # đổi sang cm
    print("Khoảng cách:", distance, "cm")
    
    if distance < 30:
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
    else:
        led.off()
    
    time.sleep(0.1)


