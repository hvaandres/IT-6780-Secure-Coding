<VirtualHost *:80>

ServerAdmin webmaster@badstore.net

DocumentRoot "C:/xampp/htdocs/badstore"

ServerName www.badstore.net

ServerAlias badstore.net *.badstore.net

ScriptAlias /cgi-bin/ "C:/xampp/htdocs/badstore/cgi-bin/"

<Directory "C:/xampp/htdocs/badstore/cgi-bin">

AllowOverride None

Options +ExecCGI

Order allow,deny

Allow from all

</Directory>

ErrorLog "logs/badstore-error.log"

CustomLog "logs/badstore-access.log" common

</VirtualHost>