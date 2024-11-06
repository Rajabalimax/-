import struct
import csv
import sys

def interpret(binary_file, output_csv, memory_range):
    memory = [0] * 256  # Пример памяти размером 256 байт
    stack = []

    with open(binary_file, 'rb') as f:
        while True:
            byte = f.read(3)
            if not byte:
                break
            opcode, operand1, operand2 = struct.unpack('BBB', byte)

            if opcode == 0x90:  # LOAD_CONST
                stack.append(operand1)
            elif opcode == 0x02:  # READ_MEM
                addr = stack.pop()
                stack.append(memory[addr])
            elif opcode == 0x63:  # WRITE_MEM
                value = stack.pop()
                addr = operand1
                memory[addr] = value
            elif opcode == 0x37:  # BIT_SHIFT_LEFT
                value = stack.pop()
                shift = memory[operand1 + operand2]
                result = (value << shift) & 0xFF  # Пример побитового сдвига
                stack.append(result)

    # Сохранение результата в CSV
    with open(output_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Address", "Value"])
        for address in range(memory_range[0], memory_range[1] + 1):
            csv_writer.writerow([address, memory[address]])

if __name__ == "__main__":
    binary_file = sys.argv[1]
    output_csv = sys.argv[2]
    memory_range = (int(sys.argv[3]), int(sys.argv[4]))
    interpret(binary_file, output_csv, memory_range)
