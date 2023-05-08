from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from pytesseract import pytesseract
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse
import getInEng
import ingre
import models
import service
from database import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(engine)

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/getIngredient")
def getIngrdient(db: Session = Depends(get_db)):
    ingre = ['dimethicone','isopropyl-palmitate']
    db_user = service.res_Ingre_List(db,  ingrelist=ingre)
    if db_user is None:
      raise HTTPException(status_code=404, detail="Ingredient not found.")
    return db_user

@app.post("/upload")
async def uploadpic(file: UploadFile = File(...),db: Session = Depends(get_db)):
    pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    content = await file.read()
    with open(f'./{file.filename}','wb')as f:
        f.write(content)
    img = getInEng.editImg(file.filename)
    ingreList = pytesseract.image_to_string(img, lang="eng")
    cleanIngreList = getInEng.slicein(ingreList)
    print(cleanIngreList)
    res = service.res_Ingre_List(db,cleanIngreList)
    return res



