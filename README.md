# TP3 - Mise en place d'un environnement Modern Data Stack avec Docker

Ce projet met en place une architecture de données moderne avec Docker Compose :

- PostgreSQL : source de données relationnelle
- MinIO : Data Lake compatible S3
- Kafka + Zookeeper : streaming temps réel
- Airflow : orchestration des pipelines

## Lancement rapide dans Codespaces

```bash
cd TP3_Docker_Modern_Data_Stack
python -m venv venv_tp3
source venv_tp3/bin/activate
pip install -r requirements.txt
docker compose up -d
```

Attendre environ 1 à 2 minutes, puis vérifier :

```bash
docker compose ps
python scripts/04_check_services.py
```

## Interfaces

- MinIO : http://localhost:9001  
  Login : `minioadmin` / `minioadmin`
- Airflow : http://localhost:8080  
  Login : `airflow` / `airflow`
- PostgreSQL : localhost:5432  
  DB : `ventes_db`, user : `admin`, password : `password`
- Kafka : localhost:9092

## Scripts utiles

```bash
python scripts/01_create_minio_bucket.py
python scripts/02_create_postgres_data.py
bash scripts/03_create_kafka_topic.sh
python scripts/04_check_services.py
```

## Arrêt

```bash
docker compose down
```

Suppression complète avec volumes :

```bash
docker compose down -v
```
