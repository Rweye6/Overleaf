// C++ code
//

//broches
const int(Alim)=2;
const int(mesure) = A0;

//grandeurs
unsigned long debutCharge;
unsigned long tau;
unsigned long tau10 = 0;
float C;
float R = 10000;
int i;


void setup()
{
// initialisation moniteur série
  Serial.begin(9600);
  Serial.println("mesure...");
  for (i=0;i<10; i++){
// Décharge préalable de C (mise à 0V pendant 1s
    pinMode (Alim, OUTPUT);
    digitalWrite (Alim, LOW);
    delay(1000); // attente d'une seconde
    
// Charge de C
    digitalWrite(Alim, HIGH);
    debutCharge=millis();
    while(analogRead(mesure)<647){
      //647 = 63% de 1023 on attend....
  }
    tau = millis() - debutCharge;
    tau10= tau10 + tau;
  }
  float (tau) = float(tau10)/10;
  float C = float(tau)*1000/R; //C en nF
//affichage :
  Serial.print("Constante de temps : ");
  Serial.print(tau);
  Serial.println(" ms ");
  Serial.print("Capacité : ");
  Serial.print(C);
  Serial.println(" nF");
}
  void loop(){
}
