#pragma once
#include <vector>
#include <string>
#include <fstream>
#include <functional>

namespace numerical_integration {

inline double rectangle_method(std::function<double(double)> f,
                                  double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.0;

    for (int i = 0; i < n; ++i) {
        double x = a + i * h;
        sum += f(x);
    }

    return h * sum;
}

inline double trapezoid_method(std::function<double(double)> f,
                                  double a, double b, int n) {
    double h = (b - a) / n;
    double sum = (f(a) + f(b)) / 2.0;

    for (int i = 1; i < n; ++i) {
        double x = a + i * h;
        sum += f(x);
    }

    return h * sum;
}

inline double simpson_method(std::function<double(double)> f,
                                double a, double b, int n) {
    if (n % 2 != 0) n++; // Ensure n is even
    double h = (b - a) / n;
    double sum = f(a) + f(b);

    for (int i = 1; i < n; ++i) {
        double x = a + i * h;
        sum += f(x) * (i % 2 == 0 ? 2.0 : 4.0);
    }

    return h * sum / 3.0;
}

inline void calculate_errors(std::function<double(double)> f,
                                double a, double b,
                                double exact_value,
                                const std::vector<int>& grid_sizes,
                                const std::string& output_file) {
    std::ofstream out(output_file);
    out.precision(15);

    out << "n h rectangle_error trapezoid_error simpson_error\n";

    for (int n : grid_sizes) {
        double h = (b - a) / n;

        double rect_error = std::abs(rectangle_method(f, a, b, n) - exact_value);
        double trap_error = std::abs(trapezoid_method(f, a, b, n) - exact_value);
        double simp_error = std::abs(simpson_method(f, a, b, n) - exact_value);

        out << n << " "
            << h << " "
            << rect_error << " "
            << trap_error << " "
            << simp_error << "\n";
    }
}

}
