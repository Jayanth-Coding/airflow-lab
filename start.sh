#!/bin/bash
sudo iptables-legacy -P FORWARD ACCEPT
docker compose up -d
docker compose ps
