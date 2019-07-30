Results:

Predictions made in real time over 6 months consistently anticipate
price. You can recreate those results with the OpenTimeStamps files included
here and the scripts in this repo.

A set of 32 trading strategies based on those predictions underperformed Bitcoin
overall, but some have started to outperform as the sample size has increased.

Average relative performance divided by average relative standard deviation is
1.15, implying a 15% higher return per volatility.

In backtesting, from 12/1/17 to 1/1/19, a forward walk based on relative frequency
search for the full set of predictions yielded a 3% loss in BTC/USD and an 11%
gain in ETH/USD, in contrast to a market loss of 65% and 80% for BTC and ETH
respectively. Backtesting raw data is not included in this repo.

For a detailed description of results in production, read "PredictingBitcoin.pdf".
As a followup, for volatility metrics, read "Volatility.pdf".

For a detailed description of backtesting results, read "Backtesting.pdf"

For a detailed description of technical methods, read "TechnicalPresentation.pdf".

Usage:

To easily use this package, you will probably need to:
1. Install pipenv--pip install pipenv
2. pipenv shell
3. pipenv install pandas
4. pipenv install matplotlib

It may work by default if you have an existing python environment.

The basic suite of commands is in run_commands.py. This includes simulating
all variants based on 1/0 buy/sell values, and plotting/animating the moving
average of the predictions.

Uncomment "adjust_arrays" in plot_moving_average.py in order to see the
predictions shifted to the right. This has been a useful way to visualize future
price change for the 10 day MA.

Note on the "translator" function in run_commands: the original names for the
strategy variants are confusing and don't match those used in the write up,
which are superior. So, the translator functions translate the time stamped
file names into the more understandable and accurate ones used in the paper.

All OTS files/zips containing predictions are in /stamps; the unzipped CSVs are
in /variants, for your convenience.

Stamp Erratum:
For June 3, there is no timestamp;
June 21 has a stamp that is improperly named as June 22;
and June 22 is stamped around 12 hours later than it should be.
All others are stamped at 11:55 PM UTC the night of the date they are named for.
