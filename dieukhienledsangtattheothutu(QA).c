#include <wiringPi.h>
#include <stdio.h>
#include <unistd.h>  // dùng cho usleep()

// Danh sách các chân GPIO theo wiringPi (khác với BCM)
int ledPins[7] = {0, 1, 2, 3, 4, 5, 6}; // Ví dụ: GPIO17 -> wiringPi pin 0

int main(void) {
    wiringPiSetup(); // Khởi tạo thư viện wiringPi

    // Thiết lập các chân là OUTPUT
    for (int i = 0; i < 7; i++) {
        pinMode(ledPins[i], OUTPUT);
        digitalWrite(ledPins[i], LOW); // Tắt LED ban đầu
    }

    while (1) {
        // Sáng từ 1 đến 7
        for (int i = 0; i < 7; i++) {
            digitalWrite(ledPins[i], HIGH);
            usleep(300000); // 300ms
        }

        // Tắt từ 7 đến 1
        for (int i = 6; i >= 0; i--) {
            digitalWrite(ledPins[i], LOW);
            usleep(300000); // 300ms
        }
    }

    return 0;
}
