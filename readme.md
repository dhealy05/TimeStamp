<h2>Introducing TradeBot</h2>

Hello there 👋! Thanks for your interest in <strong>TradeBot</strong> by Dan Healy. There’s a lot of information here; I’ll walk you through it.

TradeBot is a two tiered system to 1. <strong>predict</strong> the direction Bitcoin prices will go
in the future and 2. <strong>trade</strong> on those predictions for profit.

Since February 11, we've made predictions in real time every 15 minutes,
recorded and and <strong>time stamped</strong> the results. This repo has the time stamped files so
you can examine the results yourself.

Predictions made in that time consistently anticipate price.
You can animate the change in price vs the change in predictions using the
"animate_ma" command in run_commands.py.

Results and data analysis are described in <strong>PredictingBitcoin.pdf</strong>. Highlights:
the highest performing strategy variant made a <strong>return of 162% </strong> 📈, outperforming Bitcoin.

If you're interested in volatility, look at <strong>Volatility.pdf</strong> for a follow up. Highlights: Average relative performance divided by average relative standard deviation is
1.15, implying a </strong>15% higher</strong> return per volatility.

If you're skeptical of these results--who doesn't make money in a bull market?--
read </strong>Backtesting.pdf</strong>, which shows the simulated results for 2018.
Highlights: a forward walk based on the full set of predictions yielded a 3% loss in BTC/USD
and an 11% gain in ETH/USD, in contrast to a market loss of 65% and 80%. That's
a relative performance of <strong>277</strong> and <strong>556</strong> 🤑.
A hindsight best path for the same predictions would have gained 68% and 56%
respectively--but hindsight is 20/20 🤓.

Finally, to get a feel for how we came to this data--our methodology--read
<strong>TechnicalPresentation.pdf</strong>. It has a more in depth look at the techniques
we use to predict and analyze the data.

For a walk through the presentation, or questions about any of the above, email
me at <strong>daniel.healy05@gmail.com.</strong>

<h2>Usage:</h2>

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
