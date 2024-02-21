class Review:
    def __init__(self, product_id: int, review: dict):
        self._product_id = product_id
        self._customer_name = review["customer_name"]
        self._comment = review["comment"]
        self. rate = review["rate"]

    