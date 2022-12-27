class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_order_set = set()
        table_orders = {}
        for name, table, order in orders:
            if table not in table_orders: table_orders[table] = {}
            if order not in table_orders[table]:
                table_orders[table][order] = 0
            table_orders[table][order] += 1
            if order not in food_order_set: food_order_set.add(order)

        food_order_list = sorted(list(food_order_set))
        result = []
        result.append(["Table"] + food_order_list)

        for table_key in sorted([int(key) for key in table_orders.keys()]):
            table = str(table_key)
            order_counts = [str(table)]
            orders_for_table = table_orders[table]
            for food_order in food_order_list:
                if food_order in orders_for_table:
                    order_counts.append(str(orders_for_table[food_order]))
                else:
                    order_counts.append(str(0))
            result.append(order_counts)
        return result
