# Exercice BioStatistique

data = [
    159, 152, 171, 163, 140, 157, 162, 171, 158, 154, 163, 159, 153,
    159, 157, 159, 165, 154, 147, 156, 172, 168, 159, 155, 152, 159,
    164, 159, 157, 159, 158, 159, 154, 160, 154, 162, 156, 155, 160
]

# 1) Calcul de l'étendue (Range)

minimum = min(data)
maximum = max(data)
etendue = maximum - minimum

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Étendue =", etendue)

# 2) Répartition en classes (5 classes)
# Formule de Sturges (optionnelle) : k = 1 + 3.3 * log10(n)
# Ici on choisit 5 classes manuellement.

nb_classes = 5
class_width = etendue // nb_classes + 1

classes = []
start = minimum
for _ in range(nb_classes):
    end = start + class_width
    classes.append((start, end))
    start = end

print("\nRépartition en classes:")
for cl in classes:
    print(cl)

# 3) Tableau de distribution des fréquences
# Compter l'effectif dans chaque classe
frequency = []
for cl in classes:
    count = sum(1 for x in data if cl[0] <= x < cl[1])
    frequency.append(count)

# Affichage du tableau
print("\nTableau de distribution des fréquences:")
print("Classe\t\tEffectif\tFréquence")
total = len(data)
for cl, eff in zip(classes, frequency):
    freq = eff / total
    print(f"{cl}\t{eff}\t\t{freq:.2f}")
