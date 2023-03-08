from googletrans import Translator

translater = Translator()


out = translater.translate("आप कैसे हैं", dest='en')

print(out.text)
