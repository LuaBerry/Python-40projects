import googletrans

translator = googletrans.Translator()

sentence = input("Insert sentence: ")
result1 = translator.translate(sentence, dest='en', src='auto')
print(sentence, f" => {result1.text}")

sentence = input("Insert English sentence: ")
result2 = translator.translate(sentence, dest='ko', src='en')
print(sentence, f" => {result2.text}")