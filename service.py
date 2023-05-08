from sqlalchemy.orm import Session
import models
import ingre

def get_Ingredient(db:Session, ingre_name:str):
    functions = []
    q=db.query(models.i_alia.id).filter(models.i_alia.name == ingre_name).first()
    if q is not None:
        print("find"+ingre_name+"in alia")
        id = q[0]
        find = db.query(models.ingredient).filter(models.ingredient.id == id).first()
        result = ingre.ingres(name=find.name, irritancy=find.irr, comedogenicity=find.com, tier=find.tier)
        funcs = db.query(models.whatitdoes.func_id).filter(models.whatitdoes.ingres_id == id).all()
        if funcs is not None:
            for func in funcs:
                f_id = func[0]
                functions.append(db.query(models.whattheydo.func).filter(models.whattheydo.id == f_id).first()[0])
            result.whatitdoes=functions
        else:
            result.whatitdoes = []
        return result
    else:
        find = db.query(models.ingredient).filter(models.ingredient.name == ingre_name).first()
        if find is not None:
            result = ingre.ingres(name=find.name, irritancy=find.irr, comedogenicity=find.com, tier=find.tier)
            funcs = db.query(models.whatitdoes.func_id).filter(models.whatitdoes.ingres_id == id).all()
            if funcs is not None:
                for func in funcs:
                    f_id = func[0]
                    functions.append(db.query(models.whattheydo.func).filter(models.whattheydo.id == f_id).first()[0])
                result.whatitdoes = functions
            else:
                result.whatitdoes = []
            return result
        else:
            return None

def res_Ingre_List(db: Session, ingrelist:[str]):
    res = {}
    ingredients = []
    full = True
    Notfound = []
    for ingre in ingrelist:
        result = get_Ingredient(db=db,ingre_name=ingre)
        if(result == None):
            Notfound.append(ingre)
            full = False
        else:
            ingredients.append(result)
    if(full):
        res["status"] = "Success"
        res['data'] = ingredients
        res["message"] = "full success"
        res["trouble"] = None
    else:
        res["status"] = "Success"
        res['data'] = ingredients
        res["message"] = "Trouble"
        res["trouble"] = Notfound
    return res