/*Libs*/
#include <Ultrasonic.h>
#include <DHT.h>

/*Pinos*/
#define sensor1_trigger 2
#define sensor1_echo 3
#define sensor2_trigger 4
#define sensor2_echo 5

#define DHTPIN A1 
#define DHTTYPE DHT11 // DHT 11

/*Distancia de calibragem do sensor*/
#define H 10

/*Tempo maximo para delay sensor*/
#define T 5

/*Divisoes de segundo para captura dos sensores*/
#define C 5

/*Inicializar sensor ultrassonico*/
Ultrasonic sensor1(sensor1_trigger, sensor1_echo);
Ultrasonic sensor2(sensor2_trigger, sensor2_echo);

DHT dht(DHTPIN, DHTTYPE);

int pessoas = 0;
char buff[50];
char umichar[5];

void setup() {
  Serial.begin(9600);
  //Serial.println("Lendo dados do sensor");
  dht.begin();

  }


void loop() {
  float dist1 = sensor1.read(CM);
  float dist2 = sensor2.read(CM);
  float h = dht.readHumidity();
  int i;
/*
  Serial.print("\nDistancia s1 em cm: "); Serial.print(dist1);
  Serial.print("  Distancia s2 em cm: "); Serial.print(dist2);
  Serial.print("  Pessoas: "); Serial.print(pessoas);
  Serial.print("  Umidade: "); Serial.print(h);

  */
  dtostrf(h, 3, 1, umichar);
  sprintf(buff, "umidade: %s, pessoas: %d", umichar, pessoas);
  Serial.println(buff);


  /*Para sensor 1 acionado*/
  if (dist1 <= H){
    //Serial.print("\nPessoa entrou... ");
    i = 0;
    while(i < T*1000){
        dist2 = sensor2.read(CM);
        if(dist2 <= H){
          pessoas++;
      //    Serial.print("\nConfirmado!\n");
          i = i + T*1000;
          delay(1000/C);
          dist2 = sensor2.read(CM);
        }else{
          i = i + 1000/C;
          delay(1000/C);
        }
    }
  }

  /*Para sensor 2 acionado*/
  if (dist2 <= H){

    if (pessoas == 0){
      pessoas = 0;
    }
    else{
     // Serial.print("\nPessoa saiu... ");
      i = 0;
      while(i < T*1000){
          dist1 = sensor1.read(CM);
          if(dist1 <= H){
            pessoas--;
       //     Serial.print("\nConfirmado!\n");
            i = i + T*1000;
            dist1 = sensor1.read(CM);
            delay(1000/C);
          }
          else{
            i = i + 1000/C;
            delay(1000/C);
          }
      }
    }
  }
  delay(1000/C);
}