'''ecrire une fonction max(liste) qui prend une liste de entier et retourne la plus grande valeur
Solution simple'''


def max (liste_des_entier):
    max = l[0]
    for x in l :
        if x >= max :
            max = x
    return max 

l =[10,12,13]

print(max(l))


'''ecrire une fonction qui prend en paramètre une liste d’entier et enlève les duplications
Eg: removeDuplicates([5,5,3,1,3,7]) => [3,5,1,7] '''

def remove_duplicates (liste_des_entier):
    for x in liste_des_entier:
        for i in range(liste_des_entier.length):
            dup =0 
            if (liste_des_entier[i]==x):
                dup += 1
            if dup >1 :
                liste_des_entier.remove(liste_des_entier[i])
    return liste_des_entier
    
