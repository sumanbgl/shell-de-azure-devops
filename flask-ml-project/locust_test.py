from locust import HttpUser, task, between


class LocustTest(HttpUser):
    wait_time = between(1, 2)

    @task(5)
    def test_predict(self):
        self.client.post("https://suman-flask-ml-service.azurewebsites.net:443/predict", json={
            "CHAS": {
                "0": 0
            },
            "RM": {
                "0": 6.575
            },
            "TAX": {
                "0": 296.0
            },
            "PTRATIO": {
                "0": 15.3
            },
            "B": {
                "0": 396.9
            },
            "LSTAT": {
                "0": 4.98
            }
        })
