# GEO1000 - Assignment 0
# Authors: Ming-Chieh Hu
# Studentnumbers:

def temp_windchill(temp_in_c, windspeed_in_kmh):
    return 13.12 + 0.6215*temp_in_c-11.37*windspeed_in_kmh + 0.3965*temp_in_c*windspeed_in_kmh

if __name__ == '__main__':
    print(temp_windchill(5.0, 10.0))
    print(temp_windchill(-1, 35))

