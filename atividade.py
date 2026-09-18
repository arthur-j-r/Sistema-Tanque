import numpy as np
import matplotlib.pyplot as plt


class SistemaTanque:
    def __init__(self, ts, vo, N, c, V_ref, Kp, Ki, Kd):
        self.ts = ts
        self.c = c
        self.vo = vo
        self.N = N
        self.V_ref = V_ref
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

    def vetor_tempo(self):
        return np.arange(self.N + 1) * self.ts

    def calcular_volume(self):
        volume = np.zeros(self.N + 1)
        q_in = np.zeros(self.N)

        volume[0] = self.vo

        integral = 0
        erro_anterior = 0

        for k in range(self.N):
            erro = self.V_ref - volume[k]

            integral = integral + erro * self.ts

            derivada = (erro - erro_anterior) / self.ts

            u = (
                self.Kp * erro
                + self.Ki * integral
                + self.Kd * derivada
            )

            q_in[k] = max(0, u)

            q_out = self.c * volume[k]

            volume[k + 1] = (
                volume[k]
                + self.ts * (q_in[k] - q_out)
            )

            erro_anterior = erro

        return volume, q_in

    def printar(self):
        t = self.vetor_tempo()
        v, q_in = self.calcular_volume()

        plt.figure(figsize=(8, 4))
        plt.plot(t, v, 'o-', label="Volume")
        plt.axhline(
            y=self.V_ref,
            linestyle="--",
            label="Referência = 20 L"
        )
        plt.xlabel("Tempo (t)")
        plt.ylabel("Volume (L)")
        plt.title("Volume do tanque ao passar do tempo")
        plt.grid(True)
        plt.legend()
        plt.show()

        plt.figure(figsize=(8, 4))
        plt.plot(t[:-1], q_in, 'o-', label="Vazão de entrada")
        plt.xlabel("Tempo (t)")
        plt.ylabel("Vazão de entrada")
        plt.title("Ação de controle PID")
        plt.grid(True)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    iniciar = SistemaTanque(
        ts=1,
        vo=0,
        N=50,
        c=0.1,
        V_ref=20,
        Kp=0.5,
        Ki=0.05,
        Kd=0.1
    )

    iniciar.printar()