# cse135_site

apache credentials:
sachihiko: sachipw

Configuring mod_deflate and visiting the webpage resulted in the response header, 'Content-Encoding: gzip'.

To modify the response headers to read "Server: CSE135 Server", I installed the mod_security module, then edited the apache2.conf file and added:
`SecServerSignature: CSE135 Server`
