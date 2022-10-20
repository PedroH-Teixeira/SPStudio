"""
import cv2
from PyQt5.QtGui import QPixmap

# Função do botão capturar
class CapturarImagem:
    def __init__(self, camera=False, imagem=False):
        self.camera = cv2.VideoCapture(0)
        self.imagem = "ImagemTeste.png"

    def capturar(self):

        if self.camera.isOpened():
            validacao, frame = self.camera.read()
            if validacao:
                cv2.imwrite(self.imagem, frame)
                cv2.destroyAllWindows()
                self.camera.release()
        return

    # Mosta a imagem capturada na tela
    def mostrar_imagem(self):
        self.img = QPixmap(self.imagem)
        return

import subprocess
#subprocess.call(r'net use \\10.75.0.161 /del')
saida = subprocess.call(r'net use \\10.75.0.240 /user:admin C0s3nt1n0**$$')
print(f'Saída aqui: {saida}')

ping = subprocess.run(['ping', ip_servidor, '-n', '1'])

        print(ping.returncode)
"""
import os
from shutil import copyfile
from datetime import date

try:
    data_atual = date.today()
    ano = data_atual.strftime('%Y')
    meses = ['','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    num_mes = data_atual.strftime('%m')
    mes_atual = meses[int(num_mes)]
    nome_material = 'Teste nome material'
    n_bloco = 'E0510'
    cm = '3cm'
    seq = '01'
    lote = '111111'
    caminho = fr'Fotos/Originais/FOTOS - {ano}/{num_mes} - {mes_atual}/{nome_material}/{nome_material} {n_bloco} {cm}'
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    caminho_imagem = os.path.join(caminho, f'{nome_material} {cm} Bloco {n_bloco} Chapa {seq} Lote {lote}.jpg')

    imagem = r'temp/img/capt0000.jpg'
    copyfile(imagem, caminho_imagem)
except OSError as erro:
    print(erro)
    caminho = fr'Fotos/Originais/FOTOS - {ano}/{num_mes} - {mes_atual}/{nome_material}/{nome_material} {n_bloco} {cm}'
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    caminho_imagem = os.path.join(caminho, f'{nome_material} {cm} Bloco {n_bloco} Chapa {seq} Lote {lote}.jpg')

    imagem = r'temp/img/capt0000.jpg'
    copyfile(imagem, caminho_imagem)
