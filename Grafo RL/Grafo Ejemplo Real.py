import networkx as nx
import matplotlib.pyplot as plt

# 1. Crear un grafo dirigido (árbol de decisión)
arbol_transporte = nx.DiGraph()

# 2. Definir las conexiones entre decisiones y resultados
conexiones = [
    ("¿Llueve en Bogotá?", "Sí (Lluvia)"),
    ("¿Llueve en Bogotá?", "No (Buen Tiempo)"),
    
    ("Sí (Lluvia)", "¿Tiene Pico y Placa?"),
    ("No (Buen Tiempo)", "¿Es Hora Pico?"),
    
    ("¿Tiene Pico y Placa?", "Sí: Ir en TransMilenio / SITP"),
    ("¿Tiene Pico y Placa?", "No: Ir en Carro Particular"),
    
    ("¿Es Hora Pico?", "Sí: Usar Ciclorruta / TransMilenio"),
    ("¿Es Hora Pico?", "No: Carro / Moto / Taxi")
]

arbol_transporte.add_edges_from(conexiones)

# 3. Definir coordenadas (x, y) para darle estructura jerárquica de árbol
posiciones = {
    "¿Llueve en Bogotá?": (0, 3),
    "Sí (Lluvia)": (-2, 2),
    "No (Buen Tiempo)": (2, 2),
    "¿Tiene Pico y Placa?": (-2, 1),
    "¿Es Hora Pico?": (2, 1),
    "Sí: Ir en TransMilenio / SITP": (-3.5, 0),
    "No: Ir en Carro Particular": (-0.8, 0),
    "Sí: Usar Ciclorruta / TransMilenio": (0.8, 0),
    "No: Carro / Moto / Taxi": (3.5, 0)
}

# 4. Dibujar el grafo
plt.figure(figsize=(12, 6))
nx.draw(
    arbol_transporte, 
    posiciones, 
    with_labels=True, 
    node_color='#90caf9', 
    node_size=3200, 
    font_size=8, 
    font_weight='bold', 
    arrows=True, 
    arrowsize=15, 
    edge_color='#555555'
)

plt.title("Árbol de Decisión Cotidiano: Transporte en Bogotá", fontsize=14, fontweight='bold')
plt.show()