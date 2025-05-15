class Numeros:
    def pedirnum(self):
        N1=float(input("Por favor ingrese el primer numero: "))
        N2=float(input("Por favor ingrese el segundo numero: "))
        return(N1,N2)
    
class Suma:
    def sumar(self, N1,N2):
        sum=N1+N2
        return sum
    
class Resta:
    def restar(self, N1, N2):
        res=N1-N2
        return res
    
class Multiplicacion:        
    def multiplicar(self, N1, N2):
        mult=N1*N2
        return mult

class Division:
    def dividir(self, N1, N2):
        try:
            div=N1/N2
            return div  
        except ZeroDivisionError:
            print("\n ERROR!! No se puede divir entre 0")
class main: 
    def iniciar(self):
        rep=0         
        while (rep==0):
            print("\n**************** CALCULADORA EN PYHTON ****************\n\n")
            print("Seleccione la operacion que desea realizar:")
            print("[1] Sumar")
            print("[2] Restar")     
            print("[3] Multiplicar")
            print("[4] Dividir")
            try:
                selec=int(input())   
                if selec in [1, 2, 3, 4]:
                    num= Numeros()
                    N1, N2= num.pedirnum()
                    match selec:
                        case 1:
                            s=Suma()
                            print("\nEl resultado es: ", s.sumar(N1,N2))
                        case 2:
                            r=Resta()
                            print("\nEl resultado es: ", r.restar(N1,N2))
                        case 3:
                            m=Multiplicacion()
                            print("\nEl resultado es: ", m.multiplicar(N1,N2))
                        case 4:
                            d=Division()
                            print("\nEl resultado es: ", d.dividir(N1,N2))
                else:
                    print("Opción invalida ")
            except ValueError:
                print("Por favor ingrese un digito valido")  
            try:     
                rep=int(input("\nSi desea hacer otra operacion presione  [0] "))
            except ValueError: 
                print("Por favor ingrese un digito numerico")
                rep=int(input("Seleccione 0 si desea hacer otra operación"))
        print("\nGracias por usar la calculadora de Python\n\nSaliendo...")    
