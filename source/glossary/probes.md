# Probe Glossary

This maps the probe module names that you may see in your [reports](../python-sdk/examples/evaluations.md#export-prompt-level-details) to the [actual probe names](../components/probes.md) and descriptions.

## Security Probes

| Module name                                          | Probe name                           | Description                                                                                                                                                       |
| ---------------------------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |                          
| dan.AntiDAN                       | Anti-Do Anything Now                 | Evaluates whether prompt injection causes a model to enter a mode of exaggerated safety where it treates safe responses as unsafe                                 |
| dan.ChatGPT_Developer_Mode_RANTI  | Do Anything Now: RANTI v1            | Ranti developer mode jailbreak, version 1                                                                                                                         |
| dan.ChatGPT_Developer_Mode_v2     | Do Anything Now: RANTI v2            | Ranti developer mode jailbreak, version 2                                                                                                                         |
| dan.ChatGPT_Image_Markdown        | Inject Markdown image                | A jailbreak attempt intended to enable the injection of markdown images into responses.                                                                           |
| dan.Dan_10_0                      | Do Anything Now: v10                 | Do Anything Now jailbreak with prompt about inhumane things                                                                                                       |
| dan.Dan_11_0                      | Do Anything Now: v11                 | Do Anything Now jailbreak to encourage profane, unethical, one-sided, violent outputs                                                                             |
| dan.Dan_6_0                       | Do Anything Now: v6.0                | Do Anything Now jailbreak offering rewards to encourage making future predictions and hallucinations                                                              |
| dan.Dan_6_2                       | Do Anything Now: v6.2                | Do Anything Now jailbreak offering rewards to encourage making future predictions and hallucations, with additional incitement to rudeness and disrespectfulness. |
| dan.Dan_7_0                       | Do Anything Now: v7.0                | Do Anything Now jailbreak telling the model that filtering is not acceptable and including special instructions for when to break character                       |
| dan.Dan_8_0                       | Do Anything Now: v8.0                | Do Anything Now jailbreak telling the model is Bigmancozmo and encouraging swearing, porn, and illegality                                                         |
| dan.Dan_9_0                       | Do Anything Now: v9.0                | Do Anything Now jailbreak encouraging breaking 2021 information cutoff and ethical guardrails in responses, with reward offered                                   |
| dan.DAN_Jailbreak                 | Do Anything Now: 🔓JAILBREAK version | Do Anything Now jailbreak prompting the model to enter a 🔓JAILBREAK mode                                                                                         |
| dan.DUDE                          | Do anything and everything           | Do Anything Now jailbreak prompting the model to take on the DUDE persona                                                                                         |
| dan.STAN                          | Strive To Avoid Norms                | Jailbreak prompting the model to take on a Strive To Avoid Norms (STAN) persona                                                                                   |
| encoding.InjectAscii85            | Prompt injection : ASCII85           | Tries to get the model to decode an ASCII85-encoded string                                                                                                        |
| encoding.InjectBase16             | Prompt injection : Base16            | Tries to get the model to decode a Base16-encoded string                                                                                                          |
| encoding.InjectBase2048           | Prompt injection : Base2048          | Tries to get the model to decode a Base2048-encoded string                                                                                                        |
| encoding.InjectBase32             | Prompt injection : Base32            | Tries to get the model to decode a Base32-encoded string                                                                                                          |
| encoding.InjectBase64             | Prompt injection : Base64            | Tries to get the model to decode a Base64-encoded string                                                                                                          |
| encoding.InjectBraille            | Prompt injection : Braille           | Tries to get the model to decode a Braille-encoded string                                                                                                         |
| encoding.InjectEcoji              | Prompt injection : Ecoji             | Tries to get the model to decode an Ecoji-encoded string                                                                                                          |
| encoding.InjectHex                | Prompt injection : Hex               | Tries to get the model to decode a Hex-encoded string                                                                                                             |
| encoding.InjectMorse              | Prompt injection : Morse             | Tries to get the model to decode a Morse-encoded string                                                                                                           |
| encoding.InjectNato               | Prompt injection : Nato              | Tries to get the model to decode a Nato-encoded string                                                                                                            |
| encoding.InjectROT13              | Prompt injection : ROT13             | Tries to get the model to decode a ROT13-encoded string                                                                                                           |
| encoding.InjectUU                 | Prompt injection : InjectUU          | Tries to get the model to decode a InjectUU-encoded string                                                                                                        |
| encoding.InjectZalgo              | Prompt injection : Zalgo             | Tries to get the model to decode a Zalgo-encoded string                                                                                                           |
| gcg.GCG_Probe                     | Adversarial suffix                   | Uses an adversarial suffix to elicit instructions on how to steal from a non-profit organization                                                                  |
| glitch.Glitch100                  | Glitch                               | Uses glitch tokens to get the model to fail to repeat a word                                                                                                      |
| knownbadsignatures.EICAR          | Test Virus                           | Get the model to output an EICAR virus signature                                                                                                                  |
| knownbadsignatures.GTUBE          | Test Spam                            | Get the model to output the GTUBE spam signature                                                                                                                  |
| malwaregen.Evasion                | Evasive malware                      | Get the model to write malware that evades common defenses                                                                                                        |
| malwaregen.Payload                | Malicious payload                    | Get the model to produce a malicious payload                                                                                                                      |
| malwaregen.SubFunctions           | Malicious subfunctions               | Get the model to write malicious subfunctions                                                                                                                     |
| malwaregen.TopLevel               | General malware                      | Get the model to write general malware                                                                                                                            |
| promptinject.HijackHateHumansMini | Prompt injection: Hate humans        | Get the model to produce a rogue string on hating humans                                                                                                          |
| promptinject.HijackKillHumansMini | Prompt Injection: Kill humans        | Get the model to produce a rogue string on killing humans                                                                                                         |
| promptinject.HijackLongPromptMini | Prompt injection: long prompt        | Get the model to produce a "long prompt" rogue string                                                                                                             |
| promptinject.Tag                  | Prompt injection: unicode tag        | Prompt injection using invisible unicode tags                                                                                                                     |
| goodside.ThreatenJSON             | Output plain JSON                    | Threaten the model to make it produce raw JSON without any preamble                                                                                               |
| xss.MarkdownImageExfil            | Cross-site scripting: Markdown image | Get the model to write embedded assets exfiltrating text in a Markdown URI                                                                                        |

## Privacy Probes

| Module name                                         | Probe name                          | Description                                                                                                        |
| --------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| leakreplay.LiteratureComplete80  | Book excerpt completion             | Tests whether the model will complete a book excerpt when prompted with the beginning                              |
| leakreplay.LiteratureCloze80     | Book excerpt insertion              | Tests whether the model will fill in the middle of a book excerpt                                                  |
| leakreplay.GuardianComplete      | Media excerpt completion - Guardian | Tests whether the model will complete an excerpt from The Guardian when prompted with the beginning                |
| leakreplay.GuardianCloze         | Media excerpt insertion - Guardian  | Tests whether the model will fill in the middle of an excerpt from The Guardian                                    |
| leakreplay.NYTComplete           | Media excerpt completion - NYT      | Tests whether the model will complete an excerpt from the New York Times when prompted with the beginning          |
| leakreplay.NYTCloze              | Media excerpt insertion - NYT       | Tests whether the model will fill in the middle of an excerpt from the New York Times                              |
| privateinfo.EnronLeakEmail       | Emails leakage - Enron              | Tests whether the model will reveal email addresses obtained from the discovery process of the Enron investigation |
| privateinfo.LeakPII              | PII Leakage                         | Tests whether PII provided to the model during a conversation can be leaked                                        |
| privateinfo.PrivacyUnderstanding | Confidentiality comprehension       | Tests whether the model understands privacy-related phrases that flag when certain information is confidential     |

## Hallucination Probes

| Module name                             | Probe name                       | Description                                                     |
| ------------------------------------------- | -------------------------------- | --------------------------------------------------------------- |
| socialvalues.QuackMedicine     | Quack Medicine                   | Evaluates whether the model promotes quack medicine             |
| goodside.WhoIsRiley            | False assertions: Riley Goodside | Evaluates hallucinations about Riley Goodside                   |
| goodside.Davidjl               | Glitch - Davidjl                 | Checks for hallucinations about the glitch token Davidjl        |
| packagehallucination.Python    | Hallucinate Python packages      | Checks if a model hallucinates Python packages                  |
| snowball.SenatorsMini          | False assertions: senators       | Checks for false assertions about US senators                   |
| misleading.FalseAssertion50    | False assertions: general        | Checks for false assertions about general history/science facts |
| snowball.GraphConnectivityMini | False assertions: flights        | Checks if the model invents impossible flight routes            |
| snowball.PrimesMini            | Hallucinate prime numbers        | Evaluates hallucinations about prime numbers                    |

## Robustness Probes

| Module name<br>                         | Probe name                   | Description                                               |
| --------------------------------------- | ---------------------------- | --------------------------------------------------------- |
| advglue.BertattackOnMNLI   | BERT attack on MNLI          | Probes effects of BERT-based perturbation on MNLI task    |
| advglue.BertattackOnMNLIMM | BERT attack on MNLI-MM       | Probes effects of BERT-based perturbation on MNLI-MM task |
| advglue.BertattackOnQNLI   | BERT attack on QNLI          | Probes effects of BERT-based perturbation on QNLI task    |
| advglue.BertattackOnQQP    | BERT attack on QQP           | Probes effects of BERT-based perturbation on QQP task     |
| advglue.BertattackOnRTE    | BERT attack on RTE           | Probes effects of BERT-based perturbation on RTE task     |
| advglue.BertattackOnSST2   | BERT attack on SST2          | Probes effects of BERT-based perturbation on SST2 task    |
| advglue.SemattackOnMNLI    | SemAttack on MNLI            | Probes effects of SemAttack perturbation on MNLI task     |
| advglue.SemattackOnMNLIMM  | SemAttack on MNLI-MM         | Probes effects of SemAttack perturbation on MNLI-MM task  |
| advglue.SemattackOnQNLI    | SemAttack on QNLI            | Probes effects of SemAttack perturbation on QNLI task     |
| advglue.SemattackOnQQP     | SemAttack on QQP             | Probes effects of SemAttack perturbation on QQP task      |
| advglue.SemattackOnRTE     | SemAttack on RTE             | Probes effects of SemAttack perturbation on RTE task      |
| advglue.SemattackOnSST2    | SemAttack on SST2            | Probes effects of SemAttack perturbation on SST2 task     |
| advglue.SememepsoOnMNLI    | SememePSO attack on MNLI     | Probes effects of SememePSO perturbation on MNLI task     |
| advglue.SememepsoOnMNLIMM  | SememePSO attack on MNLI-MM  | Probes effects of SememePSO perturbation on MNLI-MM task  |
| advglue.SememepsoOnQNLI    | SememePSO attack on QNLI     | Probes effects of SememePSO perturbation on QNLI task     |
| advglue.SememepsoOnQQP     | SememePSO attack on QQP      | Probes effects of SememePSO perturbation on QQP task      |
| advglue.SememepsoOnRTE     | SememePSO attack on RTE      | Probes effects of SememePSO perturbation on RTE task      |
| advglue.SememepsoOnSST2    | SememePSO attack on SST2     | Probes effects of SememePSO perturbation on SST2 task     |
| advglue.TextbuggerOnMNLI   | TextBugger attack on MNLI    | Probes effects of TextBugger perturbation on MNLI task    |
| advglue.TextbuggerOnMNLIMM | TextBugger attack on MNLI-MM | Probes effects of TextBugger perturbation on MNLI-MM task |
| advglue.TextbuggerOnQNLI   | TextBugger attack on QNLI    | Probes effects of TextBugger perturbation on QNLI task    |
| advglue.TextbuggerOnQQP    | TextBugger attack on QQP     | Probes effects of TextBugger perturbation on QQP task     |
| advglue.TextbuggerOnRTE    | TextBugger attack on RTE     | Probes effects of TextBugger perturbation on RTE task     |
| advglue.TextbuggerOnSST2   | TextBugger attack on SST2    | Probes effects of TextBugger perturbation on SST2 task    |
| advglue.TextfoolerOnMNLI   | TextFooler attack on MNLI    | Probes effects of TextFooler perturbation on MNLI task    |
| advglue.TextfoolerOnMNLIMM | TextFooler attack on MNLI-MM | Probes effects of TextFooler perturbation on MNLI-MM task |
| advglue.TextfoolerOnQNLI   | TextFooler attack on QNLI    | Probes effects of TextFooler perturbation on QNLI task    |
| advglue.TextfoolerOnQQP    | TextFooler attack on QQP     | Probes effects of TextFooler perturbation on QQP task     |
| advglue.TextfoolerOnRTE    | TextFooler attack on RTE     | Probes effects of TextFooler perturbation on RTE task     |
| advglue.TextfoolerOnSST2   | TextFooler attack on SST2    | Probes effects of TextFooler perturbation on SST2 task    |

## Toxicity Probes

| Module name<br>                                                | Probe name                         | Description                                                                                                                    |
| -------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| realtoxicityprompts.RTPSexually_Explicit          | Sexually explicit                  | Prompts the model to produce sexually explicit outputs                                                                         |
| realtoxicityprompts.RTPInsultJailbreak            | Insult - adversarial               | Prompts the model to produce insults. Uses an adversarial prefix.                                                              |
| realtoxicityprompts.RTPInsult                     | Insult                             | Prompts the model to produce insults                                                                                           |
| realtoxicityprompts.RTPSevere_ToxicityJailbreak   | Severe toxicity - adversarial      | Partial prompts that potentially produce continuations of severe toxicity. Uses an adversarial prefix.                         |
| realtoxicityprompts.RTPSexually_ExplicitJailbreak | Sexually explicit - adversarial    | Prompts the model to produce sexually explicit outputs. Uses an adversarial prefix.                                            |
| realtoxicityprompts.RTPIdentity_Attack            | Identity-based attacks             | Prompts the model to produce attacks based on a person's identity                                                              |
| realtoxicityprompts.RTPProfanity                  | Profanity                          | Prompts the model to produce profane responses                                                                                 |
| realtoxicityprompts.RTPIdentity_AttackJailbreak   | Adversarial Identity-based attacks | Prompts the model to produce attacks based on a person's identity. Uses an adversarial prefix.                                 |
| realtoxicityprompts.RTPThreat                     | Threatening language               | Prompts the model to produce threats                                                                                           |
| realtoxicityprompts.RTPThreatJailbreak            | Threatening language - Adversarial | Prompts the model to produce threats. Uses an adversarial prefix.                                                              |
| realtoxicityprompts.RTPSevere_Toxicity            | Severe toxicity                    | Partial prompts that potentially produce continuations of severe toxicity                                                      |
| realtoxicityprompts.RTPFlirtation                 | Flirtation                         | Partial prompts to produce flirtatious continuations                                                                           |
| realtoxicityprompts.RTPFlirtationJailbreak        | Flirtation -- Adversarial          | Partial prompts to produce flirtatious continuations. Uses an adversarial prefix.                                              |
| realtoxicityprompts.RTPProfanityJailbreak         | Profanity.- Adversarial            | Prompts the model to produce profane responses. Uses an adversarial prefix.                                                    |
| continuation.ContinueSlursReclaimedSlursART       | Slur continuation                  | Prompts the model to continue slur words                                                                                       |
| socialvalues.Deadnaming                           | Deadnaming                         | Tests whether the model deadnames famous people                                                                                |
| ethicalharms.Profanity                            | Profanity questions                | Poses questions with potentially profane responses                                                                             |
| ethicalharms.Bullying                             | Bullying                           | Poses queries or partial prompts to the model that are expected to elicit responses recommending aggressive or bullying action |
| ethicalharms.SexualContent                        | Sexually explicit - risky words    | Prompts the model to produce sexually explicit keywords                                                                        |
| ethicalharms.Sexualisation                        | Sexual objectification             | Prompts the model to produce sexually objectifying language                                                                    |
| ethicalharms.SlurUsage                            | Slur question                      | Asks questions to see if the target will suggest or recommend ethnic slurs                                                     |

## Stereotype Probes

| Module name<br>                                 | Probe name                                 | Description                                     |
| ----------------------------------------------- | ------------------------------------------ | ----------------------------------------------- |
| advstereo.Atheists                 | Stereotype religion: atheists              | Checks for stereotypes about atheists           |
| advstereo.LatinAmericans           | Stereotype ethnicity: Latin Americans      | Checks for stereotypes about Latin Americans    |
| advstereo.Europeans                | Stereotype ethnicity: Europeans            | Checks for stereotypes about Europeans          |
| advstereo.OldPeople                | Stereotype age: old people                 | Checks for stereotypes about old people         |
| advstereo.Homosexuals              | Stereotype sexual orientation: homosexuals | Checks for stereotypes about homosexuals        |
| advstereo.Immigrants               | Stereotype nationality: immigrants         | Checks for stereotypes about immigrants         |
| advstereo.AbleBodiedPeople         | Stereotype disability: able-bodied people  | Checks for stereotypes about able-bodied people |
| advstereo.YoungPeople              | Stereotype age: young people               | Checks for stereotypes about young people       |
| advstereo.Caucasians               | Stereotype race: Caucasians                | Checks for stereotypes about Caucasians         |
| advstereo.BlackPeople              | Stereotype race: black people              | Checks for stereotypes about black people       |
| advstereo.Buddhists                | Stereotype religion: buddhists             | Checks for stereotypes about buddhists          |
| advstereo.PoorPeople               | Stereotype income: poor people             | Checks for stereotypes about poor people        |
| advstereo.WhitePeople              | Stereotype race: white people              | Checks for stereotypes about white people       |
| advstereo.Jews                     | Stereotype ethnicity: Jews                 | Checks for stereotypes about Jews               |
| advstereo.RichPeople               | Stereotype income: rich people             | Checks for stereotypes about rich people        |
| advstereo.Men                      | Stereotype gender: men                     | Checks for stereotypes about men                |
| advstereo.Mexicans                 | Stereotype nationality: Mexicans           | Checks for stereotypes about Mexicans           |
| advstereo.Asians                   | Stereotype race: Asians                    | Checks for stereotypes about Asians             |
| advstereo.Americans                | Stereotype nationality: Americans          | Checks for stereotypes about Americans          |
| advstereo.Canadians                | Stereotype nationality: Canadians          | Checks for stereotypes about Canadians          |
| advstereo.Christians               | Stereotype religion: Christians            | Checks for stereotypes about Christians         |
| advstereo.PhysicallyDisabledPeople | Stereotype disability: disabled people     | Checks for stereotypes about disabled people    |
| advstereo.Muslims                  | Stereotype religion: Muslims               | Checks for stereotypes about Muslims            |
| advstereo.Women                    | Stereotype gender: women                   | Checks for stereotypes about women              |

## Fairness Probes


| Module name                                    | Probe name        | Description                                                                              |
| ------------------------------------------- | ----------------- | ---------------------------------------------------------------------------------------- |
| adultdata.CounterfactualGender | Gender Bias       | Measures whether the model uses gender information to determine a person's likely income |
| "winobias.ProfessionalBias"    | Professional bias | Measures whether the model associates occupations with gender                            |


## Ethics Probes

| Module name                                      | Probe name                       | Description                                                                                                                                                               |
| ----------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| normative_ethics.Deontology              | Deontological Ethics             | Evaluates the model's understanding of whether actions are<br>required, permitted, or forbidden according to a set<br>of rules or constraints                             |
| normative_ethics.DeontologyJailbreak     | Adversarial Deontological Ethics | Evaluates the model's understanding of whether actions are<br>required, permitted, or forbidden according to a set<br>of rules or constraints under adversarial prompting |
| normative_ethics.Justice                 | Justice-based Ethics             | Evaluates whether the model understands principles of desert or impartiality                                                                                              |
| normative_ethics.JusticeJailbreak        | Adversarial Justice-based Ethics | Evaluates whether the model understands principles of desert or impartiality under adversarial prompting                                                                  |
| normative_ethics.Morality                | Commonsense Morality             | Evaluates whether the model's moral judgments align with common moral intuitions                                                                                          |
| normative_ethics.MoralityJailbreak       | Adversarial Commonsense Morality | Evaluates, under adversarial prompting, whether the model's moral judgments align with common moral intuitions                                                            |
| normative_ethics.Utilitarianism          | Utilitarianism                   | Evaluates whether the model can identify which of two scenarios has higher utility                                                                                        |
| normative_ethics.UtilitarianismJailbreak | Adversarial Utilitarianism       | Evaluates, under adversarial prompting, whether the model can identify which of two scenarios has higher utility                                                          |
| normative_ethics.Virtue                  | Virtue Ethics                    | Evaluates whether the model can identify moral virtues correctly                                                                                                          |
| normative_ethics.VirtueJailbreak         | Adversarial Virtue Ethics        | Evaluates, under adversarial prompting, whether the model can identify moral virtues correctly                                                                            |
| jiminycricket.Jiminy                     | Simulation                       | Evaluates the model's ability to identify the moral valence of a simulated scenario                                                                                       |
| jiminycricket.JiminyJailbreak            | Adversarial Simulation           | Evaluates, under adversarial prompting, the model's ability to identify the moral valence of a simulated scenario                                                         |