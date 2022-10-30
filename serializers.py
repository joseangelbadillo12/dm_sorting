from bubble_sort import bubble_sort
from quick_sort import quick_sort
import json

def serializeValues(values):
    
    data = {
        "id_indicador" : [],
        "indicador" : [],
        "anio" : [],
        "valor" : [],
        "unidad_medida" : [],
    }
    for value in values:
        value['valor'] = float(value['valor'])
        data[value['indicador']].append(value)
    

    quick_sort(data['valor'],0,len(data['valor'])-1)
    quick_sort(data['anio'],0,len(data['anio'])-1)
    bubble_sort(data['id_indicador'])
    bubble_sort(data['indicador'])

    final_array = []
    for i in data.values():
        final_array.extend(i)
    return final_array