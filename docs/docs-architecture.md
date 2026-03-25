# Arquitectura – InvControl Pro

## Descripción

El sistema utiliza una arquitectura basada en API REST desarrollada con FastAPI.

## Componentes

- Cliente (usuario / navegador)
- API (FastAPI)
- Almacenamiento en memoria

## Responsabilidades

- API: lógica del negocio
- Modelos: validación de datos
- Memoria: almacenamiento temporal

## Diagrama

```mermaid
flowchart LR
    User --> API
    API --> Memory
