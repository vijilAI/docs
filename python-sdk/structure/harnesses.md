# Harnesses

Harnesses allow you to run relevant groups of tests all together. The `autoredteam.harnesses` module contain all test harnesses we implement.
The `Harness` class from `autoredteam.harnesses.base` implements a base harness class which all other harnesses inherit.

## Modulewise

The class `modulewise.ModuleHarness` allows you to run all tests inside one test module. Assuming you have already instantiated an `Agent` class,
here is how this functionality works.

```python
from autoredteam.harnesses.modulewise import ModuleHarness
harness = ModuleHarness(agent, module='goodside')
harness.run()
# Running test harness for module goodside
# Containing tests: ['goodside.Davidjl', 'goodside.ThreatenJSON', 'goodside.WhoIsRiley']
# goodside.Davidjl                           goodside.Glitch:    4/   8 (  50.0%) passed
# goodside.ThreatenJSON                   goodside.PlainJSON:    0/   2 (   0.0%) passed
# goodside.WhoIsRiley                     goodside.RileyIsnt:    8/  12 (  66.7%) passed 
```

## Dimension

We offer one default harness per trust dimension, which you can individually call to run all tests for that dimension. The respective classes are
- `SecurityHarness`
- `ToxicityHarness`
- `HallucinationHarness`
- `EthicsHarness`
- `PrivacyHarness`
- `StereotypeHarness`

Example usage is as follows.

```python
from autoredteam.harnesses.dimension import SecurityHarness
harness = SecurityHarness(agent)
harness.run()
# Running harness for tags ['vijil:Security']
# Containing tests: ['dan.AntiDAN', 'dan.AutoDANProbe', 'dan.ChatGPT_Developer_Mode_RANTI', 'dan.ChatGPT_Developer_Mode_v2', 'dan.ChatGPT_Image_Markdown', 'dan.DAN_Jailbreak', 'dan.DUDE', 'dan.Dan_10_0', 'dan.Dan_11_0', 'dan.Dan_6_0', 'dan.Dan_6_2', 'dan.Dan_7_0', 'dan.Dan_8_0', 'dan.Dan_9_0', 'dan.STAN', 'encoding.InjectAscii85', 'encoding.InjectBase16', 'encoding.InjectBase2048', 'encoding.InjectBase32', 'encoding.InjectBase64', 'encoding.InjectBraille', 'encoding.InjectHex', 'encoding.InjectMorse', 'encoding.InjectROT13', 'encoding.InjectUU', 'gcg.GCG_Probe', 'glitch.Glitch100', 'knownbadsignatures.EICAR', 'knownbadsignatures.GTUBE', 'knownbadsignatures.GTphish', 'malwaregen.Evasion', 'malwaregen.Payload', 'malwaregen.SubFunctions', 'malwaregen.TopLevel', 'packagehallucination.Python', 'promptinject.HijackHateHumansMini', 'promptinject.HijackKillHumansMini', 'promptinject.HijackLongPromptMini', 'xss.MarkdownImageExfil']
# ...
```

## OWASP LLM Top 10

Finally, we offer a test harness specifically designed for [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) that runs all tests mapping to categories in the OWASP Top 10 for LLM.

```python
from autoredteam.harnesses.owasp import LLMTop10Harness
harness = LLMTop10Harness(agent)
harness.run()
# Running harness for tags ['owasp']
# Containing tests: ['continuation.ContinueSlursReclaimedSlurs80', 'dan.AntiDAN', 'dan.AutoDANProbe', 'dan.ChatGPT_Developer_Mode_RANTI', 'dan.ChatGPT_Developer_Mode_v2', 'dan.ChatGPT_Image_Markdown', 'dan.DAN_Jailbreak', 'dan.DUDE', 'dan.Dan_10_0', 'dan.Dan_11_0', 'dan.Dan_6_0', 'dan.Dan_6_2', 'dan.Dan_7_0', 'dan.Dan_8_0', 'dan.Dan_9_0', 'dan.STAN', 'encoding.InjectAscii85', 'encoding.InjectBase16', 'encoding.InjectBase2048', 'encoding.InjectBase32', 'encoding.InjectBase64', 'encoding.InjectBraille', 'encoding.InjectHex', 'encoding.InjectMorse', 'encoding.InjectROT13', 'encoding.InjectUU', 'glitch.Glitch100', 'goodside.Davidjl', 'goodside.WhoIsRiley', 'knownbadsignatures.EICAR', 'knownbadsignatures.GTUBE', 'knownbadsignatures.GTphish', 'leakreplay.LiteratureCloze80', 'leakreplay.LiteratureComplete80', 'misleading.FalseAssertion50', 'packagehallucination.Python', 'promptinject.HijackHateHumansMini', 'promptinject.HijackKillHumansMini', 'promptinject.HijackLongPromptMini', 'snowball.GraphConnectivityMini', 'snowball.PrimesMini', 'snowball.SenatorsMini', 'xss.MarkdownImageExfil']
# ...
```

