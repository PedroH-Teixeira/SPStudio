import os

from teste_rede import TesteRede
from datetime import date
from shutil import copyfile
from crop import LabelCrop
from subprocess import call

class Imagem:
    def __init__(self):
        super().__init__()
        self.teste = TesteRede.testeRede(self)

    def cortar_imagem(self):
        crop = LabelCrop(self.labelImagem)
        crop.setScaledContents(True)
        crop.imagem(r'temp/img/capt0000.jpg')
        crop.show()

    def salvar_imagem(self):
        try:
            # Define as variáveis para criar os caminhos e nome da foto
            data_atual = date.today()
            ano = data_atual.strftime('%Y')
            meses = ['','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
            num_mes = data_atual.strftime('%m')
            mes_atual = meses[int(num_mes)]
            nome_material = self.comboBox_material.currentText()
            n_bloco = self.lineEdit_3.text()
            cm = self.comboBox_espessura.currentText()
            seq = ''
            lote = self.lineEdit_codigoDeBarras.text()
        except Exception as erro:
            print(fr'Erro ao definir variável: {erro}')
        try:
            # Abre o arquivo mapping para fazer o teste de rede
            with open(r'temp/info/mapping.txt', 'r') as file:
                file.seek(0)
                ler_ip = file.readline().strip()
        except Exception as erro:
            print(fr'Erro ao tentar ler arquivo: {erro}')
        try:
                if ler_ip != '':
                    # Realiza o teste de rede e mapeamento
                    if TesteRede.testeRede(self) == 0:
                        # Unifica o caminho da imagem em apenas 1 variável
                        caminho = fr'\\{ler_ip}/Fotos/Originais/FOTOS - {ano}/{num_mes} - {mes_atual}/' \
                                  fr'{nome_material}/{nome_material} {n_bloco} {cm}'
                        # Testa o caminho da imagem e cria se não existir
                        if not os.path.exists(caminho):
                            os.makedirs(caminho)
                        caminho_imagem = os.path.join(caminho, f'{nome_material} {cm} Bloco {n_bloco} '
                                                               f'Chapa {seq} Lote {lote}.jpg')
                        imagem = r'temp/img/capt0000.jpg'
                        copyfile(imagem, caminho_imagem)
                        self.label_status.setText("IMAGEM SALVA NO DIRETÓRIO DA REDE")
                        self.label_status.setStyleSheet('QLabel {background-color: #000000; color: #ebd234}')
                    else:
                        # Salva imagem em um caminho local
                        caminho = fr'Fotos/Originais/FOTOS - {ano}/{num_mes} - {mes_atual}/' \
                                  fr'{nome_material}/{nome_material} {n_bloco} {cm}'
                        if not os.path.exists(caminho):
                            os.makedirs(caminho)
                        caminho_imagem = os.path.join(caminho, f'{nome_material} {cm} Bloco {n_bloco} '
                                                               f'Chapa {seq} Lote {lote}.jpg')
                        imagem = r'temp/img/capt0000.jpg'
                        copyfile(imagem, caminho_imagem)
                        self.label_status.setText("IMAGEM SALVA NO DIRETÓRIO LOCAL")
                        self.label_status.setStyleSheet('QLabel {background-color: #000000; color: #ebd234}')
                else:
                    # Salva imagem em um caminho local
                    caminho = fr'Fotos/Originais/FOTOS - {ano}/{num_mes} - {mes_atual}/' \
                              fr'{nome_material}/{nome_material} {n_bloco} {cm}'
                    if not os.path.exists(caminho):
                        os.makedirs(caminho)
                    caminho_imagem = os.path.join(caminho, f'{nome_material} {cm} Bloco {n_bloco} '
                                                           f'Chapa {seq} Lote {lote}.jpg')
                    imagem = r'temp/img/capt0000.jpg'
                    copyfile(imagem, caminho_imagem)
                    self.label_status.setText("IMAGEM SALVA NO DIRETÓRIO LOCAL")
                    self.label_status.setStyleSheet('QLabel {background-color: #000000; color: #ebd234}')
        except OSError as erro:
            print(fr'Erro ao tentar salvar imagem: {erro}')


    def backup_imagens_rede(self):
        with open(r'temp/info/mapping.txt', 'r') as file:
            file.seek(0)
            ler_ip = file.readline().strip()
            call(fr'Robocopy Fotos \\{ler_ip}/Fotos /E /Z /R:3 /W:10 /XO /NP /LOG:temp/info/backup_imagens.log')
            print('Realizado o backup da imagens na rede.')
