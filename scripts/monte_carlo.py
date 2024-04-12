# Monte Carlo Pi's calculation method is quite simple
# and consists of several easy steps:
# 1. Generate random points within a unit square.
# 2. Calculate the distance from the origin to each point.
# 3. Count the number of points that lie inside the quarter of the unit circle.
# 4. Estimate Pi as 4 times the ratio of
# the number of points inside the circle to the total number of points.
# This is because the area of the circle with the radius R is pi*R^2,
# whereas the area of the square with the side 2R is 4R^2:
# the square is inscribed circle of the square.
# The ratio of the areas is pi/4,
# so the ratio of the number of points inside the circle
# to the total number of points is pi/4, and Pi is 4 times this ratio.
# The more points we generate, the more accurate the estimation will be.
