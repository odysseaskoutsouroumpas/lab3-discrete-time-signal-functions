## Εργαστήριο 3 – Συναρτήσεις Σημάτων Διακριτού Χρόνου

Αυτό το repository περιλαμβάνει την υλοποίηση θεμελιωδών συναρτήσεων διακριτού χρόνου σε Python, μαζί με τα αντίστοιχα γραφήματα για απεικόνιση και μελέτη. Οι συναρτήσεις αυτές αποτελούν τη βάση για την κατανόηση της ψηφιακής επεξεργασίας σήματος (DSP).

### Περιεχόμενα

- `monadiaia_wsi.py`: Υλοποίηση της μονάδας ώσης δ[n]
- `monadiaki_vimatiki_akolouthia.py`: Υλοποίηση της μονάδας βήματος u[n]
- `imitonoidis_akolouthia.py`: Ημιτονοειδής ακολουθία sin(ωn)
- `sinitonoeidis_akolouthia.py`: Συνημιτονοειδής ακολουθία cos(ωn)
- `ekthetiki_akolouthia.py`: Εκθετική ακολουθία (πραγματικό και φανταστικό μέρος)
- `simata_python_vivliothiki.py`: Συγκεντρωτικός κώδικας που καλεί όλες τις παραπάνω συναρτήσεις

### Προϋποθέσεις

- Python 3.x
- matplotlib
- numpy

### Εκτέλεση

Κάθε `.py` αρχείο μπορεί να εκτελεστεί ανεξάρτητα για να εμφανίσει το αντίστοιχο γράφημα της ακολουθίας. Π.χ.:

```bash
python monadiaia_wsi.py
