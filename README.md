# Vers du DevOps (Code Engineering)

**Attention : ces TD font office de contrôle continu pour le module MLOps. Une note individuelle sera attribuée.**

## Partie I : 

### Contexte Général

Les deux séances de TD seront consacrées au déploiement (ingénierie logicielle). L'objectif est d'aborder des notions essentielles à travers un projet pratique. Ces notions seront intégrées dans l'ordre suivant :

1. Gérer la communication entre des microservices (API) avec Docker Compose, via des Domain Unix Sockets.

```diff
Dans un premier temps, j'avais implémenté la communicattion entre les microservices en utilisant les Domain Unix Sockets.
En effet, ils ont l'avantages d'être plus rapide qu'en passant par le protocole ip (les messages n'ont pas besoin d'être encapsulés dans les couches pour être envoyés sur le réseau).
Cependant, cette méthode n'est pas adaptée dans le cadre d'un déploiement à l'échelle à l'aide de Kubernetes.
C'est pour cela que j'ai décidé de développer des apis basés sur le protocole IP.
```

2. Ajouter une base de données dans l'écosystème.

```diff
J'ai implémenté une base de données PostgreSQL.
Je n'ai pas focalisé mon attention sur la sécurité du système.
```

3. Introduire les GitHub Actions (.github/workflows/ci_cd.yml).

```diff
J'ai implémenté des GitHub Actions qui builds le projet à l'aide de docker compose.
```

5. L'utilisation de Nginx est-elle nécessaire ?

```diff
Nginx n’est pas nécessaire si le routage est simple entre microservices.

Cependant Nginx devient utile voire nécessaire dans le cadre d'une mise en production sur Kubernetes pour :
- Le reverse proxy (accès unifié aux services),
- La gestion TLS/SSL (HTTPS),
- Le load balancing,
- Les routes API (URL rewriting, etc.).

Dans mon cas, j'ai décidé d'implémenter Nginx dans le Kubernetes (voir partie suivante).
```

6. Migrer de Docker Compose vers Kubernetes (Minikube) ?

```diff
Kubernetes offre une orchestration plus fine (scalabilité, résilience, monitoring).
Minikube permet un apprentissage progressif en local, avec une transition douce.

Mais :
- Si les délais sont courts, Docker Compose peut suffire pour démonstration.
- On peut préparer les manifests YAML Kubernetes en parallèle pour une future migration.

Dans mon cas, j'ai décidé de développer les 2 méthodes (Kubernetes et docker compose).
J'ai également choisi d'implémenter des fonctionnalités dans Kubernetes tel que :

1. Namespace personnalisé

- Création d’un namespace `myapp` pour isoler toutes les ressources Kubernetes de l’application.

2. ConfigMap pour initialisation PostgreSQL

- Script SQL `init.sql` : création de la table `feedback` + insertion d’une donnée de test.
- Monté dans le conteneur PostgreSQL via volume pour exécution à l’initialisation.

3. Stockage persistant pour PostgreSQL

- PersistentVolumeClaim `postgres-pvc` de 1Gi.
- Permet la persistance des données de la base même après redémarrage.

4. Déploiement PostgreSQL

- Image : `postgres:latest`.
- Variables d’environnement : `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`.
- Montages :
  - Volume persistant (`/var/lib/postgresql/data`).
  - Script d’init (`/docker-entrypoint-initdb.d`).

5. Service PostgreSQL

- Service `postgres` exposant le port 5432.
- Communication interne avec les autres services via le DNS `postgres.myapp.svc.cluster.local`.

6. Déploiement User API

- Image : `hands_on_microservices-user_api:latest`.
- Port exposé : 8000.
- Variable d’environnement : `POSTGRES_HOST=postgres`.

7. Service User API

- Service `user-api` exposant le port 8000.

8. Déploiement User Interface

- Image : `hands_on_microservices-user_interface:latest`.
- Port exposé : 8501.

9. Service User Interface

- Service `user-interface` exposé en NodePort (port 30001).
- Accès externe à l’interface utilisateur.

10. Déploiement Admin API

- Image : `hands_on_microservices-admin_api:latest`.
- Port exposé : 8001.
- Variable d’environnement : `POSTGRES_HOST=postgres`.

11. Service Admin API

- Service `admin-api` exposant le port 8001.

12. Déploiement Admin Interface

- Image : `hands_on_microservices-admin_interface:latest`.
- Port exposé : 8502.

13. Service Admin Interface

- Service `admin-interface` exposé en NodePort (port 30002).
- Accès externe à l’interface d’administration.

14. Ingress avec règles d’accès et sécurité

- Ingress `myapp-ingress` routant les requêtes :
  - `/user-interface` → service `user-interface` (port 8501).
  - `/admin-interface` → service `admin-interface` (port 8502).
- Annotations de sécurité et performance :
  - Redirection HTTPS.
  - Limitation de débit (10 RPS, burst x2).
  - Timeouts de proxy (connexion, lecture, écriture).
  - Compression GZIP activée.
  - Headers de sécurité HTTP :
    - `X-Frame-Options: DENY`
    - `X-Content-Type-Options: nosniff`
    - `X-XSS-Protection`
    - `Strict-Transport-Security`


```

### Lien vers la base commune

Une base commune vous a été fournie sous le lien suivant : [https://github.com/AghilasSini/build_api_ml.git](https://github.com/AghilasSini/build_api_ml.git). Vous devrez décider si vous souhaitez intégrer ou non les éléments mentionnés dans la liste ci-dessus. Chaque choix devra être justifié.

---

## Instructions Générales : 

Une base commune vous a été fournie. À vous de décider si vous souhaitez intégrer ou non les éléments évoqués dans la liste ci-dessus. Chaque choix devra être justifié.

---

## Partie II – Un portail web adapté 

Il s'agit de concevoir une solution prenant en compte les éléments mentionnés ci-dessus et répondant au cahier des charges illustré par la figure ci-dessous (analogie avec Umtice).

![Projet](./un_portail_pour_les_gouverner_tous.png)
---

## Partie III – Un portail web pour tous les gouvernés (conception et architecture de système pour du ML)

Il s'agit de concevoir une plateforme d'annotation automatique de données brutes. Cette plateforme devra héberger des outils de traitement automatique des langues.

---

