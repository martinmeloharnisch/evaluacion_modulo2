import locale
locale.setlocale(locale.LC_ALL, '')
lista = []
while True:
    print("")
    a=str(input("Ingresar valor número: "))
    aaa=str(a.isdigit())
    aaaa=str("True")
    #print(aaa)
    if aaa == aaaa:
        Asx = []
        #bucle para agregar separar los valores númericos
        for i in a:
            i=int(i) #se trasforma en número
            Asx.append(i)
            #print(Asx)
        z=len(Asx)
        
        def imprimir(aa,bb,cc,dd,ee,ff):
            a=" +-+ "
            a1=" | |"
            a2=" | |"
            a3=" | |"
            a4=" | |"
            a5=" | |"
            a6=" | |"
            a7=" | |"
            a8=" | |"
            a9=" | |"
            b=" +-+ " 
            b1=" | |"
            b2=" | |"
            b3=" | |"
            b4=" | |"
            b5=" | |"
            b6=" | |"
            b7=" | |"
            b8=" | |"
            b9=" | |"
            c=" +-+ " 
            c1=" | |"
            c2=" | |"
            c3=" | |"
            c4=" | |"
            c5=" | |"
            c6=" | |"
            c7=" | |"
            c8=" | |"
            c9=" | |"
            d=" +-+ " 
            d1=" | |"
            d2=" | |"
            d3=" | |"
            d4=" | |"
            d5=" | |"
            d6=" | |"
            d7=" | |"
            d8=" | |"
            d9=" | |"
            e=" +-+ " 
            e1=" | |"
            e2=" | |"
            e3=" | |"
            e4=" | |"
            e5=" | |"
            e6=" | |"
            e7=" | |"
            e8=" | |"
            e9=" | |"
            f=" +-+ "
            f1=" | |"
            f2=" | |"
            f3=" | |"
            f4=" | |"
            f5=" | |"
            f6=" | |"
            f7=" | |"
            f8=" | |"
            f9=" | |"
            ##########################################################
            if aa>=1:
                a9=" xxx"
            if aa>=2:
                a8=" xxx"
            if aa>=3:
                a7=" xxx"
            if aa>=4:
                a6=" xxx"
            if aa>=5:
                a5=" xxx"
            if aa>=6:
                a4=" xxx"
            if aa>=7:
                a3=" xxx"
            if aa>=8:
                a2=" xxx"
            if aa>=9:
                a1=" xxx"
            ##########################################################
            if bb>=1:
                b9=" xxx"
            if bb>=2:
                b8=" xxx"
            if bb>=3:
                b7=" xxx"
            if bb>=4:
                b6=" xxx"
            if bb>=5:
                b5=" xxx"
            if bb>=6:
                b4=" xxx"
            if bb>=7:
                b3=" xxx"
            if bb>=8:
                b2=" xxx"
            if bb>=9:
                b1=" xxx"
            ##########################################################
            if cc>=1:
                c9=" xxx"
            if cc>=2:
                c8=" xxx"
            if cc>=3:
                c7=" xxx"
            if cc>=4:
                c6=" xxx"
            if cc>=5:
                c5=" xxx"
            if cc>=6:
                c4=" xxx"
            if cc>=7:
                c3=" xxx"
            if cc>=8:
                c2=" xxx"
            if cc>=9:
                c1=" xxx"
            ##########################################################
            if dd>=1:
                d9=" xxx"
            if dd>=2:
                d8=" xxx"
            if dd>=3:
                d7=" xxx"
            if dd>=4:
                d6=" xxx"
            if dd>=5:
                d5=" xxx"
            if dd>=6:
                d4=" xxx"
            if dd>=7:
                d3=" xxx"
            if dd>=8:
                d2=" xxx"
            if dd>=9:
                d1=" xxx"
            ##########################################################
            if ee>=1:
                e9=" xxx"
            if ee>=2:
                e8=" xxx"
            if ee>=3:
                e7=" xxx"
            if ee>=4:
                e6=" xxx"
            if ee>=5:
                e5=" xxx"
            if ee>=6:
                e4=" xxx"
            if ee>=7:
                e3=" xxx"
            if ee>=8:
                e2=" xxx"
            if ee>=9:
                e1=" xxx"
            ##########################################################
            if ff>=1:
                f9=" xxx"
            if ff>=2:
                f8=" xxx"
            if ff>=3:
                f7=" xxx"
            if ff>=4:
                f6=" xxx"
            if ff>=5:
                f5=" xxx"
            if ff>=6:
                f4=" xxx"
            if ff>=7:
                f3=" xxx"
            if ff>=8:
                f2=" xxx"
            if ff>=9:
                f1=" xxx"
         #######################################################  
         # Agregar valores bajo el abaco  
            z1,z2,z3,z4,z5,z6="       ","       ","     ","    ","    ","  "
            if a9==" xxx":
                z1=int(100000)
            if b9==" xxx":
                z2=int(10000)
            if c9==" xxx":
                z3=int(1000)
        #
            if d9==" xxx":
                z4=int(100)
        #
            if e9==" xxx":
                z5=int(10)
        #
            if f9==" xxx":
                z6=int(1)

            print("  ",a," ", b," ",c," ",d," ",e," ",f)
            print("  ",a1,"  ",b1,"  ",c1,"  ",d1,"  ",e1,"  ",f1)
            print("  ",a2,"  ",b2,"  ",c2,"  ",d2,"  ",e2,"  ",f2)
            print("  ",a3,"  ",b3,"  ",c3,"  ",d3,"  ",e3,"  ",f3)
            print("  ",a4,"  ",b4,"  ",c4,"  ",d4,"  ",e4,"  ",f4)
            print("  ",a5,"  ",b5,"  ",c5,"  ",d5,"  ",e5,"  ",f5)
            print("  ",a6,"  ",b6,"  ",c6,"  ",d6,"  ",e6,"  ",f6)
            print("  ",a7,"  ",b7,"  ",c7,"  ",d7,"  ",e7,"  ",f7)
            print("  ",a8,"  ",b8,"  ",c8,"  ",d8,"  ",e8,"  ",f8)
            print("  ",a9,"  ",b9,"  ",c9,"  ",d9,"  ",e9,"  ",f9)
            print(" ",z1," ",z2," ",z3,"   ",z4,"   ",z5,"    ",z6)
            
        if z==6:
            imprimir(int(Asx[0]),int(Asx[1]),int(Asx[2]),int(Asx[3]),int(Asx[4]),int(Asx[5]))
        elif z>6: #Valor mal ingresado mas de 6 digitos
            print("Valor mal ingresado")
        else: #agregar ceros
            z=6-z
            #print(z)
            Asx.reverse()
            for i in range(z):
                Asx.append(0)
            Asx.reverse()
            print(Asx)
            imprimir(int(Asx[0]),int(Asx[1]),int(Asx[2]),int(Asx[3]),int(Asx[4]),int(Asx[5]))

        lista.append(a) #agrega al final de la lista el valor de variable a
        pregunta_final=str(input("¿Continuar con el programa? si o no. : "))
        if pregunta_final=="no": #termino de bucle e imprimir la lista de valores ingresados
            print("Historial de ingresos:")
            #n=1
            for i in lista:
                i=int(i)
                J= locale.format_string('%.f', i, grouping=True, monetary=True)
                print(J)
            break

    else:
        print("No ingresaste numeros")