int ledPins[] = {2, 3, 4, 5, 6};

void setup() {
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    int count = Serial.read() - '0';  // Convert char to int
    for (int i = 0; i < 5; i++) {
      digitalWrite(ledPins[i], i < count ? HIGH : LOW);
    }
  }
}