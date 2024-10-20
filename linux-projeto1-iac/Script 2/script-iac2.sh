#!/bin/bash

echo "Atualizando o servidor..."
apt-get update
apt-get upgrade -y

echo "Instalando apacha2, unzip e wget"
apt-get install apacha2 -y
apt-get install unzip -y
apt-get install wget -y

echo "Baixando e copiando os arquivos da aplicação..."
cd /tmp
wget https://github.com/denilsonbonatti/linux-site-dio/archive/refs/heads/main.zip
cd linux-site-dio-main/
cp -R * /var/www/html