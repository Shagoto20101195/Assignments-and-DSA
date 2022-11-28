// LED high is connected to pin 13
const int trigPin = 6;
const int echoPin = 5;
const int buzz = 11;

long duration;
int distance;
void setup() {
  // put your setup code here, to run once:
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzz, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration*0.034 / 2; // in cm

  if(distance <= 15)
  {
    digitalWrite(buzz, HIGH);
    tone(buzz, 100);
    delay(500);
    tone(buzz, 250);
    delay(500);
  }
  else
  {
    digitalWrite(buzz, LOW);
    noTone(buzz);   
  }    
}