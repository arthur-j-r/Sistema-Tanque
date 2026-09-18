import numpy as np
import matplotlib.pyplot as plt


class SistemaTemperatura:
    def __init__(self, ts, T0, Tout, Kh, Kl, u, N):
        self.ts = ts
        self.T0 = T0
        self.Tout = Tout
        self.Kh = Kh
        self.Kl = Kl
        self.u = u
        self.N = N

    def vetor_tempo(self):
        return np.arange(self.N + 1) * self.ts

    def calcular_temperatura(self):
        temperatura = np.zeros(self.N + 1)
        temperatura[0] = self.T0

        for k in range(self.N):
            aquecimento = self.Kh * self.u
            perda_calor = self.Kl * (temperatura[k] - self.Tout)

            temperatura[k + 1] = (
                temperatura[k]
                + self.ts * (aquecimento - perda_calor)
            )

        return temperatura

    def printar(self):
        t = self.vetor_tempo()
        temperatura = self.calcular_temperatura()

        plt.figure(figsize=(8, 4))
        plt.plot(t, temperatura, label="Temperatura")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Temperatura (°C)")
        plt.title("Temperatura da sala ao longo do tempo")
        plt.grid(True)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    iniciar = SistemaTemperatura(
        ts=1,
        T0=10,
        Tout=10,
        Kh=0.05,
        Kl=0.01,
        u=2,
        N=500
    )

    iniciar.printar()