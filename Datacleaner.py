import numpy as np

visualizacao_stories = [
    [187, 120, 88, 70, 130, 168, 213],
    [0, 0, 42, 0, 0, 55, 77],
    [91, 0, 61, 0, 71, 121, 271],
    [0, 0, 0, 0, 187, 0, 0],
    [42, 23, 34, 0, 39, 29, 36]
]

pessoas = ['Raquel', 'Lucas', 'Daniel', 'Natalia', 'Anderson']
dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

#Média de views
views_pessoas = np.array(visualizacao_stories)
mediavp = views_pessoas.mean(axis=0)

for dias, media in zip(dias_semana, mediavp):
    print(f"{dias}: {media}")

#Dia que teve mais views somada 
media_dia = views_pessoas.sum(axis=0)
max_views_sum = media_dia.argmax()
print(f"O dia que mais foi {dias_semana[max_views_sum]}")

#Dia que mais teve views na ultima semana
views_sp = views_pessoas.sum(axis=1)
views_semana = views_sp.argmax()
print(f"A pessoa com mais views foi {pessoas[views_semana]}")