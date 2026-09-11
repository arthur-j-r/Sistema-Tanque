import numpy as np
import matplotlib.pyplot as plt

class SistemaTanque:
    def __init__(self, ts, vo, qin, N,c):
        self.ts = ts
        self.c = c
        self.vo = vo
        self.qin = qin
        self.N = N

    def vetor_tempo(self):
        return np.arange(self.N + 1) * self.ts

    def calcular_volume(self):
        volume = np.zeros(self.N + 1)
        volume[0] = self.vo

        for k in range(self.N):
            q_out = self.c * volume[k]
            volume[k + 1] = volume[k] + self.ts * (self.qin - q_out)
            
        return volume

    def printar(self):
        t = self.vetor_tempo()
        v = self.calcular_volume()

        plt.figure(figsize=(8, 4))
        plt.plot(t, v, 'o-', label="Volume")
        plt.xlabel("Tempo (t)")
        plt.ylabel("Volume (L)")
        plt.title("Volume do tanque ao passar do tempo")
        plt.grid(True)
        plt.legend()
        plt.show()

if __name__ == "__main__":
    iniciar = SistemaTanque(ts=1, vo=0, qin=5, N=50,c=0.1)
    iniciar.printar()