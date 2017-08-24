#!/usr/bin/python3
import database

if __name__ == '__main__':
    n = 0
    orders = []
    for order_id, order_startime in database.get_orders():
        # print(order_id, order_startime)
        n += 1
        orders.append(int(order_id))

    database.remove_orders(orders)
