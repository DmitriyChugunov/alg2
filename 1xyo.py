def shortest_distance(s):
    x_positions = [i for i, char in enumerate(s) if char == 'X']
    y_positions = [i for i, char in enumerate(s) if char == 'Y']

    if not x_positions or not y_positions:
        return 0

    min_distance = float('inf')

    for x in x_positions:
        for y in y_positions:
            distance = abs(x - y) - 1
            if distance < min_distance:
                min_distance = distance

    return min_distance
input_string = "XggggXooOXggggY"
result = shortest_distance(input_string)
print("Кратчайшее расстояние между X и Y:", result)