class InventoryAllocator:
    def allocate(self, order, distribution):
        """
        :param order: a dictionary of items and amount to order, e.g. {apple: 5, banana: 5, orange: 5}
        :param distribution: a list of dictionary objects of warehouse and its inventory,
        e.g. [{ name: owd, inventory: { apple: 5, orange: 10 } }, { name: dm, inventory: { banana: 5, orange: 10 } } ]
        :return: shipment: a list of dictionary objects of warehouse and respective shipment,
        e.g. [{owd: {apple: 5, orange:5}}, {dm: {banana:5}}]

        This function allocates cheapest shipment given order and inventory distribution
        """
        shipment = []
        current_index = 0
        items = list(order.keys())
        while items and current_index < len(distribution):
            current_warehouse = distribution[current_index]
            current_shipment = {}
            for item in items:
                if item in current_warehouse['inventory'] and current_warehouse['inventory'][item]:
                    current_shipment[item] = min(order[item], current_warehouse['inventory'][item])
                    order[item] -= current_shipment[item]
            items[:] = [item for item in items if order[item] > 0]
            if current_shipment:
                shipment.append({current_warehouse['name']: current_shipment})
            current_index += 1
        if items:
            # if order is not completely filled, return empty list
            shipment = []
        return shipment
