from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"Message": "Hey sup!"}

@app.get("/root/options")
def get_options():
    return{"message": "No options available"}

