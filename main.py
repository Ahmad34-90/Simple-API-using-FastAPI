from fastapi import FastAPI

app =FastAPI()

@app.get("/")
async def home():
    return {"message":"That is home endpoint"}

@app.get("/about")
async def about():
    return {"message": "taht is About Endpint"}

@app.get("/contact")
async def contact():
    return {"message": "that is Contact endpoint"}