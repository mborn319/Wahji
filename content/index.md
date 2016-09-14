# About Wahji
Wahji is brilliant.

## How to use Wahji
Wahji has three main commands:
* wahji new [site_name]
* wahji build [site_name]
* wahji remove [site_name]

### Wahji new [site_name]
Say we want to create a site called "Confer's Amazing Website". We run `wahji new confer`. A new confer/ folder is created under the Wahji directory. This confer/ folder has a wahji.yml file, which is used for configuration of the confer site, and the ready-to-start-editing folder structure of the new site.

### Wahji build [site_name]
Note that site_name is not necessary (and, indeed, ignored completely) if the user is anywhere in the wahji/confer directory, at which point the site name is assumed to be confer.
This folder checks the configuration defined in confer/wahji.yml and copies the files from /wahji/themes/<specified_theme> to wahji/confer/themes/confer.
Wahji has three main commands

### wahji remove [site_name]
Deletes the directory for the given site name, OR assume the site_name based on the current site name.

