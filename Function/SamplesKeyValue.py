#///////////////////////////////////////////////////////
#                                                      #
# Define functions to read input datasets, paths at T2 #
#                                                      #
#///////////////////////////////////////////////////////

import datetime
import collections

#Get nth key, value of MC
def getMCVal(mcDict, n):
    return mcDict[list(mcDict)[n]]

def getMCKey(mcDict, n):
    return list(mcDict)[n]
    '''
    val = getMCVal(mcDict, n)
    #today_date = str(datetime.date.today()).replace("-","")
    if val !="":
        start_name = val.split("/")[1].split("_")[0]
        key = start_name #+"_Ntuple"+str(today_date)
        if start_name == "ST":
            start_name = start_name+ "_" +val.split("/")[1].split("_")[1]
            key = start_name #+"_Ntuple"+str(today_date)
            return key
        else:
            return key
    '''
#Get nth key, value of DATA
def getDataVal(dataDict, n):
    return dataDict[list(dataDict)[n]]

def getDataKey(dataDict, n):
    return list(dataDict)[n]
    '''
    val = getDataVal(dataDict, n)
    if val !="":
        name = val.replace("MINIAOD","")
        key = name.replace("/","_").replace("-","_")
        return key
    '''
def getLFNDirBaseMC(channel_MC, mcSampDict, m):
    outLFNDirBase = '/store/user/rverma/test2/Crab'+ channel_MC+ '/'+getMCKey(mcSampDict, m)+"_"+ channel_MC
    return outLFNDirBase

def getLFNDirBaseData(channel_Data, dataSampDict, m):
    outLFNDirBase = '/store/user/rverma/test2/Crab'+ channel_Data+ '/'+getDataKey(dataSampDict, m)+"_"+ channel_Data
    return outLFNDirBase

#PATHS OF NTUPLE AT T2_IN_TIFR
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling
def getPathsAtT2(samp_channel, samp_dict, n):
    '''
    /cms/store/user/rverma/
    ntuple/CrabMuonsMC/QCD_ntuple_2017-03-15_MuonsMC/
    QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8/
    crab_QCD_ntuple_2017-03-15_MuonsMC/170315_214120/
    0000/W1JetsToLNu_ntuple_2017-03-15_muons_98.root
    '''
    local_crab_dir = samp_channel
    local_crab_subdir = getMCKey(samp_dict, n) +"_"+samp_channel
    t2_user_dir = '/store/user/rverma/Crab/test2/'
    t2_crab_dir = local_crab_dir+'/'+local_crab_subdir
    t2_samp_name = "/"+getMCVal(samp_dict, n).split("/")[1]
    t2_samp_subdir = "/"+local_crab_subdir

    year_full = str(datetime.date.today()).split("-")[0]
    year_short = year_full.replace(year_full[0],"").replace(year_full[1],"")
    month = str(datetime.date.today()).split("-")[1]
    day = str(datetime.date.today()).split("-")[2]
    t2_submit_date = "/"+year_short+ month+ day
    t2_submit_time = "_"+str(datetime.datetime.now().time()).replace(":","").split(".")[0]
    t2_submit_date_time = t2_submit_date + t2_submit_time
    t2_ntuple_file = "/0000/"+getMCKey(samp_dict, n)+ samp_channel+ "_Ntuple.root"
    t2_full_path = '/cms'+ t2_user_dir+ t2_crab_dir+ t2_samp_name+ t2_samp_subdir#+ t2_submit_date_time+ t2_ntuple_file

    return t2_full_path

#NICE WAY TO PRINT STRINGS
def toPrint(string, value):
    length = (len(string)+len(str(value))+2)
    line = "-"*length
    print "* "+ line +                    " *"
    print "| "+ " "*length +              " |"
    print "| "+ string+ ": "+ str(value)+ " |"
    print "| "+ " "*length +              " |"
    print "* "+ line +                    " *"

