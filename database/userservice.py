from database import get_db
from database.models import User, UserAnswers, Rating
from datetime import datetime

def register_user_db(name: str, phone_number: str) -> int:
    db = next(get_db())
    checker = db.query(User).filter_by(name=name).first()
    if checker:
        return 0

    new_user = User(name=name, phone_number=phone_number, reg_date=datetime.now())
    db.add(new_user)
    db.commit()
    return new_user.id

def get_user_score_db(user_id: int) -> int:
    db = next(get_db())
    try:
        checker = db.query(Rating).order_by(Rating.user_score.desc()).all()
        leaders_list = [user.id for user in checker]
        return leaders_list.index(user_id) + 1
    except:
        return 0

def get_top5_db():
    db = next(get_db())
    checker = db.query(Rating).order_by(Rating.user_score.asc()).all()
    return checker[-1:-6:-1]

def add_user_answer_db(user_id: int, question_id: int, user_answer: int) -> bool:
    db = next(get_db())
    new_answers = UserAnswers(user_id=user_id, question_id=question_id, user_answer=user_answer)
    db.add(new_answers)
    db.commit()
    question_correct_answer = db.query(Questions).filter_by(question_id=question_id).first().answer
    exact_user_score = db.query(Rating).filter_by(user_id=user_id).first()
    if exact_user_score:
        score = exact_user_score.user_score
        if user_answer == question_correct_answer:
            score += 1
            db.commit()
            return True
    else:
        new_rating = Rating(user_id=user_id)
        db.add(new_rating)
        db.commit()
    return False

# def check_user_answer_db(user_id: int, question_id: int, answer: int, user_answer: int) -> int:
#     db = next(get_db())
#     try:
#         answer_db = db.query(Questions).filter_by(Question.answer).first()
#         user_answer = db.query(UserAnswers).filter_by(UserAnswers.user_answer).first()
#         user_score = db.query(Rating).filter_by(Rating.user_id).first()
#         if answer_db == user_answer:
#             user_score.user_score += 1
#     except:
#         return 0

