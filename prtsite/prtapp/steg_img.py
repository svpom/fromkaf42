from PIL import Image

def encode_mes(mes_user, img, files_name):
    offset = 0
    for ch in mes_user:
        b_ch = bin(ord(ch))
        if len(b_ch) != 10:# 10 because 0bxxxxxxxx
            b_ch = b_ch[0:2] + '0'*(10 - len(b_ch)) + b_ch[2:]#for privideni9 to fixed length, equal 8 bits
        part_coord = -8
        for i in range(2, 6):# this diaposon for comftrbl offset incr
            y = int(offset / img.width)
            x = offset % img.width
            pix_blue = img.getpixel((x, y))[2]#get blue part of pixel
            if part_coord + 2 == 0:
                if len(bin(pix_blue))>=4:
                    mod_blue = int(bin(pix_blue)[2:-2] + b_ch[part_coord:], 2)
                    offset += 1#making start offset for next char
                else:
                    mod_blue = int(bin(pix_blue)[2:] + b_ch[part_coord:], 2)
                    offset += 1#making start offset for next char
            else:#4 because may be 0bx or 0bxx
                if len(bin(pix_blue))>=4:
                    mod_blue = int((((bin(pix_blue))[2:-2]) + (b_ch[part_coord:part_coord + 2])), 2)
                    part_coord+=2
                    offset += i#for each next iteration
                else:
                    mod_blue = int(((bin(pix_blue)[2:]) + (b_ch[part_coord:part_coord + 2])), 2)
                    part_coord+=2
                    offset += i#for each next iteration
            img.putpixel((x, y), (img.getpixel((x,y))[0], img.getpixel((x,y))[1], mod_blue))
    img.save("prtapp/media/images/output/" + files_name, "BMP")

def decode_mes(img, mes_len):
    mes_len = int(mes_len)
    offset = 0
    dec_mes = ""
    i = 0
    while i < mes_len:
        ch = ""
        for j in range(2, 6):
            y = int(offset / img.width)
            x = offset % img.width
            pix_blue = bin(img.getpixel((x, y))[2])
            if len(pix_blue) >=4:
                part = pix_blue[-2:]#last 2 bits in blue
            else:#0b0 or 0b1
                part = '0' + pix_blue[-1:]
            ch += part
            if j!=5:
                offset += j
            else:
                offset += 1
        dec_mes += chr(int(ch, 2))
        i += 1
    return dec_mes

def main():
    choice = input("Введите 1 для кодирования сообщения или 2 для его раскодирования: \n")
    if int(choice) == 1:
        while True:
            mes_user = input("Введите сообщение в ASCII, которое нужно закодировать: \n")
            path_to_img = input("Введите путь к контейнеру(изображению bmp): \n")
            img = Image.open(path_to_img)
            if int(img.height * img.width / 10) <  len(mes_user):#1 char to each 10 symbols
                print("The message is too long. Please, try again.")
            else:
                break
        encode_mes(mes_user, img)
        print("You've got an 'encoded_image'. Check your folder.\n")
    if int(choice) == 2:
        path_to_img = input("Введите путь к контейнеру(изображению bmp): \n")
        mes_len = int(input("Введите длину передаваемого сообщения: \n"))
        img = Image.open(path_to_img)
        print(("Decoded message is: %s \n") % decode_mes(img, mes_len))

if __name__ == '__main__':
   main()
