# -*- coding: utf-8 -*-
from locust import HttpUser, TaskSet, task


class FirstTestClass(TaskSet):
    # @task attribute' methodumuzun task olduğunu belirtmek için kullanıyoruz.
    @task
    def index(self):
        self.client.get("/locustio/locust")

    @task
    def profile(self):
        with self.client.get("/orgs/locustio/people", catch_response=True) as response:
            if 200 == response.status_code:
                response.success()


class MyFirstLocust(HttpUser):
    # İstek yapılacak host (isteğe bağlı), konsoldan da verebilirsiniz.
    host = "https://github.com"

    # Test Class'ımız
    task_set = FirstTestClass

    # İstekler arası minimum ve maksimum bekleme süresi milisaniye cinsinden, Default "1000"
    min_wait = 0
    max_wait = 7000
