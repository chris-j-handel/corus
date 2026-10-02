#include <stdio.h>
#include <stdlib.h>
#include "resolver_pure_v265.c"
int main(int argc,char**argv){
  int N=atoi(argv[1]),turns=atoi(argv[2]),mode=atoi(argv[3]);
  /* the ring holds only what stands: a sparse association, seq -> sign */
  assoc_t stands; assoc_init(&stands);
  for(int i=0;i<N;i++) assoc_set(&stands,i,(i%2==0)?1:-1);
  carry_t *commencing=NULL; int ncommencing=0;
  face_t *sq=malloc((size_t)3*N*sizeof(face_t)); int nsq=0;
  printf("[");
  for(int t=0;t<turns;t++){
    face_t *acc=malloc((size_t)2*N*sizeof(face_t)); int nacc=0;
    for(int i=0;i<N;i++){
      int L=assoc_get(&stands,((i-1)%N+N)%N,0);
      if(L!=0){ acc[nacc].sequencing=i; acc[nacc].morality=L; nacc++; }
      if(mode==1){ int R=assoc_get(&stands,(i+1)%N,0); if(R!=0){ acc[nacc].sequencing=i; acc[nacc].morality=R; nacc++; } }
    }
    cstore_t nc; cstore_init(&nc);
    _1_self_coupling(commencing,ncommencing,acc,nacc,sq,&nsq,&nc);
    assoc_free(&stands); assoc_init(&stands);          /* only what stands */
    for(int i=0;i<nsq;i++)
      if(sq[i].sequencing>=0 && sq[i].sequencing<N)
        assoc_set(&stands,sq[i].sequencing,sq[i].morality);
    for(int i=1;i<nc.count;i++){                       /* the writing-down is the trace's */
      int a=nc.seq[i],b=nc.mor[i],c2=nc.comp[i],d=nc.reatt[i],j=i-1;
      while(j>=0 && nc.seq[j]>a){ nc.seq[j+1]=nc.seq[j]; nc.mor[j+1]=nc.mor[j];
        nc.comp[j+1]=nc.comp[j]; nc.reatt[j+1]=nc.reatt[j]; j--; }
      nc.seq[j+1]=a; nc.mor[j+1]=b; nc.comp[j+1]=c2; nc.reatt[j+1]=d;
    }
    /* print "S=.. C=.." as a JSON string */
    printf("%s\"S=", t? ",":"");
    for(int i=0;i<N;i++) printf("%s%d", i?",":"", assoc_get(&stands,i,0));  /* the trace's line, made here */
    printf(" C=");
    for(int i=0;i<nc.count;i++) printf("%s%d:%d:%d:%d", i?";":"", nc.seq[i],nc.mor[i],nc.comp[i],nc.reatt[i]);
    printf("\"");
    free(acc);
    if(commencing) free(commencing);
    /* copy new carry into commencing */
    ncommencing=nc.count; { int cn = nc.count>0?nc.count:1; commencing=malloc((size_t)cn*sizeof(carry_t)); }
    for(int i=0;i<nc.count;i++){ commencing[i].sequencing=nc.seq[i]; commencing[i].morality=nc.mor[i]; commencing[i].competency=nc.comp[i]; commencing[i].re_attentioning=nc.reatt[i]; }
    cstore_free(&nc);
  }
  printf("]\n");
  return 0;
}
