void setup()
{
  Serial.begin(115200);
}

int i = 0;

void loop()
{
  i += 5;
  
  Serial.println(i);
  delay(200);
}
