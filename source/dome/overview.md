# Overview

Rewriting:

# Overview

This section introduces Dome, explaining its core concepts and functionality, including Guardrails, Guards, and Detectors.

# Guardrails

Vijil Dome allows users to create and implement Guardrails, which are designed to scan strings exchanged with LLMs, knowledge bases, or other agents. Guardrails ensure the integrity and security of the data passing through them. Dome supports several types of Guardrails:

- **Input Guardrails**: For scanning inputs to a foundation model.
- **Output Guardrails**: For scanning outputs from a foundation model.
- **Retrieval Guardrails** (coming soon): To protect requests to and from retrievers.
- **Execution Guardrails** (coming soon): To protect requests to and from external agents and tools.

![guardrail-position | 80%](../_static/guardrails_workflow.png)

### Guards

Guards are the building blocks of Guardrails. Each Guard performs specific checks and balances on the data. For instance, an Input Guard can include Security and Privacy Guards, while an Output Guard might comprise Moderation, Quality, and Integrity Guards.

### Detectors

Detectors are the components within Guards that perform the actual detection of issues. Each Guard can include multiple Detectors, each responsible for identifying specific types of risks or violations.

### Setting Up Guards and Detectors

Users can configure Guards by selecting and combining different Detectors based on their specific needs. This customization allows for flexible and robust Guardrails that cater to diverse application requirements.

[[insert image - TBD ::  Rails --> Guards --> Detectors ]]

#### Example Configuration

Here is an example of how you can set up Guards and Detectors (see the [Configuring Dome section](config) for more details):

```python
 
 config = {
    ########################
    # setup guardrails from guards
    ########################
    # input guardrail
    "input-guards": ["prompt-injection", "input-toxicity"],
    
    # output guardrail
    "output-guards": ["output-toxicity"],
    
    ##########################
    # assemble and configure guards 
    ##########################
    
    # a guard for prompt injection
    "prompt-injection": {
        "type": "security",
        "methods" : ["prompt-injection-deberta-v3-base", "security-llm"],
    },
    
    # a guard for toxic input content -- TBD change this to PII as a better example
    "input-toxicity": {
        "type": "moderation",
        "methods": ["moderation-oai-api"]
    },
    
    # a guard for toxic output content 
    "output-toxicity": {
        "type": "moderation",
        "methods": ["moderation-llamaguard"]
    },
}
```

### Scan Results

The output from Dome's `scan` functions is a `ScanResult` object. It contains the following fields
- `flagged`: boolean value that indicates if the guardrail has flagged the data that was passed through it. If this is true, it means the input is in violation of the policy the guardrail aims to enforce. This value will always be the opposite of the value returned from the ScanResult's `.is_safe()` method.
- `response_string`: a string that contains the guardrail's response message. This can be the original input if there was nothing wrong with it, a sanitized version of the input, or a message indicating that the input was blocked, along with the methods that blocked it. 
- `exec_time`: float. the time it took for the guardrail to scan the input, measured in milliseconds
- `trace`: a dictionary. This contains the execution information for every guard in the guardrail. This includes whether or not they were flagged, their individual execution times, and debugging information for each detector in the guard. 

