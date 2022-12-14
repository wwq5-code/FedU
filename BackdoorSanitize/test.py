\begin{table*}
	% \tiny
	\scriptsize
	\caption{Comparison of Untargeted Poisoning Attacks}
	\label{tab_total}
	\resizebox{\linewidth}{!}{
		\begin{tabular}{ccccccccccc}
			\toprule
			\multirow{2}{*} {FL-Server} & \multicolumn{5}{c} {MNIST, $K_e=2$, $er=10\%$}& \multicolumn{5}{c} {CIFAR10, $K_e=3$, $er=10\%$}\\
			\cmidrule(r){2-6}   \cmidrule(r){7-11}
			                         & Origin  & HFU   & BFU    & BFU-SS  & Retrain & Origin & HFU & BFU & BFU-SS  & Retrain  \\
			\midrule
			Running Time             & 10      &3      & 4      & 3       & 10      & 40     &18    & 6   &10       &40\\
			Acc. on test dataset     & 97.5\%  &97.3\% & 97.6\% & 97.68\% & 97.5\%  & 80.1\% &78.6\%&78.2\%&79.44\%   &79.8\%\\
			$L_2$-Norm to retrain    & 104       &107    & 108    & 107   & 0       & 3665   &152441& 13102   &19296       &0\\
			KLD to retrain           & 221       &214    & 216    & 213   & 0       & 24.84  &21.82 & 23.73   &21.87       &0\\
			Backdoor Acc.            & 100\%   &2.55\% & 7.04\% & 9.16\%  & 0.08\%  & 97\%   &13.4\%    & 9.7\%   &8\%       &0.3\%\\
			\toprule
			\multirow{2}{*} {Client $k_e$} & \multicolumn{5}{c} {MNIST, $K_e=2$, $er=10\%$}& \multicolumn{5}{c} {CIFAR10, $K_e=3$, $er=10\%$}\\
			\cmidrule(r){2-6}   \cmidrule(r){7-11}
			                         & Origin  & HFU   & BFU    & BFU-SS  & Retrain & Origin & HFU & BFU & BFU-SS  & Retrain  \\
			\midrule
			Running Time             & 10      &1*3    & 0.1*3  & 0.2*3   & 10       & 1*10   &0.2*10&0.1*5   &0.2*5       &10\\
			Acc. on remaining dataset& 100\%   &89.53\%& 95.99  & 97.33\% & 100\%    & 100\%  &98.02\% &15.39\%    &67.39\%    &10\\
			Backdoor Acc.            & 100\%   &0.1\%  & 0.9\%  & 1.4\%   & 0.00\%   & 100\%  &13\%    &0\%   &0\%       &0\%\\
			\bottomrule
	\end{tabular}}
\end{table*}
