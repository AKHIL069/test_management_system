from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, models, dependencies

router = APIRouter()

@router.get("/tests", response_model=List[schemas.Test])
def read_tests(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    tests = crud.get_tests(db, skip=skip, limit=limit)
    return tests

@router.post("/tests", response_model=schemas.Test)
def create_test(test: schemas.TestCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_test(db=db, test=test)

@router.put("/tests/{test_id}", response_model=schemas.Test)
def update_test(test_id: int, test: schemas.TestUpdate, db: Session = Depends(dependencies.get_db)):
    db_test = crud.update_test(db, test_id=test_id, test=test)
    if db_test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return db_test

@router.delete("/tests/{test_id}", response_model=schemas.Test)
def delete_test(test_id: int, db: Session = Depends(dependencies.get_db)):
    db_test = crud.delete_test(db, test_id=test_id)
    if db_test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return db_test

@router.get("/tests/{test_id}/questions", response_model=List[schemas.Question])
def read_questions(test_id: int, db: Session = Depends(dependencies.get_db)):
    questions = crud.get_questions(db, test_id=test_id)
    return questions

@router.post("/tests/{test_id}/questions", response_model=schemas.Question)
def create_question(test_id: int, question: schemas.QuestionCreate, db: Session = Depends(dependencies.get_db)):
    question.test_id = test_id
    return crud.create_question(db=db, question=question)

@router.put("/questions/{question_id}", response_model=schemas.Question)
def update_question(question_id: int, question: schemas.QuestionUpdate, db: Session
