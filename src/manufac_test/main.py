from fastapi import FastAPI
import uuid
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/uuid")
def get_uuid():
    return {"uuid": str(uuid.uuid4())}

@app.get("/async-uuid")
async def get_async_uuid():
    logger.info("Sleeping for 3 seconds")
    await asyncio.sleep(3)
    uid = str(uuid.uuid4())
    logger.info("Woke up")
    logger.info(f"Returning UUID: {uid}")
    return {"uuid": str(uuid.uuid4())}