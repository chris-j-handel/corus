def bi_coupling(commencing_co_agency, accepted_bi_morality, bi_attentioning):
    offering = {sequencing: competency
                for sequencing, morality, competency, re_attentioning in commencing_co_agency}
    bi_inversioning = [(sequencing, morality)
                       for sequencing, morality in accepted_bi_morality if morality != 0]
    for sequencing, morality, competency, re_attentioning in commencing_co_agency:
        if morality > 0:
            bi_inversioning.append((sequencing, -1))
        if morality < 0:
            bi_inversioning.append((sequencing, 1))
    bi_moral_attentioning = {}
    for sequencing, morality in bi_inversioning:
        if morality > 0:
            bi_moral_attentioning[sequencing] = bi_moral_attentioning.get(sequencing, 0) + 1
        if morality < 0:
            bi_moral_attentioning[sequencing] = bi_moral_attentioning.get(sequencing, 0) - 1
    bi_moral_sequencing = [
        (sequencing, 1 if bi_moral_attentioning.get(sequencing, 0) > 0
            else (-1 if bi_moral_attentioning.get(sequencing, 0) < 0 else 0))
        for sequencing in range(bi_attentioning)
    ]
    re_commencing_co_agency = {}
    for sequencing, morality, competency, re_attentioning in commencing_co_agency:
        if re_attentioning + 1 <= 3 or (re_attentioning + 1 == 4 and competency > 0):
            re_commencing_co_agency[sequencing] = (morality, competency, re_attentioning + 1)
    for sequencing, morality in bi_moral_sequencing:
        if morality != 0:
            re_commencing_co_agency[sequencing] = (morality, 0 - offering.get(sequencing, 1), 0)
    return (
        bi_moral_sequencing,
        [(sequencing, morality, competency, re_attentioning)
         for sequencing, (morality, competency, re_attentioning)
         in sorted(re_commencing_co_agency.items())],
    )