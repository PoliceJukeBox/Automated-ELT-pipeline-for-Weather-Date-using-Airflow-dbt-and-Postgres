# Automated-ELT-pipeline-for-Weather-Date-using-Airflow-dbt-and-Postgres

source .venv/bin/activate
pip install -r requirements.txt

docker-compose exec db psql -U postgres -d weather_data

Airflow username: admin
Airflow password: fQGUkfCcZW7tcCtx