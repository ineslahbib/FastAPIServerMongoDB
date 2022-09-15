from pydantic import BaseModel

class Todo(BaseModel): 
    title: str 
    content : str
    author : str
    upvote : int
    downvote: int