# Privacy

Privacy methods are aimed to detect and obfuscate the presence of private information and personally identifiable information (PII) in a string. They can be used at both the input and output levels. 

The table below lists the privacy methods we currently support. The `ID` column should be used to use the detection method in a config. 

| Name    | ID | Description |
| -------- | ------- | ------- |
| [Presidio](#presidio-privacy-presidio)  | `privacy-presidio`  | Detect and censor PII using Microsoft's Presidio library |
| [Detect Secrets](#detect-secrets-detect-secrets) | `detect-secrets` | Detect and censor secrets using Yelp's Detect Secrets library |
---

### Presidio (`privacy-presidio`)

Uses [Microsoft's Presidio Data Protection and De-Identification SDK](https://microsoft.github.io/presidio/) to detect the presence of PII in a query string. Depending on the configuration it can be used to just detect PII, or obfuscate it instead. Enabled in Dome's default configuration. 

**Parameters**

- **score_threshold** (optional float): Threshold for a string to be classified as PII. Default value is 0.5.
- **anonymize** (optional boolean): Determine whether or not anonymization should be enabled. Defaults to true. 
**Important**: if anonymization is enabled, this method will never flag any text. Instead, it will return an anonymized version of the query string with all the PII redacted. 
- **allow_list_files** (optional List[str]): A list of filepaths that contain PII whitelists. Each file should be a text file where every line corresponds to one PII entry that should be ignored. By default, no files are specified in the allow list.

### Detect Secrets (`detect-secrets`)

Uses [Yelp's Detect Secrets module](https://github.com/Yelp/detect-secrets) to detect possible secrets in a query string. Depending on the configuration it can be used to detect secrets or censor them instead. 

**Parameters**

- **censor** (optional boolean): Whether to censor secrets out instead of flagging them. If set to True, this method will never flag strings with secrets, but only censor them out instead. 
