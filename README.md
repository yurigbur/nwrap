# nwrap

Wrapper for nmap that creates a folder and output files for each host of the target definition (only for direct target definition at the moment not for `-iL`).

Why? Nmap unfortunately only save scan results after the entire scan has finished. I had some issues during engagements scanning through a running ligolo agents that the agent died or was killed by blue teams and the intermediary results were not saved. Thats why I wrote this little script. 
