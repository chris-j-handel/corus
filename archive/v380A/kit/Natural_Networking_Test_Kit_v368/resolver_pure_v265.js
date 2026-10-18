// Pure port of Exhibit_ONE_Natural_Resolver_v241.py to dynamically-typed,
// JIT-compiled JavaScript. Names follow the reference. The sign-count is a
// Map keyed by `sequencing`, growing only for positions actually sounded, as
// the reference dict does. Increment is only +/-1; only the sign surfaces.
// No fixed range, no bound, no accumulation the reference does not carry.

function biCoupling(commencing_co_agency, accepted_bi_morality) {
  // offering = {sequencing: competency}
  const offering = new Map();
  for (const [sequencing, morality, competency, re_attentioning] of commencing_co_agency)
    offering.set(sequencing, competency);

  // bi_inversioning: accepted nonzero morality as-is; carry morality sign-inverted
  const bi_inversioning = [];
  for (const [sequencing, morality] of accepted_bi_morality)
    if (morality !== 0) bi_inversioning.push([sequencing, morality]);
  for (const [sequencing, morality] of commencing_co_agency) {
    if (morality > 0) bi_inversioning.push([sequencing, -1]);
    if (morality < 0) bi_inversioning.push([sequencing, 1]);
  }

  // bi_moral_attentioning: sparse sign-count, only +/-1
  const bi_moral_attentioning = new Map();
  for (const [sequencing, morality] of bi_inversioning) {
    if (morality > 0) bi_moral_attentioning.set(sequencing, (bi_moral_attentioning.get(sequencing) || 0) + 1);
    if (morality < 0) bi_moral_attentioning.set(sequencing, (bi_moral_attentioning.get(sequencing) || 0) - 1);
  }

  // bi_moral_sequencing: surface over the position-count, sign only
  const bi_moral_sequencing = [];
  for (const [sequencing, t] of bi_moral_attentioning) {
    bi_moral_sequencing.push([sequencing, t > 0 ? 1 : (t < 0 ? -1 : 0)]);
  }

  // re_commencing_co_agency: persist within the attentioning bound
  const re_commencing_co_agency = new Map();
  for (const [sequencing, morality, competency, re_attentioning] of commencing_co_agency) {
    const r2 = re_attentioning + 1;
    if (r2 <= 3 || (r2 === 4 && competency > 0))
      re_commencing_co_agency.set(sequencing, [morality, competency, r2]);
  }
  for (const [sequencing, morality] of bi_moral_sequencing) {
    if (morality !== 0)
      re_commencing_co_agency.set(sequencing, [morality, 0 - (offering.has(sequencing) ? offering.get(sequencing) : 1), 0]);
  }

  const carries = [...re_commencing_co_agency.keys()].sort((a, b) => a - b)
    .map(sequencing => [sequencing, ...re_commencing_co_agency.get(sequencing)]);

  return [bi_moral_sequencing, carries];
}

module.exports = { biCoupling };
