#include <Keypad.h>

const int ROW_NUM = 4; //four rows
const int COLUMN_NUM = 4; //four columns

int analogPinWater = A0; // potentiometer wiper (middle terminal) connected to analog pin 3
                    // outside leads to ground and +5V
int val = 0;  // variable to store the value read

int raspberryPiPinWater = 10;
int raspberryPiPinButton = 13;
int motionSensorPin = 12;
int pinDisarmentPin = 0;
int pinArmentPin = 1;


String tempPin;
static const char * const pinCodes[] = {"1234", "0852", "1111"};


char keys[ROW_NUM][COLUMN_NUM] = {
  {'1','2','3', 'A'},
  {'4','5','6', 'B'},
  {'7','8','9', 'C'},
  {'*','0','#', 'D'}
};

byte pin_rows[ROW_NUM] = {7, 6, 5, 4}; //connect to the row pinouts of the keypad
byte pin_column[COLUMN_NUM] = {3, 2, 8, 9}; //connect to the column pinouts of the keypad
  //val = analogRead(analogPin);  // read the input pin
  //Serial.println(val);          // debug value

Keypad keypad = Keypad( makeKeymap(keys), pin_rows, pin_column, ROW_NUM, COLUMN_NUM );

// void readWaterLevel(){
//   val = analogRead(analogPin);  // read the input pin
//   Serial.println(val);          // debug value
//}

void pingRaspberryPi(int Condition){
  if(Condition == 10){
    digitalWrite(raspberryPiPinWater, HIGH);
    //delay(3000);
    Serial.println("Pinged Water");
    digitalWrite(raspberryPiPinWater, LOW);

    } 
    else if(Condition == 13){
    digitalWrite(raspberryPiPinButton, HIGH);
    //delay(3000);
    Serial.println("Distress button pushed");
    digitalWrite(raspberryPiPinButton, LOW);

    }
}

void readWaterLevel(){
  int value = analogRead(analogPinWater);
  if(value >= 300){
    Serial.println('Water level overflowing!!!');
    pingRaspberryPi(10);
  }
}

//pin check 
void pinEntry(String pin){
  bool incorrect = true;
  for(int i = 0; i < 3; i++){
    if(pin == pinCodes[i]){
      pinEntryCorrect();
      Serial.println("Correct pin!");
      incorrect = false;
      break;
    }
  }
  if(incorrect == true){
    pinEntryIncorrect();
    Serial.println("PIN INCORRECT. YOU WILL BE SENTENCED TO DEATH.");
  }
}

void pinEntryCorrect(){
  digitalWrite(pinDisarmentPin, HIGH);
  delay(30);
  digitalWrite(pinDisarmentPin, LOW);
}

void pinEntryIncorrect(){
  digitalWrite(pinArmentPin, HIGH);
  delay(2000);
  digitalWrite(pinArmentPin, LOW);
}

void motionSensor(){
  int motionVal = digitalRead(motionSensorPin);
  if(motionVal == HIGH){

  }
  delay(1000);
}


void setup(){
  Serial.begin(9600);
  pinMode(raspberryPiPinWater, OUTPUT);
  pinMode(raspberryPiPinButton, OUTPUT);
  pinMode(motionSensorPin, INPUT);
  
  pinMode(pinDisarmentPin, OUTPUT);
  pinMode(pinArmentPin, OUTPUT);
  digitalWrite(pinDisarmentPin, LOW);
  digitalWrite(pinArmentPin, LOW);

  digitalWrite(raspberryPiPinWater, LOW);
  digitalWrite(raspberryPiPinButton, LOW);

}

void loop(){

  char key = keypad.getKey();
  if (key){
    Serial.println(key);
    if(key == 'D'){
      pingRaspberryPi(13);
    }
    if(key == '1'||key == '2' ||key == '3' ||key == '4' ||key == '5' ||key == '6' ||key == '7' ||key == '8' ||key == '9' ||key == '0' ||key == '*' ||key == '#' ||key == 'C' ||key == 'B' ||key == 'A'){
      if (tempPin.length() < 4){
        tempPin += key;
        Serial.println(tempPin);
      }
      if (tempPin.length() == 4){
        Serial.println("Testing PIN");
        pinEntry(tempPin);
        tempPin = "";
      }
    }
  }
  readWaterLevel();



}