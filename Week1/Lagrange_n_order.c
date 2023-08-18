#include <stdio.h>
#include <math.h>


float lintp(float *xx,float *yy,float x,int n){
    float nr[n+1];          //n+1 points for nth order polynomial
    int i,j;
    for(i=0;i<=n;i++){
        nr[i]=x-xx[i];      // Calculating Numerator
    }
    float yp=0;
    for (i=0;i<=n;i++){
        float p=1;
        for(j=0;j<=n;j++){
            if (i!=j){      //Skipping the i==j term in numerator making it nth order polynomial
                p=p*(nr[j])/((xx[i])-(xx[j]));      // calculating Pᵢ(x) for given x
            }
        }
        yp=yp+p*(yy[i]);    // Adding up all Pᵢ(x)yᵢ for given x
    }
    return yp;              // final interpolated value
}

void locate(float *xx,int n,float x, int *j,int l){     //function to locate the nearest n points for given x
int ju,jm,jl;
jl=0;              //using two points as -infinity and + infinity to account for values of x outside give range
ju=l+1;
while(ju-jl>1){
    jm=(ju+jl)>>1;
    if (x>=xx[jm])
        jl=jm;
    else
        ju=jm;
}
if (x==xx[0]) 
    *j=0;
else if (x==xx[l]) 
    *j=l-n;
else{
    if(jl<(n>>1))  *j=0;
    else    *j=jl-(n>>1);

}
}


void main()
{
FILE *fptr;
fptr = fopen("out.txt","w");
float xx[9];
float yy[9];
xx[0]=0;
yy[0]=0;
int i,j;
int n=3;
int l=8;
float diff=2*M_PI/l;
for (i=1;i<=l;i++){
    xx[i]=xx[i-1]+diff;
    yy[i]=sin(xx[i]);
}
float x=0;
float y;
diff=2*M_PI/100;
for(i=0;i<100;i++){
    locate(xx,n,x,&j,l);
    fprintf(fptr,"%f %f\n",x,lintp(&xx[j],&yy[j],x,n));
    x=x+diff;
}
fclose(fptr);
}