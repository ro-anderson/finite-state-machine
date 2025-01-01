from statemachine import StateMachine, State

class TrafficLightMachine(StateMachine):
    "A traffic light state machine"
    green = State('Green', initial=True)
    yellow = State('Yellow')
    red = State('Red')

    cycle = (
        green.to(yellow) |
        yellow.to(red) |
        red.to(green)
    )

    # Define a reset event that transitions from any state to green
    reset_event = green.from_(green, yellow, red)

    def before_cycle(self, event, source, target):
        print(f"Transitioning from {source.id} to {target.id}")

    def before_reset_event(self, event, source, target):
        print(f"Resetting from {source.id} to {target.id}")

    def on_enter_red(self):
        print("Entered Red: Stop")

    def on_enter_green(self):
        print("Entered Green: Go")

    def on_enter_yellow(self):
        print("Entered Yellow: Caution")

if __name__ == "__main__":
    sm = TrafficLightMachine()
    sm.cycle()  # Green -> Yellow
    sm.cycle()  # Yellow -> Red
    sm.reset_event()  # Reset to Green

    # Generate the graph
    graph = sm._graph()
    graph.write_png('./fsm/traffic_light/traffic_light.png')