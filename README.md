- - -  - 📖 WebBuster Manual - - - - - 

webbuster – A simple tool for directory brute forcing.

--------------SYNOPSIS-----------
-- webbuster -w WORDLIST [-t THREADS] URL

------------DESCRIPTION------------

WebBuster is a Python-based tool that performs directory brute forcing against a target web server.
It takes a list of potential directory names and checks which ones exist on the server.

---------OPTIONS-----------

-w WORDLIST
Path to the wordlist file containing directory names (one per line).
(Required)

-t THREADS
Number of threads to use for concurrent requests. Default is 10.
(Optional)

URL
The target base URL (e.g., http://127.0.0.1:8080 or http://example.com).
(Required)

-h, --help
Show help message and exit.

---------EXAMPLES-----------

Basic usage (default threads = 10):

webbuster -w wordlist.txt http://127.0.0.1:8080


With custom threads:

webbuster -w /usr/share/wordlists/dirb/common.txt -t 20 http://testphp.vulnweb.com


Help menu:

webbuster -h

----------EXIT STATUS---------

0 – Successful execution.

1 – Errors (missing arguments, invalid URL, etc.).

-----------AUTHOR-----------

Written by vinsmoke.

----------DISCLAIMER-------

This tool is for educational purposes only.
Use only on systems you own or have explicit permission to test.
