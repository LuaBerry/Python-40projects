from os import linesep
import os
from pickletools import read_long1
import googletrans
from pyparsing import line

translator = googletrans.Translator()

dir_path = os.path.dirname(os.path.abspath(__file__))
orgFile_path = input("Input file name :")
wrtFile_path = dir_path + "\\" + orgFile_path.split('.')[0] + "_toKor.txt"
orgFile_path = dir_path + "\\" + orgFile_path

with open(orgFile_path, 'r') as f:
    texts = f.readlines()

for line in texts:
    result = translator.translate(line, dest='ko')
    print(result.text)
    with open(wrtFile_path, 'a', encoding='UTF-8') as f:
        f.write(result.text + '\n')