# Diccionarios Iniciales
productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10.0, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8.0, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1.0, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2.0, False, False],
}

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
}

# Funciones de Validación
def val_no_vacio(texto): return texto.strip() != ""
def val_peso(peso): return peso > 0
def val_sn(opcion): return opcion.lower() in ['s', 'n']
def val_entero_positivo(num): return num > 0
def val_unidades(unidades): return unidades >= 0

def buscar_codigo(codigo, productos, stock):
    return codigo.upper() in productos

#
def unidades_categoria(categoria, productos, stock):
    total = 0
    cat_buscada = categoria.lower()
    for codigo, datos in productos.items():
        if datos[1].lower() == cat_buscada:
            total += stock[codigo][1]
    print(f"El total de unidades disponibles es: {total}")

def busqueda_precio(p_min, p_max, productos, stock):
    resultados = []
    for codigo, datos in stock.items():
        precio = datos[0]
        unidades = datos[1]
        if p_min <= precio <= p_max and unidades > 0:
            nombre = productos[codigo][0]
            resultados.append(f"{nombre}--{codigo}")
    
    if not resultados:
        print("No hay productos en ese rango de precios.")
    else:
        resultados.sort()
        print(f"Los productos encontrados son: {resultados}")

def actualizar_precio(codigo, nuevo_precio, productos, stock):
    if buscar_codigo(codigo, productos, stock):
        stock[codigo.upper()][0] = nuevo_precio
        return True
    return False

def eliminar_producto(codigo, productos, stock):
    if buscar_codigo(codigo, productos, stock):
        cod = codigo.upper()
        del productos[cod]
        del stock[cod]
        return True
    return False

def agregar_producto(codigo, nombre, cat, marca, peso, imp, cach, precio, unidades, productos, stock):
    if buscar_codigo(codigo, productos, stock):
        return False
    productos[codigo.upper()] = [nombre, cat, marca, peso, imp == 's', cach == 's']
    stock[codigo.upper()] = [precio, unidades]
    return True

def leer_opcion():
    try:
        op = int(input("Ingrese opción: "))
        if 1 <= op <= 6: return op
    except ValueError:
        pass
    print("Debe seleccionar una opción válida")
    return None

# Programa Principal
def main():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría\n2. Búsqueda de productos por rango de precio")
        print("3. Actualizar precio de producto\n4. Agregar producto")
        print("5. Eliminar producto\n6. Salir")
        print("=====================================")
        
        op = leer_opcion()
        
        if op == 1:
            cat = input("Ingrese categoría a consultar: ")
            unidades_categoria(cat, productos, stock)
            
        elif op == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= p_min:
                        busqueda_precio(p_min, p_max, productos, stock)
                        break
                    else: print("Rangos inválidos.")
                except ValueError: print("Debe ingresar valores enteros")
                
        elif op == 3:
            while True:
                cod = input("Ingrese código del producto: ")
                pre = int(input("Ingrese nuevo precio: "))
                if actualizar_precio(cod, pre, productos, stock):
                    print("Precio actualizado")
                else: print("El código no existe")
                if input("¿Desea actualizar otro precio (s/n)?: ").lower() != 's': break
                
        elif op == 4:
            c = input("Código: "); n = input("Nombre: "); cat = input("Categoría: ")
            m = input("Marca: "); p = float(input("Peso (kg): ")); imp = input("¿Es importado? (s/n): ")
            cach = input("¿Es para cachorro? (s/n): "); pre = int(input("Precio: ")); u = int(input("Unidades: "))
            
            if all([val_no_vacio(c), val_no_vacio(n), val_no_vacio(cat), val_no_vacio(m), 
                    val_peso(p), val_sn(imp), val_sn(cach), val_entero_positivo(pre), val_unidades(u)]):
                if agregar_producto(c, n, cat, m, p, imp, cach, pre, u, productos, stock):
                    print("Producto agregado")
                else: print("El código ya existe")
            else: print("Datos inválidos, no se registró el producto.")
            
        elif op == 5:
            cod = input("Ingrese código: ")
            if eliminar_producto(cod, productos, stock): print("Producto eliminado")
            else: print("El código no existe")
            
        elif op == 6:
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()

# Fin del Programa 