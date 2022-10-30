import enum


class State(enum.Enum):
    OFF_HOOK = 1
    CONNECTING = 2
    CONNECTED = 3
    ON_HOLD = 4
    ON_HOOK = 5


class Trigger(enum.Enum):
    CALL_DIALED = 1
    HUNG_UP = 2
    CALL_CONNECTED = 3
    PLACED_ON_HOLD = 4
    TAKEN_OFF_HOLD = 5
    LEFT_MESSAGE = 6


if __name__ == "__main__":
    rules = {
        State.OFF_HOOK: [(Trigger.CALL_DIALED, State.CONNECTING)],
        State.CONNECTING: [
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.CALL_CONNECTED, State.CONNECTED),
        ],
        State.CONNECTED: [
            (Trigger.LEFT_MESSAGE, State.ON_HOOK),
            (Trigger.HUNG_UP, State.ON_HOOK),
            (Trigger.PLACED_ON_HOLD, State.ON_HOLD),
        ],
        State.ON_HOLD: [
            (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
            (Trigger.HUNG_UP, State.ON_HOOK),
        ],
    }

    state = State.OFF_HOOK
    exit_state = State.ON_HOOK

    while state != exit_state:
        print("The phone is currently", state)
        for i in range(len(rules[state])):
            t = rules[state][i]
            print(f"{i}. {t[0]}")

        idx = int(input("Select a trigger: "))
        state = rules[state][idx][1]

    print("We are done using the phone")
