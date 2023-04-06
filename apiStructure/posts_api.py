from apiStructure.api_Utilities import APIUtilities


class Posts(APIUtilities):
    def __init__(self):
        super().__init__("posts")

    def get_all_posts(self):
        return self.send_request("GET", url=f"{self.url}")

    def get_a_post_by_id(self, post_id):
        return self.send_request("GET", url=f"{self.url}/{post_id}")

    def create_a_post(self, data):
        return self.send_request("POST", url=f"{self.url}", json=data)

    def update_a_post(self, post_id, data):
        return self.send_request("PUT", url=f"{self.url}/{post_id}", json=data)

    def partially_update_a_post(self, post_id, data):
        return self.send_request("PATCH", url=f"{self.url}/{post_id}", json=data)

    def delete_a_post(self, post_id):
        return self.send_request("DELETE", url=f"{self.url}/{post_id}")
