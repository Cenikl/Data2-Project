import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import re

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

    top_installed_app = total_rates_ranked.groupby("Installs").sum() 

    top_10_installed_app = app_rating_ranking.head(20)
   
    top_10_installed_app.plot(kind='bar')
    plt.ylabel('Installation')
    plt.xlabel('Rating')
    plt.title('Évolution des installations par rapport au note donnée par l\'utilisateur')
    plt.show()

## Etude de 4 cas de plus rated application pour savoir les avances données par les updates
    grouped_by_app = total_rates_ranked.groupby("App").sum()
    app1 = grouped_by_app.loc["Boys Photo Editor - Six Pack & Men's Suit"]
    app2 = grouped_by_app.loc["Animated Photo Editor"]
    app3 = grouped_by_app.loc["ROBLOX"]

## Corrélation entre ces application
    df = pd.DataFrame({'Boys Photo Editor - Six Pack & Men\'s Suit': app1, 'Animated Photo Editor': app2,'ROBLOX' : app3})

    corr = df.corr()

    sb.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Corrélation entre les application les plus notéess')
    plt.show()
   

def comparing_category_with_installation(data):
    data['Installs'] = pd.to_numeric(data['Installs'], errors='coerce')

# Group by category and calculate the sum of installations
    category_installs = data.groupby("Category")["Installs"].sum()

# Create a bar plot for the number of installations per category
    plt.figure(figsize=(10, 6))
    category_installs.plot(kind="bar")
    plt.title("Number of installation per category")
    plt.xlabel("Category")
    plt.ylabel("Number of installation")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

# Show the plot
    plt.show()

def clean_price(price):
    if price == 'Free':
        return 0.00
    elif price == 'Everyone':
        return 0.00
    else:
        return float(price.replace('$',''))

def difference_between_paid_and_free_apps():
    data1['Price'] = pd.to_numeric(data1['Price'], errors='coerce')
    data1['Installs'] = pd.to_numeric(data1['Installs'], errors='coerce')
    data1['Price'].fillna(0).astype(str)
    data1['Rating'] = data1['Rating'].replace(19.0,5.0)
    filtered_df = data1[data1['Price'] != 0.00]

    y_min = 0
    y_max = 600

    plt.scatter(filtered_df['Price'], filtered_df['Installs'],alpha=0.5)
    plt.xlabel('Price ($)')
    plt.ylabel('Installs')
    plt.title('Difference in Installs between Paid and Free Apps')
    plt.xticks(rotation=45)
    plt.ylim(y_min,y_max)
    plt.show()

def rating_apps_considering_prices():
    data1['Price'] = data1['Price'].apply(clean_price)
    data1['Installs'] = pd.to_numeric(data1['Installs'], errors='coerce')
    data1['Price'].fillna(0).astype(str)
    data1['Rating'] = data1['Rating'].replace(19.0,5.0)
    filtered_df = data1[data1['Price'] != 0.00]

    plt.scatter(filtered_df['Price'], filtered_df['Rating'],alpha=0.5)
    plt.xlabel('Price ($)')
    plt.ylabel('Rating')
    plt.title('Rating of the Apps')
    plt.xticks(rotation=45)
    plt.show()

rating_apps_considering_prices()
comparing_category_with_installation(data1)
difference_between_paid_and_free_apps()