from app.crud.base import CRUDBase
from app.models.product import Product


class CRUDProduct(CRUDBase[Product]):
    pass


product_crud = CRUDProduct(Product)