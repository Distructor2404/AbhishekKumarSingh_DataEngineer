from xml.etree import ElementTree
import csv

xml = ElementTree.parse("dataset.xml") #Locat the XML file
csvfile = open("Final_data_set.csv", 'w', encoding='utf-8') #saving the csv file
csvfile_writer = csv.writer(csvfile)

csvfile_writer.writerow(["FinInstrmGnlAttrbts.Id","FinInstrmGnlAttrbts.FullNm","FinInstrmGnlAttrbts.ClssfctnTp","FinInstrmGnlAttrbts.NtnlCcy","FinInstrmGnlAttrbts.CmmdtyDerivInd","Issr"]) #Row Names
for fin in xml.findall(".//FinInstrmRptgRefDataDltaRpt/FinInstrm/TermntdRcrd"): #Finding the xml tags

    if (fin):
        Id = fin.find(".//FinInstrmGnlAttrbts/Id")
        Fu = fin.find("./FinInstrmGnlAttrbts/FullNm")
        Cl = fin.find("./FinInstrmGnlAttrbts/ClssfctnTp")
        Nt = fin.find("./FinInstrmGnlAttrbts/NtnlCcy")
        Cm = fin.find("./FinInstrmGnlAttrbts/CmmdtyDerivInd")
        isr =  fin.find("Issr")
        
        csv_line = [Id.text,Fu.text,Cl.text,Nt.text,Cm.text,isr.text] #pushing the data to csv file in Rows
        csvfile_writer.writerow(csv_line)
csvfile.close()
