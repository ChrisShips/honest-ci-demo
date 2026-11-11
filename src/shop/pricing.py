"""What a basket costs, in integer cents.

Money is never a float here: 0.1 + 0.2 is not 0.3, and the cent a float loses
turns up months later as books that do not balance.
"""

from __future__ import annotations

#: Lines of this many items or more get BULK_PERCENT off.
BULK_FROM = 10
BULK_PERCENT = 5
#: Orders from this subtotal up ship free.
FREE_SHIPPING_FROM = 5000
SHIPPING_FEE = 495


def line_total(unit_price: int, quantity: int) -> int:
    """One line of the basket: ``quantity`` items at ``unit_price`` each."""

    total = unit_price * quantity
    if quantity >= BULK_FROM:
        return discounted(total, BULK_PERCENT)
    return total


def discounted(total: int, percent: int) -> int:
    """``total`` less ``percent`` percent, the discount rounded half up.

    Half a cent goes to the customer: a discount of 199.5 cents is 200.
    """

    if not 0 <= percent <= 100:
        raise ValueError("a discount is between 0 and 100 percent")
    return total - (total * percent + 50) // 100


def shipping(subtotal: int) -> int:
    """Shipping for an order of ``subtotal`` cents."""

    return 0 if subtotal >= FREE_SHIPPING_FROM else SHIPPING_FEE
