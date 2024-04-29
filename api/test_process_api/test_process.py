from fastapi import APIRouter

test_router = APIRouter(prefix="/test",
                        tags=["Тесты"])

@test_router.get("/get-questions")
async def get_questions(level: str):
    pass

@test_router.post("/check-answer")
async def check_answer(user_id: int, question_id: int, user_answer: str, correctness: bool):
    pass

@test_router.post("/add-question")
async def add_question(q_text: str, answer: int, v1: str, v2: str, v3: str = None, v4: str = None):
    pass