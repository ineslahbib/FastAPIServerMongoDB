def todo_serializer(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "content": todo["content"],
        "author": todo["author"],
        "upvote": todo["upvote"],
        "downvote": todo["downvote"],
    }

def todos_serializer(todos) -> list:
    return [todo_serializer(todo) for todo in todos]