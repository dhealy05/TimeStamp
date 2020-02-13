<h2>Introducing TradeBot</h2>

Hello there 👋! Thanks for your interest in <strong>TradeBot</strong> by <strong>Dan Healy</strong>.

TradeBot is a two tiered system to
1. <strong>predict</strong> the direction Bitcoin prices will go in the future and
2. <strong>trade</strong> on those predictions for profit.

Since February 11, we've made predictions in <strong>real time</strong> every 15 minutes,
recorded and and <strong>time stamped</strong> the results. This repo has the time stamped files so
you can examine the results yourself.

The primary strategy has made a <strong>return of 176.25%</strong>,
a <strong>50% higher</strong> return than Bitcoin, with <strong>10% lower volatility.</strong>

If you're skeptical of these results--who doesn't make money in a bull market?--
we performed walk forward tests for Bitcoin and Ether for the year 2018,
when BTC lost 65% of its value and ETH lost 80% of its value.

<strong>The results</strong>: a 3% loss in BTC and an 11% gain in ETH.
That's a relative performance of <strong>277%</strong> and <strong>556%</strong> 🤑.

Detailed supplementary analysis is available in <strong>PredictingBitcoin.pdf</strong>,
<strong>Backtesting.pdf</strong>, and <strong>Volatility.pdf</strong>. Our technical
methods are described in <strong>TechnicalPresentation.pdf</strong>.

Finally, <strong>correlation.mp4</strong> shows the scatterplot of relative frequency of prediction
vs change in price, over 30 days. Take a look to see the <strong>direct relationship</strong>
between predictions and price change.

For a walk through the presentation, or questions about any of the above, email
me at <strong>daniel.healy05@gmail.com.</strong>

<h2>Usage:</h2>

To easily use this package, you will probably need to:

1. Install pipenv--pip install pipenv
2. pipenv shell
3. pipenv install pandas
4. pipenv install matplotlib

It may work by default if you have an existing python environment.

The basic suite of commands is in run.py. This includes simulating
all variants based on 1/0 buy/sell values, and plotting/animating the moving
average of the predictions.

Uncomment "adjust_arrays" in plot_moving_average.py in order to see the
predictions shifted to the right. This has been a useful way to visualize future
price change for the 10 day MA.

Note on the "translator" function in run: the original names for the
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
