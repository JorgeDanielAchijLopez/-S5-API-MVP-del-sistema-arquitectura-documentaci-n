# InvControl Pro API

Sistema de gestión de inventario y ventas desarrollado como MVP técnico para pequeños y medianos negocios.

## Problema

Muchos negocios gestionan su inventario y ventas de forma manual (Excel o papel), lo que genera errores en el control de stock, diferencias entre inventario físico y sistema, y falta de claridad sobre las ganancias.

## Solución

InvControl Pro permite registrar productos, controlar inventario, registrar ventas y actualizar el stock automáticamente mediante una API REST.

## Flujo principal

Crear producto → Consultar producto → Registrar venta → Actualizar stock automáticamente

## Tecnologías

Python, FastAPI, Uvicorn, OpenAPI

## Ejecución local
Instalar dependencias:

pip install fastapi uvicorn

Ejecutar la API:

python -m uvicorn main:app --reload

Abrir en el navegador:

http://127.0.0.1:8000/docs
