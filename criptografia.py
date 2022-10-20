import rsa


class Criptografar:
    def __init__(self):
        super().__init__()
        self.chavePublica, self.chavePrivada = rsa.newkeys(512)

    def codificar_valores(self, valor):
        valor_criptografado = rsa.encrypt(valor.encode(), self.chavePublica)
        with open(r'temp/info/privateKey.pem', 'w+') as file:
            file.write(self.chavePrivada.save_pkcs1().decode())
        return valor_criptografado

    def decodificar_valores(self, valor_criptografado):
        with open(r'temp/info/privateKey.pem', 'r') as file:
            dec_chave = file.read()
            chavePrivada = rsa.PrivateKey.load_pkcs1(dec_chave)
        valor_decriptografado = rsa.decrypt(valor_criptografado, chavePrivada).decode()
        return valor_decriptografado
