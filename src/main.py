import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from src.config import settings 
#from src.controllers import tictactoe_controller, session_controller, user_controller
from src.controllers import user_controller

app = FastAPI(
    title="Classic Games",
    description="Backend for data engineering and AI-driven classic games.",
    version="0.0.1"
)

# 1. Include Routers (Connecting your Controllers)
# This keeps your main file clean and scales as you add more games
# app.include_router(user_controller.router, prefix="/user", tags=["User Management"])
# app.include_router(session_controller.router, prefix="/session", tags=["Sessions"])
# app.include_router(tictactoe_controller.router, prefix="/ttt", tags=["Tic Tac Toe"])

app.include_router(user_controller.router, prefix="/user", tags=["User Management"])

@app.get("/")
async def health_check():
    """
    Check if the API and configuration are loaded correctly.
    """
    return {
        "status": "online",
        "debug_mode": settings.DEBUG_MODE,
        "database": "SQLite (Connected)"
    }

# Example of a specific game interaction route (Pathways from your brief)
# @app.post("/ttt/play/{session_id}") # 
# async def play_ttt_move(session_id: int, move_data: dict):
#     # This calls the logic in your specific game controller
#     try:
#         updated_state = await tictactoe_controller.process_move(session_id, move_data)
#         return updated_state
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))


# python -m src.main
if __name__ == "__main__":
    uvicorn.run("src.main:app", port=settings.APP_PORT, log_level=settings.DEBUG_MODE, reload=True)