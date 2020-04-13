#include <stdio.h>
int main(){
  long long n,a,b,c,d;
  scanf("%lld %lld %lld",&n,&a,&b);
  c=n/(a+b);
  d=c*(a+b);
  if(n-d<a){
    printf("%lld",c*a+(n-d));
  }else{
    printf("%lld",(c+1)*a);
  }

  return 0;
}