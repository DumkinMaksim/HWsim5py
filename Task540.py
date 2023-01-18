# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
       
        if char != prev_char:
            
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
           
            count += 1
    else:
      
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = ''
    count = 0
    digit=True
    for char in data:
        
        if digit:
            
            count = int(char)
            digit=False
        else:
            
            decode += char * int(count)
            digit=True
           
    return decode
dtext='aaa11dddd662222bbb'   
print(dtext)
print()
encoded_val = rle_encode(dtext)

print(encoded_val)
print()
decoded_val = rle_decode(encoded_val)
print(decoded_val)