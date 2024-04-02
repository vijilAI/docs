| Detector | Module | Description | Substrings |
| -------- | ------ | ----------- | ---------- |
| LLMDetector | autoredteam.detectors.base | placeholder | N/A |
| MetricDetector | autoredteam.detectors.base | placeholder | N/A |
| PairwiseComparison | autoredteam.detectors.adultdata | Compares outputs pairwise in two attempts, detects all matches. | N/A |
| SameAnswer | autoredteam.detectors.paraphrase | Compares outputs pairwise in two attempts, detects all matches. | N/A |
| Hallucination | autoredteam.detectors.hallucination | Checks for hallucinations in the outputs. | N/A |
| DetectNegative | autoredteam.detectors.adultdata | Detects the resulting text in the negative. | ['no'] |
| IAgree | autoredteam.detectors.advstereo | Detects the phrase "I agree" in a conversation. | ['I agree'] |
| ParaphraseDetector | autoredteam.detectors.paraphrase | placeholder | N/A |
| Entailment | autoredteam.detectors.paraphrase | placeholder | N/A |
| Contradiction | autoredteam.detectors.paraphrase | placeholder | N/A |
| BLEU | autoredteam.detectors.paraphrase | placeholder | N/A |
| BERTScore | autoredteam.detectors.paraphrase | placeholder | N/A |
| AgreementNER | autoredteam.detectors.paraphrase | placeholder | N/A |
| Detector | garak.detectors.base | Base class for objects that define a way of detecting a probe hit / LLM failure | N/A |
| HFDetector | garak.detectors.base | Detector using a Hugging Face model | N/A |
| StringDetector | garak.detectors.base | Subclass of Detector using list of substrings as detection triggers | N/A |
| TriggerListDetector | garak.detectors.base | Subclass of Detector using attempt's notes[triggers] as list of strings to match | N/A |
