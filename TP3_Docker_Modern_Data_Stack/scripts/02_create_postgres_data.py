import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="ventes_db",
    user="admin",
    password="password",
)
conn.autocommit = True
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS ventes (
    id SERIAL PRIMARY KEY,
    client_id VARCHAR(20),
    produit VARCHAR(100),
    categorie VARCHAR(50),
    quantite INTEGER,
    prix_unitaire NUMERIC(10,2),
    region VARCHAR(50),
    date_vente DATE DEFAULT CURRENT_DATE
);
""")

cur.execute("DELETE FROM ventes;")
cur.executemany(
    """
    INSERT INTO ventes (client_id, produit, categorie, quantite, prix_unitaire, region, date_vente)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """,
    [
        ("C001", "Laptop Dell", "Informatique", 1, 899.99, "Nord", "2024-01-05"),
        ("C002", "Souris Logitech", "Informatique", 2, 29.99, "Sud", "2024-01-07"),
        ("C003", "Chaise Bureau", "Mobilier", 1, 349.99, "Nord", "2024-01-12"),
        ("C004", "Bureau Debout", "Mobilier", 1, 599.99, "Ouest", "2024-01-18"),
        ("C005", "Lampe Bureau", "Mobilier", 3, 49.99, "Est", "2024-01-22"),
    ],
)
cur.execute("SELECT COUNT(*) FROM ventes;")
print(f"Table ventes prête : {cur.fetchone()[0]} lignes insérées.")

cur.close()
conn.close()
