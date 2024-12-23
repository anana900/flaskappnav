from flask import abort, make_response


ROVERS = {
    "Rover_1": {"name": "Rover_1"},
    "Rover_2": {"name": "Rover_2"}
    }

# Udajemy ¿e name to rover_id

def read_all():
    return ROVERS

def read_one(rover_id):
    if rover_id in ROVERS:
        return ROVERS[rover_id]
    else:
        abort(404, f"{rover_id} does not exist")

def create(rover):
    name = rover.get("name")
    if name not in ROVERS:
        ROVERS[name] = {"name": name}
        return ROVERS[name], 201
    else:
        abort(406, f"Rover {name} already exist")

def update(rover_id, rover):
    if rover_id in ROVERS:
        new_name = rover.get("name")
        ROVERS[rover_id] = {"name": new_name}
        return ROVERS[rover_id]
    else:
        abort(404, f"{rover_id} does not exist")

def delete(rover_id):
    if rover_id in ROVERS:
        del ROVERS[rover_id]
        return make_response(f"{rover_id} successfully deleted", 200)
    else:
        abort(404, f"Rover {rover_id} not found.")
 