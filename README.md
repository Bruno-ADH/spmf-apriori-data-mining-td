# TD SPMF — Frequent Itemset Mining avec Apriori

Ce dépôt contient le travail réalisé dans le cadre d'un TD de **Data Mining / Fouille de données** consacré à l'extraction d'itemsets fréquents avec **SPMF** et l'algorithme **Apriori**.

## Objectifs du TD

- découvrir la bibliothèque SPMF ;
- comprendre le format des données transactionnelles ;
- exécuter Apriori avec l'interface graphique de SPMF ;
- appeler SPMF depuis Python avec `subprocess` ;
- vérifier la cohérence entre l'interface graphique et le script ;
- mesurer l'évolution du temps d'exécution et du nombre d'itemsets selon le support minimum ;
- comparer les observations avec l'article fondateur d'Apriori.

## Technologies utilisées

- **Java** — nécessaire pour exécuter `spmf.jar`
- **SPMF 2.67a**
- **Python 3**
- module standard `subprocess`
- module standard `time`

## Structure proposée du projet

```text
TD_SPMF/
├── README.md
├── .gitignore
├── apriori_spmf.py
├── experiment_apriori.py
```

Les fichiers volumineux ou facilement téléchargeables (`spmf.jar`, datasets, résultats générés) ne sont pas versionnés.

## Pré-requis

Vérifier Java :

```bash
java -version
```

Vérifier Python :

```bash
python --version
```

Télécharger ensuite SPMF depuis le site officiel :

- https://www.philippe-fournier-viger.com/spmf/

Les jeux de données utilisés dans le TD sont notamment :

- `retail.txt`
- `chess.txt`

Ils sont disponibles depuis la page officielle des datasets SPMF.

## Exécution d'Apriori avec SPMF

Exemple en ligne de commande :

```bash
java -jar spmf.jar run Apriori retail.txt output.txt 1%
```

## Exécution depuis Python

Le script `apriori_spmf.py` lance SPMF via `subprocess`, lit le fichier de sortie et compte les itemsets fréquents.

Exécution :

```bash
python apriori_spmf.py
```

Sur `retail` avec `minsup = 1%`, l'expérience a donné :

- **159 itemsets fréquents**
- **633 ms** dans l'interface graphique SPMF

## Expérimentation temps / support

L'expérimentation a été menée sur `retail`, avec **3 répétitions par valeur de support**. Le temps ci-dessous correspond à la moyenne mesurée par Python autour de l'appel à SPMF.

| Support minimum | Temps moyen (s) | Nombre d'itemsets |
|---:|---:|---:|
| 50 % | 1.1675 | 1 |
| 40 % | 0.9350 | 2 |
| 30 % | 0.9397 | 3 |
| 20 % | 0.8481 | 3 |
| 10 % | 0.9785 | 9 |
| 5 % | 1.0279 | 16 |
| 2 % | 1.0216 | 55 |
| 1 % | 1.2330 | 159 |

### Observation

Lorsque le support minimum diminue, le nombre d'itemsets fréquents augmente fortement. Le temps d'exécution reste ici proche d'une seconde pour la plupart des valeurs, car le coût du lancement de la JVM et des accès disque représente une part non négligeable sur des exécutions aussi courtes.

## Machine utilisée pour les mesures

- **CPU :** Intel Core i5-5300U @ 2.30 GHz
- **RAM :** 11.9 Go
- **OS :** Microsoft Windows 10 Professionnel — 10.0.19045

## Référence scientifique

R. Agrawal et R. Srikant, **“Fast Algorithms for Mining Association Rules”**, Proceedings of the 20th International Conference on Very Large Data Bases (VLDB), 1994.

PDF : https://www.vldb.org/conf/1994/P487.PDF

## Notes

Ce dépôt correspond à un travail académique de prise en main de SPMF et d'expérimentation autour de l'algorithme Apriori.

Les fichiers générés par les exécutions et les datasets ne sont pas suivis par Git afin de garder le dépôt léger et reproductible.
