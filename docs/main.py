from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="InvControl Pro API")

products = {}
sales = []

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int

class Sale(BaseModel):
    product_id: int
    quantity: int

@app.post("/products")
def create_product(product: Product):
    if product.id in products:
        raise HTTPException(status_code=400, detail="Producto ya existe")
    products[product.id] = product
    return {"message": "Producto creado"}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return products[product_id]

@app.post("/sales")
def create_sale(sale: Sale):
    if sale.product_id not in products:
        raise HTTPException(status_code=404, detail="Producto no existe")

    product = products[sale.product_id]

    if product.stock < sale.quantity:
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    product.stock -= sale.quantity
    sales.append(sale)

    return {"message": "Venta registrada"}

@app.put("/products/{product_id}/stock")
def update_stock(product_id: int, stock: int):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    products[product_id].stock = stock
    return {"message": "Stock actualizado"}