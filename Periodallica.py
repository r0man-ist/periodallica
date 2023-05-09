# script to bulk-download the ocr-ed html text of journal issues in Gallica using the parentArk from the BnF catalogue général
# will create html files for each issue referenced in gallica (including header-only files those for which there is no OCR!)
# might produce duplicates if there is more than 1 instance of an issue in gallica!
# will skip issues where access to the full text is denied
# will produce no usable result, if there is a forward to retronews. those files are easily sorted by size...
# 20s timer built in to avoid 429-warning. this might be too generous, though.
# it's bulky, slow and inelegant -- but seems to work...

import urllib.request
import xml.etree.ElementTree as ET
import time

# get a list of years in which the periodical has issues in Gallica
def getyears (parentARK):
    response = urllib.request.urlopen("https://gallica.bnf.fr/services/Issues?ark="+parentARK+"/date")
    tree = ET.fromstring(response.read())
    listyears = []
    for year in tree:
        listyears.append(year.text)
    print("There are records for issues issues in these years:"+str(listyears))
    return listyears

#get a list of arks for individual issues
def getissues (parentARK):
    years = getyears(parentARK)
    listissues = []
    for year in years:
        response = urllib.request.urlopen("https://gallica.bnf.fr/services/Issues?ark=" + parentARK + "/date&date="+year)
        tree = ET.fromstring(response.read())
        for issue in tree.findall('issue'):
            ark = issue.get('ark')
            listissues.append(ark)
    print("There are records for "+str(len(listissues))+" issues")
    return listissues

# write the text from each issue into a seperate html file named after the ark for the issue
def write_to_file(parentArk):
    list = getissues(parentArk)
    countdl = 0
    count403 = 0
    for ark in list:
        time.sleep(20)
        try:
            page = urllib.request.urlopen("https://gallica.bnf.fr/ark:/12148/"+ark+".texteBrut")
            #page = urllib.request.urlopen("https://gallica.bnf.fr/ark:/12148/bpt6k3814205s.texteBrut")# this will produce a 403 exception -- here for testing purposes
            f = open(f"{ark}.html","wb")
            content = page.read()
            f.write(content)
            f.close()
            countdl = countdl + 1
        except urllib.error.URLerror as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
            else:
                continue
    print(str(countdl)+" files have been written")
    print(str(count403)+" files could not be downloaded")

#write_to_file("ark:/12148/cb32814317r")
getissues('cb326950195')



