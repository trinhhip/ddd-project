class OrderAction:
    def __init__(self, repository, order_id) -> None:
        self.repository = repository
        self.order_id = order_id
        
    def __call__(self, order_id):
        # Load order by id, set status order to state order
        order = self.repository.get_order_by_id(order_id)
        order.status = 1
        return self.repository.save(order)