import numpy as np
import matplotlib.pyplot as plt

class SistemaTanque:
    def __init__(self, ts, vo, qin, qout, N):
        self.ts = ts
        self.vo = vo
        self.qin = qin
        self.qout = qout
        self.N = N

    def vetor_tempo(self):
        return np.arange(self.N + 1) * self.ts

    def calcular_volume(self):
        volume = np.zeros(self.N + 1)
        volume[0] = self.vo

        for k in range(self.N):
            volume[k + 1] = volume[k] + self.ts * (self.qin - self.qout)
            
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
    iniciar = SistemaTanque(ts=1, vo=100, qin=5, qout=2, N=20)
    iniciar.printar()