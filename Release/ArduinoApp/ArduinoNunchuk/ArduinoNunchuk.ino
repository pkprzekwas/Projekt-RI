/*
 * ArduinoNunchukDemo.ino
 *
 * Copyright 2011-2013 Gabriel Bianconi, http://www.gabrielbianconi.com/
 *
 * Project URL: http://www.gabrielbianconi.com/projects/arduinonunchuk/
 *
 */

#include <Wire.h>
#include <ArduinoNunchuk.h>

#define BAUDRATE 19200

ArduinoNunchuk nunchuk = ArduinoNunchuk();
String message;
String temp;
void setup()
{
  Serial.begin(BAUDRATE);
  nunchuk.init();
}

void loop()
{
  nunchuk.update();
  message=String("");
  temp=String( nunchuk.analogX, DEC);
  message+=(temp + " ");
  temp=String(nunchuk.analogY, DEC);
   message+=(temp + " ");
  temp=String(nunchuk.accelX, DEC);
   message+=(temp + " ");
  temp=String(nunchuk.accelY, DEC);
   message+=(temp + " ");
  temp=String(nunchuk.accelZ, DEC);
   message+=(temp + " ");
  temp=String(nunchuk.zButton, DEC);
   message+=(temp + " ");
  temp=String(nunchuk.cButton, DEC);
   message+=(temp + " ");
  Serial.println(message);
 /* Serial.print(' ');
  Serial.print(nunchuk.analogY, DEC);
  Serial.print(' ');
  Serial.print(nunchuk.accelX, DEC);
  Serial.print(' ');
  Serial.print(nunchuk.accelY, DEC);
  Serial.print(' ');
  Serial.print(nunchuk.accelZ, DEC);
  Serial.print(' ');
  Serial.print(nunchuk.zButton, DEC);
  Serial.print(' ');
  Serial.println(nunchuk.cButton, DEC);*/
}
