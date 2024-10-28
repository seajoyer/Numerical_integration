import numpy as np
from typing import Callable
from .types import IntegrationResult

def rectangle_method_left(
    func: Callable[[float], float],
    a: float,
    b: float,
    n: int
) -> IntegrationResult:

    h = (b - a) / n
    x = np.linspace(a, b - h, n)

    integral = h * sum(func(x))

    return IntegrationResult(
        method_name="Rectangle method left",
        value=float(integral),
        step_size=h
    )

def rectangle_method_mid(
    func: Callable[[float], float],
    a: float,
    b: float,
    n: int
) -> IntegrationResult:

    h = (b - a) / n
    x = np.linspace(a + h/2, b - h/2, n)

    integral = h * sum(func(x))

    return IntegrationResult(
        method_name="Rectangle method mid",
        value=float(integral),
        step_size=h
    )

def rectangle_method_right(
    func: Callable[[float], float],
    a: float,
    b: float,
    n: int
) -> IntegrationResult:

    h = (b - a) / n
    x = np.linspace(a + h, b, n)

    integral = h * sum(func(x))

    return IntegrationResult(
        method_name="Rectangle method right",
        value=float(integral),
        step_size=h
    )

def trapezoidal_method(
    func: Callable[[float], float],
    a: float,
    b: float,
    n: int
) -> IntegrationResult:

    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    integral = h * (func(a) + func(b)) / 2.0
    integral += h * sum(func(x[1:-1]))

    return IntegrationResult(
        method_name="Trapezoidal method",
        value=float(integral),
        step_size=h
    )

def simpson_method(
    func: Callable[[float], float],
    a: float,
    b: float,
    n: int
) -> IntegrationResult:

    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's method")

    h = (b - a) / n
    x = np.linspace(a, b, n+1)

    integral = func(a) + func(b)
    integral += 4.0 * sum(func(x[1:-1:2]))
    integral += 2.0 * sum(func(x[2:-1:2]))
    integral *= h / 3.0

    return IntegrationResult(
        method_name="Simpson method",
        value=float(integral),
        step_size=h
    )
