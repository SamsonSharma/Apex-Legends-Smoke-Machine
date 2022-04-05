char Data;
int pin=10;

void setup() {
  pinMode(pin,OUTPUT);
  Serial.begin(9600);

}

void loop() {
  if(Serial.available() > 0){
    Data = Serial.read();
    Serial.print(Data);

  if(Data == '1'){
    digitalWrite(pin, HIGH);
    }

    else if(Data == '0'){
      digitalWrite(pin, LOW);
      }

  }
}
