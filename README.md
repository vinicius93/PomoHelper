# PomoHelper
Ajudante de foco automatizado para prática da técnica pomodoro

Basicamente é monitorado o arquivo Json de sessão do firefox (localizado na pasta %AppData%) onde é possível identificar a aba atual com sua respectiva URL

Uma vez com essa informação é feita a comparação da Url com as dos Sites Youtube e Facebook, onde, em caso positivo é enviado o conjunto de comandos do teclado
(Ctrl + F4) na qual fecha a Aba atual do firefox

Todo o processo de extração dos dados atuais e suas comparações estão dentro de um laço de repetição onde só é terminado ao final de 20 minutos, 
fazendo a comparação da hora de inicio da executação do código com a hora atual em cada loop do laço principal;
