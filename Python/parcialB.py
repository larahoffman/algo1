# Parcial Comision B
from queue import Queue as Cola

def copiar_cola(c:Cola[tuple]) -> Cola[tuple]:
    cola_aux = Cola()
    res = Cola()

    while(not c.empty()):
        elemento:tuple = c.get()
        cola_aux.put(elemento)
    while(not cola_aux.empty()):
        elemento:tuple = cola_aux.get()
        c.put(elemento)
        res.put(elemento)
    return res

def reordenar_cola_priorizando_vips(filaClientes:Cola[tuple]) -> Cola[str]:
    cola_aux = copiar_cola(filaClientes)
    resultado = Cola()
    lista_vips:list = []
    lista_comunes:list = []

    while(not cola_aux.empty()):
        cliente:tuple = cola_aux.get()
        if cliente[1] == "vip":
            lista_vips.append(cliente)
        elif cliente[1] == "comun":
            lista_comunes.append(cliente)
    for cliente_vip in lista_vips:
        resultado.put(cliente_vip[0])
    for cliente_comun in lista_comunes:
        resultado.put(cliente_comun[0])
    return resultado

cola = Cola()
cola.put(("Pepe", "vip"))
cola.put(("Ana", "vip"))
cola.put(("Juancito", "comun"))
cola.put(("Yesi", "vip"))
cola.put(("Ricardo", "comun"))
print(reordenar_cola_priorizando_vips(cola).queue)
