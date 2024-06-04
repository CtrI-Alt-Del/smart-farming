# from dataclasses import asdict

# from .auth_user import AuthUser


# def get_user(stored_user_data) -> AuthUser:
#     id = stored_user_data["id"]
#     role = stored_user_data["role"]

#     user = users_repository.get_by_id(id)

#     if user is None:
#         return AuthUser(is_active=False)

#     return AuthUser(role=role, **asdict(user))
