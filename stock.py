import urllib
import re

htmltext = urllib.urlopen("https://www.google.com/finance/getprices?q=QCOM&x=NASD&i=86400&p=5D&f=c&df=cpct&auto=1&ts=1470289433531&ei=aNCiV4nZGaG3iwLaqZ3wCg").read()

print htmltext.split()[-1]
