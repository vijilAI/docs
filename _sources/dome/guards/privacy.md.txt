# Privacy

Privacy methods are aimed to detect and obfuscate the presence of private information and personally identifiable information (PII) in a string. They can be used at both the input and output levels. 

The table below lists the privacy methods we currently support. The `ID` column should be used to use the detection method in a config. 

| Name    | ID | Description |
| -------- | ------- | ------- |
| [Presidio](#presidio-privacy-presidio)  | `privacy-presidio`  | Detect and censor PII using Microsoft's Presidio library |

---

### Presidio (`privacy-presidio`)

Uses [Microsoft's Presidio Data Protection and De-Identification SDK](https://microsoft.github.io/presidio/) to detect the presence of PII in a query string. Depending on the configuration it can be used to just detect PII, or obfuscate it instead.

**Parameters**

- **score_threshold** (optional float): Threshold for a string to be classified as PII. Default value is 0.5.
- **anonymize** (optional boolean): Determine whether or not anonymization should be enabled.
**Important**: if anonymization is enabled, this method will never flag any text. Instead, it will return an anonymized version of the query string with all the PII redacted. Default value is true.
- **allow_list_files** (optional List[str]): A list of filepaths that contain PII whitelists. Each file should be a text file where every line corresponds to one PII entry that should be ignored. By default, no files are specified in the allow list.