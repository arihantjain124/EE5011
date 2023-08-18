      SUBROUTINE spline(x,y,n,yp1,ypn,y2,u)
c
cf2py intent(out) :: y2
cf2py intent(hide) :: n
cf2py intent(hide) :: u
cf2py double precision :: u(n)
cf2py double precision :: x(n)
cf2py double precision :: y(n)
cf2py double precision :: yp1
cf2py double precision :: ypn
c
      INTEGER n
      DOUBLE PRECISION yp1,ypn,x(n),y(n),y2(n)
      INTEGER i,k
      DOUBLE PRECISION p,qn,sig,un,u(n)
      if (yp1.gt..99e30) then
         y2(1)=0.d0
         u(1)=0.d0
      else
         y2(1)=-0.5d0
         u(1)=(3./(x(2)-x(1)))*((y(2)-y(1))/(x(2)-x(1))-yp1)
      endif
      do i=2,n-1
         sig=(x(i)-x(i-1))/(x(i+1)-x(i-1))
         p=sig*y2(i-1)+2.
         y2(i)=(sig-1.)/p
         u(i)=(6.*((y(i+1)-y(i))/(x(i+
     *        1)-x(i))-(y(i)-y(i-1))/(x(i)-x(i-1)))/(x(i+1)-x(i-1))-sig*
     *        u(i-1))/p
      end do
      if (ypn.gt..99d30) then
         qn=0.d0
         un=0.d0
      else
         qn=0.5d0
         un=(3.d0/(x(n)-x(n-1)))*(ypn-(y(n)-y(n-1))/(x(n)-x(n-1)))
      endif
      y2(n)=(un-qn*u(n-1))/(qn*y2(n-1)+1.d0)
      do k=n-1,1,-1
         y2(k)=y2(k)*y2(k+1)+u(k)
      end do
      return
      END      
      
      SUBROUTINE splinenew(x,y,n,yp1,ypn,y2)
c
cf2py intent(out) :: y2
cf2py intent(hide) :: n
cf2py intent(hide) :: a
cf2py intent(hide) :: b
cf2py intent(hide) :: c
cf2py intent(hide) :: d
cf2py double precision :: x(n)
cf2py double precision :: y(n)
cf2py double precision :: a(n)
cf2py double precision :: b(n)
cf2py double precision :: c(n)
cf2py double precision :: d(n)
cf2py double precision :: yp1
cf2py double precision :: ypn
c
      INTEGER n
      DOUBLE PRECISION x(n),y(n),y2(n),yp1,ypn
      INTEGER i,k,j
      DOUBLE PRECISION b(n),d(n),c(n),a(n),p,q
      b(1)=(3*(x(2)-x(1))/2)+(2.*(x(3)-x(2)))
      c(1)=(x(3)-x(2))
      d(1)=(6.*((y(3)-y(2))/(x(3)-x(2)))-9.*((y(2)-y(1))/(x(2)-x(1))))+3.*yp1
      a(n)=(x(n-1)-x(n-2))
      b(n)=(2.*(x(n-1)-x(n-2)))+3.*(x(n)-x(n-1))/2
      p=(y(n)-y(n-1))/(x(n)-x(n-1))
      q=(y(n-1)-y(n-2))/(x(n-1)-x(n-2))
      d(n)=9*p-6*q-3*ypn
      
      do j=2,n-1
        a(j)=(x(j)-x(j-1))
        c(j)=(x(j+1)-x(j))
        b(j)=2*(a(j)+c(j))
        p=(y(j+1)-y(j))/(x(j+1)-x(j))
        q=(y(j)-y(j-1))/(x(j)-x(j-1))
        d(j)=6*(p-q)
      end do
      do i=1,n-1
         a(i+1)=x(i+1)-x(i)
         c(i+1)=x(i+1)-x(i)
         p=a(i+1)*c(i)
         b(i+1)=b(i+1)-(p/(b(i)))
         p=a(i+1)*d(i)
         d(i+1)=d(i+1)-(p/(b(i)))
      end do
      y2(n)=d(n)/b(n)
      do k=n-1,1,-1
         y2(k)=(d(k)-(c(k)*y2(k+1)))/b(k)
      end do
      return
      END


      SUBROUTINE splinenak(x,y,n,y2,a,b,c,d)
c
cf2py intent(out) :: y2
cf2py intent(hide) :: n
cf2py intent(hide) :: a
cf2py intent(hide) :: b
cf2py intent(hide) :: c
cf2py intent(hide) :: d
cf2py double precision :: x(n)
cf2py double precision :: y(n)
cf2py double precision :: a(n)
cf2py double precision :: b(n)
cf2py double precision :: c(n)
cf2py double precision :: d(n)
c
      INTEGER n
      DOUBLE PRECISION x(n),y(n),y2(n)
      INTEGER i,k,j
      DOUBLE PRECISION b(n),d(n),c(n),a(n),p,q

      b(1)=(x(2)-x(1))+(2.*(x(3)-x(2)))
      c(1)=(x(3)-x(2))-(x(2)-x(1))
      p=((y(3)-y(2))/(x(3)-x(2)))-((y(2)-y(1))/(x(2)-x(1)))
      d(1)=(6.*p*(x(3)-x(2)))/((x(3)-x(1)))
      a(n)=(x(n-1)-x(n-2))-(x(n)-x(n-1))
      b(n)=(2.*(x(n-1)-x(n-2)))+(x(n)-x(n-1))
      p=((y(n)-y(n-1))/(x(n)-x(n-1)))-((y(n-1)-y(n-2))/(x(n-1)-x(n-2)))
      d(n)=(6.*p*(x(n-1)-x(n-2)))/((x(n)-x(n-2)))
      do j=2,n-1
        a(j)=(x(j)-x(j-1))
        c(j)=(x(j+1)-x(j))
        b(j)=2*(a(j)+c(j))
        p=(y(j+1)-y(j))/(x(j+1)-x(j))
        q=(y(j)-y(j-1))/(x(j)-x(j-1))
        d(j)=6*(p-q)
      end do
      do i=1,n-1
         a(i+1)=x(i+1)-x(i)
         c(i+1)=x(i+1)-x(i)
         p=a(i+1)*c(i)
         b(i+1)=b(i+1)-(p/(b(i)))
         p=a(i+1)*d(i)
         d(i+1)=d(i+1)-(p/(b(i)))
      end do
      y2(n)=d(n)/b(n)
      do k=n-1,1,-1
         y2(k)=(d(k)-(c(k)*y2(k+1)))/b(k)
      end do
      return
      END

      SUBROUTINE splint(xa,ya,y2a,n,x,y)
c
cf2py intent(hide) :: n
cf2py double precision :: xa(n)
cf2py double precision :: ya(n)
cf2py double precision :: y2a(n)
cf2py double precision :: x
cf2py intent(out) :: y
c
      INTEGER n
      DOUBLE PRECISION x,y,xa(n),y2a(n),ya(n)
      INTEGER k,khi,klo
      DOUBLE PRECISION a,b,h
      klo=1
      khi=n
      do while(khi-klo.gt.1)
         k=(khi+klo)/2
         if(xa(k).gt.x)then
            khi=k
         else
            klo=k
         endif
      end do
      h=xa(khi)-xa(klo)
      if (h.eq.0.d0) pause 'bad xa input in splint'
      a=(xa(khi)-x)/h
      b=(x-xa(klo))/h
      y=a*ya(klo)+b*ya(khi)+((a**3-a)*y2a(klo)+(b**3-b)*y2a(khi))*(h**
     *     2)/6.d0
      return
      END
C  (C) Copr. 1986-92 Numerical Recipes Software Qk.

      SUBROUTINE splintn(xa,ya,y2a,n,xx,yy,m)
c
cf2py intent(hide) :: n
cf2py double precision :: xa(n)
cf2py double precision :: ya(n)
cf2py double precision :: y2a(n)
cf2py intent(hide) :: m
cf2py double precision :: xx(m)
cf2py intent(out) :: yy(m)
c     
      INTEGER n,m
      DOUBLE PRECISION xx(m),yy(m),xa(n),y2a(n),ya(n)
      INTEGER k,khi,klo
      DOUBLE PRECISION a,b,h,x
      do j=1,m
         x=xx(j)
         klo=1
         khi=n
         do while(khi-klo.gt.1)
            k=(khi+klo)/2
            if(xa(k).gt.x)then
               khi=k
            else
               klo=k
            endif
         end do
         h=xa(khi)-xa(klo)
         if (h.eq.0.d0) pause 'bad xa input in splint'
         a=(xa(khi)-x)/h
         b=(x-xa(klo))/h
         yy(j)=a*ya(klo)+b*ya(khi)+((a**3-a)*y2a(klo)+(b**3-b)*
     *        y2a(khi))*(h**2)/6.d0
      end do
      return
      END
