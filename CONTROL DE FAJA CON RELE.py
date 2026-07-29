 // CONTROL DE FAJA CON RELE
// Avanza 2 segundos, se detiene 10 segundos y repite infinito
// Rele activado con LOW

#define RELE_MOTOR 7   // Pin D7 controla el rele

void setup() {
  Serial.begin(9600);

  pinMode(RELE_MOTOR, OUTPUT);

  // Rele apagado al iniciar
  digitalWrite(RELE_MOTOR, HIGH);

  Serial.println("Sistema iniciado con rele");
}

void loop() {
  // ENCENDER MOTOR POR 2 SEGUNDOS
  digitalWrite(RELE_MOTOR, LOW);
  Serial.println("Motor encendido");
  delay(2200);

  // APAGAR MOTOR POR 10 SEGUNDOS
  digitalWrite(RELE_MOTOR, HIGH);
  Serial.println("Motor apagado");
  delay(10000);
}
