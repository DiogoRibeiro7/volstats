import pandas as pd
from volatilitystats.utils.confidence import compute_confidence_bands as compute_confidence_bands

def component_garch_log_likelihood(params, returns): ...
def estimate_component_garch_params(returns: pd.Series, with_confidence: bool = False, stderr_fraction: float = 0.1) -> dict: ...
