class TuringMachineDivide6Bits:
    def __init__(self, grouped_binary_input):
        self.cinta = list(grouped_binary_input)  # Cinta con los bloques de 24 bits marcados por '|'
        self.output_cinta = []  # Cinta de salida con grupos de 6 bits y marcadores
        self.pointer = 0  # Puntero en la cinta de entrada
        self.state = "READ_BIT"  # Estado inicial de la máquina
        self.bit_counter = 0  # Contador de bits para agrupar en bloques de 6

    def run(self):
        while self.pointer < len(self.cinta):
            if self.state == "READ_BIT":
                self.read_bit()
            elif self.state == "WRITE_GROUP_MARKER":
                self.write_group_marker()
            elif self.state == "MOVE_TO_NEXT_GROUP":
                self.move_to_next_group()
        
        return ''.join(self.output_cinta)  # Devuelve la cinta con grupos de 6 bits y separadores

    def read_bit(self):
        # Lee el bit actual y lo añade a la cinta de salida si no es un separador de bloque
        if self.cinta[self.pointer] != '|':
            self.output_cinta.append(self.cinta[self.pointer])
            self.bit_counter += 1  # Incrementa el contador de bits
            if self.bit_counter == 6:  # Si alcanzamos 6 bits, cambia al estado para escribir el marcador de grupo
                self.state = "WRITE_GROUP_MARKER"
            else:
                self.pointer += 1  # Mueve el puntero al siguiente bit
        else:
            # Si encontramos un separador de bloque '|', lo añadimos y avanzamos
            self.output_cinta.append('|')
            self.pointer += 1

    def write_group_marker(self):
      
        self.output_cinta.append(':')  
        self.state = "MOVE_TO_NEXT_GROUP" 

    def move_to_next_group(self):
       
        self.bit_counter = 0
        self.pointer += 1  
        self.state = "READ_BIT"
        

if __name__ == "__main__":
    grouped_binary_input = "010011010110000101101110|"
    division_machine = TuringMachineDivide6Bits(grouped_binary_input)
    divided_output = division_machine.run()
    print("Entrada en bloques de 24 bits:", grouped_binary_input)
    print("Salida con grupos de 6 bits:", divided_output)
