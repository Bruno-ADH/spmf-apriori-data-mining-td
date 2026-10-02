import subprocess
import time

supports = ["50%", "40%", "30%", "20%", "10%", "5%", "2%", "1%"]
repetitions = 3

print("support ; temps_moyen_s ; nombre_itemsets")

for support in supports:
    temps = []
    nombre_itemsets = None

    for i in range(repetitions):
        output_file = f"retail_{support.replace('%', '')}_{i}.txt"

        commande = [
            "java", "-jar", "spmf.jar",
            "run", "Apriori",
            "retail.txt",
            output_file,
            support
        ]

        debut = time.perf_counter()

        subprocess.run(
            commande,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        fin = time.perf_counter()
        temps.append(fin - debut)

        with open(output_file, "r", encoding="utf-8") as f:
            nombre_itemsets = sum(
                1 for ligne in f
                if "#SUP:" in ligne
            )

    temps_moyen = sum(temps) / len(temps)

    print(
        f"{support} ; "
        f"{temps_moyen:.4f} ; "
        f"{nombre_itemsets}"
    )