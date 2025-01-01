from fastapi import FastAPI
from conversation_machine import ConversationMachine

app = FastAPI()

# Instances of state machines
conversation_fsm = ConversationMachine()

# Conversation Machine Endpoints
@app.get("/conversation/state")
def get_conversation_state():
    return {"state": conversation_fsm.current_state.id}

@app.post("/conversation/greet")
def greet():
    conversation_fsm.greet()
    return {"state": conversation_fsm.current_state.id}

@app.post("/conversation/ask")
def ask():
    conversation_fsm.ask()
    return {"state": conversation_fsm.current_state.id}

@app.post("/conversation/answer")
def answer():
    conversation_fsm.answer()
    return {"state": conversation_fsm.current_state.id}

@app.post("/conversation/end")
def end_conversation():
    conversation_fsm.end_conversation()
    return {"state": conversation_fsm.current_state.id}

@app.post("/conversation/reset")
def reset_conversation():
    conversation_fsm.reset_event()
    return {"state": conversation_fsm.current_state.id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
