FROM nginx:latest

# Copiez le fichier de configuration nginx.conf dans le conteneur
COPY nginx.conf /etc/nginx/nginx.conf

# Exposez le port 80 pour le service
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
