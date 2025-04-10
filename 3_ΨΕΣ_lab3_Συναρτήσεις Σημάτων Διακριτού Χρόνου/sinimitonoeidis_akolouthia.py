import numpy as np                         # Εισαγωγή της βιβλιοθήκης NumPy για αριθμητικούς υπολογισμούς
import matplotlib.pyplot as plt            # Εισαγωγή της βιβλιοθήκης matplotlib για δημιουργία γραφημάτων

# Συνάρτηση για δημιουργία συνημιτονοειδούς ακολουθίας
def cos_akolouthia(N, f):
    w = 2 * np.pi * f                      # Υπολογισμός γωνιακής συχνότητας
    n = np.arange(N)                       # Δημιουργία χρονικών δεικτών από 0 έως N-1
    y = np.cos(w * n)                      # Υπολογισμός των τιμών της συνημιτονοειδούς ακολουθίας

    # Σχεδίαση γραφήματος
    markerline, stemlines, baseline = plt.stem(n, y)  # Σχεδίαση διακριτού γραφήματος (stem)
    plt.setp(markerline, color="blue")                # Ορισμός χρώματος για τα σημεία
    plt.setp(stemlines, color="green")                # Ορισμός χρώματος για τις γραμμές
    plt.title(f"Συνημιτονοειδής ακολουθία με f = {f}") # Τίτλος γραφήματος
    plt.xlabel("n")                                   # Ετικέτα άξονα x
    plt.ylabel("cos(ωn)")                             # Ετικέτα άξονα y
    plt.grid(True)                                    # Ενεργοποίηση πλέγματος
    plt.show()                                        # Εμφάνιση του γραφήματος

# Παράδειγμα χρήσης της συνάρτησης
cos_akolouthia(100, 0.1)

