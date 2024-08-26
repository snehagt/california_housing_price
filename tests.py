# Error - 1

# Column Names:
# ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 
# 'population', 'households', 'median_income', 'median_house_value', 'ocean_proximity']
# C:\Users\sneha.gupta\Crash_course\california_housing_price\analysis.py:149: RuntimeWarning:
#  invalid value encountered in cast
#   col_data = col_data.astype(int)
# Traceback (most recent call last):
#   File "C:\Users\sneha.gupta\Crash_course\california_housing_price\main.py", line 185, in <module>
#     main()
#   File "C:\Users\sneha.gupta\Crash_course\california_housing_price\main.py", line 55, in main
#     analysis.calculate_statistics(data, column_names)
#   File "C:\Users\sneha.gupta\Crash_course\california_housing_price\analysis.py", line 150,
#  in calculate_statistics
#     mode_values[i] = np.argmax(np.bincount(col_data))
#   File "<__array_function__ internals>", line 200, in bincount
# ValueError: 'list' argument must have no negative elements

#Resolution: You have to remove missing values before calculation of general statistics, since mean
# does not take missing values.