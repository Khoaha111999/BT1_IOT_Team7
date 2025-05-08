#include <wiringPi.h>
#include <stdio.h>

#define LED_PIN 0  // WiringPi pin 0 = BCM GPIO17

int main(void) {
    // Khởi tạo thư viện
    if (wiringPiSetup() == -1) {
        printf("Không thể khởi tạo WiringPi\n");
        return 1;
    }

    pinMode(LED_PIN, OUTPUT);  // Đặt chân là output

    while (1) {
        digitalWrite(LED_PIN, HIGH);  // Bật LED
        delay(500);                   // Delay 500ms
        digitalWrite(LED_PIN, LOW);   // Tắt LED
        delay(500);                   // Delay 500ms
    }

    return 0;
}
