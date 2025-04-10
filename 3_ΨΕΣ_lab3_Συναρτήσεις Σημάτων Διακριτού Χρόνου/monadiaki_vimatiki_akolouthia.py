import numpy as np
import matplotlib.pyplot as plt


# Sinartisi gia tin monadiaki vimatiki akolouthia
def unitary_uowm(n, N):
    # Dimiourgia dianusmatos me N stoixeia, arxika me midenika
    u = np.zeros(N)

    # Apo to deigma n kai meta, i timi tou dianusmatos ginetai 1
    u[n:] = 1

    return u


# Paradeigma klisis tis sinartisis
n = 10
N = 100

# Dimiourgia tis akolouthias
u = unitary_uowm(n, N)

# Oρισμος του backend 'agg'
plt.switch_backend('agg')

# Emfanisi tis akolouthias
plt.stem(u)
plt.title('Monadiaki Vimatiki Akolouthia u(n)')
plt.xlabel('Deigma')
plt.ylabel('Timh u(n)')


plt.savefig('monadiaki_vimatiki_akolouthia.png')  #
