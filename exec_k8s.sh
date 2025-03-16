#!/bin/bash

set -e  # Stop on error

# 📍 Chemin vers le fichier YAML (chemin absolu si nécessaire)
K8S_YAML="k8s/kubernetes.yaml"

# 📍 Paths absolus des services
ROOT_DIR=$(pwd)
USER_API_PATH="$ROOT_DIR/user_api"
USER_INTERFACE_PATH="$ROOT_DIR/user_interface"
ADMIN_API_PATH="$ROOT_DIR/admin_api"
ADMIN_INTERFACE_PATH="$ROOT_DIR/admin_interface"

# 📢 Étape 1 : Activer l'environnement Docker de Minikube
echo "🔧 Switching Docker to Minikube environment..."
eval $(minikube docker-env -u)

# 📢 Étape 2 : Build des images Docker avec paths explicites
echo "🐳 Building Docker images with --no-cache..."
docker build -t hands_on_microservices-user_api:latest "$USER_API_PATH"
docker build -t hands_on_microservices-user_interface:latest "$USER_INTERFACE_PATH"
docker build -t hands_on_microservices-admin_api:latest "$ADMIN_API_PATH"
docker build -t hands_on_microservices-admin_interface:latest "$ADMIN_INTERFACE_PATH"

# 📢 Étape 3 : Charger les images dans Minikube
echo "📦 Loading images into Minikube..."
minikube image load hands_on_microservices-user_api:latest
minikube image load hands_on_microservices-user_interface:latest
minikube image load hands_on_microservices-admin_api:latest
minikube image load hands_on_microservices-admin_interface:latest

# 📢 Étape 4 : Supprimer les anciens pods
echo "🧹 Deleting old pods..."


# 📢 Étape 5 : Appliquer les fichiers Kubernetes
echo "🚀 Deploying to Minikube..."
kubectl apply -f "$K8S_YAML"

# 📢 Étape 6 : Vérifier les pods
echo "📡 Waiting for pods to be ready..."
kubectl wait --for=condition=Ready pod -l app -n myapp --timeout=120s

# 📢 Étape 7 : Afficher les URL des interfaces
echo "🌐 Access your services:"
#minikube service user-interface -n myapp
minikube service admin-interface -n myapp
