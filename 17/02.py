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

def oobounds(pos, xlim, ylim):
    if pos[0] > xlim[1]:
        return True
    elif pos[1] < ylim[0]:
        return True
    else:
        return False

xlim = (207,263)
ylim = (-115,-63)
# xlim = (20,30)
# ylim = (-10,-5)
max_iter = 300
max_y = 0
max_velocity = 0
valid_velocities = []



for velocity in [(i, j) for i in range(300) for j in range(-115,120)]:
    position = (0, 0)
    out_of_bounds = False
    hit_pos = False
    init_vlct = velocity
    while not hit_pos and not out_of_bounds:
        position, velocity = shoot(position, velocity)
        hit_pos = hit(position, xlim, ylim)
        if hit_pos == True:
            valid_velocities.append(init_vlct)
        out_of_bounds = oobounds(position, xlim, ylim)

print(len(valid_velocities))