import qrcode
import os

dir_path = os.path.dirname(os.path.abspath(__file__)) + "\\"
text_path = dir_path + "QRtexts.txt"
with open(text_path, 'rt', encoding='UTF-8') as f:
    read_lines = f.readlines()
    for line in read_lines:
        line = line.strip()
        print(line)

        qr_img = qrcode.make(line)
        save_path = dir_path + line.split('.')[0] + ".png"
        qr_img.save(save_path)