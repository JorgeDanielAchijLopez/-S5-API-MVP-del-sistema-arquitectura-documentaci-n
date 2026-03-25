
---


```markdown
# Requirements – InvControl Pro

## Backlog

Trello:
https://trello.com/invite/b/69a13d69fc56024f57f95125/ATTIfdd25a428ed3c6fcf224fff46a57acd0C0F953F1/invcontrol-pro-product-backlog 

## Historias de Usuario

1. Registrar productos (Must)
2. Registrar ventas (Must)
3. Conciliar inventario (Must)
4. Registrar facturas (Must)
5. Ver reportes (Should)
6. Historial de movimientos (Should)
7. Gestión de usuarios (Could)
8. Exportar PDF (Won’t)

## Historias con Given/When/Then

### Historia 1: Registrar producto

Given que el usuario está en el sistema  
When ingresa un producto válido  
Then el sistema lo guarda correctamente  

### Historia 2: Registrar venta

Given que el producto tiene stock  
When se registra una venta  
Then el sistema descuenta el inventario  

## MVP Rationale

El MVP se enfoca en el control de inventario y ventas, ya que representan el núcleo del sistema. Estas funcionalidades permiten operar el negocio y calcular ganancias básicas. Otras funcionalidades como reportes avanzados o exportaciones se dejan para futuras versiones.
