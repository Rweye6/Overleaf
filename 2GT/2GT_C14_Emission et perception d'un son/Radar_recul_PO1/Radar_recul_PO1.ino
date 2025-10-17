//Variables :

int ER = 4;             // capteur ultrasons sur D4 const plus rigoureux!
int chrono; 
float distance;
const float celerite = 340.0;

void setup()
{
Serial.begin(9600);
pinMode(5, OUTPUT);
}

void loop()
{
//émission d'une salve de 10 µs
pinMode(ER, OUTPUT);    // paramétrage du module en sortie (émission)
digitalWrite(ER, HIGH); //broche niveau haut : émission
delayMicroseconds(10);  //délai de 10 µs     
digitalWrite(ER, LOW);  //broche niveau bas : fin d'émission
pinMode(ER, INPUT);     // paramétrage du module en entrée (réception)

//mesure de la durée
chrono = pulseIn(ER, HIGH); // arrêt chronométrage quand on reçoit un signal
delay(500);

//calcul de la distance
distance=celerite*0.5*chrono*1E-6;


if ( (distance=celerite*0.5*chrono*1E-6 <0.08) && (distance=celerite*0.5*chrono*1E-6 >0.02) ) {tone(5,500,100);
delay (25);

}

else {if (distance=celerite*0.5*chrono*1E-6<0.02) {tone(5,1000,500);
delay (50);

}

}}
