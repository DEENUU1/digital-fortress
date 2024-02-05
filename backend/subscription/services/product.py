from subscription.repository.product import ProductRepository
from typing import List, Dict
from ..serializers import OutputProductSerializer
from subscription.repository.product_price import ProductPriceRepository
from ..models import ProductPrice, Product

class ProductService:

    def __init__(self, repository: ProductRepository):
        self._repository = repository

    def get_by_id(self, _id: int) -> Dict:
        product = self._repository.get_by_id(_id)
        serializer = OutputProductSerializer(product)
        return serializer.data

    def get_all(self) -> List[Dict]:
        products = self._repository.get_all()
        serializer = OutputProductSerializer(products, many=True)
        return serializer.data

    def create_free_product(self) -> Product:
        product_price_repository = ProductPriceRepository()
        print(1)
        prices = []
        for idx, currency in enumerate(ProductPrice.CURRENCIES):
            if not product_price_repository.price_exists(value=0, currency="PLN"):
                price = ProductPriceRepository().create(data={"value": 0, "currency": currency, "price_id": idx})
                prices.append(price)
            else:
                continue
        print(2)
        existing_product = self._repository.product_exists_by_name("Free")
        if not existing_product:
            product = self._repository.create({
                "name": "Free",
                "description": "This is a standard plan.",
                "max_project_storage": 300,
                "num_of_projects": 3,
                "is_active": True,
                "is_free": True
            })
            print(3)
        else:
            product = self._repository.get_by_name("Free")
        print(4)
        for x in prices:
            print(5)
            product.price.add(x)
            print(6)
        print(7)
        product.save()
        print(8)
        return product