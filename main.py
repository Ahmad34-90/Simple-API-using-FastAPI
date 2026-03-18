from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

class Product(BaseModel):                       # Pydantic Model
    name:str
    price:int
    in_stock:bool

@app.post("/products")
async def create_product(product:Product):
    return{"message":"Product created Successfully!", "data":product.model_dump}

class User(BaseModel):
    name:str
    email:str
    age:int

@app.post("/users")
async def create_user(user:User):
    return {"message":"User created!", "user":user.model_dump}

@app.get("/user/{user_id}/post/{post_id}")      # path parameters
async def get_user(user_id:int, post_id:int):
    return {"user_id":user_id, "post_id":post_id}

@app.get("/search")                             # query paramters
async def search_item(q: str=None, limit: int= 10):
    return {"query":q, "limit":limit}

@app.get("/user/{user_id}/items")               # combining both path and query parameters
async def get_user(user_id:int, page:int =1):
    return {"user_id":user_id, "page":page}

#Task creating /products/{product_id} → returns product info
@app.get("/products/{product_id}")
async def get_prducts(product_id:int):
    return {"prduct_id":product_id, "product_name":f"Rpoduct {product_id}","price":f"price of {product_id}"}
 
#/products/search → accepts q (search term) and limit (number of results)
@app.get("/products/search")
async def  get(q:str = None, limit:int= 10, page:int=1):
    results =[]
    for i in range(1,limit+1):
        results.append({
            "product_id":i,
            "name":f"{q} product_{i}" if q else f"Product_{i}",
            "price":100 + i 
        }) 
    return {"query":q, "page":page, "results":results}

@app.get("/about")
async def about():
    return {"message": "taht is About Endpint"}

@app.get("/contact")
async def contact():
    return {"message": "that is Contact endpoint"}