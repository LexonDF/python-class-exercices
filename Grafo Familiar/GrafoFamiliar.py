import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D

# 1. Inicializar el grafo
G = nx.Graph()

# 2. Definir el centro de la red y las comunidades
centro = "Diego Figueredo"

familia = [
    "William Figueredo",
    "Cristian Figueredo",
    "Daniela Figueredo",
    "Tatiana Figueredo",
    "Martin",
    "Lucas",
]

universidad = [
    "Deiber Rodriguez",
    "Angelo Jerez",
    "Nicolas Prieto",
    "Snaider Castro",
    "Andres Rodriguez",
    "Sofia Martinez",
    "Paula Homez",
    "Juan Pencue",
    "Samuel Santander",
]

barrio = [
    "Sebastian Murillo",
    "Nicol Soler",
    "Nathan Gonzales",
    "Jeisson Rodriguez",
]

# 3. Agregar nodos con su respectivo atributo de comunidad
G.add_node(centro, comunidad="Centro")

for persona in familia:
  G.add_node(persona, comunidad="Familia")

for persona in universidad:
  G.add_node(persona, comunidad="Universidad")

for persona in barrio:
  G.add_node(persona, comunidad="Barrio")

# 4. Agregar conexiones (aristas)
# Conectar a Diego con todos los integrantes de su red
for persona in familia + universidad + barrio:
  G.add_edge(centro, persona)

# --- Conexiones internas (Relaciones secundarias) ---

# Familia (Relaciones humanas)
G.add_edge("William Figueredo", "Cristian Figueredo")
G.add_edge("William Figueredo", "Daniela Figueredo")
G.add_edge("William Figueredo", "Tatiana Figueredo")
G.add_edge("Cristian Figueredo", "Daniela Figueredo")

# Relaciones de las Mascotas (Martin y Lucas con la familia y entre ellos)
G.add_edge("Martin", "Lucas")  # Las mascotas se relacionan entre sí
G.add_edge("Martin", "William Figueredo")  # Vínculo con el padre
G.add_edge("Lucas", "Daniela Figueredo")  # Vínculo cercano con hermanos
G.add_edge("Martin", "Tatiana Figueredo")

# Universidad (Compañeros interconectados)
G.add_edge("Deiber Rodriguez", "Angelo Jerez")
G.add_edge("Deiber Rodriguez", "Nicolas Prieto")
G.add_edge("Angelo Jerez", "Snaider Castro")
G.add_edge("Nicolas Prieto", "Andres Rodriguez")
G.add_edge("Snaider Castro", "Andres Rodriguez")
G.add_edge("Sofia Martinez", "Paula Homez")
G.add_edge("Sofia Martinez", "Juan Pencue")
G.add_edge("Paula Homez", "Samuel Santander")
G.add_edge("Juan Pencue", "Samuel Santander")
G.add_edge("Andres Rodriguez", "Sofia Martinez")

# Barrio
G.add_edge("Sebastian Murillo", "Nicol Soler")
G.add_edge("Nathan Gonzales", "Jeisson Rodriguez")
G.add_edge("Sebastian Murillo", "Nathan Gonzales")

# 5. Asignar colores a los nodos según su comunidad
colores_comunidad = {
    "Centro": "#ff4d4d",  # Rojo suave (Diego)
    "Familia": "#4da6ff",  # Azul claro
    "Universidad": "#5cd65c",  # Verde claro
    "Barrio": "#ffbb33",  # Naranja
}

node_colors = [
    colores_comunidad[G.nodes[node].get("comunidad", "Centro")]
    for node in G.nodes()
]

# 6. Configurar la visualización del grafo
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, seed=42, k=0.18)

# Dibujar nodos, aristas y etiquetas
nx.draw_networkx_nodes(
    G, pos, node_color=node_colors, node_size=850, alpha=0.92
)
nx.draw_networkx_edges(G, pos, width=1.2, alpha=0.4, edge_color="gray")
nx.draw_networkx_labels(
    G,
    pos,
    font_size=9,
    font_family="sans-serif",
    font_weight="bold",
    font_color="#222222",
)

# 7. Crear leyenda personalizada
legend_elements = [
    Line2D(
        [0],
        [0],
        marker="o",
        color="w",
        label="Centro de Red (Diego)",
        markerfacecolor="#ff4d4d",
        markersize=12,
    ),
    Line2D(
        [0],
        [0],
        marker="o",
        color="w",
        label="Familia y Mascotas",
        markerfacecolor="#4da6ff",
        markersize=12,
    ),
    Line2D(
        [0],
        [0],
        marker="o",
        color="w",
        label="Amigos Universidad (Interconectados)",
        markerfacecolor="#5cd65c",
        markersize=12,
    ),
    Line2D(
        [0],
        [0],
        marker="o",
        color="w",
        label="Amigos de Barrio",
        markerfacecolor="#ffbb33",
        markersize=12,
    ),
]

plt.legend(
    handles=legend_elements,
    loc="upper right",
    title="Comunidades de la Red",
    fontsize=10,
    title_fontsize=11,
)

plt.title(
    "Red Social Personal - Diego Figueredo (Familia, Mascotas y Amigos)",
    fontsize=16,
    fontweight="bold",
    pad=20,
)
plt.axis("off")
plt.tight_layout()

# 8. Mostrar la imagen resultante
plt.show()