import pandas as pd
from sqlalchemy import create_engine, text

# Definition des paramètres de connexion à la base de données
db_username = 'postgres'
db_password = 'pass123'
db_host = '127.0.0.1'
db_port = '5432'
db_name = 'postgres'

# Création du moteur SQLAlchemy
engine = create_engine(f'postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# Exécution d'une requête simple
sql_query = """SELECT ville_nom_reel, ville_departement, ville_code_postal, ville_population_2012
            FROM public.ville
            ORDER BY ville_population_2012 DESC
            LIMIT 10"""

df_grandes_villes = pd.read_sql(sql_query, engine)
print("Séléction des plus grandes villes:")
print(df_grandes_villes)

# Exécution d'une requête paramètrée
departement_a_rechercher = "78"

sql_query = text("""SELECT ville_nom_reel, ville_departement, ville_code_postal, ville_population_2012
                FROM public.ville
                WHERE ville_departement = :departement_code""")
params = {"departement_code": departement_a_rechercher}
df_villes_departement = pd.read_sql_query(sql_query, engine, params=params)

print(f"Séléction de quelques villes du département {departement_a_rechercher}")
print(df_villes_departement.head(10))
