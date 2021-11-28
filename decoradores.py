
def funcion_decoradora(funcion_parametro):
    def funcion_interior():

        # Acciones adicionales que decoran
        print("vamos a realizar un calculo: ")


        funcion_parametro()

        # Acciones adicionales que decoran
        print("Hemos terminado el calculo")
    
    return funcion_interior




@funcion_decoradora
def suma():
    print(15 + 20)


@funcion_decoradora
def resta():
    print(30 - 10)


suma()
resta()