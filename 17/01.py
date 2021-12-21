def shoot(start, vlct):
    pos = (start[0] + vlct[0], start[1] + vlct[1])
    if vlct[0] > 0:
        vel_updated = (vlct[0] - 1, vlct[1] - 1)
    elif vlct[0] < 0:
        vel_updated = (vlct[0] + 1, vlct[1] - 1)
    else:
        vel_updated = (0, vlct[1] - 1)
    return pos, vel_updated


def hit(pos, xlim, ylim):
    if pos[0] >= xlim[0] and pos[0] <= xlim[1] and pos[1] >= ylim[0] and pos[1] <= ylim[1]:
        return True
    else:
        return False


# x_min = 207
# x_max = 263
# y_min = -115
# ymax = -63
xlim = (207,263)
ylim = (-115,-63)
# xlim = (20,30)
# ylim = (-10,-5)
max_iter = 300
max_y = 0
max_velocity = 0
valid_velocities = []



for velocity in [(i, j) for i in range(264) for j in range(115)]:
    position = (0, 0)
    counter = 0
    reached_max_iter = False
    hit_pos = False
    init_vlct = velocity
    curr_max_y = 0
    while not hit_pos and not reached_max_iter:
        position, velocity = shoot(position, velocity)
        if position[1] > curr_max_y:
            curr_max_y = position[1]
        hit_pos = hit(position, xlim, ylim)
        if hit_pos == True and curr_max_y > max_y:
            max_y = curr_max_y
            max_velocity = init_vlct
        counter += 1
        if counter >= max_iter:
            reached_max_iter = True

print(max_velocity)
print(max_y)