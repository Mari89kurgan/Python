# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(text):
    count = 1
    index = 1
    sym = text[index]
    cod_text = []
    for i in text:
        if i in sym:
            count += 1
        else:
            cod_text.append(i)
            cod_text.append(str(count))
            count = 1
        index += 1
        sym = text[index:index + 1]
    return ''.join(cod_text)


def rle_decode(text):
    decoded_file = ''
    for i, number in enumerate(text):
        if number.isdigit():
            decoded_file += text[i - 1] * int(number)
    return decoded_file


with open('file.txt', 'w') as data:
    data.write('aaaaBBBccaaccddddd')

with open('file.txt', 'r') as data:
    encode = data.read()

with open('file_encode.txt', 'w') as file:
    file.write(rle_encode(encode))

with open('file_encode.txt', 'r') as file:
    decoded = file.read()

with open('file_decode.txt', 'w') as file:
    file.write(rle_decode(decoded))
