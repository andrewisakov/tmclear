select first ? distinct oh.orderid, o.starttime
from orders_h oh
join orders o on (o.id=oh.orderid)
join order_states os on (os.id=o.state)
where (oh.statetime < ?) and (os.systemstate > 1)
order by oh.orderid
