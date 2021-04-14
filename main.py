# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from sqlite3 import Date

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017/')
# donner la database
esmeDB = client['supermarche']
# Création des collections
produit= esmeDB['produit']
commande = esmeDB['commande']
InventaireProduit = esmeDB['InventaireProduit']
Caisse = esmeDB['Caisse']

# Création BDD

InventaireProduit1 = {"_id": "1",
                      "Quantité": 20
}
InventaireProduit2 = {"_id": "2",
                      "Quantité": 10
}

InventaireProduit3 = {"_id": "3",
                      "Quantité": 2
}

InventaireProduit4 = {"_id": "4",
                      "Quantité": 3
}

Produit1 = {"_id": "1",
            "Nom_Produit": "Pasta",
             "Description_Produit": "Produit Italien",
            "Inventaire": [InventaireProduit1]
}

Produit2 = {"_id": "2",
            "Nom_Produit": "Riz",
            "Description_Produit": "Produit Indien, basmathi",
            "Inventaire": [InventaireProduit2]
            }

Produit3 = {"_id": "3",
            "Nom_Produit": "Pack d'Eau",
            "Description_Produit": "Eau Cristalline",
            "Inventaire": [InventaireProduit3]
}

Produit4 = {"_id": "4",
            "Nom_Produit": "Fromage",
            "Description_Produit": "Produit Français",
            "Inventaire": [InventaireProduit4]
}

Commande1 = {"_id": "1", "Date": '13/04/2021', "Paniers":[Produit2, Produit4, Produit4]}
Commande2 = {"_id": "2", "Date": '13/04/2021', "Paniers":[Produit1, Produit4]}
Commande3 = {"_id": "3", "Date": '14/04/2021', "Paniers":[Produit2, Produit3, Produit3]}
Commande4 = {"_id": "4", "Date": '14/04/2021', "Paniers":[Produit1, Produit2]}

Caisse1 = {"_id": "1",
"commande": [Commande2, Commande4]

}
Caisse2 = {"_id": "2",
"commande": [Commande3, Commande1]

}


# On insert l'inventaire
'''x1 = InventaireProduit.insert_one(InventaireProduit1)
x2 = InventaireProduit.insert_one(InventaireProduit2)
x3 = InventaireProduit.insert_one(InventaireProduit3)
x4 = InventaireProduit.insert_one(InventaireProduit4)
print(x1)
print(x2)
print(x3)
print(x4)'''

# On insert les produits
'''x1 = produit.insert_one(Produit1)
x2 = produit.insert_one(Produit2)
x3 = produit.insert_one(Produit3)
x4 = produit.insert_one(Produit4)
print(x1)
print(x2)
print(x3)
print(x4)'''

# On insert les commandes
'''x1 = commande.insert_one(Commande1)
x2 = commande.insert_one(Commande2)
x3 = commande.insert_one(Commande3)
x4 = commande.insert_one(Commande4)
print(x1)
print(x2)
print(x3)
print(x4)'''



# On insert les caisses
'''x1 = Caisse.insert_one(Caisse1)
x2 = Caisse.insert_one(Caisse2)
print(x1)
print(x2)'''

pipe = [{'_id': None, 'TotalDesCommandes' : {}}]
aggregation = Caisse.aggregate()

