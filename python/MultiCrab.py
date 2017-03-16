from subprocess import call, check_output
import sys, os

from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException
from SamplesKeyValue import toPrint
#https://lost-contact.mit.edu/afs/cern.ch/ubackup/z/zdemirag/public/forSid/crabNero_80X.py

def multiCrabSubmit(config, path_T2):
    ### for some reason only the first dataset is submitted correctly, work around
    if len(sys.argv) ==1:
        ## book the command and run python
        cmd = "python " + sys.argv[0] + " '" + config.General.requestName + "'"
        print ""
        print "calling: "+cmd
        call(cmd,shell=True)
        return
    if len(sys.argv) > 1:
        ## if it is not in the request try the next
        if sys.argv[1] !=  config.General.requestName: return
        ###
        print "--- Submitting " + "\033[01;32m" + config.Data.inputDataset.split('/')[1] + "\033[00m"  + " ---"
        toPrint("LFNDirBase at T2", path_T2)
        config.Data.outputDatasetTag = config.General.requestName
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


