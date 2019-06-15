#!/usr/bin/env python

import wildbob_common
import sys

class TextProgress(wildbob_common.SwigOpProgress):
    def UpdateStatus(self, p):
        print "\r%.2f          " %(p),
    def Done(self):
        print "\nDone"
    def Update(self):
        print "?",

# FIXME: wrap this somewhere
_error = wildbob_common._GetErrorObj()
wildbob_common.RInitSystem()

lister = wildbob_common.RPackageLister()
t = TextProgress()
lister.setProgressMeter(t)

if not lister.openCache(False, False):
    print "error opening cache file"
    _error.DumpErrors()
    sys.exit(1)

#pkg = lister.getPackage("wildbob")
#print pkg.name()
#print pkg.installedVersion()
#print pkg.section()

vector_pkgs = lister.getPackages()
print "Available packages: %s", vector_pkgs.size()

i=0
while i<vector_pkgs.size():
    pkg = vector_pkgs[i]
    print pkg.name()
    print pkg.installedVersion()
    print
    i += 1


