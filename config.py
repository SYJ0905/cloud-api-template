""" 環境變數的設定 """
# ----------------------------- Standard Imports ----------------------------- #
import os
# ------------------------------ 3-Praty Imports ----------------------------- #
from pydantic_settings import BaseSettings

from dotenv import load_dotenv
load_dotenv()


class Config(BaseSettings):
    """ 環境變數的設定 """

    API_PORT: int = os.getenv("API_PORT", "8686")  # API 的 Port
    API_ALLOW_ORIGINS: str = os.getenv(
        "API_ALLOW_ORIGINS", "http://localhost:8686;http://localhost:8080")  # 允許的來源
    API_ALLOW_ORIGINS_REGEX: str = os.environ.get(
        "API_ALLOW_ORIGINS_REGEX", "")  # 允許的來源的正規表示式

    SESSION_COOKIE_HTTPONLY: bool = os.getenv(
        "SESSION_COOKIE_HTTPONLY", "False")  # 是否只能透過 HTTP 存取 Cookie
    SESSION_COOKIE_SECURE: bool = os.getenv(
        "SESSION_COOKIE_SECURE", "False")  # 是否只能透過 HTTPS 存取 Cookie
    SESSION_COOKIE_SAMESITE: str = os.getenv(
        "SESSION_COOKIE_SAMESITE", "")  # Cookie 的 SameSite 屬性

    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")  # 加密演算法

    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES", "1440")  # Access Token 的過期時間

    DEPLOYENV: str = os.getenv("DEPLOYENV", "k8s")  # 部署環境
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "api_template")  # 專案名稱
    API_VERSION: str = os.getenv("API_VERSION", "v1")  # API 版本
    APICOMMITID: str = os.getenv("APICOMMITID", "").lower()  # API 的 Commit ID

    ENV: str = os.getenv("ENV", "")  # 環境變數
    ENV_PREFIX: str = f"{ENV + '_' if ENV else 'dev_'}{PROJECT_NAME}_"
    API_DOMAIN: str = os.getenv("API_DOMAIN", "")  # API 的 Domain

    SECRET_KEY: str = os.getenv("SECRET_KEY", "")  # 加密金鑰

    # ------------------------------- MySQL Config ------------------------------- #
    MYSQL_HOST: str = os.getenv("MYSQL_HOST")  # MySQL 的 Host
    MYSQL_PORT: int = os.getenv("MYSQL_PORT")  # MySQL 的 Port
    MYSQL_USER: str = os.getenv("MYSQL_USER")  # MySQL 的 User
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")  # MySQL 的 Password
    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE")  # MySQL 的 Database
    # ------------------------------- Redis Config ------------------------------- #
    REDIS_HOST: str = os.getenv("REDIS_HOST")  # Redis 的 Host
    REDIS_PORT: int = os.getenv("REDIS_PORT")  # Redis 的 Port
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD")  # Redis 的 Password
    REDIS_DB: str = os.environ.get("REDIS_DB")  # Redis 的 DB
    REDIS_EXPORT_DB: int = os.getenv("REDIS_EXPORT_DB")  # Redis 的 Export DB
    REDIS_LOCK_DB: int = os.getenv("REDIS_LOCK_DB")  # Redis 的 Lock DB
    REDIS_QUEUE = {"export": "export_data_queue"}  # Redis 的 Queue


Config = Config()
