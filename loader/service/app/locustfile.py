# -*- coding:utf-8 -*-
"""locust-test-module"""
from locust import TaskSet, task
from locust_plugins.users import RestUser

class MyTaskSet(TaskSet):
    """taskSet"""
    @task
    def post_product_id(self, **kwargs):
        headers = {
            'Authorization': 'Bearer '
        }
        json = {
            "id": "123fkjfoiqw1"
        }
        """post_product_id"""
        return self.client.post("/product", json=json, headers=headers)

class MyLocust(RestUser):
    """locustClass"""
    tasks = [MyTaskSet]
    min_wait = 1000
    max_wait = 3000
    host = "http://localhost:8083"
