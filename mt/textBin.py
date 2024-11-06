class TuringMachineToBinary:
    def __init__(self, input_data):
        self.cinta = list(input_data)  # Cinta de entrada con el texto ASCII
        self.binary_cinta = []  # Cinta de salida donde almacenaremos la conversión binaria
        self.pointer = 0  # Puntero en la cinta de entrada
        self.state = "READ_ASCII"  # Estado inicial de la máquina

    def run(self):
        while self.pointer < len(self.cinta):
            if self.state == "READ_ASCII":
                self.read_ascii()
            elif self.state == "CONVERT_TO_BINARY":
                self.convert_to_binary()
            elif self.state == "WRITE_BINARY":
                self.write_binary()
            elif self.state == "MOVE_TO_NEXT_CHAR":
                self.move_to_next_char()
        
        return ''.join(self.binary_cinta)  # Devuelve la cinta binaria completa como cadena

    def read_ascii(self):
        # Lee el carácter ASCII actual en la posición del puntero
        self.current_char = self.cinta[self.pointer]
        self.state = "CONVERT_TO_BINARY"  # Cambia al estado de conversión

    def convert_to_binary(self):
        # Convierte el carácter ASCII actual a una secuencia de 8 bits
        self.binary_representation = f"{ord(self.current_char):08b}"  # Convierte a binario con 8 bits
        self.state = "WRITE_BINARY"  # Cambia al estado de escritura

    def write_binary(self):
        # Escribe cada bit de la representación binaria en la cinta binaria
        self.binary_cinta.extend(self.binary_representation)  # Añade los bits a la cinta de salida
        self.state = "MOVE_TO_NEXT_CHAR"  # Cambia al estado de avance

    def move_to_next_char(self):
        # Avanza el puntero al siguiente carácter
        self.pointer += 1
        self.state = "READ_ASCII"  # Vuelve al estado de lectura para el siguiente carácter



if __name__ == "__main__":
    # Ejemplo de uso
    input_text = "Carlos"

    turing_machine = TuringMachineToBinary(input_text)

    # Ejecutar la máquina y obtener la salida en binario
    binary_output = turing_machine.run()

    # Mostrar el resultado en binario
    print("Entrada en texto:", input_text)
    print("Salida en binario:", binary_output)
