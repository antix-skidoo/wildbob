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

class TextAcquireProgress(wildbob_common.SwigAcquireStatus):
    def UpdatePulse(self, FetchedBytes, CurrentCPS, CurrentItems):
        print "Pulse: fetchedB %i, cps %s, currentItems %i" % (FetchedBytes, CurrentCPS, CurrentItems)
    def Start(self):
        print "TextAcquireProgress.Start"
    def Stop(self):
        print "TextAcquireProgress.Stop"
    def Fetched(self, size, resume):
        print "Fetched: %i %i" %(size,resume)

class TextInstallProgress(wildbob_common.SwigInstallProgress):
    def startUpdate(self):
        print "startUpdate"
    def finishUpdate(self):
        print "finishUpdate"

if len(sys.argv) < 2:
    print "need argument"
    sys.exit(1)

# FIXME: wrap this somewhere
_error = wildbob_common._GetErrorObj()
wildbob_common.RInitSystem()

lister = wildbob_common.RPackageLister()
t = TextProgress()
lister.setProgressMeter(t)

if not lister.openCache(False):
    print "error opening cache file"
    _error.DumpErrors()
    sys.exit(1)

pkg = lister.getPackage(sys.argv[1])
if pkg == None:
    print "Can't find pkg %s" % sys.argv[1] 
    sys.exit(1)

pkg.setReInstall(True)
pkg.setInstall()

#aProgress = wildbob_common.SwigAcquireStatus()
#iProgress = wildbob_common.SwigInstallProgress()
aProgress = TextAcquireProgress()
iProgress = TextInstallProgress()
lister.commitChanges(aProgress,iProgress)
