import numpy as np   
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

# Συνάρτηση για ημιτονοειδή ακολουθία
def imitono(N, f):
    w = 2 * np.pi * f
    n = np.arange(N)
    y = np.sin(w * n)

    # Σχεδίαση γραφήματος
    markerline, stemlines, baseline = plt.stem(n, y)  # Διακριτή απεικόνιση
    plt.setp(markerline, color="blue")  # Ρύθμιση χρώματος για τα σημεία
    plt.setp(stemlines, color="green")  # Ρύθμιση χρώματος για τις γραμμές
    plt.title(f"Ημιτονοειδής ακολουθία με f = {f}")  # Τίτλος γραφήματος
    plt.xlabel("n")  # Ετικέτα οριζόντιου άξονα
    plt.ylabel("sin(ωn)")  # Ετικέτα κάθετου άξονα
    plt.grid(True)  # Ενεργοποίηση πλέγματος
    plt.savefig("imitonoidis_akolouthia.png")  # Αποθήκευση γραφήματος ως εικόνα
    plt.close()  # Κλείσιμο γραφήματος

# Παράδειγμα κλήσης της συνάρτησης
imitono(100, 0.1)
