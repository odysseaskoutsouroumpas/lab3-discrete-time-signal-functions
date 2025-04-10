import numpy as np  # Εισαγωγή της βιβλιοθήκης numpy για χρήση πινάκων και υπολογισμών
import matplotlib.pyplot as plt  # Εισαγωγή της βιβλιοθήκης matplotlib για τη δημιουργία γραφημάτων

# Συνάρτηση για τη μονάδιαια ώση
def monadiaia_wsh(thesi, megethos):
    pinakas = np.zeros(megethos)  # Δημιουργία πίνακα με μηδενικά
    if 0 <= thesi < megethos:  # Έλεγχος αν η θέση είναι εντός ορίων
        pinakas[thesi] = 1  # Τοποθέτηση της μονάδας στη σωστή θέση
    return pinakas  # Επιστροφή του πίνακα

# Παράδειγμα χρήσης της συνάρτησης
megethos_pinaka = 100  # Ορισμός του μεγέθους του πίνακα
thesi_mia = 3  # Ορισμός της θέσης που θα εισαχθεί το 1
eksodos = monadiaia_wsh(thesi_mia, megethos_pinaka)  # Κλήση της συνάρτησης

# Απεικόνιση με γράφημα
plt.stem(range(megethos_pinaka), eksodos)  # Διάγραμμα stem για διακριτά σημεία
plt.title("Μονάδιαια Ώση δ(n)")  # Τίτλος γραφήματος
plt.xlabel("n")  # Ετικέτα άξονα x
plt.ylabel("δ(n)")  # Ετικέτα άξονα y
plt.grid(True)  # Ενεργοποίηση πλέγματος
plt.show()  # Εμφάνιση του γραφήματος
