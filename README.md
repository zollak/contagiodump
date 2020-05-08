# contagiodump

Contagio is a collection of the latest malware samples, threats, observations, and analyses. Clean documents are collected from various open sources. Clean files in EXE, XLS(X), DOC(X), RTF, ZIP, 7Z, RAR, JAR, PDF, MACH-O, and ELF file formats. Malicious files in PDF, RTF, XLS, MACH-O, ELF, and JAR file formats.

You can find more info about the files on the Contagio Malware Dump page: http://contagiodump.blogspot.com/

This python script helps to download all archived files.

Requirements:
```
Python 2. 7
approx. 10GB storage space 
```

Usage:
```
git clone https://github.com/zollak/contagiodump.git
cd contagiodump/
wget http://contagiomobile.deependresearch.org
virtualenv --python=python2.7 .env
source .env/bin/activate
pip install -r requirements.txt 
python get_files.py
deactivate
```


The zip files are password protected.

The password scheme is infected666 followed by the last character before the zip extension. e.g abc.zip will have the password infected666c. See the name of the file you are downloading and the character before the dot. The old files (prior to 2012) may have the pass 'infected'

Disclaimer
Malware samples are available for download by any responsible whitehat researcher. By downloading the samples, anyone waives all rights to claim punitive, incidental and consequential damages resulting from mishandling or self-infection.
