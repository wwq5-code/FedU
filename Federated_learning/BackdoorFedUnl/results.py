# \begin{table*}
# 	% \tiny
# 	\scriptsize
# 	\caption{Comparison of Untargeted Poisoning Attacks}
# 	\label{tab_total}
# 	\resizebox{\linewidth}{!}{
# 		\begin{tabular}{ccccccccccc}
# 			\toprule
# 			\multirow{2}{*} {FL-Server} & \multicolumn{5}{c} {MNIST, $K_e=2$, $er=10\%$}& \multicolumn{5}{c} {CIFAR10}\\
# 			\cmidrule(r){2-6}   \cmidrule(r){7-11}
# 			                         & Origin  & HFU   & BFU    & BFU-SS  & Retrain & Origin & HFU & BFU & BFU-SS  & Retrain  \\
# 			\midrule
# 			Running Time             & 10      &3      & 4      & 3       & 10      & 7      &8    & 9   &10       &11\\
# 			Acc. on test dataset & 97.5\%  &97.3\% & 97.6\% & 97.68\% & 97.5\%  & 7      &8    & 9   &10       &11\\
# 			$L_2$-Norm to retrain    & 104       &107    & 108    & 107   & 0       & 7      &8    & 9   &10       &11\\
# 			KLD to retrain           & 221       &214    & 216    & 213   & 0       & 7      &8    & 9   &10       &11\\
# 			Backdoor Acc.       & 100\%   &2.55\% & 7.04\% & 9.16\%  & 0.08\%  & 7      &8    & 9   &10       &11\\
# 			\toprule
# 			\multirow{2}{*} {Client $k_e$} & \multicolumn{5}{c} {MNIST, $K_e=2$, $er=10\%$}& \multicolumn{5}{c} {CIFAR10}\\
# 			\cmidrule(r){2-6}   \cmidrule(r){7-11}
# 			                         & Origin  & HFU   & BFU    & BFU-SS  & Retrain & Origin & HFU & BFU & BFU-SS  & Retrain  \\
# 			\midrule
# 			Running Time             & 10      &1+rem. & 1      & 2       & 10       & 7      &8    & 9   &10       &11\\
# 			Acc. on remaining dataset& 100\%   &89.53\%& 95.99  & 97.33\% & 100\%    & 7      &8    & 9   &10       &11\\
# 			Backdoor Acc.       & 100\%   &0.1\%  & 0.9\%  & 1.4\%   & 0.00\%   & 7      &8    & 9   &10       &11\\
# 			\bottomrule
# 	\end{tabular}}
# \end{table*}