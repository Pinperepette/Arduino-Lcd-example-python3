#include <LiquidCrystal.h>

LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.print("start");
}

void loop() {
  if (Serial.available()) {
    delay(100); 
    lcd.clear();
    while (Serial.available() > 0) {
      char c = Serial.read();
      lcd.write(c);
    }
  }
}