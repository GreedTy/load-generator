# -*- coding:utf-8 -*-
"""locust-test-module"""
from locust import TaskSet, task
from locust_plugins.users import RestUser

class MyTaskSet(TaskSet):
    """taskSet"""
    @task
    def post_dna_kits_users_uid(self, **kwargs):
        headers = {
            'x-hb-app-id': 'appversion_1',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRRUVkbHRieVhpN2RBVWNMYjUwM1Bib1dzUDRxM2xZYlZzd3dRb00waTE0In0.eyJleHAiOjE2NjQzNTc4NzAsImlhdCI6MTY2NDM1NDI3MCwiYXV0aF90aW1lIjoxNjY0MzU0MjcwLCJqdGkiOiJmYjU0ZDMwNy1jZTUxLTQzN2ItYTJiMy0zNTM2OWZlNzgzNTMiLCJpc3MiOiJodHRwczovL2FjY291bnRzLmlkLWltLmRldi9hdXRoL3JlYWxtcy9oZWFsZXJiIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImY6OWQ0YWM1YmItNDU2Yy00OGQxLThiN2QtNDI3MjZlMWUzODgzOnloaTAwMjUyMSIsInR5cCI6IkJlYXJlciIsImF6cCI6InRlc3QtY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6IjIwNzk1YjdiLTI5Y2QtNDIzNS04YjUyLTI4ZmNiMzNmYjJhNCIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJST0xFX1VTRVIiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJlbWFpbCBwcm9maWxlIiwic2lkIjoiMjA3OTViN2ItMjljZC00MjM1LThiNTItMjhmY2IzM2ZiMmE0IiwidWlkIjoieWhpMDAyNTIxIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoieWhpMDAyNTIxIiwicHJlZmVycmVkX3VzZXJuYW1lIjoieWhpMDAyNTIxIiwiZ2l2ZW5fbmFtZSI6InloaTAwMjUyMSIsImZhbWlseV9uYW1lIjoiIiwiZW1haWwiOiJ5aGkwMDI1MjFAbmV0bWFyYmxlLmNvbSJ9.L9ULltqwHNRURjwpXekG9Wsao8nNLqKf7U_cXSn4bR-P-N3WZfW6LGqDb6xr8l0XAQhN891fvU6uU_witPfpQdVw7K03TldeZo2k6BnZU8149mosEf6wAx-yYik1Itag6U1zM2ZkLnJumZdTdTU8_iXMQLmTta4iXrUSdH3pi4MWq7bBa3wJ28VTtiTjRsgBM_LLMm6RPMzl2EF4J2MT8GtFNqxSTTWI-HnKYInt3Js9dqa4yCkja65CJXI1LwQ5grnkHft8ezmuI234l6zwC-8zczFjJjFGD9WKRm2LWFWKVAIzJBtMEbsfRkY76fRJVrpqJFo9lP7VDWgfWzg_NA'
        }
        json = {
            "id": "yhi002521",
            "gender": "male",
            "raceCategory": "KOREAN",
            "birthDate": "2022-07-19",
            "name": "홍길동",
            "ci": "string",
            "email": "gildong@netmarble.com",
            "address": "서울 구로구 디지털로26길 38",
            "addressDetail": "넷마블신사옥 13층",
            "zipCode": "08393",
            "cellphoneNumber": "01099998888",
            "phoneNumber": "01099997777"
        }
        """post_dna_kits_users_uid"""
        return self.client.post("/phr-dna/apps/v1/users", json=json, headers=headers)

    # @task
    # def get_dna_analyses(self, **kwargs):
    #     """get_dna_analyses"""
    #     return self.client.get("/phr-dna/apps/v1/dna-analyses", name="/dna-analyses", **kwargs)
    #
    # @task
    # def post_dna_analyses(self, **kwargs):
    #     """get_user_dna"""
    #     return self.client.post("/phr-dna/apps/v1/dna-analyses", name="/dna-analyses", **kwargs)
    #
    # @task
    # def post_dna_kits_users_uid(self, uid, **kwargs):
    #     """post_dna_kits_users_uid"""
    #     return self.client.post("/phr-dna/apps/v1/dna-kits/users/{0}".format(uid)
    #                             , name="/dna-kits/users/{uid}", **kwargs)
    #
    # @task
    # def patch_dna_kits_users_uid(self, uid, **kwargs):
    #     """patch_dna_kits_users_uid"""
    #     return self.client.patch("/phr-dna/apps/v1/dna-kits/users/{0}".format(uid)
    #                              , name="/dna-kits/users/{uid}", **kwargs)
    #
    # @task
    # def post_messages_completed(self, **kwargs):
    #     """post_messages_completed"""
    #     return self.client.post("/phr-dna/apps/v1/messages/completed"
    #                             , name="/messages/completed", **kwargs)
    #
    # @task
    # def get_trait(self, **kwargs):
    #     """get_trait"""
    #     return self.client.get("/phr-dna/apps/v1/trait"
    #                            , name="/trait", **kwargs)
    #
    # @task
    # def post_trait_users_uid(self, uid, **kwargs):
    #     """post_trait_users_uid"""
    #     return self.client.post("/phr-dna/apps/v1/trait/users/{0}".format(uid)
    #                             , name="/trait/users/{uid}", **kwargs)


class MyLocust(RestUser):
    """locustClass"""
    tasks = [MyTaskSet]
    min_wait = 1000
    max_wait = 3000
    host = "https://api.hb.id-im.dev"
