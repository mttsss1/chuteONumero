import random 

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
    
    def Iniciar(self):
        while self.tentar_novamente == True:
        if int(self.valor_do_chute) > self.valor_aleatorio:
            print('Chute um valor mais baixo!')
            break
            elif int(self.valor_do_chute) < self.valor_aleatorio:
            print('Chute um valor mais alto!')
            break
            if int(self.valor_do_chute) == self.valor_aleatorio:
            self.tentar_novamente = False
            print('PARABÉNS VOCÊ ACERTOU!!')
            break
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()
            

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio =  random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()