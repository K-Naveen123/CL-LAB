frequency_1=3;
amplitude_1=1.5;
frequency_2=7;
amplitude_2=0.8;
num_samples=1000;
t=(0:1:num_samples);
sinwave1=amplitude_1*sin(2*pi*frequency_1*t);
sinwave2=amplitude_2*sin(2*pi*frequency_2*t);
sinwave=sinwave1+sinwave2;
plot(t,sinwave)
