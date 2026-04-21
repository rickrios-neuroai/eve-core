state = {
    "system_health": 0.95,
    "confidence": 0.82,
    "last_action": "pressure_check",
    "environment_status": "stable"
}

def evaluate_self(state):
    if state["system_health"] < 0.7:
        return "WARNING"
    elif state["confidence"] < 0.5:
        return "UNCERTAIN"
    return "STABLE"

def reflect(state):
    evaluation = evaluate_self(state)

    if evaluation == "WARNING":
        action = "request_maintenance"
    elif evaluation == "UNCERTAIN":
        action = "collect_more_data"
    else:
        action = "continue_operation"

    return action

print("System evaluation:", evaluate_self(state))
print("Decision:", reflect(state))
