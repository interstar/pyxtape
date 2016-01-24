import sys, os, urlparse, urllib
from subprocess import call

#sox short.au long.au longer.au

def munge(l) :
    p = urlparse.urlparse((l.split("=")[1]).strip())
    
    #return os.path.abspath(os.path.join(p.netloc, p.path))    
    return urllib.unquote((l.split("=")[1]).strip())[7:]
    

def takeN(n,xs) :
    i = 0
    while (i<(len(xs)-1)) :
        yield xs[i],xs[i+1]
        i=i+1
        

def getType(name) : return name.split(".")[-1]


def makeMix(plsName, transitionTimes) :
    trackno = 0

    f = open(plsName) 
    lines = f.readlines()[2:] 
    paths = [munge(l) for l in lines if l[0:4]=="File"]
    
    print "==== Track %s :: %s" % (trackno,paths[0])
    call(["rm","mix.wav"])
    call(["avconv","-i",paths[0],"mix.wav"])
    trackno=trackno+1    
    
    #part 1 [8,6,8,8,9,15]
    for path,cross in zip(paths[1:],transitionTimes) :
        print "==== Track %s :: %s" % (trackno,path)       
        call(["mv","mix.wav","old.wav"])
        nextType = getType(path)

        if nextType in ["flac","wma","m4a"] :
            tmp = "./tmp.wav"
            tmp2 = "./tmp2.wav"
            call(["rm",tmp])
            call(["avconv","-i",path,tmp])
        else : 
            tmp = "./tmp.%s"%nextType                       
            tmp2 = "./tmp2.%s"%nextType
            call(["cp",path,tmp])                    
       

        call(["sox",tmp,"-r","44100",tmp2])
        #call(["sox","-norm",tmp2,tmp])
    
        print "Merging %s with %s" % ("old.wav",tmp2)
        
        command = ["./crossfade_cat.sh", "%s"%cross, "old.wav", tmp2, "auto", "auto"]
        call(command)
        trackno=trackno+1    


#makeMix("list2.pls",[2,4,2,2,2,2,3,3])
if __name__ == '__main__' :
    from sys import argv
    mixname = argv[1]
    trans = argv[2]
    makeMix(argv[1],trans.split(","))
    
