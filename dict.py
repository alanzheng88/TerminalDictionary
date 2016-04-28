import sys
import re
from DictionaryServices import *

def main():
    try:
        searchword = sys.argv[1].decode('utf-8')
    except IndexError:
        errmsg = 'You did not enter any terms to look up in the Dictionary.'
        raise Exception(errmsg)
    wordrange = (0, len(searchword))
    dictresult = DCSCopyTextDefinition(None, searchword, wordrange)
    if not dictresult:
        errmsg = "'%s' not found in Dictionary." % (searchword)
        raise Exception(errmsg.encode('utf-8'))
    else:
        dictresult = re.sub(ur'(\u25b6)', u'\\n\\n\\1', dictresult, flags=re.UNICODE)
        dictresult = re.sub(ur'(\u2022)', u'\\n\\t\\1', dictresult, flags=re.UNICODE)
        dictresult = re.sub('(ORIGIN)', '\\n\\n\\1', dictresult)
        dictresult = re.sub('^|$', '\\n', dictresult)
        print dictresult.encode('utf-8')

if __name__ == '__main__':
    main()
