#!/bin/bash
until docker info >/dev/null 2>&1; do echo "waiting for docker..."; sleep 2; done
sudo iptables-legacy -P FORWARD ACCEPT
docker compose up -d
docker compose ps
