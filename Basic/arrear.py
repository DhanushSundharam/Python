students=["abithverson","Arunkarthick","dhanishwar","dhanaraj","gopi","ruban","gowtham","xlzm"]
def paidarrearfees(x):
    if (x[0]=="a" or x[0]=="A") or (x[0]=="g" or x[0]=="G"):
        print ( f"{x} this guys are not paid in  arear fees")
    else:
        print( f"{x} you are paid ")
(list(map(paidarrearfees,students)))
