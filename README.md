# nwrap

Wrapper for nmap that creates a folder and output files for each host of the target definition (only for direct target definition at the moment not for `-iL`).

Why? Nmap unfortunately only save scan results after the entire scan of a group has finished. I had some issues during engagements scanning through a running ligolo agents that the agent died or was killed by blue teams and the intermediary results were not saved. Thats why I wrote this little script. 

The current functionallity can also be achieved with the group size setting --max-hostgroups 1 but I intend to add some python-based parallelization in the future to still have parallelization with individual outputs. Furthermore, I want to add a storing of the `-vv` output that intermediary output for a single host is still partially stored which can be useful for ultra-slow scans.
