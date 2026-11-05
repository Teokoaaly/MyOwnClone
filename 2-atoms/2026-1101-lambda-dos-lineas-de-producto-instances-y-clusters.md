---
id: 2026-1101-lambda-dos-lineas-de-producto-instances-y-clusters
type: atom
certainty: solid
sources: [sources/2026-11-01-lambda-gpu-pricing.md]
links: ["[[2026-1101-lambda-1-click-clusters-minimo-16-gpus-y-escala-hasta-2000]]", "[[2026-1101-lambda-cluster-mas-caro-que-la-instancia-del-mismo-gpu]]", "[[2026-1101-lambda-precio-reservado-1-ano-sin-publicar]]"]
---

## Claim
Lambda publica la página de precios con **dos líneas de producto claramente separadas**: "Instances pricing" — *"Deploy NVIDIA B200, H100, A100, or GH200 instances in minutes with self-serve, first-come access"*, con CTA "Launch GPU instance" y precio público por GPU/hora — y "1-Click Clusters pricing" — *"Production-ready clusters from 16 to 2,000+ NVIDIA B200 or H100 GPUs"*, donde **todas las filas tienen como CTA "Talk to our team"** en lugar de precio de autoservicio, más un tercer peldaño "Superclusters" mencionado en la cabecera sin tabla.

## Why It Matters
Explica por qué la página tiene dos lógicas de precio distintas y por qué el vault debe leerlas como dos mercados: el precio público es solo del tramo self-serve, y el tramo grande (cluster y capacidad reservada) **no tiene precio público**, se negocia. Para el vault esto importa porque el precio que se cita en cualquier comparación ("Lambda cuesta X") es el del tramo self-serve, que es el que nadie usa para training y el que sí usa alguien que quiere una máquina suelta. La distinción Instances/Clusters/Superclusters es además el mismo eje que separa producto gestionado de producto de plataforma en todo el corpus del vault.

## Nota de extensión 2026-11-03
Ambas desciciones son verbatim de `sources/2026-11-01-lambda-gpu-pricing.md` (secciones "1-Click Clusters pricing" e "Instances pricing"). La captura del 2026-10-31 y la del 2026-11-02 contienen solo estas dos líneas, no Superclusters.
