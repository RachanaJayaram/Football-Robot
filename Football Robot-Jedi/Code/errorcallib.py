import motion as m
def error_store():
        filename=raw_input("Enter surface name: ")

        try:
                f=open(filename+".txt","r")
                content=f.read()

        except IOError:


                return(error(filename))


        if content=='':

                return(error(filename))
                f.close()

        if content!='':

                ans=raw_input("Surface exists in database do you want to recallibrate?y/n: ")

                if (ans=='n'):

                        listie=content.split()
                        listie=listie[0].split(',')

                        e1=float(listie[0])
                        e2=float(listie[1])
                        f.close()

                        print(e1)
                        print(e2)
                        return((e1,e2))
                else:
                        return(error(filename))
                        f.close()


def error(surfacename):
        f=1

        print("\n\nERROR CALLIBRATION \n\n")
        rac=raw_input("start?")

        while(f==1):
                print("\nGOING  50  forward : \n")
                m.forward(50)
                x=int(raw_input("How far did it go?\n\n"))
                e1=50.0/x
                print(e1)
                y=raw_input("Continue?(y/n)\n")


                print("\nGOING  30  forward : \n")
                m.forward(30,e1)
                x=int(raw_input("How far did it go?\n\n"))
                e1=e1*(30.0/x)
                print(e1)
                y=raw_input("Continue?(y/n)\n")

                print("\nGOING  40  forward : \n")
                m.forward(40,e1)
                x=int(raw_input("How far did it go?\n\n\n"))
                e1=e1*(40.0/x)
                print(e1)
                y=raw_input("Continue?(y/n)\n")


                print("\nGOING  50  forward : \n")
                m.forward(50,e1)
                x=raw_input("\n\n\n\n\nProceed further?(y/n)\n")
                if(x=='y'):
                        f=0;
        f=1
        while(f==1):
                print("\n\n\n\n\nGOING 90 clockwise : \n")
                m.clockwise(90)
                x=int(raw_input("How much did it turn?\n\n"))
                e2=90.0/x
                print(e2)
                y=raw_input("Continue?(y/n)\n")

                print("\nGOING 180 clockwise : \n")
                m.clockwise(180,e2)
                x=int(raw_input("How much did it turn?\n\n"))
                e2*=(180.0/x)
                print(e2)

                y=raw_input("Continue?(y/n)\n")

                print("\nGOING 270 clockwise : \n")
                m.clockwise(270,e2)
                x=int(raw_input("How much did it turn?\n\n"))
                e2*=(270.0/x)
                print(e2)
                y=raw_input("Continue?(y/n)\n")



                print("\nGOING 360 clockwise : \n\n")
                m.clockwise(360,e2)
                x=int(raw_input("How much did it turn?\n"))
                e2*=(360.0/x)
                print(e2)

                y=raw_input("Continue?(y/n)\n")


                print("\nGOING 60 clockwise : \n")
                m.clockwise(60,e2)
                x=raw_input("\n\n\n\n\nProceed further?(y/n)\n")
                if(x=='y'):

                        f=0;

        f=open(surfacename+".txt","w+")
        f.write(str(e1)+','+str(e2)+"\n")
        f.close()
        print("DATA STORED\n")
        x=raw_input("continue?")
        if(x):
            return((e1,e2))
