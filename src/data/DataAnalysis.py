import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data1 = pd.DataFrame(pd.read_csv('Transformed.csv'))


def getTopRated():
## Identifier les 10 applications les plus populaires
    grouped = data1.groupby("Rating").sum()
    app_rating_ranking = grouped.iloc[:,-1]
    total_rates_ranked = pd.merge(data1,app_rating_ranking,on='Rating')
    
## Étudier les types d'applications qui sont les plus populaires par genres
    total_unique_type = total_rates_ranked.groupby(["Genres","Type"]).sum()
    grouped_by_genre = total_unique_type.sort_values(by=total_rates_ranked.columns[-1], ascending=False).iloc[:,-1]

## Suivre l'évolution de l'utilisation des applications en fonction de ses rating

    top_installed_app =total_rates_ranked.groupby(total_rates_ranked.columns[1]).sum() 

    top_10_installed_app = top_installed_app.head(10)
   
    top_10_installed_app.plot(kind='bar')
    plt.ylabel('dernier mis à jour ')
    plt.title('Évolution de l\'utilisation des 10 applications les plus notée en fonction de ses mises à jours')
    #plt.show()

## Etude de 4 cas de plus rated application pour savoir les avances données par les updates
    grouped_by_app = total_rates_ranked.groupby("App").sum()
    app1 = grouped_by_app["Boys Photo Editor - Six Pack & Men's Suit"]
    app2 = grouped_by_app["Animated Photo Editor"]
    app3 = grouped_by_app["ROBLOX"]
    app4 = grouped_by_app["B Mobile Access"]

    plt.figure(figsize=(12, 6))
    plt.plot(app1, label='Boys Photo Editor - Six Pack & Men\'s Suit')
    plt.plot(app2, label='Animated Photo Editor')
    plt.plot(app4, label='B Mobile Access')
    plt.plot(app3, label='ROBLOX')
    plt.ylabel('Rating per Application')
    plt.title('Évolution des nombres d\'installation selon les updates')
    plt.legend()
    

## Corrélation entre ces application
    df = pd.DataFrame({'Boys Photo Editor - Six Pack & Men\'s Suit': app1, 'Animated Photo Editor': app2, 'B Mobile Access': app4,'ROBLOX' : app3})

    corr = df.corr()

    sb.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Corrélation entre les application les plus notéess')
    plt.show()

## Conclusion

def comparing_category_with_installation():
    category_installs = data1.groupby("Category")["Installs"].sum()

    # Créer un graphique à barres pour le nombre d'installations par catégorie
    plt.figure(figsize=(10, 6))
    category_installs.plot(kind="bar")
    plt.title("Nombre d'installations par catégorie d'application")
    plt.xlabel("Catégorie")
    plt.ylabel("Nombre d'installations")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Afficher le graphique
    plt.show()

comparing_category_with_installation()