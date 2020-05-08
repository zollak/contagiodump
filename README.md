# contagiodump

Python 2. 7 required and approx. 10GB for all files for download. 

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
