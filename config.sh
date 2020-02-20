#!/bin/bash


echo -n "Porject name: "
read PROJECT_NAME

echo -n "ELK version: "
read ELK_VERSION

echo -n "ES port: "
read ES_PORT

echo -n "Kibana port: "
read KIBANA_PORT

sed -i -e "s/^USERNAME=[A-Za-z0-9_]*/USERNAME=$USER/g" .env
sed -i -e "s/^DGID=[A-Za-z0-9_]*/DGID=$(id -g)/g" .env
sed -i -e "s/^DUID=[A-Za-z0-9_]*/DUID=$(id -u)/g" .env
sed -i -e "s/^ELK_VERSION=[A-Za-z0-9_\.]*/ELK_VERSION=$ELK_VERSION/g" .env
sed -i -e "s/^ES_PORT=[A-Za-z0-9_]*/ES_PORT=$ES_PORT/g" .env
sed -i -e "s/^KIBANA_PORT=[A-Za-z0-9_]*/KIBANA_PORT=$KIBANA_PORT/g" .env
sed -i -e "s/^PROJECT_NAME=[A-Za-z0-9_\.\-]*/PROJECT_NAME=$PROJECT_NAME/g" .env

printf '=%.s' {1..30}
echo
echo "Project = $PROJECT_NAME"
echo "USERNAME =  $USER"
echo "UID =  $(id -u)"
echo "GID =  $(id -g)"
echo "ELK =  $ELK_VERSION"
echo "ES Port =  $ES_PORT"
echo "Kibana Port =  $KIBANA_PORT"
printf '=%.s' {1..30}
