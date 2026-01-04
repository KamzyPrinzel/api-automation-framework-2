from utils.config import Config
from services.base_service import BaseService

class PostService(BaseService):
    def get_post(self):
        return self.get(f"{Config.post_base_url}/posts")
    
    def get_single_post (self, post_id):
        return self.get(f"{Config.post_base_url}/posts/{post_id}")
    
    def create_post(self, title, body, post_id, headers):
        payload = {
            "title": title,
            "body": body,
            "post_id": post_id
        }
        return self.post(f"{Config.post_base_url}/posts", payload, headers)
    
    def update_post(self, title, post_id, headers):
        payload = {
            "title": title
        }
        return self.put(f"{Config.post_base_url}/posts/{post_id}", payload, headers)
    
    def delete_post(self, post_id):
        return self.delete(f"{Config.post_base_url}/posts/{post_id}")