import random
#0 
print("Tanuló adatai egy sorban.")

#1
adatSorBe=input("Kérem a tanuló adatait ';'-vel elválasztva: ")
reszletek = adatSorBe.split(';')

tanulo={}
tanulo['nev']=reszletek[0]
tanulo['szId']=reszletek[1]
tanulo['magassag']=int(reszletek[2])
tanulo['tomeg']=float(reszletek[3].replace(',' , '.'))

#2
tanulo['nev']='Váradi László'
tanulo['szId']=str(random.randint(2000,2005))+'.'+str(random.randint(1,12))+'.'+str(random.randint(1,28))
tanulo['magassag']=random.randint(150,220)
tanulo['tomeg']=random.randint(65,100)+random.random()

#3
reszletek[0]=tanulo['nev']
reszletek[1]=tanulo['szId']
reszletek[2]=str(tanulo['magassag'])
reszletek[3]=str(tanulo['tomeg'])
adatSorKi = "#" .join(reszletek)
print(adatSorKi)