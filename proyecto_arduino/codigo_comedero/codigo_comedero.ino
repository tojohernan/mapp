#include "DHT.h" // incluyo ibreria de sensor temperatura

/*   ==============>>> CONEXIONES   <<<================

HC-SR04 conexiones:
  VCC al arduino 5v 
  GND al arduino GND
  Echo al Arduino pin 6 
  Trig al Arduino pin 7
  
COOLER
  pin 13
LUCES
  pin 3
SENSOR TEMPERATURA DHT
  pin 8
*/

//===========================================

//	VARIABLES DE ALIMENTO(sensor distancia) 

#define PECHO 6
#define PTRIG 7
float porcentaje_lleno;
long duracion, distancia;   
int luz=3;
int motor=4;
int estado_motor=0;
int estado_cooler=0;
//-------------------------------------------

//	VARIABLES SDE SENSOR DE TEMPERATURA

#define DHTPIN 8 
#define DHTTYPE DHT11 
DHT dht(DHTPIN, DHTTYPE); 
int cooler=5;
int estado_luz=0;
//=============================================

// INICIO 

void setup() {   
  Serial.begin (9600);       // inicializa el puerto seria a 9600 baudios
  
  // DEFINE PINES SENSOR DISTANCIA
  pinMode(PECHO, INPUT);     // define el pin 6 como entrada (echo)
  pinMode(PTRIG, OUTPUT);    // define el pin 7 como salida  (triger)
  
  // PIN MOTOR LLENADO
  pinMode(motor, OUTPUT);            // Define el pin 4 como salida 
  
  // PIN LUCES 
  pinMode(luz, OUTPUT);            // Define el pin 1 como salida
  //pinMode(2, OUTPUT);            // Define el pin 2 como salida
  
  // PIN COOLER
  pinMode(cooler, OUTPUT);
  
  //SENSOR TEMPERATURA
  dht.begin();
}


void loop() {

    if(Serial.available()>0) //Comprobamos si en el buffer hay datos
  {
    int dato=Serial.read();  //Lee cada carácter uno por uno y se almacena en una variable
    Serial.println(dato);  //Imprimimos en la consola el carácter recibido
  }else{
    Serial.println("no entra");  //Imprimimos en la consola el carácter recibido
  }
  
  digitalWrite(PTRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(PTRIG, HIGH);   // Genera el pulso de triger por 10ms
  delayMicroseconds(10);
  digitalWrite(PTRIG, LOW);
  duracion = pulseIn(PECHO, HIGH);
  distancia = (duracion/2) / 29;            // Calcula la distancia en centimetros
  porcentaje_lleno = ((((-100)*distancia)+6000)/50); // Calcula el porcentaje que esta lleno
  

//==============================================

// LOGICA DE LLENADO  
 
  if (distancia >= 500 || distancia <= 0){  // si la distancia es mayor a 500cm o menor a 0cm 
    Serial.println("ERROR LECTURA");                  // no mide nada
  }
  else {
		if (porcentaje_lleno <= 20 && estado_motor == 0){
		digitalWrite(motor,HIGH);
		estado_motor=1;
                }
		else if (porcentaje_lleno >= 100 && estado_motor == 1){
		digitalWrite(motor,LOW);
		estado_motor=0;
		}
	}

//============================================

// CONTROL DE TEMPERATURA
	
  float Temperatura = dht.readTemperature();
  float Humedad = dht.readHumidity();
  int temp_min = 30;
  int temp_max = 34;
  int temp_ideal= ((temp_max-temp_min)/2);
  
  if (Temperatura >=temp_min && Temperatura <=temp_max){
	if (estado_luz == 1){
	digitalWrite(luz,LOW);
	estado_luz=0;
	}
	if (estado_cooler == 1){
	digitalWrite(cooler,LOW);
	estado_cooler=0;
	}
  }
  else if (Temperatura <= temp_min && estado_luz == 0){
   digitalWrite(luz,HIGH);
   estado_luz=1;
	}
  else if ( Temperatura >= temp_max && estado_cooler == 0){
	digitalWrite(cooler,HIGH);
	estado_cooler=1;
	}
	
//====================================
 
//String jsonString = "{\"temp\":";jsonString += Temperatura;jsonString +="\",\"hum\":";jsonString += Humedad;jsonString +="\",\"porc_lleno\":";jsonString += porcentaje_lleno;jsonString +="\"}";
//Serial.println(jsonString);
Serial.print(Temperatura);  
Serial.print(",");
Serial.print(Humedad);
Serial.print(",");
Serial.println(porcentaje_lleno);

  delay(5000);
} 
