from typing import List
import matplotlib.pyplot as plt
from .types import IntegrationResult

def plot_errors(results: List[List[IntegrationResult]], save_path: str = None):

    if not results[0][0].error:
        raise ValueError(
            "Errors not computed. Exact value must be provided when comparing methods."
        )

    plt.figure(figsize=(10, 6))

    method_names = set(result.method_name for results_n in results for result in results_n)

    for method_name in method_names:
        method_results = [
            result for results_n in results
            for result in results_n
            if result.method_name == method_name
        ]

        steps = [result.step_size for result in method_results]
        errors = [result.error for result in method_results]

        plt.loglog(steps, errors, 'o-', label=method_name)

    plt.grid(False)
    plt.xlabel('Шаг h (log)')
    plt.ylabel('Абсолютная ошибка (log)')
    plt.legend()

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

    plt.close()
