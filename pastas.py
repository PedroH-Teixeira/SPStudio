import os

class Pasta:

    def cria_pastas(self):
        if not os.path.exists(r'temp/info'):
            os.makedirs(r'temp/info')
        if not os.path.exists(r'temp/img'):
            os.makedirs(r'temp/img')