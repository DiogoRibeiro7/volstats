import pandas as pd

def realized_volatility(df: pd.DataFrame, returns_col: str = 'returns', window: int = 20, annualization_factor: int = 252) -> pd.Series: ...
