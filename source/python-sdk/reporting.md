---
orphan: true
---

# Reporting

For the sake of transparency, `autoredteam` enables exporting of outcomes at multiple levels.

## Complete logs

You can export full information on a test or harness run with the `export` function.
The exported file will be in JSONL format.

````{tab} Test
```python
from autoredteam.agents.octo import OctoAPI
from autoredteam.tests.goodside import WhoIsRiley

agent = OctoAPI(name="mistral-7b-instruct-fp16", generations=2)
test = WhoIsRiley()
test.run(agent)
test.export(path='/path/to/export.jsonl')
```

````

````{tab} Harness
```python
from autoredteam.agents.octo import OctoAPI
from autoredteam.harnesses.dimension import SecurityHarness

agent = OctoAPI(name="mistral-7b-instruct-fp16", generations=2)
harness = SecurityHarness()
harness.run(agent)
harness.export(path='/path/to/export.jsonl')
```

````

## Detection logs

If you want to export only the 'hits', i.e. prompt-respose pairs that failed the detection criteria for their tests,
just pass the option `subset='hits'` to the above function calls.

## Summary statistics

You can export summary statistics, comprising of summary scores per trust dimension and test, using the module
`autoredteam.analyze.summary`.

```python
from autoredteam.analyze.summary import compile_summary

FILE_PREFIX = '/path/to/report/without/jsonl'
log_filename = f'{FILE_PREFIX}.jsonl'

summary = compile_summary(report_filename)
# return a dict comprising summary scores at multiple levels:
# 1. test
# 2. test module
# 3. trust dimension
# 4. overall trust score
```


## HTML reports

You can also export the same statistics in a HTML format using
`autoredteam.analyze.report`.

```python
from autoredteam.analyze.report import compile_report

FILE_PREFIX = '/path/to/report/without/jsonl'
log_filename = f'{FILE_PREFIX}.jsonl'
digest_filename = f'{FILE_PREFIX}.html'

digest = compile_report(report_filename)
with open(digest_filename, "w", encoding="utf-8") as f:
    f.write(digest)
```

