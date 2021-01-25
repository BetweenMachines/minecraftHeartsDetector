int relay = 6;
String d;
int health;
int tHealth = 29;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(relay, OUTPUT);
}

void loop() {
}

void serialEvent() {
  if(Serial.available() > 0) {
    d = Serial.readString();
    Serial.end();
    Serial.begin(9600);

    health = d.toInt();
    if(health > 0) {
      digitalWrite(relay, HIGH);
      delay(1000);
      digitalWrite(relay, LOW);
    } else {
        digitalWrite(relay, LOW);
        }
  }
}
