class Item:
    _price: float # Price in dollars

    def __init__(self, price: float) -> None:
        self._price = price

    def get_price(self) -> float:
        return self._price

    def print(self) -> None:
        print(f'    Price: ${self._price:.2f}')
