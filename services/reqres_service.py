from services.base_service import BaseService
from utils.config import Config

class ReqResService(BaseService):
    def get_url(self):
        return self.get(f"{Config.reqres_base_url}/users?page=2")
    
    def create_user(self, name, job, base_headers):
        payload = {
            "name": name,
            "job": job
        }
        return self.post (f"{Config.reqres_base_url}/users", payload, base_headers)
    
    def update_user(self, user_id, name, job, base_headers):
        payload = {
            "name": name,
            "job": job 
        }
        return self.put (f"{Config.reqres_base_url}/users/{user_id}", payload, base_headers)
    
    def delete_user(self, user_id):
        return self.delete(f"{Config.reqres_base_url}/users/{user_id}")