from apiStructure.api_Utilities import APIUtilities


class Comments(APIUtilities):

    def __init__(self):
        super().__init__("comments")

    def get_all_comments(self):
        return self.send_request("GET", url=f"{self.url}")

    def get_a_comment_by_id(self, commentId):
        return self.send_request("GET", url=f"{self.url}/{commentId}")

    def create_a_comment(self, payload):
        return self.send_request("POST", url=f"{self.url}", json=payload)

    def update_a_comment(self, commentId, payload):
        return self.send_request("PUT", url=f"{self.url}/{commentId}", json=payload)

    def partially_update_a_comment(self, commentId, payload):
        return self.send_request("PATCH", url=f"{self.url}/{commentId}", json=payload)

    def delete_a_comment(self, commentId):
        return self.send_request("DELETE", url=f"{self.url}/{commentId}")


