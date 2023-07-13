import os
from criptografia import Criptografar
from subprocess import call

class TesteRede:
    def __init__(self):
        super().__init__()
        self.criptografia = Criptografar()


    def testeRede(self):
        if os.path.exists(r'temp/info/mapping.txt'):
            with open(r'temp/info/mapping.txt', 'r') as file:
                file.seek(0)
                local = file.readline().strip()
                ler_ip = local.split('\\')[0]
                ler_usuario = file.readline().strip()

        if os.path.exists(r'temp/info/password.bin'):
            with open(r'temp/info/password.bin', 'rb') as file:
                file.seek(0)
                ler_senha = file.read()
                dec_ler_senha = self.criptografia.decodificar_valores(ler_senha)

        #ping = call(fr'ping -n 1 {ler_ip}')
        if ler_ip != '':
            caminho_completo_servidor = fr'net use \\{ler_ip} /user:{ler_usuario} {dec_ler_senha}'
            conectado = call(caminho_completo_servidor)
            if conectado == 0 and os.path.exists(fr'\\{local}'):
                self.label_circ_1.setStyleSheet(
                    "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, "
                    "fy:0.5, stop:0.420455 rgba(0, 255, 0, 255), stop:1 rgba(0, 170, 0, "
                    "255)); border-radius: 12%;")
                return 0
            else:
                self.label_circ_1.setStyleSheet(
                    "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, "
                    "fy:0.5, stop:0.420455 rgba(255, 0, 0, 255), stop:1 rgba(164, 0, 0, "
                    "255)); border-radius: 12%;")
                return 1
        else:
            self.label_circ_1.setStyleSheet(
                "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, "
                "fy:0.5, stop:0.420455 rgba(255, 0, 0, 255), stop:1 rgba(164, 0, 0, "
                "255)); border-radius: 12%;")
            return 1