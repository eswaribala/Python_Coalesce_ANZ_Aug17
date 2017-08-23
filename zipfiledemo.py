'''
Created on 26-Jun-2017

@author: BALASUBRAMANIAM
'''
import zipfile
import os
def zip(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", 
                         zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join
                                      (dirname, filename))
            arcname = absname[len(abs_src) + 1:]
           
            print ('zipping %s as %s' % (os.path.join
                                         (dirname, 
                                          filename),
                                        arcname))
            zf.write(absname, arcname)
    zf.close()

zip("G:/test", "g:/zipexl")