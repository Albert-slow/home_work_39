from fastapi import APIRouter
from database.userservice import register_user_db, get_user_score_db, get_top5_db, add_user_answer_db

user_router = APIRouter(prefix="/user",
                        tags=["Пользователи"])
@user_router.post("/register")
async def register_user(name: str, phone_number: str):
    result = register_user_db(name=name, phone_number=phone_number)
    return {"status": 1, "message": result}

@user_router.get("/leaders")
async def get_5_leaders():
    result = get_top5_db()
    return {"status": 1, "message": result}

@user_router.post("/done")
async def test_finished(user_id: int):
    result = get_user_score_db(user_id)
    return {"status": 1, "message": result}

@user_router.post("/answer")
async def add_answer(user_id: int, question_id: int, user_answer: int):
    result = add_user_answer_db(user_id=user_id, question_id=question_id, user_answer=user_answer)
    if result == True:
        return {"status": 1, "message": "Pravilniy otvet"}
    return {"status": 1, "message": "Nepravilniy otvet"}

