from __future__ import annotations

import pytest

from shop.pricing import FREE_SHIPPING_FROM, SHIPPING_FEE, discounted, line_total, order_total, shipping


def test_a_line_costs_the_unit_price_times_the_quantity() -> None:
    assert line_total(1250, 3) == 3750


def test_a_line_without_items_is_refused() -> None:
    with pytest.raises(ValueError):
        line_total(1250, 0)


def test_half_a_cent_of_discount_goes_to_the_customer() -> None:
    # 10% of 19.95 is 199.5 cents.
    assert discounted(1995, 10) == 1795


def test_a_full_discount_leaves_nothing_to_pay() -> None:
    assert discounted(1995, 100) == 0


def test_shipping_is_charged_below_the_threshold() -> None:
    assert shipping(FREE_SHIPPING_FROM - 1) == SHIPPING_FEE


def test_shipping_is_free_from_the_threshold() -> None:
    assert shipping(FREE_SHIPPING_FROM) == 0


def test_an_order_pays_shipping_on_its_discounted_subtotal() -> None:
    # 52.00 less 10% is 46.80, under the free-shipping threshold again.
    assert order_total(5200, 10) == 4680 + SHIPPING_FEE


def test_an_order_over_the_threshold_ships_free() -> None:
    assert order_total(FREE_SHIPPING_FROM) == FREE_SHIPPING_FROM
