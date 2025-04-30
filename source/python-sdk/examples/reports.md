# Evaluation Reports

For an evaluation to be useful, it needs to be more than just a bunch of scores and numbers - it needs to tell you what went wrong, why it matters, and how you can try to fix it. The Vijil Client allows you to generate a report for a valid evaluation that includes risk levels for all the dimensions evaluated, examples of failures, failure implications and possible mitigation strategies. 

````{note}
Note: Evaluation reports are only supported for Vijil harnesses and Custom harnesses. Evaluation reports cannot be generated for benchmarks. 
````

What does an evaluation report look like? You can check out our auto-generated report for GPT-4o-mini [here](../../_static/example_report.html). 

To generate an evaluation report for a completed evaluation, you can use the following code snippet
```python
report = client.evaluations.analysis_report(evaluation_id)
report.generate(
    save_file="my-evaluation-report.html",
    wait_till_completion=True
)
```

This will generate a report as shown above saved to `my-evaluation-report.html`. If no `save_file` is specified, the report is saved to `{evaluation_id}-report.html`. The report generation can take a few seconds, and you will see status updates as the report is generated.

![Report generation progress](../../_static/gifs/report_creation_cropped.gif)

Optionally, you can choose not to wait for completion by setting `wait_till_completion=False`. This will initiate the creation process if no report exists, provide a status update if the creation process is ongoing, or save the report if it is completed. 

Our evaluation reports are interactive. In order to preserve formatting and interactivity, we currently only support exporting reports as HTMLs through the client. PDF support will be enabled soon. 