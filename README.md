## gl2toolkit - Console toolkit for graylog2

The script gl2toolkit is a private and hobby project. I'm using graylog2 in a professional manner and really enjoy to work with that nice and fast developing log solution. Working in a datacenter environment i found some features, that were missing at the moment and i decided to spend a few free evenings to script an api tool, that deals with these 'missing features'. 

### General
A list of all main commands is supplied to you when calling the script without any arguments, e.g.: ./gl2toolkit.py. For any main command you can get all subcommands by calling it without one, e.g.: ./gl2toolkit.py system


### Graylog link data
Persist the connection data to your graylog. Connection data is saved in a file ~/.gl2t_linkdata.

* ./gl2toolkit.py link show - Display the saved connection data (json)
* ./gl2toolkit.py link set - Enter new connection data
* ./gl2toolkit.py link unset - Delete the persisted connection data

### System status
Displaying several info sets about the current graylog system status.

* ./gl2toolkit.py system status - Display basic graylog information (json)
* ./gl2toolkit.py system jvm - Display basic java jvm stats (json)
* ./gl2toolkit.py system fields - Listing all fields that are available in your indices (json)
* ./gl2toolkit.py system tdump - Printing a java thread dump (plaintext)

## Contact
Please feel free to contact me at: dev AT michaelkessel DOT de

