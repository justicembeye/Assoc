import os
import django
from django.core.management import execute_from_command_line
import psycopg2
from psycopg2 import sql

# === CONFIGURATION DE LA BASE DE DONNÉES ===
DB_NAME = "assoc"
DB_USER = "postgres"
DB_PASSWORD = "Crypto98@"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_ADMIN_PASSWORD = "Crypto98@"  # Mot de passe de l'utilisateur 'postgres'

# === CRÉATION DE LA BASE DE DONNÉES ===
def create_database():
    try:
        # Connexion à PostgreSQL en tant qu'utilisateur "postgres"
        connection = psycopg2.connect(
            dbname="postgres", user="postgres", password=DB_ADMIN_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        connection.autocommit = True
        cursor = connection.cursor()

        # Vérification si l'utilisateur existe déjà
        cursor.execute(
            sql.SQL("SELECT 1 FROM pg_roles WHERE rolname = %s"), [DB_USER]
        )
        if cursor.fetchone():
            print(f"L'utilisateur {DB_USER} existe déjà.")
        else:
            # Création de l'utilisateur
            cursor.execute(
                sql.SQL("CREATE USER {} WITH PASSWORD %s").format(sql.Identifier(DB_USER)),
                [DB_PASSWORD],
            )
            print(f"Utilisateur '{DB_USER}' créé avec succès.")

        # Vérification si la base de données existe déjà
        cursor.execute(
            sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [DB_NAME]
        )
        if cursor.fetchone():
            print(f"La base de données '{DB_NAME}' existe déjà.")
        else:
            # Création de la base de données
            cursor.execute(
                sql.SQL("CREATE DATABASE {} OWNER {}").format(
                    sql.Identifier(DB_NAME), sql.Identifier(DB_USER)
                )
            )
            print(f"Base de données '{DB_NAME}' créée avec succès.")

        cursor.close()
        connection.close()
    except psycopg2.Error as e:
        print(f"Erreur lors de la création de la base de données : {e}")
        exit(1)


# === CONFIGURATION DJANGO ===
def configure_django():
    # Configuration dynamique de Django settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assoc.settings")
    django.setup()

    # Migration des modèles
    print("Application des migrations...")
    execute_from_command_line(["manage.py", "migrate"])
    print("Migrations appliquées avec succès.")


if __name__ == "__main__":
    print("Création de la base de données...")
    create_database()

    print("Configuration de Django...")
    configure_django()

    print("Tout est prêt !")
