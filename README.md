# text-extractor

This program is used to extract only text from the html files 
in current folder and all sub folders.

Use the program 'httrack' to mirror a website as html files.
Then use this program to extract only text.


Run the following commands


sudo cp extract-text.py /bin

sudo cp html2text.py /bin

sudo chmod a+x /bin/extract-text.py

sudo chmod a+x /bin/html2text.py




Then, goto the folder where the html files are. Ex /tmp/blog

cd /tmp/blog
extract-text.py

This will extract all the text in save in a file named "out.txt"
