# docker

docker-compose down && docker rmi -f $(docker images -a -q) && docker-compose up -d

cat /var/www/nextcloud/config/autoconfig.php

docker rmi -f $(docker images -a -q)
docker compose up --force-recreate -d