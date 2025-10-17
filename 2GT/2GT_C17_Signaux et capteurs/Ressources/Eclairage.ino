//commande d'un éclairage

const int photoD = A0 ; // branchement module photoDiode
const int DELPin = 2 ; // branchement module DEL
float N ; // niveau lu
float UE ; // tension d'entrée

// int ValeurSeuil = ...... ;

void setup() {
    Serial.begin(9600) ;
    pinMode(photoD, INPUT) ;
    pinMode(DELPin, OUTPUT) ;
}

void loop(){
    N = analogRead(photoD) ; // lecture sur le module photoD
    // float UE = ...... ; // calcul de la tension d'entrée

    delay(1000) ;
    Serial.print(N) ;
    Serial.print("  tension d'entrée UE = ");
    //Serial.print(UE);
    Serial.println("V");
}
