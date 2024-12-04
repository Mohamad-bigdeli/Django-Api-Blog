from locust import HttpUser, task, between


class QuickstartUser(HttpUser):

    def on_start(self):
        response = self.client.post(
            url="blog/api/v2/jwt/create/",
            data={
                "email": "admin@admin.com",
                "password": "Mhmdbigeli031@",
            },
        ).json()
        self.client.headers = {
            "Authorization": f"Bearer {response.get('access', None)}"
        }

    @task
    def post_list(self):
        self.client.get("blog/api/v1/posts/")

    @task
    def post_category(self):
        self.client.get("blog/api/v1/category/")
