def nearest_water_station(N):
    quotient, remainder = divmod(N, 5)
    if remainder > 2.5:
        quotient += 1
    return quotient * 5

print(nearest_water_station(int(input())))