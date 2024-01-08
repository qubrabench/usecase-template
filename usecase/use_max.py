from qubrabench.algorithms.max import max
from qubrabench.benchmark import track_queries, named_oracle


def max_value_of_function(it, f):
    with track_queries() as tracker:
        result = max(it, key=named_oracle("max_key")(f), error=1e-5)
        stats = tracker.get_stats("max_key")

    return result, stats
