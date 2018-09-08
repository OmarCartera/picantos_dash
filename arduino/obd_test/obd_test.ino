#include <OBD2UART.h>

/*
 *      The circuit:
 *
 *    LCD         Arduino
 *     RS           12
 *   Enable         11
 *     D4            5
 *     D5            4
 *     D6            3
 *     D7            2
 *    R/W          ground
 *     V0          ground
*/

#include <Arduino.h>
#include <Wire.h>

#include <LiquidCrystal.h>

COBD obd;

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int col = 0;
int index = 0;
int i =0;

bool light = LOW;

int value = 0;

// make some custom characters:
byte first[8] = {
  0b10000,
  0b10000,
  0b10000,
  0b10000,
  0b10000,
  0b10000,
  0b10000,
  0b10000
};

byte second[8] = {
  0b11000,
  0b11000,
  0b11000,
  0b11000,
  0b11000,
  0b11000,
  0b11000,
  0b11000
};

byte third[8] = {
  0b11100,
  0b11100,
  0b11100,
  0b11100,
  0b11100,
  0b11100,
  0b11100,
  0b11100
};

byte fourth[8] = {
  0b11110,
  0b11110,
  0b11110,
  0b11110,
  0b11110,
  0b11110,
  0b11110,
  0b11110
};

byte fifth[8] = {
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111,
  0b11111
};

void setup()
{
  // we'll use the debug LED as output
  pinMode(13, OUTPUT);

  // initialize LCD and set up the number of columns and rows:
  lcd.begin(16, 2);

  // create a new character
  lcd.createChar(0, first);
  lcd.createChar(1, second);
  lcd.createChar(2, third);
  lcd.createChar(3, fourth);
  lcd.createChar(4, fifth);


  // set the cursor to the top left
  lcd.setCursor(0, 0);

  // start communication with OBD-II UART adapter
  obd.begin();
  
  // initiate OBD-II connection until success
  while(!obd.init())
  {
    digitalWrite(13, light);
    delay(500);
    light = !(light);
  }
}


void loop()
{
  if (obd.readPID(PID_RPM, value))
  {
    // RPM is successfully read and its value stored in variable 'value'
  
    index = map(value, 0, 4000, 0, 80)%5;
    col   = map(value, 0, 4000, 0, 80)/5;


    for(int i=0; i<col; i++)
    {
      lcd.setCursor(i, 0);
      lcd.write(4);
    }

    lcd.write(index);

    lcd.setCursor(10, 1);
    lcd.print(value);

    delay(75);
  }

  lcd.clear();
}
