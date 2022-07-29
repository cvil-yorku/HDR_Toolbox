%
%       HDR Toolbox demo 1:
%	   1) Load "Bottles_Small.pfm" HDR image
%	   2) Show the image in linear mode
%	   3) Show the image in gamma mode
%	   4) Tone map and show the image using Reinhard's TMO 
%	   5) Show and Apply Color Correction to the tone mapped image
%	   6) Save the tone mapped image as PNG
%
%       Author: Francesco Banterle
%       Copyright February 2011 (c)
%
%
clear all;

disp('1) Load the image Bottles_Small.pfm using hdrimread');
img = hdrimread('demos/newHDR.hdr');


img = imresize(img,0.25);

img = max(img, 0);

TMOS = [ "Ashikhmin", "Banterle", "Chiu", "Drago", "Durand", "Exponential", "Ferwerda", "KimKautzConsistent", "Krawczyk", "Kuang", "Lischinski", "Logarithmic", "Normalize", "Pattanaik", "Raman", "Reinhard","ReinhardDevlin", "Schlick", "Tumblin", "VanHateren", "WardGlobal", "WardHistAdj", "YPFerwerda", "YPTumblin", "YPWardGlobal"];
for i = 1:length(TMOS)
 
    f = str2func(TMOS(i)+"TMO");
    imgTMO = f(img);
    imgTMO = max(imgTMO, 0);
    imgOut = GammaTMO(imgTMO, 2.2, 0, 0);
    imwrite(imgOut, 'demos/output/' + TMOS(i) +'.png');

end
