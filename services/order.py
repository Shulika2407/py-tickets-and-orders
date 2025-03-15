from django.db import transaction
from django.db.models import QuerySet
from db.models import Ticket, Order


def create_order(tickets: list[Ticket], date=None):
    if date:
        with transaction.atomic():
            order = Order.objects.filter(created_at=data).create()
            for ticket in tickets:
                Ticket.objects.create(order=order, **ticket)
            return order


def get_orders(username: str=None) -> QuerySet:
    if username:
        orders = Order.objects.filter(user__username=username)
        return orders
    else:
        orders = Order.objects.all()
        return orders
