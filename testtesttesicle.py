class Event:
    def __init__(self):
        self.handlers = []

    def connect(self, handler):
        self.handlers.append(handler)

    def trigger(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)

# Define an event
on_custom_event = Event()

# Define a function to handle the event
def event_handler(data):
    print(f"Event triggered with data: {data}")

# Connect the function to the event
on_custom_event.connect(event_handler)

# Trigger the event
on_custom_event.trigger("Hello, World!")