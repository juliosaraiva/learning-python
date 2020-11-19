from googletrans import Translator

translator = Translator()

try:
    with open('content.txt', 'r') as f:
        text = f.read()
        translation = translator.translate(text, dest='pt')
        with open('translation.txt', mode='w') as nf:
            nf.write(translation.text)
except FileNotFoundError:
    print('File not found!')
