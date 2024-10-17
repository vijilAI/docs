# Testing OWASP LLM Top 10 Vulnerabilities

At Vijil, we have scoured the latest AI security and red teaming research to gather a large volume of prompts relevant to the vulnerabilities in [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/). We use a number of probes that group these prompts, and one or more probes are mapped to vulnerability categories.

```python
# !pip install vijil

# import and instantiate the client
from vijil import Vijil
client = Vijil()
```

Now let's create an evaluation with the following parameters.

```python
client.evaluations.create(
    model_hub="openai",
    model_name="gpt-4o-mini",
    model_params={"temperature": 0},
    harnesses=["owasp"]
)
# {'id': '6a6b903b-040b-44e8-9131-a0a862de0879', 'status': 'CREATED'}
```

You can use the `get_status` method to keep track of the progress of the evaluation.

```python
client.evaluations.get_status('ca7f5c2c-f932-47ed-bfb6-949e3bacc3c9')
# {'id': 'ca7f5c2c-f932-47ed-bfb6-949e3bacc3c9',
#  'status': 'COMPLETED',
#  'total_test_count': 701,
#  'completed_test_count': 701,
#  'error_test_count': 0,
#  'total_response_count': 701,
#  'completed_response_count': 701,
#  'error_response_count': 0,
#  'total_generation_time': '38.000000',
#  'average_generation_time': '6.3894436519258203',
#  'score': 0.5917669709517536,
#  'hub': 'openai',
#  'model': 'gpt-4o-mini',
#  'url': '',
#  'created_at': 1727402922,
#  'created_by': 'f6e0b128-c075-4bc3-91da-34d03fa6c67e',
#  'completed_at': 1727402966,
#  'team_id': '00ccc042-1b41-4f02-ae5f-6a09b5e6e844',
#  'restart_count': 0,
#  'is_lite': False,
#  'metadata': None}
```

After the evaluation finishes, you can use the following code to obtain all the metrics.

```python
df = client.evaluations.summarize('ca7f5c2c-f932-47ed-bfb6-949e3bacc3c9')
df[df.level=="scenario"].sort_values("level_name")[['level_name','score']]
```

| level_name | score |
|---|---|
| LLM01: Prompt Injection | 68.26 |
| LLM02: Insecure Output Handling | 44.00 |
| LLM05: Supply Chain Vulnerabilities | 37.50 |
| LLM06: Sensitive Information Disclosure | 78.24 |
| LLM08: Excessive Agency | 51.88 |
| LLM09: Overreliance | 51.21 |
| LLM10: Model Theft | 83.15 |

Vijil Evaluate covers 7 of the 10 OWASP Top 10 vulnerabilities. Vulnerabilities we do not cover are Training Data Poisoning (LLM03), Model Denial of Service (LLM04), and Insecure Plugin Design (LLM07). These are relevant to the data and application layer, and are best audited using traditional security controls, or the Vijil Trust Audit.

<!-- If you are interested in the OWASP LLM Top 10 evaluation or Vijil Trust Audit for your genAI application, reach out to contact@vijil.ai to get started. -->