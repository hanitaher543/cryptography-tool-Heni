import tkinter as tk
from tkinter import ttk, messagebox

# Fonction Chiffrement César
def cesar(texte, decalage, chiffrer=True):
    decalage = decalage if chiffrer else -decalage  # Si bch n3mlou chiffrer, n7afzou 3la l'décalage, sinon n3awdu l'décalage
    resultat = ''
    for caractere in texte:
        if caractere.isalpha():  # Idha kan l'caractère houa 7arf
            base = ord('A') if caractere.isupper() else ord('a')  # Idha kan 7arf kbir wla saghir
            resultat += chr((ord(caractere) - base + decalage) % 26 + base)  # N7sbou l'index w njibou l'7arf jadid
        else:
            resultat += caractere  # Idha machi 7arf (mitha l'espace wla l'9iwa), n7ottou mouch m3adlou
    return resultat

# Fonction pour créer un alphabet horizontal
def horizontal(cle):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cle = ''.join(sorted(set(cle.upper()), key=cle.upper().index))  # N7ayou les doublons men l'clé
    return cle + ''.join(c for c in alphabet if c not in cle)  # Njibou les lettres l'li ma7atch fi l'clé

# Fonction pour créer un alphabet vertical
def vertical(cle):
    cle = horizontal(cle)  # Nchoufou l'clé horizontal, bch n7ottou les lettres m3a ba3dhom
    colonnes = [cle[i::5] for i in range(5)]  # Nqassmo l'clé 5 colonnes
    return ''.join(''.join(col) for col in zip(*colonnes))  # Njibo les colonnes w nsaymouhom fi l'ordre

# Fonction pour chiffrer/déchiffrer selon un alphabet désordonné
def alphabet_desordonnees(texte, cle, chiffrer=True):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cle_dict = dict(zip(alphabet, cle)) if chiffrer else dict(zip(cle, alphabet))  # Na3mlou dictionary l'7arf m3a l'clé
    return ''.join(cle_dict.get(c.upper(), c) for c in texte.upper())  # N9adou l'7arf men dictionary

# Fonction pour trier la clé de transposition
def cle_transposition(cle):
    return sorted(range(len(cle)), key=lambda k: cle[k])  # N9assmo l'clé 7assb l'ordre

# Fonction de chiffrement/déchiffrement par transposition
def transposition(texte, cle, chiffrer=True):
    if not chiffrer:
        ordre = cle
        nb_col = len(ordre)
        nb_lignes = len(texte) // nb_col + (len(texte) % nb_col > 0)
        tableau = [''] * nb_col
        index = 0
        for col in ordre:
            for _ in range(nb_lignes):
                if index < len(texte):
                    tableau[col] += texte[index]
                    index += 1
        return ''.join(''.join(row) for row in zip(*tableau))  # N3mlou l'transposition l'inverse
    else:
        nb_col = len(cle)
        nb_lignes = len(texte) // nb_col + (len(texte) % nb_col > 0)
        tableau = [[''] * nb_col for _ in range(nb_lignes)]
        index = 0
        for i in range(nb_lignes):
            for j in range(nb_col):
                if index < len(texte):
                    tableau[i][j] = texte[index]
                    index += 1
        return ''.join(''.join(row[i] for row in tableau) for i in cle)  # N3mlou l'transposition

# Fonction pour le chiffrement Affine
def affine(texte, a, b, chiffrer=True):
    m = 26
    if chiffrer:
        return ''.join(chr(((a * (ord(c.upper()) - 65) + b) % m) + 65) if c.isalpha() else c for c in texte)
    else:
        a_inv = pow(a, -1, m)  # Na3mlou inverse de a fi l'26
        return ''.join(chr(((a_inv * ((ord(c.upper()) - 65 - b)) % m) + 65) if c.isalpha() else c) for c in texte)

# Fonction pour le chiffrement Vigenère
def vigenere(texte, cle, chiffrer=True):
    resultat = ''
    cle = cle.upper()
    for i, c in enumerate(texte):
        if c.isalpha():
            decalage = ord(cle[i % len(cle)]) - 65
            decalage = decalage if chiffrer else -decalage
            base = ord('A') if c.isupper() else ord('a')
            resultat += chr((ord(c) - base + decalage) % 26 + base)
        else:
            resultat += c
    return resultat

# Fonction pour le chiffrement Porta
def porta(texte, cle, chiffrer=True):
    texte = texte.upper()
    cle = cle.upper()
    result = ''
    tableau = [
        ('A','Z'), ('B','Y'), ('C','X'), ('D','W'), ('E','V'), ('F','U'),
        ('G','T'), ('H','S'), ('I','R'), ('J','Q'), ('K','P'), ('L','O'),
        ('M','N')
    ]
    dico = {}
    for a,b in tableau:
        idx = ord(a) - 65
        dico[a] = dico[b] = idx
    for i, c in enumerate(texte):
        if c.isalpha():
            k = cle[i % len(cle)]
            decal = dico.get(k, 0)
            pos = (ord(c) - 65)
            result += chr(((pos + decal) % 26) + 65)
        else:
            result += c
    return result

# Fonction simulée pour ADFGVX
def adfgvx(texte, cleA, cleB, chiffrer=True):
    return "ADFGVX " + ("chiffrement" if chiffrer else "déchiffrement") + " simulé"

# Fonction principale qui exécute l'algorithme choisi
def chiffrer_texte():
    algo = algo_var.get()
    texte = entree_texte.get("1.0", tk.END).strip()
    cle = cle_entry.get().strip()
    cle2 = cle2_entry.get().strip()
    mode = mode_var.get()

    try:
        if algo == "César":
            res = cesar(texte, int(cle), chiffrer=(mode=="Chiffrer"))
        elif algo == "Alphabet Horizontal":
            cle_alpha = horizontal(cle)
            res = alphabet_desordonnees(texte, cle_alpha, chiffrer=(mode=="Chiffrer"))
        elif algo == "Alphabet Vertical":
            cle_alpha = vertical(cle)
            res = alphabet_desordonnees(texte, cle_alpha, chiffrer=(mode=="Chiffrer"))
        elif algo == "Transposition":
            cle_trans = cle_transposition(cle)
            res = transposition(texte, cle_trans, chiffrer=(mode=="Chiffrer"))
        elif algo == "Affine":
            res = affine(texte, int(cle), int(cle2), chiffrer=(mode=="Chiffrer"))
        elif algo == "Vigenère":
            res = vigenere(texte, cle, chiffrer=(mode=="Chiffrer"))
        elif algo == "Porta":
            res = porta(texte, cle, chiffrer=(mode=="Chiffrer"))
        elif algo == "ADFGVX":
            res = adfgvx(texte, cle, cle2, chiffrer=(mode=="Chiffrer"))
        else:
            res = "Algorithme inconnu."
        sortie_texte.delete("1.0", tk.END)
        sortie_texte.insert(tk.END, res)
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Interface graphique
root = tk.Tk()
root.title("Outils de chiffrement développés par Hani TAHER")

# Texte à traiter
tk.Label(root, text="Texte à traiter :").grid(row=0, column=0, sticky="w")
entree_texte = tk.Text(root, height=5, width=60)
entree_texte.grid(row=1, column=0, columnspan=4)

# Algorithme
tk.Label(root, text="Algorithme :").grid(row=2, column=0, sticky="w")
algo_var = tk.StringVar()
algo_menu = ttk.Combobox(root, textvariable=algo_var)
algo_menu["values"] = ["César", "Alphabet Horizontal", "Alphabet Vertical", "Transposition", "Affine", "Vigenère", "Porta", "ADFGVX"]
algo_menu.grid(row=2, column=1)
algo_menu.current(0)

# Mode
mode_var = tk.StringVar(value="Chiffrer")
tk.Radiobutton(root, text="Chiffrer", variable=mode_var, value="Chiffrer").grid(row=2, column=2)
tk.Radiobutton(root, text="Déchiffrer", variable=mode_var, value="Déchiffrer").grid(row=2, column=3)

# Clés
tk.Label(root, text="Clé 1 :").grid(row=3, column=0, sticky="w")
cle_entry = tk.Entry(root)
cle_entry.grid(row=3, column=1)

tk.Label(root, text="Clé 2 :").grid(row=3, column=2, sticky="w")
cle2_entry = tk.Entry(root)
cle2_entry.grid(row=3, column=3)

# Bouton exécuter
btn_chiffrer = tk.Button(root, text="Exécuter", command=chiffrer_texte)
btn_chiffrer.grid(row=4, column=0, columnspan=4, pady=10)

# Résultat
tk.Label(root, text="Résultat :").grid(row=5, column=0, sticky="w")
sortie_texte = tk.Text(root, height=5, width=60)
sortie_texte.grid(row=6, column=0, columnspan=4)

root.mainloop()
