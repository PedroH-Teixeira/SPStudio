import os

class Pasta:

    def cria_pastas(self):
        # Pastas
        if not os.path.exists(r'temp/info'):
            os.makedirs(r'temp/info')
        if not os.path.exists(r'temp/img'):
            os.makedirs(r'temp/img')

        # Arquivos
        with open(r'temp/info/mapping.txt', 'a') as file:
            file.write('')
