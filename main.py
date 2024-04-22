from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def user_create(self):
        payload = {
            "id": 726784601,
            "username": "tahacinar",
            "firstName": "Taha",
            "lastName": "Cinar",
            "email": "tahacinar@outlook.com.tr",
            "password": "72678460101",
            "phone": "5355353535",
             "userStatus": 1
            }
        self.client.post("v2/user", json=payload)

    @task
    def get_user_info(self):
        self.client.get("v2/user/tahacinar")

    @task
    def get_user_login(self):
        payload = {
            "username": "tahacinar",
            "password": "72678460101"
        }
        self.client.get("v2/user/login", params=payload)

    @task
    def get_user_logout(self):
        self.client.get("v2/user/logout")

    # @task
    # def delete_user(self):
    #     payload = {
    #         "id": 4367317471,
    #         "username": "TestBerke1234",
    #         "firstName": "Berkesdfsd",
    #         "lastName": "Yorulmazdsf",
    #         "email": "testberke2@test.com",
    #         "password": "123",
    #         "phone": "5437322831",
    #         "userStatus": 1
    #         }
    #     self.client.post("/v2/user", json=payload)
    #     self.client.delete("/v2/user/TestBerke1234")


    @task
    def put_user_update(self):
        payload = {
            "id": 72678460101,
            "username": "tahacinar",
            "firstName": "Taha",
            "lastName": "Cinar",
            "email": "tahacinar@outlook.com.tr",
            "password": "7267846010101",
            "phone": "535535353535",
            "userStatus": 1
        }
        self.client.put("v2/user/tahacinar", json=payload)