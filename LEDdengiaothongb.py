import RPi.GPIO as GPIO
import time

# Thiết lập chân GPIO
RED_PIN = 17
YELLOW_PIN = 27
GREEN_PIN = 22

# Cấu hình GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

def turn_off_all():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)

def traffic_light_cycle():
    try:
        while True:
            # Đèn đỏ bật (3 giây)
            turn_off_all()
            GPIO.output(RED_PIN, GPIO.HIGH)
            print("Đèn Đỏ - Dừng lại!")
            time.sleep(3)
            
            # Đèn xanh bật (4 giây)
            turn_off_all()
            GPIO.output(GREEN_PIN, GPIO.HIGH)
            print("Đèn Xanh - Được đi!")
            time.sleep(4)
            
            # Đèn vàng bật (1 giây)
            turn_off_all()
            GPIO.output(YELLOW_PIN, GPIO.HIGH)
            print("Đèn Vàng - Chuẩn bị dừng!")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("Dừng chương trình")
    finally:
        turn_off_all()
        GPIO.cleanup()

# Chạy chương trình
if __name__ == "__main__":
    traffic_light_cycle()