# from typing import Dict

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from app.data import MongoDB

# API = FastAPI(
#     title="Underdog Devs DS API"
#     version="0.0.2"
#     docs_url='/',
# )

# API.db = MongoDB('UnderdogDevs')

# # API.db is so "API" function isn't overwritten

# API.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_credentials=True
#     allow_methods=['*'],
#     allow_headers=['*'],
# )


# @API.get("/version")
# async def version():
#     return{"result": API.version}


# @API.post("/create")
# async def create(collection_name: str, data: Dict):
#     """ Creates a new record """
#     return {"result": API.db.create(collection_name, data)}


# @API.post("/read")
# async def read(collection_name: str, data: Dict):
#     """ Returns Records based on query """
#     return {"return": API.db.read(collection_name, data)}


# @API.post("/update")
# async def update(collection_name: str, query: Dict, update_data: Dict):
#     """ Updates records based on query """
#     API.db.update(collection_name, query, update_data)
#     return{"result": {"query": query, "updated_data": update_data}}


# @API.post("/search")
# async def update(collection_name: str, user_search: str):
#     """ Returns all records that match the user_search. """
#     return {"result": API.db.search(collection_name, user_search)}