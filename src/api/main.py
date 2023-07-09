
from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from apiService.author import router as author_router
from apiService.book import router as book_router
from apiService.user import router as user_router
from dbCreation import create_tables

from dependencies import get_current_active_user

app = FastAPI()
''' allows some
origins = [
    "http://localhost",
    "http://localhost:3000",  # Replace with your frontend URL
]
'''
origins = ["*"] #allow any

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

version="v1"
app.include_router(author_router, prefix=f"/{version}/api")
app.include_router(book_router, prefix=f"/{version}/api")
app.include_router(user_router, prefix=f"/{version}/api")



@app.on_event("startup")
async def startup_event():
    create_tables()

@app.get("/protected")
async def protected_route(current_user: str = Depends(get_current_active_user)):
    return {"message": "This route is protected"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



