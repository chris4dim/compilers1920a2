import re  #eisagwgh module re


def function(m):   #dhmiourgia synarthshs function gia antikatastash xarakthrwn &amp;&gt;&lt;nbsp;

    if (m.group(0)=='&amp;'):
        return '&'
    
    elif (m.group(0)=='&gt;'):
        return '>'

    elif (m.group(0)=='&lt;'):
        return '<'

    else:
        return ' '  

rexp1 = re.compile('<title>(.+?)</title>')  #tairiasma periexomenou tou tag <title></title>

rexp2 = re.compile('<!--.*?-->',re.DOTALL)  #tairiasma twn sxoliwn pou briskontai anamesa apo <!-- kai -->

rexp3 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL)  #tairiasma periexomenwn twn tags <script></script> kai <style></style>

rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)  #tairiasma periexomenwn tou tag <a></a> kai ths href

rexp51 = re.compile(r'<.+?>|</.+?>',re.DOTALL)   #tairiasma twn tags tou keimenou me morfh <> </>
rexp52 = re.compile(r'<.+?/>',re.DOTALL)         #tairiasma twn tags tou keimenou me morfh </>

rexp6 = re.compile(r'&(amp|gt|lt|nbsp);')   #tairiasma tou keimenou me morfh &amp;&gt;&lt;nbsp;

rexp7 = re.compile(r'\s+')   #tairiasma sunexomenwn xarakthrwn whitespace



with open('testpage.txt','r') as fp:   #diabasma apo to arxeio testpage.txt

    text = fp.read()

    m = rexp1.search(text)   #anazhthsh gia tairiasma apo to rexp1

    print(m.group(1))        #ektupwsh merous tou tairiasmatos  rexp1

    text = rexp2.sub(' ',text)  #apaloifh olwn twn sxoliwn

    text = rexp3.sub(' ',text)  #apaloifh twn tags <script></script> kai <style></style>

    for m in rexp4.finditer(text):   #anazhthsh olwn twn tairiasmatwn toy rexp4
        print('{}    {}'.format(m.group(1),m.group(2)))   # ektupwsh merous tou tairiasmatos tou rexp4

    text = rexp51.sub(' ',text)  #apaloifh tags tou keimenou me morfh <> </>
    text = rexp52.sub(' ',text)  #apaloifh tags tou keimenou me morfh </>

    text = rexp6.sub(function,text)   #antikatastash tou keimenou me morfh &amp;&gt;&lt;nbsp;

    text = rexp7.sub(' ',text)   #antikatastash synexomenwn xarakthrwn me ena xarakthra whitespace

print(text)   #ektupwsh telikou keimenou

