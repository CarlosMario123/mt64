class TuringMachineGroup24Bits:
    def __init__(self, binary_input):
        self.cinta = list(binary_input)  # Cinta con los bits binarios de entrada
        self.output_cinta = []  # Cinta de salida con bloques de 24 bits y marcadores
        self.pointer = 0  # Puntero en la cinta de entrada
        self.state = "READ_BIT"  # Estado inicial de la máquina
        self.bit_counter = 0  # Contador de bits para agrupar en bloques de 24

    def run(self):
        while self.pointer < len(self.cinta):
            if self.state == "READ_BIT":
                self.read_bit()
            elif self.state == "WRITE_MARKER":
                self.write_marker()
            elif self.state == "MOVE_TO_NEXT_BLOCK":
                self.move_to_next_block()
        
        return ''.join(self.output_cinta)  # Devuelve la cinta con bloques de 24 bits y separadores

    def read_bit(self):
        # Lee el bit actual y lo añade a la cinta de salida
        self.output_cinta.append(self.cinta[self.pointer])
        self.bit_counter += 1  # Incrementa el contador de bits
        if self.bit_counter == 24:  # Si alcanzamos 24 bits, cambia al estado para escribir el marcador
            self.state = "WRITE_MARKER"
        else:
            self.pointer += 1  # Mueve el puntero al siguiente bit

    def write_marker(self):
        # Añade un marcador para indicar el final del bloque de 24 bits
        self.output_cinta.append('|')  # Agrega un separador para el bloque de 24 bits
        self.state = "MOVE_TO_NEXT_BLOCK"  # Cambia al estado de avanzar al siguiente bloque

    def move_to_next_block(self):
        # Reinicia el contador de bits y vuelve a leer el siguiente bloque de 24 bits
        self.bit_counter = 0
        self.pointer += 1  # Avanza el puntero al siguiente bit
        self.state = "READ_BIT"  # Cambia al estado para leer el siguiente bloque de bits

if __name__ == "__main__":
    binary_input = "010011010110000101101110"
    grouping_machine = TuringMachineGroup24Bits(binary_input)
    grouped_output = grouping_machine.run()
    print("Entrada binaria:", binary_input)
    print("Salida con bloques de 24 bits:", grouped_output)

# Mostrar el resultado con los bloques de 24 bits

