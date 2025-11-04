import networkx as nx
import matplotlib.pyplot as plt

class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class Postre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None  


class ListaPostres:
    def __init__(self):
        self.postres = {}

   
    def mostrar_ingredientes(self, nombre_postre):
        if nombre_postre not in self.postres:
            print(f"El postre '{nombre_postre}' no existe.")
            return
        actual = self.postres[nombre_postre].ingredientes
        if not actual:
            print(f"El postre '{nombre_postre}' no tiene ingredientes registrados.")
            return
        print(f"Ingredientes del postre '{nombre_postre}':")
        while actual:
            print(f" - {actual.nombre}")
            actual = actual.siguiente

    
    def insertar_ingrediente(self, nombre_postre, nuevo_ingrediente):
        if nombre_postre not in self.postres:
            print(f"El postre '{nombre_postre}' no existe.")
            return
        nuevo = NodoIngrediente(nuevo_ingrediente)
        cabeza = self.postres[nombre_postre].ingredientes
        if not cabeza:
            self.postres[nombre_postre].ingredientes = nuevo
        else:
            actual = cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        print(f"Ingrediente '{nuevo_ingrediente}' agregado a '{nombre_postre}'.")

    def eliminar_ingrediente(self, nombre_postre, ingrediente):
        if nombre_postre not in self.postres:
            print(f"El postre '{nombre_postre}' no existe.")
            return
        actual = self.postres[nombre_postre].ingredientes
        anterior = None
        while actual:
            if actual.nombre == ingrediente:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.postres[nombre_postre].ingredientes = actual.siguiente
                print(f"Ingrediente '{ingrediente}' eliminado de '{nombre_postre}'.")
                return
            anterior = actual
            actual = actual.siguiente
        print(f"Ingrediente '{ingrediente}' no encontrado en '{nombre_postre}'.")

    def alta_postre(self, nombre_postre, lista_ingredientes):
        if nombre_postre in self.postres:
            print(f"El postre '{nombre_postre}' ya existe.")
            return
        nuevo_postre = Postre(nombre_postre)
        cabeza = None
        anterior = None
        for ing in lista_ingredientes:
            nodo = NodoIngrediente(ing)
            if cabeza is None:
                cabeza = nodo
            else:
                anterior.siguiente = nodo
            anterior = nodo
        nuevo_postre.ingredientes = cabeza
        self.postres[nombre_postre] = nuevo_postre
        print(f"Postre '{nombre_postre}' dado de alta correctamente.")

    def baja_postre(self, nombre_postre):
        if nombre_postre not in self.postres:
            print(f"El postre '{nombre_postre}' no existe.")
            return
        del self.postres[nombre_postre]
        print(f"Postre '{nombre_postre}' eliminado correctamente.")

    def mostrar_postres(self):
        if not self.postres:
            print("No hay postres registrados.")
            return
        print("Lista de postres:")
        for nombre in sorted(self.postres.keys()):
            print(f" - {nombre}")

    def graficar(self):
        if not self.postres:
            print("No hay postres para graficar.")
            return

        G = nx.DiGraph()
        pos = {}
        x, y = 0, 0

        for i, (nombre, postre) in enumerate(sorted(self.postres.items())):
            postre_node = f"POSTRE: {nombre}"
            G.add_node(postre_node)
            pos[postre_node] = (x, y)

            
            actual = postre.ingredientes
            last_node = postre_node
            ing_x = x + 1
            while actual:
                ing_node = f"{nombre}-{actual.nombre}"
                G.add_node(ing_node)
                G.add_edge(last_node, ing_node)
                pos[ing_node] = (ing_x, y)
                last_node = ing_node
                ing_x += 1
                actual = actual.siguiente
            y -= 1.5

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue",
                arrows=True, font_size=9, font_weight="bold")
        plt.title("Estructura de datos: POSTRES → INGREDIENTES")
        plt.show()


if __name__ == "__main__":
    sistema = ListaPostres()

    sistema.alta_postre("Pay de Limón", ["limón", "galleta", "leche condensada"])
    sistema.alta_postre("Brownie", ["chocolate", "harina", "azúcar", "huevo"])
    sistema.alta_postre("Flan", ["leche", "huevo", "azúcar"])

    sistema.insertar_ingrediente("Brownie", "nueces")
    sistema.eliminar_ingrediente("Flan", "huevo")

    sistema.mostrar_postres()
    sistema.mostrar_ingredientes("Brownie")

    
    sistema.graficar()

    #2
    def eliminar_repetidos(self):
        print("\n=== Eliminando elementos repetidos de POSTRES ===")

        nombres_unicos = {}
        for nombre, postre in list(self.postres.items()):
            if nombre not in nombres_unicos:
                nombres_unicos[nombre] = postre
            else:
                print(f"Postre duplicado '{nombre}' eliminado.")
                del self.postres[nombre]

        
        for nombre, postre in self.postres.items():
            vistos = set()
            actual = postre.ingredientes
            anterior = None
            while actual:
                if actual.nombre in vistos:
                    print(f"Ingrediente duplicado '{actual.nombre}' eliminado de '{nombre}'.")
                    
                    if anterior:
                        anterior.siguiente = actual.siguiente
                    else:
                     
                        postre.ingredientes = actual.siguiente
                else:
                    vistos.add(actual.nombre)
                    anterior = actual
                actual = actual.siguiente

        print("=== Eliminación de duplicados finalizada ===\n")
