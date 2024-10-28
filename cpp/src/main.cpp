#include "numerical_integration/integrators.hpp"
#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
#include <cmath>

const double EXACT_VALUE = 1.2853981633974483;

double func(double x) { return std::sqrt(2.0 - x * x); }

int main() {
    const double a = 0.0;
    const double b = 1.0;

    std::cout << "Exact value of the integral: " << EXACT_VALUE << std::endl;

    std::vector<int> grid_sizes;
    for (int n = 10; n <= 1000; n *= 2) {
        grid_sizes.push_back(n);
    }

    numerical_integration::calculate_errors(
        func, a, b, EXACT_VALUE, grid_sizes, "integration_errors.dat");

    std::system("gnuplot scripts/plot_errors.gnu");

    return 0;
}
