import subprocess
import time

# Fichiers d'entrée et de sortie
fichier_entree = "retail.txt"
fichier_sortie = "retail_script_1percent.txt"

# Seuil de support minimum (1%)
seuil_support = "1%"

# Construction de la commande pour lancer SPMF avec l'algorithme Apriori
commande_spmf = [
    "java",
    "-jar",
    "spmf.jar",
    "run",
    "Apriori",
    fichier_entree,
    fichier_sortie,
    seuil_support
]

print("Exécution de la commande suivante :")
print(" ".join(commande_spmf))

# Démarrer la mesure du temps avant d'exécuter la commande
debut_temps = time.perf_counter()

# Exécution de la commande SPMF
resultat = subprocess.run(
    commande_spmf,
    capture_output=True,
    text=True
)

# Fin de la mesure du temps
fin_temps = time.perf_counter()

# Affichage de la sortie de SPMF
print(resultat.stdout)

# Si des erreurs sont présentes, les afficher
if resultat.stderr:
    print("Erreurs détectées lors de l'exécution :")
    print(resultat.stderr)

# Lecture des résultats dans le fichier de sortie
with open(fichier_sortie, "r", encoding="utf-8") as fichier:
    # On ne garde que les lignes contenant "#SUP:" qui indiquent les itemsets fréquents
    itemsets_frequents = [
        ligne.strip()
        for ligne in fichier
        if "#SUP:" in ligne
    ]

# Affichage du nombre total d'itemsets fréquents trouvés
print(f"Nombre total d'itemsets fréquents : {len(itemsets_frequents)}")

# Affichage du temps d'exécution mesuré
print(f"Temps d'exécution mesuré par Python : {fin_temps - debut_temps:.3f} seconde(s)")

# Affichage des 10 premiers itemsets fréquents pour donner un aperçu
print("\nExemples d'itemsets fréquents trouvés :")
for itemset in itemsets_frequents[:10]:
    print(itemset)
