# FMC

## Models

- [x] **Department**
    - id
    - name
    - created_at
    - updated_at

- [x] **City**
    - id
    - name
    - department
    - created_at
    - updated_at

- [x] **District**
    - id
    - name
    - city
    - created_at
    - updated_at

- [x] **Member**
    - id
    - name
    - firstName
    - email
    - phone
    - city
    - district
    - created_at
    - updated_at
    

## functions
- [] **Gestion des Membres**
  - [x] Ajouter un membre:
    - Saisir les informations (nom, prenom, email, telephone, ville, quartier, etc.).
  - [x] Modifier un membre:
    - Modifier les details d'un membres existant.
  - [x] Supprimer un membre:
    - Supprimer definitivement un membre de la base de donnees.
  - [x] Lister les membres:
    - Voir une liste paginee des membres avec filtres (par departement, ville, quartier).
  - [] Rechercher un membre:
    - Recherche par nom, prenom, email ou telephone.
  - [] Exporter les membres:
    - Generer des fichiers Excel, CSV ou PDF des membres enregistres.
  - [x] Visualiser les details d'un membre:
    - voir une page dedie pour un membre avec toutes ses information

- [x] **Gestion des Departement**
  - [x] Ajouter un departement:
    - Creer un nouveau departement.
  - [x] Modifier un departement:
    - Modifier le nom d'un departement existant.
  - [x] Supprimer un departement:
    - Supprimer un departement et ses donnees associees (villes, quartiers, membres).
  - [x] Lister les departements:
    - Voir tout les departements avec leur ville correspondant.
    
- [x] **Gestion des Villes**
  - [x] Ajouter une ville:
    - Associer une ville a un departement.
  - [x] Modifier une ville:
    - Modifier le nom ou l'appartenance departement d'une ville.
  - [x] Supprimer une ville:
    - Supprimer une ville et ses quartiers associes.
  - [x] Lister les villes:
    - Voir toutes les villes avec leur quartier correspondant.
        
- [x] **Gestion des Quartiers**
  - [x] Ajouter un quartier:
    - Associer un quartier a une ville.
  - [x] Modifier un quartier:
    - Modifier le nom ou la ville d'un quartier.
  - [x] Supprimer un quartier:
    - Supprimer un quartier d'une ville specifique.
  - [x] Lister les quartiers:
    - voir tous les quartiers pour une ville donnes.

- [] **Tableau de Bord**
  - [] Statistiques:
    - Nombre total de membres, villes, departements et quartiers.
    - Repartition des membres par departement, ville, quartier.
  - [] Graphiques:
    - Graphiques circulaire ou barres pour les repartition.
  - [] Dernieres activites:
    - Liste des derniers membres ajouter ou modifies.

- [] **Gestion des Utilisateurs et Securite**
  - [] Connexion securises:
    - Authentification par mot de passe avec possibilite de reinitialisation.
  - [] Changement de mot de passe:
    - Permettre a l'administrateur de modifier son mot de passe.
  - [] Journal des activites:
    - Enregistrer les action effectuees dans le panneau (ajout, modification, suppression).

- [] **Autres Fonctionnalites**
  - [] Notifiations:
    - Recevoir des alertes pour les taches importantes (comme les nouveaux membres ajoutes).
  - [] Sauvegarde de la base de donnees:
    - Exporter une sauvegarde complete pour eviter les pertes de donnees.
  - [] Support technique:
    - Integrer une section pour contacter l'equipe de maintenance en cas de probleme.