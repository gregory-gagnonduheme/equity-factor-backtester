# Parameters - universe, dates, factor settings

# UPDATE BEFORE STARTING

# Universe
UNIVERSE = "S&P 500"
START_DATE = "2015-01-01"
END_DATE = "2024-12-31"

# Factor settings
MOMENTUM_LOOKBACK = 12   # months
MOMENTUM_SKIP = 1        # skip most recent month (standard)
VOLATILITY_WINDOW = 63   # trading days (~3 months)

# Backtest settings
REBALANCE_FREQ = "M"     # monthly
TOP_N_STOCKS = 20        # number of stocks held long
TRANSACTION_COST = 0.001 # 10bps per trade

# Paths
DATA_DIR = "data/raw/"
OUTPUT_DIR = "outputs/"