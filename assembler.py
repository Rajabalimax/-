import struct
import sys

COMMANDS = {
    'LOAD_CONST': 0x90,  # Пример команды для загрузки константы
    'READ_MEM': 0x02,    # Чтение значения из памяти
    'WRITE_MEM': 0x63,   # Запись значения в память
    'BIT_SHIFT_LEFT': 0x37  # Побитовый циклический сдвиг влево
}

def hex_to_int(hex_str):
    """Преобразование строки в шестнадцатеричном формате в целое число."""
    return int(hex_str, 16)

def assemble(input_file, output_file, log_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    binary_instructions = []
    log_entries = []

    for line in lines:
        parts = line.strip().split()
        command = parts[0]
        operand = hex_to_int(parts[1])  # Используем новую функцию для преобразования

        if command in COMMANDS:
            opcode = COMMANDS[command]
            instruction = struct.pack('BBB', opcode, operand & 0xFF, (operand >> 8) & 0xFF)
            binary_instructions.append(instruction)
            log_entries.append(f"{command}={operand}")

    with open(output_file, 'wb') as f:
        f.writelines(binary_instructions)

    with open(log_file, 'w') as f:
        f.write("\n".join(log_entries))

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    log_file = sys.argv[3]
    assemble(input_file, output_file, log_file)
