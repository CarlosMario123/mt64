class TuringMachineMapBase64:
    def __init__(self, divided_input):
        self.cinta = list(divided_input) 
        self.output_cinta = []  
        self.pointer = 0  
        self.state = "READ_GROUP"
        self.current_group = [] 
        self.base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    def run(self):
        while self.pointer < len(self.cinta):
            if self.state == "READ_GROUP":
                self.read_group()
            elif self.state == "MAP_TO_BASE64":
                self.map_to_base64()
            elif self.state == "MOVE_TO_NEXT_GROUP":
                self.move_to_next_group()
        
        return ''.join(self.output_cinta) 

    def read_group(self):
        # Lee un bit del grupo actual y lo añade a `current_group` si no es un separador
        if self.cinta[self.pointer] not in [':', '|']:
            self.current_group.append(self.cinta[self.pointer])
            if len(self.current_group) == 6:  # Si tenemos 6 bits, cambia al estado de mapeo
                self.state = "MAP_TO_BASE64"
            self.pointer += 1
        else:
            # Si encontramos un separador, lo saltamos y avanzamos
            self.pointer += 1

    def map_to_base64(self):
       
        decimal_value = int(''.join(self.current_group), 2)  # Convierte el grupo a decimal
        self.output_cinta.append(self.base64_table[decimal_value])  # Mapea al carácter Base64
        self.state = "MOVE_TO_NEXT_GROUP"  # Cambia al estado de avance

    def move_to_next_group(self):
        # Reinicia `current_group` para el próximo grupo de 6 bits y vuelve a leer
        self.current_group = []
        self.state = "READ_GROUP"

if __name__ == "__main__":
    divided_input = "010011:010110:000101:101110|"
    mapping_machine = TuringMachineMapBase64(divided_input)
    base64_output = mapping_machine.run()
    print("Entrada en grupos de 6 bits:", divided_input)
    print("Salida en caracteres Base64:", base64_output)
    