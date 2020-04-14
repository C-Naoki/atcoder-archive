#include <stdio.h>
int main(){
  int a,b,A,B,t=-1;
  scanf("%d %d",&a,&b);
  A=12.5*a;
  if(a%2==1){
    A++;
  }
  for(int i=0;i<12;i++){
     B=A/10;
    if(B==b){
      t=A;
      break;
    }
    A++;
  }
  if(a%2==0){
    B=A/10;
    if(B==b){
      t=A;
    }
  }
  printf("%d",t);
  return 0;
}