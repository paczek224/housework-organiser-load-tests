from locust import HttpUser, task, between


class User(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_home(self):
        self.client.get("/")

    def on_start(self):
        print("Starting user task")
