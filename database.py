#!/usr/bin/python3
import fdb
import datetime
import settings


def get_orders():
    SELECT_ORDERS = '\n'.join(open('sql/select_orders.sql', 'r').readlines())
    date_time = datetime.datetime.now().date()-datetime.timedelta(days=settings.MIN_DAYS)
    date_time = datetime.datetime(date_time.year, date_time.month, date_time.day, 7, 0)
    with fdb.connect(**settings.DB) as db:
        c = db.cursor()
        c.execute(SELECT_ORDERS, (settings.MAX_ORDERS, date_time))
        for order_id, order_startime in c.fetchall():
            yield order_id, order_startime
        c.close()


def remove_orders(orders):
    DELETE_ORDERS_H = '\n'.join(open('sql/delete_orders_h.sql', 'r').readlines())
    DELETE_ORDER_COORDS = '\n'.join(open('sql/delete_order_coords.sql', 'r').readlines())
    DELETE_ORDERS_STOPS = '\n'.join(open('sql/delete_orders_stops.sql', 'r').readlines())
    DELETE_ORDER = '\n'.join(open('sql/delete_order.sql', 'r').readlines())
    with fdb.connect(**settings.DB) as db:
        c = db.cursor()
        for oid in orders:
            print(f'deleting {oid}')
            c.execute(DELETE_ORDERS_H, (oid,))
            c.execute(DELETE_ORDER_COORDS, (oid,))
            c.execute(DELETE_ORDERS_STOPS, (oid,))
            c.execute(DELETE_ORDER, (oid,))
        c.close()
        db.commit()
