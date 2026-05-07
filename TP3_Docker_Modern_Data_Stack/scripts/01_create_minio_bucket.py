from minio import Minio

BUCKETS = ["raw", "bronze", "silver", "gold"]

client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False,
)

for bucket in BUCKETS:
    if not client.bucket_exists(bucket):
        client.make_bucket(bucket)
        print(f"Bucket créé : {bucket}")
    else:
        print(f"Bucket existe déjà : {bucket}")

print("MinIO est prêt.")
