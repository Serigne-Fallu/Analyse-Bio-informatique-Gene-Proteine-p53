import matplotlib.pyplot as plt

# Création des données
methodes = ['Analyse de séquences', 'Alignement', 'Prédiction de structure']
etapes = [3, 5, 2]

# Création de la figure
fig, ax = plt.subplots()
ax.bar(methodes, etapes)

# Personnalisation de la figure
ax.set_xlabel('Méthodes')
ax.set_ylabel('Nombre d\'étapes')
ax.set_title('Étude bioinformatique du gène p53')

# Affichage de la figure
plt.show()
