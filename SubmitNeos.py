
def Neos():
    import sys
    import xmlrpc.server
    import xmlrpc.client


    NEOS_HOST="neos-server.org"
    NEOS_PORT=3333

    # Connect to NEOS
    neos = xmlrpc.client.ServerProxy("https://%s:%d" % (NEOS_HOST, NEOS_PORT))
    xmlfile = open("Neos.txt", 'r')
    xml = ""
    buffer = 1
    while buffer:
        buffer = xmlfile.read()
        xml += buffer
    xmlfile.close()
    (jobNumber, password) = neos.submitJob(xml)
    offset = 0
    status = ""
    while status != "Done":
                (msg, offset) = neos.getIntermediateResults(jobNumber, password, offset)
                status = neos.getJobStatus(jobNumber, password)
    msg3 = neos.getFinalResults(jobNumber, password).data
    es=str(msg3.decode("utf-8"))
    es = es.split('\n', 1)[-1]
    f=open('RtaNeos.csv',"w")        
    f.write(es)
    f.close()



def AlistamientoTexto():
    d=input("Ingresa el número de arboles quiere generar")
    with open("Part1.txt", "r") as myfile:
        data1=myfile.read()
    myfile.close()
    with open("model.txt", "r") as myfile:
        data2=myfile.read()
    myfile.close()
    with open("Part2.txt", "r") as myfile:
        data3=myfile.read()
    myfile.close()

    with open("data.txt", "r") as myfile:
        data4=myfile.read()
    myfile.close()

    with open("Part3.txt", "r") as myfile:
        data5=myfile.read()
    myfile.close()
    total=data1+data2+data3+data4+data5
    f=open('Neos.txt',"w") 
    f.write(total)
    f.close()

AlistamientoTexto()
Neos()

