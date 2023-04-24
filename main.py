import uvicorn
from fastapi import FastAPI

from api.currency import route
from database.models import Base
from database.session import engine

app = FastAPI(title='mobicult')
app.include_router(route)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    uvicorn.run('main:app', host='localhost', port=8001, reload=True)
