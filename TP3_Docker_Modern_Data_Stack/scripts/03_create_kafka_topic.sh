#!/usr/bin/env bash
set -e

docker exec kafka_broker kafka-topics --create \
  --if-not-exists \
  --topic ventes_temps_reel \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1

echo "Topics disponibles :"
docker exec kafka_broker kafka-topics --list --bootstrap-server localhost:9092
