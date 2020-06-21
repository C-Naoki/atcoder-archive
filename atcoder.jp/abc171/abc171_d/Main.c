#include <stdio.h>
#include <stdlib.h>
 
int main(void) {
 int n;
 scanf("%d",&n);
 long  int sum1=0,a_count[100001] = {0},t;
 for(int i=0;i<n;i++){
  scanf("%ld",&t);
  //aの和と数値ごとの出現回数を格納する。
  a_count[t]++;//数値ごとの出現回数
  sum1+=t;//aの和
 }
 int q;
 scanf("%d",&q);
 int b[q],c[q];
 for(int i=0;i<q;i++){
  scanf("%d%d",&b[i],&c[i]);
  sum1+=(c[i]-b[i])*a_count[b[i]];
  a_count[c[i]] += a_count[b[i]];
  a_count[b[i]] = 0;
  printf("%ld\n",sum1);
 }
 
}