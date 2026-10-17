/* Pure port of Exhibit_ONE_Natural_Resolver_v241.py to statically-typed,
   compiled C. Faithful to the reference's purity: no range, no bound,
   no preallocated ceiling, no ranged zeroing. The sign-count is a sparse
   association keyed by `sequencing`, grown only for positions actually
   sounded, exactly as the reference dict grows. Increment is only +/-1;
   only the sign surfaces. Names follow the reference. */

#include <stdlib.h>

typedef struct { int sequencing, morality, competency, re_attentioning; } carry_t;
typedef struct { int sequencing, morality; } face_t;

/* A sparse association from `sequencing` to an int value, growing as needed.
   This is the C rendering of the reference dict: it holds only positions
   actually placed into it, and grows without any fixed ceiling. */
typedef struct { int *sequencing; int *value; int count, cap; } assoc_t;

static void assoc_init(assoc_t *a) { a->sequencing = NULL; a->value = NULL; a->count = 0; a->cap = 0; }
static void assoc_free(assoc_t *a) { free(a->sequencing); free(a->value); }
static int  assoc_find(const assoc_t *a, int seq) {
    for (int i = 0; i < a->count; i++) if (a->sequencing[i] == seq) return i;
    return -1;
}
static void assoc_grow(assoc_t *a) {
    int ncap = a->cap ? a->cap * 2 : 4;
    a->sequencing = (int *)realloc(a->sequencing, (size_t)ncap * sizeof(int));
    a->value      = (int *)realloc(a->value,      (size_t)ncap * sizeof(int));
    a->cap = ncap;
}
/* get with default, exactly like dict.get(seq, dflt) */
static int assoc_get(const assoc_t *a, int seq, int dflt) {
    int i = assoc_find(a, seq); return i < 0 ? dflt : a->value[i];
}
/* set, creating the position if absent */
static void assoc_set(assoc_t *a, int seq, int val) {
    int i = assoc_find(a, seq);
    if (i < 0) { if (a->count == a->cap) assoc_grow(a); i = a->count++; a->sequencing[i] = seq; }
    a->value[i] = val;
}

/* The full re-commencing carry as a sparse, growing store keyed by sequencing,
   each holding (morality, competency, re_attentioning). Like the reference
   dict re_commencing_co_agency. */
typedef struct { int *seq; int *mor; int *comp; int *reatt; int count, cap; } cstore_t;
static void cstore_init(cstore_t *s){ s->seq=NULL;s->mor=NULL;s->comp=NULL;s->reatt=NULL;s->count=0;s->cap=0; }
static void cstore_free(cstore_t *s){ free(s->seq);free(s->mor);free(s->comp);free(s->reatt); }
static int  cstore_find(const cstore_t *s,int seq){ for(int i=0;i<s->count;i++) if(s->seq[i]==seq) return i; return -1; }
static void cstore_grow(cstore_t *s){
    int nc=s->cap?s->cap*2:4;
    s->seq=(int*)realloc(s->seq,(size_t)nc*sizeof(int));
    s->mor=(int*)realloc(s->mor,(size_t)nc*sizeof(int));
    s->comp=(int*)realloc(s->comp,(size_t)nc*sizeof(int));
    s->reatt=(int*)realloc(s->reatt,(size_t)nc*sizeof(int));
    s->cap=nc;
}
static void cstore_set(cstore_t *s,int seq,int mor,int comp,int reatt){
    int i=cstore_find(s,seq);
    if(i<0){ if(s->count==s->cap) cstore_grow(s); i=s->count++; s->seq[i]=seq; }
    s->mor[i]=mor; s->comp[i]=comp; s->reatt[i]=reatt;
}

/* _1_self_coupling. commencing_co_agency: array of carry_t (length ncommencing).
   accepted_bi_morality: array of face_t (length naccepted). Writes the surface
   into bi_moral_sequencing_out with its own count (caller provides room for at
   most ncommencing + naccepted face_t), and the new carry as a cstore_t. */
void _1_self_coupling(const carry_t *commencing_co_agency, int ncommencing,
                 const face_t *accepted_bi_morality, int naccepted,
                 face_t *bi_moral_sequencing_out, int *nbi_moral_sequencing_out,
                 cstore_t *re_commencing_out) {
    /* offering = {sequencing: competency} from the commencing carry */
    assoc_t offering; assoc_init(&offering);
    for (int i = 0; i < ncommencing; i++)
        assoc_set(&offering, commencing_co_agency[i].sequencing, commencing_co_agency[i].competency);

    /* bi_moral_attentioning: the sparse sign-count. accepted nonzero morality
       counted as-is; commencing carry morality sign-inverted. Only +/-1. */
    assoc_t bi_moral_attentioning; assoc_init(&bi_moral_attentioning);
    for (int i = 0; i < naccepted; i++) {
        int m = accepted_bi_morality[i].morality, s = accepted_bi_morality[i].sequencing;
        if (m > 0) assoc_set(&bi_moral_attentioning, s, assoc_get(&bi_moral_attentioning, s, 0) + 1);
        if (m < 0) assoc_set(&bi_moral_attentioning, s, assoc_get(&bi_moral_attentioning, s, 0) - 1);
    }
    for (int i = 0; i < ncommencing; i++) {
        int m = commencing_co_agency[i].morality, s = commencing_co_agency[i].sequencing;
        if (m > 0) assoc_set(&bi_moral_attentioning, s, assoc_get(&bi_moral_attentioning, s, 0) - 1);
        if (m < 0) assoc_set(&bi_moral_attentioning, s, assoc_get(&bi_moral_attentioning, s, 0) + 1);
    }

    /* bi_co_now: the surface over what the releasing carries, sign only */
    for (int i = 0; i < bi_moral_attentioning.count; i++) {
        int t = bi_moral_attentioning.value[i];
        bi_moral_sequencing_out[i].sequencing = bi_moral_attentioning.sequencing[i];
        bi_moral_sequencing_out[i].morality = (t > 0) ? 1 : (t < 0 ? -1 : 0);
    }
    *nbi_moral_sequencing_out = bi_moral_attentioning.count;

    /* re_commencing_co_agency: persist within the attentioning bound */
    cstore_init(re_commencing_out);
    for (int i = 0; i < ncommencing; i++) {
        int r2 = commencing_co_agency[i].re_attentioning + 1;
        if (r2 <= 3 || (r2 == 4 && commencing_co_agency[i].competency > 0))
            cstore_set(re_commencing_out, commencing_co_agency[i].sequencing,
                       commencing_co_agency[i].morality, commencing_co_agency[i].competency, r2);
    }
    /* fresh surface re-enters the carry, overwriting its sequencing */
    for (int i = 0; i < *nbi_moral_sequencing_out; i++) {
        int sequencing = bi_moral_sequencing_out[i].sequencing;
        int morality   = bi_moral_sequencing_out[i].morality;
        if (morality != 0)
            cstore_set(re_commencing_out, sequencing, morality,
                       0 - assoc_get(&offering, sequencing, 1), 0);
    }

    assoc_free(&offering);
    assoc_free(&bi_moral_attentioning);
}
