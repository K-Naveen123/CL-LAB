

clc;
clear all;
close all;

x=[]
xl=input("Enter length of array:")
y=0
for i=1:xl
  f=input("Enter x[n]:")
  x=[x,f];
end
yl=input("Enter length of y[k]:")
k=1:0.01:yl

for i=1:xl
  y+=x(i)*cos(2*pi*i*k)
end
plot(y)





