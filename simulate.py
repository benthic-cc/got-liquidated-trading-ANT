"""Replay a fictional, isolated long position in the terminal."""

import argparse
import re
from decimal import Decimal


ENTRY_PRICE = Decimal("100.00")
INITIAL_MARGIN = Decimal("100.00")
MAINTENANCE_RATE = Decimal("0.005")
DEFAULT_PRICES = tuple(map(Decimal, ("103", "101", "97", "94", "90.40", "88")))


def parse_price(value):
    if not re.fullmatch(r"[0-9]{1,9}(?:\.[0-9]{1,2})?", value):
        raise argparse.ArgumentTypeError("use a positive price with up to two decimals")
    price = Decimal(value)
    if price <= 0:
        raise argparse.ArgumentTypeError("price must be greater than zero")
    return price


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prices", nargs="*", type=parse_price, help="prices after entry")
    parser.add_argument("--leverage", type=int, default=10, help="1 to 100 (default: 10)")
    args = parser.parse_args()
    if not 1 <= args.leverage <= 100:
        parser.error("--leverage must be between 1 and 100")

    prices = args.prices or DEFAULT_PRICES
    size = INITIAL_MARGIN * args.leverage / ENTRY_PRICE

    print(f"ANT paper desk | LONG {size:g} units @ {ENTRY_PRICE:.2f} | {args.leverage}x")
    print(f"{'Tick':>4} {'Price':>14} {'Equity':>17} {'Maintenance':>17}  Status")

    for tick, price in enumerate((ENTRY_PRICE, *prices)):
        equity = INITIAL_MARGIN + size * (price - ENTRY_PRICE)
        maintenance = size * price * MAINTENANCE_RATE
        liquidated = equity <= maintenance
        status = "LIQUIDATED" if liquidated else "OPEN"
        print(f"{tick:>4} {price:>14.2f} {equity:>17.2f} {maintenance:>17.2f}  {status}")
        if liquidated:
            print('\nClaude: "There is something on the right side of the chart now."')
            return

    print('\nClaude: "The position is still open. So is the question."')


if __name__ == "__main__":
    main()
