from fastapi import FastAPI
app=FastAPI()
@app.get("/landing_page")
def landing():
    return {"message":"This is the landing page"}

