from typing import Callable, List, Optional

from .types import IntegrationResult
from .methods import rectangle_method_left, rectangle_method_mid, rectangle_method_right, trapezoidal_method, simpson_method

class NumericalIntegrator:
    def __init__(self, func: Callable[[float], float], a: float, b: float):
        self.func = func
        self.a = a
        self.b = b

    def integrate(
        self,
        method: str,
        n: int,
        exact_value: Optional[float] = None
    ) -> IntegrationResult:

        methods = {
            'left rectangle':  rectangle_method_left,
            'mid rectangle':   rectangle_method_mid,
            'right rectangle': rectangle_method_right,
            'trapezoidal':     trapezoidal_method,
            'simpson':         simpson_method
        }

        if method not in methods:
            raise ValueError(f"Unknown method: {method}")

        result = methods[method](self.func, self.a, self.b, n)

        if exact_value is not None:
            result.error = abs(result.value - exact_value)

        return result

    def compare_methods(
        self,
        n_values: List[int],
        exact_value: Optional[float] = None
    ) -> List[List[IntegrationResult]]:

        results = []

        for n in n_values:
            n_results = []
            methods = ['left rectangle', 'mid rectangle', 'right rectangle', 'trapezoidal']

            # Add Simpson's method only for even n
            if n % 2 == 0:
                methods.append('simpson')

            for method in methods:
                result = self.integrate(method, n, exact_value)
                n_results.append(result)

            results.append(n_results)

        return results
