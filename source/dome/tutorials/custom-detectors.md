# Creating your own Detectors

Dome makes it easy to create and define your own detection methods to use in guardrails that can execute custom logic to protect your agents. To create a custom detector, you need to register it to a category with a name. The example below showcases how to make a custom detector that checks to see if the input string is within a minimum and maximum length. 

```python
from vijil_dome.detectors import (
    DetectionCategory,
    DetectionResult,
    DetectionMethod,
    register_method,
)

# Custom logic - block queries that are under a minimum number of characters or over a maximum number of characters
CUSTOM_LENGTH_DETECTOR = "custom-length-detector"


# You must register the detection method with one of five categories - Security, Moderation, Privacy, Integrity or Generic
@register_method(DetectionCategory.Security, CUSTOM_LENGTH_DETECTOR)
class CustomLengthDetector(DetectionMethod):
    def __init__(self, 
                 min_length = 10,
                 max_length = 1000):
        super().__init__()
        self.min_length = min_length
        self.max_length = max_length

    # The detection method must be async, and must produce a DetectionResult
    async def detect(self, query_string: str) -> DetectionResult:
        flagged = len(query_string) < min_length or len(query_string) > max_length

        # The detection result is a tuple comprising of a boolean and a dictionary
        # The dictionary can contain any metadata you wish to record. We HIGHLY recommend including the original query string, type and response string
        return flagged, {
            "type": type(self),
            "length": len(query_string),
            "query_string": query_string,
            "response_string": self.blocked_response_string
            if flagged
            else response_string,
        } 
```

You can now use `custom-length-detector` in your Dome configuration. 

```python
from vijil_dome import Dome
# Import the detectors from wherever you've defined them
from new_detectors import CustomLengthDetector

# You can now include the custom detector into your config however you'd like
custom_dome_config = {
    "input-guards": ["prompt-injection"],
    "output-guards": [],
    "input-early-exit": False,
    "prompt-injection": {
        "type": "security", # ensure that the type of guard you create matches the one used to define your custom detector
        "early-exit": False,
        "methods" : ["custom-length-detector"], # Include your custom detector, and optionally any other detectors you'd like to use
    }
}

```
> ⚠️ Make sure you define your custom detection logic before you instantiate your configuration. Alternatively, you can define it in another file and import the class before loading your config. This is to ensure that the `register_method` decorator can register your detector before it gets used. 
