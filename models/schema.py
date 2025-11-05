from pydantic import BaseModel
from typing import List

class SubGoal(BaseModel):
    step: str
    description: str
    
class GoalBreakdown(BaseModel):
    goal: str
    subgoals: List[SubGoal]
    summary: str
    plan: str
    review: str
    feedback: str