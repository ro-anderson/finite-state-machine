from statemachine import StateMachine, State

class ConversationMachine(StateMachine):
    "A conversation state machine"
    greeting = State('Greeting', initial=True)
    asking = State('Asking')
    answering = State('Answering')
    farewell = State('Farewell', final=True)

    # Define transitions
    greet = greeting.to(asking)
    ask = asking.to(answering)
    answer = answering.to(asking)
    end_conversation = (asking.to(farewell) | answering.to(farewell))

    # Define a reset event that transitions from any state back to 'Greeting'
    reset_event = greeting.from_(greeting, asking, answering)

    # Callbacks for entering states
    def on_enter_greeting(self):
        print("Bot: Hello! How can I assist you today?")

    def on_enter_asking(self):
        print("Bot: What would you like to know?")

    def on_enter_answering(self):
        print("Bot: Here's the information you requested.")

    def on_enter_farewell(self):
        print("Bot: Goodbye!")

    # Optional callback before resetting
    def before_reset_event(self, event, source, target):
        print(f"Resetting from {source.id} to {target.id}")

if __name__ == "__main__":
    sm = ConversationMachine()
    sm.greet()
    sm.ask()
    sm.answer()
    sm.end_conversation()
    #sm.reset_event()

    # Generate the graph
    graph = sm._graph()
    graph.write_png('./fsm/conversation/conversation_machine.png')