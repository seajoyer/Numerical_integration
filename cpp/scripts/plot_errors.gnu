set terminal pngcairo enhanced font 'Arial,12' size 800,600
set output 'error_comparison.png'

set xlabel 'Шаг h'
set ylabel 'Ошибка'
set logscale xy
set grid

set key right bottom

plot [:0.15] 'integration_errors.dat' using 2:3 with linespoints title 'Rectangle Method Left', \
             'integration_errors.dat' using 2:4 with linespoints title 'Rectangle Method Mid', \
             'integration_errors.dat' using 2:5 with linespoints title 'Rectangle Method Right', \
             'integration_errors.dat' using 2:6 with linespoints title 'Trapezoid Method', \
             'integration_errors.dat' using 2:7 with linespoints title 'Simpson Method',
