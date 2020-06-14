#include <stdio.h>
int main(){
  int k,n,num1,num2,num,s,number,big,a;

  scanf("%d %d",&k,&n);

  scanf("%d %d",&num1,&num2);

  s=num2-num1;

  num=num2;

  big=s;

  for(int i=2;i<n;i++){

    scanf("%d",&number);

    s=number-num;

    num=number;

    if(big<s){
      big=s;
    }
  }

  a=k+num1-num;

  if(big<a){
    big=a;
  }

  printf("%d",k-big);

  return 0;
}
