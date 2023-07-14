# SPStudio - Stone Photo Studio
Programa que captura imagens de chapas "Stone Photo Studio" criado em Python

Após compilar com <i>pyinstaller</i>, transferir as pastas "<i>icons</i>" e "<i>library</i>" para a raiz do programa.

Adicionar os seguintes valores em Variáveis de Ambiente do windows:

<b>Path:</b> "Local do Programa"\library\bin

<b>Nome da Variável:</b> CAMLIBS </br>
<b>Valor da Variável: </b> "Local do Programa"\library\lib\libgphoto2\2.5.30

<b>Nome da Variável:</b> IOLIBS </br>
<b>Valor da Variável: </b> "Local do Programa"\library\lib\libgphoto2_port\0.12.1

Alterar o driver da camera para o driver WinUSB usando o programa "zadig"

