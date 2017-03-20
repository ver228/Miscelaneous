

% take all the spectra and fit them to get the bending modulus, plot
% everything and compare to get differences.
clear all
folderANALYSIS = 'T:\lp389\FluoAlkane_25_3_15\cleaned';
cd(folderANALYSIS)

ttMAT = '*.mat';
ttMATnames = dir(ttMAT);            % these are all the files.mat in the folder

NVes = size(ttMATnames,1);
%%
% per ogni vescicola

VESresults = cell(NVes,6);

for j = 1:NVes                    % il meno uno e` per l'ultimo file .mat che non e` un'analisi
    
    j
    clear movie ves_i_ANALYSIS
    ves_i_ANALYSIS = ttMATnames(j).name;
    load(ves_i_ANALYSIS)
    
    ttFrames2 = ttFrames(1:round(length(ttFrames)*3/4));
    GoodFrames = setdiff(ttFrames2,BADframes);
    hold on
    movie.get_spectrum(true,GoodFrames);
    
    VESresults{j,1}=movie.spectrum;
    
    ttFrames = size(movie.contour_fine,1);
    
    NN = (ttFrames - length(BADframes))/ttFrames
    
    %pause
    
end

%%

addpath('E:\MATLABscripts')

figure(1)

colors = jet(NVes);

%Good_No_alkane = [2 4 12 13 15];                % you may want to include 3 5
%Good_alkane10 = [1 5 6 7 8 13];                 % you may want to include 4 14
%Good_alkane6 = [2 4];                           % you may want to include 3
%Bad_DOPCtemp = [14 16 17 30 33];

Good07 = [2:12, 17 19 20 23 25];
Good07mic = [1 2 4 5 ,7:10, 12]

for j = 1:NVes
    
    j
    clear nmax
    
    if isempty(VESresults{j,1})~=1 %&& ismember(j,Bad_DOPCtemp)~=1
        
        res = VESresults{j,1};
        ps = res.static.ps;
        q = res.static.q;
        tau = res.corr.tau;
        autoC = res.corr.g2(:,2:end);
        autoC_time = res.corr.g2(:,1);
        L = res.L;
        T = res.T;
        R = res.R;
        
        figure(1)
        %subplot(121)
        hold off
        plot(q(5:end),ps(5:end),'.-','Color',colors(j,:))
        %plot(q(7:end),spectrum(7:end),'.-g')
        
        %         subplot(122)
        %         hold on
        %         Ltau = length(tau);
        %         plot(q(2:Ltau),tau(2:end),'.-','Color',colors(j,:))
        %plot(q(2:Ltau),tau(2:end),'.-m')
        
        %         if j==2
        %
        %             subplot(133)
        %             hold on
        %             for gg = 1:40
        %                 plot(autoC_time, autoC(:,gg),'.-','Color',colors(j,:))
        %             end
        %         end
        
        %subplot(121)
        set(gca,'XScale','log','YScale','log')
        
        %subplot(122)
        %set(gca,'XScale','log','YScale','log')
        
        %%% fit the spectrum to get the bending modulus and the surface tension
        
        [lim,~] = ginput;
        %lim = 3*10^6;
        if isempty(lim)==1 
            continue
        end
        
        GoodQ = q<lim;
        nmax = find(GoodQ,1,'last');
        %nmax=20;            % forse e` bene sceglierlo a mano
        range = [6:nmax];
        
        
        %subplot(121)
        hold on
        plot(q(nmax),ps(nmax),'sk')
        
        [s,ds,k,dk,gamma] = fit_vesicles_fluctuations_Lucia(res,range);
        
        qs=logspace(log10(q(range(1))),log10(q(range(end))),1000)';
        modelstatic=PSDq_Lucia(log10(s),log10(k),gamma,T,L,qs);
        
        %subplot(121)
        hold on
        plot(qs,modelstatic,'-k')
        
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
        %%% fit the taus to look at the membrane viscosity
        %         n = 10^-3;
        %         rangeTAU = (3:7);
        %         fitTAU(q, tau, n, s, k*100, R, rangeTAU);
        
        
        VESresults{j,2}=k;
        VESresults{j,3}=dk;
        VESresults{j,4}=s;
        VESresults{j,5}=ds;
        VESresults{j,6}=R;
        VESresults{j,7}=T;
        
        name = ttMATnames(j).name;
        %         vesNN = str2double(name(9:10));
        %
        %         if vesNN(1)==0
        %            vesNN = vesNN(2);
        %         end
        %
        %         VESresults{j,8} = vesNN;
        
        %vesNN = str2num(name(5));
        vesNN = name(5);
        
        if vesNN == '_'
            VESresults{j,8} = 0;
        elseif vesNN == '4'
            VESresults{j,8} = 4;
        elseif vesNN == '8'
            VESresults{j,8} = 8;
        end
        
        pause
        
    end
    
end




%%
% plot kappas for different T

COLORS_temp = jet(5);               % a different colour for each temperature
%figure(1)
%gcf
%hold on

M = NaN(10);

%Bad_DOPCtemp = [22 31 32];
%rGood = [2 3 4 5 8 9 11 17 18 19 20 21 23 25 26]
%2 5 15 19 31 32

%Good = [1:12,16:26];
%Good = [1,4,5];
GoodAlkaneEpifluo = [1:3, 5:8, 10:14, 16, 18:26, 27, 30:33, 35:39];   % these have been used in the fig produced on 23/03/2015 where the max mode was mode 20 4/5 of the whole frames
%GoodAlkaneEpifluoBIS = [2:3, 5:7, 10:11, 14:21, 23:27, 29:30, 34:43];

openfig('/Users/ajaver/Desktop/Cavendish/Luci/RES.fig')
h = gcf;
hhh = findall(h,'Type','axes');

for k = GoodAlkaneEpifluo
    if VESresults{k,8} == 0                 % this is for the alkane
        col = 1;
    elseif VESresults{k,8} == 2
        col = 2;
    elseif VESresults{k,8} == 6
        col = 3;
    end
    
    %    if vesNN(1)==0
    %        vesNN = vesNN(2);
    %    end
    
    if isempty(VESresults{k,1})~=1 %&& ismember(k,Bad_DOPCtemp)~=1
        
        R = VESresults{k,6}/(10^-6);               % in microns
        kappa = VESresults{k,2};
        er_kappa = VESresults{k,3};
        
        sT = VESresults{k,4};
        er_sT = VESresults{k,5};
        
        Temp = VESresults{k,7};
        %[~,indxT,~] = intersect([283.15 288.15 293.15 298.15 303.15],Temp);
        
        %M(indxT,sum(~isnan(M(indxT,:)))+1) = kappa;
        %hold(h, 'on');
        % COLORS_temp(vesNN,:)
        %hold(handles(2),'on')
        %hold on
        axes(hhh(2));
        hold(hhh(2),'on');
        errorbar(VESresults{k,8},kappa,er_kappa/2,'.','Color',COLORS_temp(col+2,:))
        %plot(handles(2),VESresults{k,8},kappa,'.','Color',COLORS_temp(col+2,:))
        %pause(0.1)
        axes(hhh(1));
        hold(hhh(1),'on');
        %hold on
        errorbar(VESresults{k,8},sT,er_sT/2,'.','Color',COLORS_temp(col+2,:))
%         %plot(handles(1),VESresults{k,8},sT,'.','Color',COLORS_temp(col+2,:))
        %pause(0.1)
        
    end
    
end

% subplot(121)
% 
% xlabel('Temperature, T (^\circK)')
% ylabel('Bending Modulus, \kappa (J)')
% 
% subplot(122)
% 
% xlabel('Temperature, T (^\circK)')
% ylabel('Surface Tension, \sigma (J/m^2)')


% subplot(121)
% xlabel('Alkane percentage, p (mol %)')
% ylabel('Bending Modulus, \kappa (J)')
% xlim([-1 9])
% 
% subplot(122)
% xlabel('Alkane percentage, p (mol %)')
% ylabel('Surface Tension, \sigma (J/m^2)')
% xlim([-1 9])