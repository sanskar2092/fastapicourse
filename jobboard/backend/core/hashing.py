from passlib.context import CryptContext


pwt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_password(plain_pwd, hashed_pwd):
        return pwt_context.verify(plain_pwd, hashed_pwd)

    @staticmethod
    def get_password_hash(plain_pwd):
        return pwt_context.hash(plain_pwd)
