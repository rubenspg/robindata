class Transaction(object):
    def __init__(self, symbol, date, order_type, side, fees, quantity, average_price):
        super().__init__()
        self.symbol = symbol
        self.date = date
        self.order_type = order_type
        self.side = side
        self.fees = fees
        self.quantity = quantity
        self.average_price = average_price
