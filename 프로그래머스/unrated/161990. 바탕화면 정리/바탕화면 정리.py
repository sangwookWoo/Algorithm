def solution(wallpaper):
    x_list = []
    y_list = []
    for y, row in enumerate(wallpaper):
        for x, col in enumerate(row):
            if col == "#":
                x_list.append(x)
                y_list.append(y)
                
    return min(y_list), min(x_list), max(y_list) + 1, max(x_list) + 1
