import statistics as st 

def analyser_ventes(transactions):
    
    # 1. Nettoyage : filtrer les valeurs négatives ou nulles
    valides = [t for t in transactions if t > 0]
    
    if not valides:
        return {
            "nb_transactions": 0,
            "somme_totale": 0.0,
            "moyenne": 0.0,
            "mediane": 0.0,
            "ecart_type": 0.0,
            "maximum": 0.0,
            "minimum": 0.0,
            "anomalies": []
        }

    # 2. Calculs statistiques
    nb_transactions = len(valides)
    somme_totale = sum(valides)
    moyenne = somme_totale / nb_transactions
    mediane = st.median(valides)
    
    # Écart-type (échantillon, nécessite au moins 2 valeurs)
    ecart_type = st.stdev(valides) if nb_transactions > 1 else 0.0
    
    maximum = max(valides)
    minimum = min(valides)

    # 3. Détection des anomalies (transactions > 2 * moyenne)
    seuil_anomalie = 2 * moyenne
    anomalies = [t for t in valides if t > seuil_anomalie]

    # 4. Structure de sortie sous forme de dictionnaire
    return {
        "nb_transactions": nb_transactions,
        "somme_totale": somme_totale,
        "moyenne": moyenne,
        "mediane": mediane,
        "ecart_type": ecart_type,
        "maximum": maximum,
        "minimum": minimum,
        "anomalies": anomalies
    }
#guilaummmmmmmmmme
# 5. Bloc d'exécution et de test 
if __name__ == "__main__":
    donnees_test = [150, 250, -20, 0, 300, 1500, 450, 120, 220, 1100, 50]
    
    resultats = analyser_ventes(donnees_test)
    
    for indicateur, valeur in resultats.items():
        if isinstance(valeur, float):
            print(f"- {indicateur} : {valeur:,.2f}")
        else:
            print(f"- {indicateur} : {valeur}")