from fastapi import FastAPI

app = FastAPI()


# 30 users
users = [
    {"id": 1, "name": "Subham"},
    {"id": 2, "name": "Rahul"},
    {"id": 3, "name": "Amit"},
    {"id": 4, "name": "Raj"},
    {"id": 5, "name": "John"},
    {"id": 6, "name": "David"},
    {"id": 7, "name": "Ravi"},
    {"id": 8, "name": "Ankit"},
    {"id": 9, "name": "Priya"},
    {"id": 10, "name": "Neha"},
    {"id": 11, "name": "Suman"},
    {"id": 12, "name": "Karan"},
    {"id": 13, "name": "Arjun"},
    {"id": 14, "name": "Vikash"},
    {"id": 15, "name": "Pooja"},
    {"id": 16, "name": "Sneha"},
    {"id": 17, "name": "Rohit"},
    {"id": 18, "name": "Manish"},
    {"id": 19, "name": "Akash"},
    {"id": 20, "name": "Deepak"},
    {"id": 21, "name": "Anjali"},
    {"id": 22, "name": "Nikhil"},
    {"id": 23, "name": "Varun"},
    {"id": 24, "name": "Meena"},
    {"id": 25, "name": "Sahil"},
    {"id": 26, "name": "Rakesh"},
    {"id": 27, "name": "Kavita"},
    {"id": 28, "name": "Sameer"},
    {"id": 29, "name": "Nitin"},
    {"id": 30, "name": "Suresh"}
]


# -------------------------
# GET
# -------------------------

@app.get("/")
def home():
    return {
        "message": "FastAPI backend is running"
    }


@app.get("/users")
def get_users():
    return {
        "users": users
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:

        if user["id"] == user_id:
            return user

    return {
        "message": "User not found"
    }


# -------------------------
# POST
# -------------------------

@app.post("/users")
def create_user(user: dict):

    new_id = len(users) + 1

    new_user = {
        "id": new_id,
        "name": user["name"]
    }

    users.append(new_user)

    return {
        "message": "User created",
        "user": new_user
    }


# -------------------------
# PUT
# -------------------------

@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):

    for existing_user in users:

        if existing_user["id"] == user_id:

            existing_user["name"] = user["name"]

            return {
                "message": "User updated",
                "user": existing_user
            }

    return {
        "message": "User not found"
    }


# -------------------------
# DELETE
# -------------------------

@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            return {
                "message": "User deleted",
                "user": user
            }

    return {
        "message": "User not found"
    }