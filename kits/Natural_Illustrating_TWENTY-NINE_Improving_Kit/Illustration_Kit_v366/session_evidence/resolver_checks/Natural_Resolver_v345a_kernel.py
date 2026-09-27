def co_bi_coupling(co_carrying, bi_arriving):
    bi_co_bi_transmissioning = {
        bi_offering: bi_co_bi_co_bi_torusing
        for bi_offering, co_bi_co_bi_co_corusing, bi_co_bi_co_bi_torusing, bi_co_inseparating
        in co_carrying}
    bi_co_inversioning = [
        (bi_offering, co_bi_co_bi_co_corusing)
        for bi_offering, co_bi_co_bi_co_corusing in bi_arriving
        if co_bi_co_bi_co_corusing != 0]
    for bi_offering, co_bi_co_bi_co_corusing, bi_co_bi_co_bi_torusing, bi_co_inseparating in co_carrying:
        if co_bi_co_bi_co_corusing > 0:
            bi_co_inversioning.append((bi_offering, -1))
        if co_bi_co_bi_co_corusing < 0:
            bi_co_inversioning.append((bi_offering, 1))
    bi_co_tunneling = {}
    for bi_offering, co_bi_co_bi_co_corusing in bi_co_inversioning:
        if co_bi_co_bi_co_corusing > 0:
            bi_co_tunneling[bi_offering] = bi_co_tunneling.get(bi_offering, 0) + 1
        if co_bi_co_bi_co_corusing < 0:
            bi_co_tunneling[bi_offering] = bi_co_tunneling.get(bi_offering, 0) - 1
    bi_co_surfacing = [
        (bi_offering, 1 if bi_co_tunneling[bi_offering] > 0
            else (-1 if bi_co_tunneling[bi_offering] < 0 else 0))
        for bi_offering in bi_co_tunneling]
    co_bi_carrying = {}
    for bi_offering, co_bi_co_bi_co_corusing, bi_co_bi_co_bi_torusing, bi_co_inseparating in co_carrying:
        if bi_co_inseparating + 1 <= 3 or (bi_co_inseparating + 1 == 4 and bi_co_bi_co_bi_torusing > 0):
            co_bi_carrying[bi_offering] = (
                co_bi_co_bi_co_corusing, bi_co_bi_co_bi_torusing, bi_co_inseparating + 1)
    for bi_offering, co_bi_co_bi_co_corusing in bi_co_surfacing:
        if co_bi_co_bi_co_corusing != 0:
            co_bi_carrying[bi_offering] = (
                co_bi_co_bi_co_corusing, 0 - bi_co_bi_transmissioning.get(bi_offering, 1), 0)
    return (
        bi_co_surfacing,
        [(bi_offering, co_bi_co_bi_co_corusing, bi_co_bi_co_bi_torusing, bi_co_inseparating)
         for bi_offering, (co_bi_co_bi_co_corusing, bi_co_bi_co_bi_torusing, bi_co_inseparating)
         in co_bi_carrying.items()])
