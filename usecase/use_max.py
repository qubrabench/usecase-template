from typing import Callable, Sequence

import numpy as np
import pytest
from qubrabench.algorithms.max import max
from qubrabench.benchmark import QueryStats, oracle, track_queries


def max_value_of_function(it: Sequence[float], f: Callable[[float], float]):
    return max(it, key=f, error=1e-5)


def test_use_max_quadratic():
    @oracle
    def f(x: float):
        return 4 * x - x**2

    N = 10000

    with track_queries() as tracker:
        domain = np.linspace(-10, 10, num=N)
        result = max_value_of_function(domain, f)
        assert result == pytest.approx(2, rel=1e-3)

        assert tracker.get_stats(f) == QueryStats(
            classical_actual_queries=N,
            classical_expected_queries=N,
            quantum_expected_classical_queries=0,
            quantum_expected_quantum_queries=pytest.approx(15610.0172),
        )
