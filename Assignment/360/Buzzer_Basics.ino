void setup() {
  // put your setup code here, to run once:
  pinMode(12, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  tone(12, 261); //Middle C
  delay(1000);

  tone(12, 277); //C#
  delay(1000);

  tone(12, 294); //D
  delay(1000);

  tone(12, 311); //D#
  delay(1000);

  tone(12, 330); //E
  delay(1000);
 
  tone(12, 349); //F
  delay(1000);

  tone(12, 370); //F#
  delay(1000);

  tone(12, 392); //G
  delay(1000);

  tone(12, 415); //G#
  delay(1000);

  tone(12, 440); //A
  delay(1000);
}
