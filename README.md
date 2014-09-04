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
* ./gl2toolkit.py system tdump - Printing a java thread dump (plain text)

### User management
Several tools for user related information and privilege management.

User listing and dumping:

* ./gl2toolkit.py user list - Dump overview of registered users (formatted text)
* ./gl2toolkit.py user fulldump <USER ID OR NAME> - Dump user details (json)
* ./gl2toolkit.py user permdump <USER ID OR NAME> - Dump all permissions assigned to user (json)


Permission listing:

* ./gl2toolkit.py user permdump <USER ID OR NAME> streamonly - Dump all stream related permissions assigned to user (json)
* ./gl2toolkit.py user permdump <USER ID OR NAME> dashonly - Dump all dashboard related permissions assigned to user (json)
* ./gl2toolkit.py user permdump <USER ID OR NAME> streamdash - Dump all dashboard and stream related permissions assigned to user (json)

Permission copying:

* ./gl2toolkit.py user copyperm <USERNAME SRC> <USERNAME DST> - Copy all stream and dashboard permissions from src to dst user (mixed)
* ./gl2toolkit.py user copyperm <USERNAME SRC> <USERNAME DST> streamonly - Copy all stream permissions from src to dst user (mixed)
* ./gl2toolkit.py user copyperm <USERNAME SRC> <USERNAME DST> dashonly - Copy all dashboard permissions from src to dst user (mixed)
* ./gl2toolkit.py user copyperm <USERNAME SRC> <USERNAME DST> streamdash - Copy all stream and dashboard permissions from src to dst user (mixed)


## Planned Features
* Some more failure tolerance
* More system feedback and checks
* Reporting and "inventory" feature
* simple export and archiving feature

## Contact
Please feel free to contact me at: dev AT michaelkessel DOT de

