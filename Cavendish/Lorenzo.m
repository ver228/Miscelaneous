
L = 70; %Total length of the vesicle
A = 5; %amplitud of the oscilations
C = L/2*pi; % vescle's radio
k = 6; %"mode"

theta = 0:0.01:2*pi;

time_n_samples = 200;
w = 2*pi/time_n_samples; %time resolution as a period 2*pi

imsize = [255, 255]; %size of the artifitial image
center = round(imsize/2); %center of the image
tot_pix = imsize(1)*imsize(2); %total number of pixels in the image

Ibuff = zeros(imsize(1), imsize(2), time_n_samples, 'uint8'); %buffer with the discretized simulatios

for j = 1:time_n_samples
    R = A*sin(w*j)*sin(theta*k) + C;
    x = R.*cos(theta);
    y = R.*sin(theta);
    
    ind = sub2ind(size(Ibuff), round(x+center(1)), round(y+center(2)), j*ones(size(x)));
    Ibuff(ind) = 1;
end
%%
%visualization purposes. Create a movie of vescile simulation. Comment if not required.
figure
F(size(I,3)) = struct('cdata',[],'colormap',[]);
for kk = 1:size(I,3)
    disp(kk)
    imshow(I(:,:,kk),[])
    drawnow
    F(kk) = getframe;
    
end
movie(F, 5, 25)

%%
current_I = 50; %first image to start "scannning" in Ibuff. For this particular simulation if 0 is choosen it corresponde to zero amplitud(a cicle)

Rsingle = A*sin(w*current_I)*sin(theta*k) + C;
Ysingle = abs(fft(Rsingle)); 

for scanning_rate = [1/40, 1/4, 1/1, 2/1]/255 %[1/10000, 1/1000, 1/300, 1/100]
    
    %discletise the indexes for the "scanned" image
    
    %frame in the buffer from where a pixel will be taken for a given scanning rate
    t = mod(round((0:(tot_pix-1))*scanning_rate+current_I),time_n_samples)+1;
    
    %scanning lines, first in x and then in y. This assume simple scanning
    %in one direction.
    x = repmat(1:imsize(1), 1,imsize(2));
    y = repmat(1:imsize(2), imsize(1),1);
    y = y(:)';
    
    %obtain the averaged (scanned) image
    Iind = sub2ind(size(Ibuff), x, y, t);
    Iavg = reshape(Ibuff(Iind), imsize);
    
    %convert to polar coordinates to visualize the contour
    [xnew,ynew] = find(Iavg);
    xnew = xnew-center(1);
    ynew = ynew-center(2);
    Rnew = sqrt((xnew).^2+(ynew).^2);
    thetanew = atan2(xnew, ynew)+pi;
    [thetanew, dumI] = sort(thetanew);
    Rnew = Rnew(dumI);
    
    figure,
    subplot(1,3,1)
    imshow(Iavg,[])
    title(sprintf('Scanned image\n %i pix per delta time', round(1/scanning_rate)))
    
    subplot(1,3,2), hold on
    plot(thetanew,Rnew)
    xlabel('\theta (radians)')
    ylabel('Radious (pixels)')
    
    plot(theta,Rsingle);
    xlim([0 2*pi])
    
    subplot(1,3,3), hold on
    Ynew = abs(fft(Rnew));
    
    plot(2:25, Ysingle(2:25)) 
    plot(2:25, Ynew(2:25))
    title('FFT')
end
