frequencies = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

def coupling(carry, tasting, frequency, thickness):
    thinning = (1 / ((1 + 5**0.5) / 2)) ** thickness
    reach = 1 / ((1 + 5**0.5) / 2) ** 3
    # carry opening
    carry = [(position, sign, reaching * thinning) for position, sign, reaching in carry if reaching * thinning >= reach]
    # tasting
    arriving = list(tasting(frequency))
    # inverting
    for position, sign, reaching in carry:
        position_at_sway = position % frequency
        if sign > 0: arriving.append((position_at_sway, -1))
        elif sign < 0: arriving.append((position_at_sway, 1))
    # swaying
    sway = {}
    for position, sign in arriving:
        if sign > 0: sway[position] = sway.get(position, 0) + 1
        if sign < 0: sway[position] = sway.get(position, 0) - 1
    # surfacing
    span = max((position for position, sign in arriving), default=-1) + 1
    surface = [
        (position, 1 if sway.get(position, 0) > 0 else (-1 if sway.get(position, 0) < 0 else 0))
        for position in range(span)
    ] if span > 0 else []
    # carry closing
    recoiling = {}
    for position, sign, reaching in [(position, sign, reaching * thinning) for position, sign, reaching in carry if reaching * thinning >= reach]:
        recoiling[position] = (sign, reaching)
    for position, sign in surface:
        if sign != 0: recoiling[position] = (sign, 1.0)
    return surface, [(position, sign, reaching) for position, (sign, reaching) in sorted(recoiling.items())]

def interleaving(tasting):
    forward = []
    backward = []
    rebounding = []
    for substrate_index in range(16):
        lower_frequency = frequencies[substrate_index]
        upper_frequency = frequencies[substrate_index + 1]
        thickness = upper_frequency - lower_frequency
        # forward carry traveling
        surface, forward = coupling(forward, tasting, lower_frequency, thickness)
        rebounding.append(surface)
        # backward carry attending
        for attending_step in range(thickness):
            attending_surface, backward = coupling(backward, tasting, upper_frequency, 1)
        # backward carry traveling
        surface, backward = coupling(backward, tasting, upper_frequency, thickness)
        rebounding.append(surface)
        # forward carry attending
        for attending_step in range(thickness):
            attending_surface, forward = coupling(forward, tasting, lower_frequency, 1)
    return rebounding
