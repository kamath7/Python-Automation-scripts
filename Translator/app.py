from googletrans import Translator

translator = Translator()

translation = translator.translate("Por Que?", dest="en").text 
print(translation)

#install googletrans using - pip install googletrans==3.1.0a0