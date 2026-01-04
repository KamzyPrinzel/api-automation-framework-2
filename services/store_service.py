from services.base_service import BaseService
from utils.config import Config

class StoreService(BaseService):
    def get_all_products(self):
        return self.get(f"{Config.store_base_url}/products")
    
    def get_single_products(self, product_id):
        return self.get(f"{Config.store_base_url}/{product_id}")