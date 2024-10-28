import numpy as np
from numerical_integration import *
from matplotlib import pyplot as plt

from numerical_integration import visualization

def main():

    f = lambda x: np.sqrt(2 - x**2)

    integrator = NumericalIntegrator(f, 0, 1)

    exact_value = 1.2853981633974483

    n_values = [10, 20, 40, 80, 160, 320]

    results = integrator.compare_methods(n_values, exact_value)

    print("Результаты численного интегрирования:")
    print(f"Точное значение: {exact_value}\n")

    for n, n_results in zip(n_values, results):
        print(f"Количество разбиений: {n}")
        for result in n_results:
            print(f"{result.method_name}:")
            print(f"  Значение: {result.value:.10f}")
            print(f"  Ошибка: {result.error:.10f}")
        print()

    plt.rcParams.update({'font.size': 16})
    visualization.plot_errors(results)

    # x = np.linspace(0, 1, 1000)
    # y = f(x)

    # plt.plot(x, y, label=r"$f(x) = \sqrt{2 - x^2}$")
    # plt.xlabel("x")
    # plt.ylabel("f(x)")
    # plt.legend()
    # plt.grid(True)
    # plt.show()

if __name__ == "__main__":
    main()
