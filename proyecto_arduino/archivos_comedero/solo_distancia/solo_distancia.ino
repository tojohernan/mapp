#define PECHO 6
#define PTRIG 7
float distancia;
float duracion;

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
pinMode(PECHO,INPUT);
pinMode(PTRIG, OUTPUT);
}

void loop() {
  digitalWrite(PTRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(PTRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PTRIG, LOW);
  duracion = pulseIn(PECHO, HIGH);
  distancia = (duracion/2)/29;
  Serial.println(distancia);
  delay(50000);
}
