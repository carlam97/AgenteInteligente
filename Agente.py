import random

class Ambiente:
    def __init__(self, matriz, reservatorio):
        self.matriz = matriz
        self.reservatorio = reservatorio

    def apresentacao(self):
        print("----------------------------------------------------------")
        print("Os apartamentos são distribuídos da seguinte forma: \n")
        print("|401 402 403 404| \n |301 302 303 304|\n |201 202 203 204|\n |101 102 103 104|\n")
        print("O nível ideal de água em cada apartamento é acima de 30L")
        print("----------------------------------------------------------")

    def incial(self):
        print("Quantidade inicial de água no reservatório: %dL\n." % (self.reservatorio))
        for l in range(0, len(self.matriz)):
            for c in range(0, len(self.matriz[0])):
                self.reservatorio -= self.matriz[l][c]
        print("Distribuição inicial:")
        for l in range(0, len(self.matriz)):
            print(self.matriz[l])
        print("\nQuantidade de água restante no reservatório: %dL." % (self.reservatorio))

class Agente:
    def __init__(self, matriz):
        self.matriz = matriz

    def sensor(self):
        ideal = False
        total = 0
        print("---------------------------------- sensor ----------------------------------------")
        for l in range(0, len(self.matriz)):
            for c in range(0, len(self.matriz[0])):
                if self.matriz[l][c] < 30:
                    print("\n O apartamento que recebeu apenas %dL não está no nível desejado." % (self.matriz[l][c]))
                    print("Será necessário acrescentar no mínimo %dL no reservatório para atingir o nível ideal." % (
                                30 - self.matriz[l][c]))
                if self.matriz[l][c] >= 30:
                    total += 1
                else:
                    total = 0
                if total == len(self.matriz) * len(self.matriz[0]):
                    ideal = True
        if ideal:
            print("\n O agente inteligente identificou que todos os apartamentos estão com níveis iguais ou superiores ao nível ideal.\n")

    def atuador(self, reservatorio):
        print("---------------------------------- atuador ----------------------------------------")
        for l in range(0, len(self.matriz)):
            for c in range(0, len(self.matriz[0])):
                if self.matriz[l][c] < 30:
                    print("\n Para o apartamento que necessita de %dL" % (30 - self.matriz[l][c]))
                    antigo = self.matriz[l][c]
                    self.matriz[l][c] += random.randint(30 - self.matriz[l][c], 30)
                    novo = self.matriz[l][c]
                    reservatorio -= (novo - antigo)
                    print("O agente inteligente destinou %dL de água" % (novo - antigo))
        print("\nDistribuição final:")
        for l in range(0, len(self.matriz)):
            print(self.matriz[l])
        print("\nQuantidade final de água no reservatório: %dL" % (reservatorio))

def main(reservatorio_inicial=1000, num_linhas=4, num_colunas=4):
    matriz = [[random.randint(0, 50) for _ in range(num_colunas)] for _ in range(num_linhas)]

    condominio = Ambiente(matriz, reservatorio_inicial)
    condominio.apresentacao()
    condominio.incial()
    reservatorio = condominio.reservatorio
    solucao = Agente(condominio.matriz)
    solucao.sensor()
    solucao.atuador(reservatorio)
    solucao.sensor()

if __name__ == "__main__":
    reservatorio_inicial = 1000  # Valor padrão, pode ser alterado conforme necessário
    main(reservatorio_inicial)
