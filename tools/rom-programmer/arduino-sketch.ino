#define ADDRESS1_CLK 6  // 6
#define ADDRESS2_CLK 11 // 11
#define ADDRESS1_PIN 10 // 10
#define ADDRESS2_PIN 12 // 12

#define DATA_PIN 8 // 8
#define DATA_CLK 7 // 7

#define WRITE_PIN 5
#define CLEAR_PIN 9
#define STATUS_LED 13

byte buffer[64];
int buffer_pointer;

void setup() {
  Serial.begin(9600);

  pinMode(ADDRESS1_CLK, OUTPUT);
  pinMode(ADDRESS2_CLK, OUTPUT);
  pinMode(DATA_CLK, OUTPUT);
  pinMode(ADDRESS1_PIN, OUTPUT);
  pinMode(ADDRESS2_PIN, OUTPUT);
  pinMode(DATA_PIN, OUTPUT);
  pinMode(WRITE_PIN, OUTPUT);
  pinMode(CLEAR_PIN, OUTPUT);
  pinMode(STATUS_LED, OUTPUT);

  digitalWrite(WRITE_PIN, HIGH);
  digitalWrite(CLEAR_PIN, HIGH);

  Serial.print("online");
}

void loop() {
  digitalWrite(STATUS_LED, LOW);
  while (Serial.available() < 2) {}
  

  int page = Serial.read() << 6;
  int size = Serial.read();
  while (Serial.available()) {Serial.read();}
  
  Serial.print("\xff\x01");

  
  buffer_pointer = 0;
  int s = size;

  while (s > 32) {
    
    digitalWrite(STATUS_LED, LOW);
    while (Serial.available() < 32) {}
    digitalWrite(STATUS_LED, HIGH);

    for (int i=0; i<32; i++)
      buffer[i+buffer_pointer] = Serial.read();
    buffer_pointer += 32;
    s -= 32;
    Serial.print("\xff\x02");
  }
  
  while (Serial.available() < s) {}
  for (int i=0; i<s; i++)
    buffer[i+buffer_pointer] = Serial.read();
  Serial.print("\xff\x02");
  while (!Serial.available()) {}
  while (Serial.available() > 1) {}
  while (Serial.available()) {Serial.read();}

  for (int i=0; i<size; i++) {
    writeDataRom((i & 0x3f) + page, (int) buffer[i]);
    digitalWrite(WRITE_PIN, LOW);
    digitalWrite(WRITE_PIN, HIGH);
    delay(10);
  }
    
  Serial.print("\xff\x03");
  while (Serial.available()) {Serial.read();}
}

void writeDataRom(int address, int data) {
  digitalWrite(CLEAR_PIN, LOW);
  digitalWrite(CLEAR_PIN, HIGH);
  digitalWrite(DATA_CLK, LOW);
  digitalWrite(ADDRESS1_CLK, LOW);
  digitalWrite(ADDRESS2_CLK, LOW);

  shiftOut(DATA_PIN, DATA_CLK, MSBFIRST, data & 0xFF);
  shiftOut(ADDRESS1_PIN, ADDRESS1_CLK, MSBFIRST, address & 0xFF);
  shiftOut(ADDRESS2_PIN, ADDRESS2_CLK, MSBFIRST, (address & 0xFF00) >> 8);
  
}
