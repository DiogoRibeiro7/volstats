import numpy as np
import pandas as pd

def two_scale_realized_volatility(returns: np.ndarray | pd.Series, K: int = 2) -> float: ...
def tsrv_series(df: pd.DataFrame, price_column: str, time_column: str, freq: str = '1D', K: int = 2) -> pd.Series: ...
