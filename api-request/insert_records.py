import psycopg2
from api_request import mock_fetch_data

def connect_to_db():
    print("Connecting to the database...")
    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            port=5432,
            dbname="weather_data",
            user="postgres",
            password="postgres"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise

def create_table(conn):
    print("Creating the weather_data table if it doesn't exist...")
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE SCHEMA IF NOT EXISTS dev;
                CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                    id SERIAL PRIMARY KEY,
                    city TEXT,
                    temperature FLOAT,
                    weather_description TEXT,
                    wind_speed FLOAT,
                    time TIMESTAMP,
                    inserted_at TIMESTAMP DEFAULT NOW(),
                    utc_offset TEXT
                );
            """)
            conn.commit()
            print("Table created successfully.")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
        raise

conn = connect_to_db()
create_table(conn)