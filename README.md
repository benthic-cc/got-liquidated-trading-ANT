# Got Liquidated Trading ANT

A fictional paper trading log featuring Claude from Anthropic.

| Time | Log |
| --- | --- |
| 09:30 | I sent Claude a price chart and asked whether it would go up or down. |
| 09:31 | Claude said the right side of the chart was blank. |
| 09:32 | I took that to mean there was room to go up. |
| 09:36 | My paper position got liquidated. |
| 09:37 | I sent the chart back. Claude said, "There is something on the right side of the chart now." |

## After-hours debrief

**Me** — I followed the plan.

**Claude** — What was the plan?

**Me** — Open the position first. Come up with a plan later.

Claude checked the box under “Execution.” The box to its right, “Trading Plan,” was still blank.

## Replay the liquidation

Run either command from the repository root with Python 3. The simulator uses only the standard library.

```sh
python simulate.py
python simulate.py --leverage 2 103 97 90.40 88
```

By default, the simulator opens a long position at 100.00 with 100.00 in initial margin and 10× leverage. At each price, it updates the account equity and maintenance margin. When equity falls to or below the maintenance margin, the script prints `LIQUIDATED` and stops the replay.

The second command replays a custom price sequence at 2× leverage. Replace the prices after `--leverage 2` with your own, or run `python simulate.py --help` for the available options. The model uses a fixed maintenance margin rate of 0.5% and ignores fees and slippage.
