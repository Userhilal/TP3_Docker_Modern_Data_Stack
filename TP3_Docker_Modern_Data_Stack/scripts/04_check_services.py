import socket
from minio import Minio
import psycopg2
from kafka.admin import KafkaAdminClient

checks = []

def port_open(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)
        return s.connect_ex((host, port)) == 0

for name, port in [("PostgreSQL", 5432), ("MinIO API", 9000), ("MinIO Console", 9001), ("Kafka", 9092), ("Airflow", 8080)]:
    ok = port_open("localhost", port)
    checks.append((name, ok))

try:
    conn = psycopg2.connect(host="localhost", port=5432, dbname="ventes_db", user="admin", password="password")
    conn.close()
    checks.append(("Connexion PostgreSQL", True))
except Exception as e:
    checks.append((f"Connexion PostgreSQL ({e})", False))

try:
    client = Minio("localhost:9000", access_key="minioadmin", secret_key="minioadmin", secure=False)
    list(client.list_buckets())
    checks.append(("Connexion MinIO", True))
except Exception as e:
    checks.append((f"Connexion MinIO ({e})", False))

try:
    admin = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id="tp3-check")
    topics = admin.list_topics()
    admin.close()
    checks.append((f"Connexion Kafka - topics: {topics}", True))
except Exception as e:
    checks.append((f"Connexion Kafka ({e})", False))

print("\n=== Vérification des services TP3 ===")
for name, ok in checks:
    print(("OK" if ok else "KO") + " - " + name)
