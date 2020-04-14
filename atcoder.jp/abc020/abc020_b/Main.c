#include <stdio.h>
int main(){
  int a,b;
  scanf("%d %d",&a,&b);
  if(b<10){
    printf("%d\n",(a*10+b)*2);
  }else if(b<100){
    printf("%d\n",(a*100+b)*2);
  }else{
    printf("%d\n",(a*1000+b)*2);
  }
  
  return 0;
}