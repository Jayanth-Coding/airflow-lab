from datetime import datetime
from airflow.sdk import dag, task

@dag(schedule=None, start_date=datetime(2026, 1, 1), tags=["lesson1"])
def hello_airflow():

    @task
    def say_hello():
        print("Hello from Airflow!")
        return {"name": "Jayanth", "team": "Aubrant"}
    
    @task
    def oops():
           raise ValueError("something went wrong")

    @task
    def greet(name: str):
        print(f"Welcome to Airflow, Mr. {name['name']} of {name['team']}")

    greet(say_hello()) >> oops()

hello_airflow()