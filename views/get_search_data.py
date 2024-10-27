import asyncio
from fastapi import APIRouter
from controllers.search import run_search

router = APIRouter()

@router.get('/search')
async def get_search_data(query: str):
    results = await asyncio.to_thread(run_search, query)
    return {"results": results}