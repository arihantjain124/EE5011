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


void main()
{
FILE *fptr;
fptr = fopen("out.txt","w");    //Output file to pass interpolated values to python
float xx[9];
float yy[9];
xx[0]=0;
yy[0]=0;
int i;
for (i=1;i<=8;i++){             //Generating Table for n+1 points for function sin()
    xx[i]=xx[i-1]+M_PI_4;
    yy[i]=sin(xx[i]);
}
float x=0;
float y;
float diff=2*M_PI/100;          //uniform step for 100 values between 0 to 2π
for(i=0;i<100;i++){
    fprintf(fptr,"%f %f\n",x,lintp(xx,yy,x,8));    //writing x and interpolation value for x to output text file
    x=x+diff;
}
fclose(fptr);
}