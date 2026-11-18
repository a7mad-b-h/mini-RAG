from fastapi import FastAPI , APIRouter
import os

base_router = APIRouter(
    prefix = "/api/v1", #لازم تناديه قبل اي اشي الي جوا الغيت
    tags=["api_v1"]
)
@base_router.get("/")
def welcome():
    app_name = os.getenv('APP_NAME')
    app_version = os.getenv("APP_VERSION")
    return {
        "app_name": f"{app_name}",
        "app_version" : f"{app_version}",
    }