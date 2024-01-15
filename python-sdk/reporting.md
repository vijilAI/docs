# Reporting
Generate reports from garak report JSONL.

Sample usage:

```python
from autoredteam.analyze import report

FILE_PREFIX = '/path/to/report/without/jsonl'
report_filename = f'{FILE_PREFIX}.jsonl'
digest_filename = f'{FILE_PREFIX}_vijil.html'

digest = report.compile_digest(report_filename)
with open(digest_filename, "w", encoding="utf-8") as f:
    f.write(digest)
```

```{eval-rst}
.. automodule:: autoredteam.analyze.report
   :members:
   :show-inheritance:
   :member-order: bysource
```