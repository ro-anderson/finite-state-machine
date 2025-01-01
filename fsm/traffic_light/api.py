from fastapi import FastAPI
from traffic_light import TrafficLightMachine

app = FastAPI()
fsm = TrafficLightMachine()

@app.get("/state")
def get_current_state():
    return {"state": fsm.current_state.id}

@app.post("/cycle")
def cycle():
    fsm.cycle()
    return {"state": fsm.current_state.id}

@app.post("/reset")
def reset():
    fsm.reset_event()
    return {"state": fsm.current_state.id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)