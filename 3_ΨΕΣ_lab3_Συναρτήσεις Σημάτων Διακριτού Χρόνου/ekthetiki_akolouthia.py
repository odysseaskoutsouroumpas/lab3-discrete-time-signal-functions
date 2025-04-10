import numpy as np  # Για μαθηματικές πράξεις και πίνακες
import matplotlib
matplotlib.use('agg')  # Χρήση backend agg για αποθήκευση εικόνων
import matplotlib.pyplot as plt  # Για γραφήματα

# Συνάρτηση για εκθετική ακολουθία
def exp_akolouthia(N, f):
    w = 2 * np.pi * f  # Υπολογισμός γωνιακής συχνότητας
    n = np.arange(N)   # Δημιουργία δεικτών χρόνου από 0 έως N-1
    y = np.exp(1j * w * n)  # Υπολογισμός εκθετικής ακολουθίας

    # Υπολογισμός επιμέρους τιμών
    real_part = np.real(y)  # Πραγματικό μέρος
    imag_part = np.imag(y)  # Φανταστικό μέρος
    abs_val = np.abs(y)     # Μέτρο
    phase = np.angle(y)     # Φάση

    # Δημιουργία γραφημάτων
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.stem(n, real_part)  # Πραγματικό μέρος
    plt.title("Πραγματικό μέρος")
    plt.xlabel("n")
    plt.ylabel("Real")
    plt.grid(True)

    plt.subplot(2, 2, 2)
    plt.stem(n, imag_part)  # Φανταστικό μέρος
    plt.title("Φανταστικό μέρος")
    plt.xlabel("n")
    plt.ylabel("Imag")
    plt.grid(True)

    plt.subplot(2, 2, 3)
    plt.stem(n, abs_val)  # Μέτρο
    plt.title("Μέτρο")
    plt.xlabel("n")
    plt.ylabel("|y|")
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.stem(n, phase)  # Φάση
    plt.title("Φάση")
    plt.xlabel("n")
    plt.ylabel("Φάση (rad)")
    plt.grid(True)

    # Αποθήκευση εικόνας
    plt.tight_layout() #Διάταξη γραφημάτων
    plt.savefig("ekthetiki_akolouthia.png")
    plt.close()

# Παράδειγμα κλήσης της συνάρτησης
exp_akolouthia(100, 0.1)
