const int moistureSensorPin = A0; // Moisture sensor analog pin
const int moistureThreshold = 300; // Adjust this threshold based on your sensor and soil

void setup() {
  pinMode(moistureSensorPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // Read the moisture level from the sensor
  int moistureLevel = analogRead(moistureSensorPin);
  
  // Send the moisture level to the serial port
  Serial.println(moistureLevel);

  // Wait for 1 second before the next reading
  delay(10000);
}
