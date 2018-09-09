/*
  The circuit:

      LCD         Arduino
 *     RS           12
 *   Enable         11
 *     D4            5
 *     D5            4
 *     D6            3
 *     D7            2
 *    R/W          ground
 *     V0          ground
*/

// include the library code:
#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

String clr = "                ";

int col = 0;
int index = 0;

int temp_col = 0;

int value = 0;
int temp_value = 0;

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


void setup() {
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
}

void loop()
{
  temp_col = col;
  temp_value = value;
  
  lcd.setCursor(0, 0);

  value = analogRead(A6);
  
  index = map(value, 0, 1023, 0, 80)%5;
  col   = map(value, 0, 1023, 0, 80)/5;


  for(int k=0; k<col; k++)
  {
    lcd.setCursor(k, 0);
    lcd.write(4);
  }

  lcd.write(index);

  lcd.setCursor(10, 1);
  lcd.print(value);

  delay(10);

  if(temp_col != col)
  {
      lcd.setCursor(0, 0);
      lcd.print(clr);
  }

  if(abs(value-temp_value) >= 12)
  {
    lcd.setCursor(10, 1);
    lcd.print("    ");
  }
}
