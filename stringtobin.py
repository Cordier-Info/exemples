a_string = "À l'aide, je suis une petite erreur perdue dans ce salmigondis et je ne veux pas qu'on m'élimine..."

a_byte_array = bytearray(a_string, "utf8")
byte_list = []

for byte in a_byte_array:
    binary_representation = bin(byte)
    byte_list.append(binary_representation)

for b in byte_list :
	print(b[2:].zfill(8),end='')
