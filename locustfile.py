from locust import HttpUser, task, between


class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 0.3)

    @task(1)
    def get_entities(self):
        self.client.get("/entities?event_title=Pink")
