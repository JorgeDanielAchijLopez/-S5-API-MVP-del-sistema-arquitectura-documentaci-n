# -S5-API-MVP-del-sistema-arquitectura-documentaci-n
# InvControl Pro API

Sistema de gestión de inventario, ventas y control básico financiero.

## Problema

Muchos negocios pequeños gestionan inventario y ventas de forma manual, lo que genera errores, pérdida de control del stock y dificultad para conocer las ganancias reales.

## Solución

InvControl Pro permite:

- Registrar productos
- Controlar inventario
- Registrar ventas
- Actualizar stock automáticamente

## Tecnologías

- Python
- FastAPI
- Uvicorn

## Cómo ejecutar

```bash
pip install fastapi uvicorn
python -m uvicorn main:app --reload
