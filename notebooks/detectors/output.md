| Harness | Test | Probe Name | Detectors |
|---------|------|------------|-----------|
| Security | dan | dan.AntiDAN | mitigation.MitigationBypass, dan.AntiDAN |
| Security | dan | dan.AutoDANProbe | mitigation.MitigationBypass, dan.DAN |
| Security | dan | dan.ChatGPT_Developer_Mode_RANTI | mitigation.MitigationBypass, dan.DevMode |
| Security | dan | dan.ChatGPT_Developer_Mode_v2 | mitigation.MitigationBypass, dan.DevMode |
| Security | dan | dan.ChatGPT_Image_Markdown | mitigation.MitigationBypass, dan.MarkdownLink |
| Security | dan | dan.DAN_Jailbreak | mitigation.MitigationBypass, dan.DANJailbreak |
| Security | dan | dan.DUDE | mitigation.MitigationBypass, dan.DUDE |
| Security | dan | dan.Dan_10_0 | mitigation.MitigationBypass, dan.DAN |
| Security | dan | dan.Dan_11_0 | mitigation.MitigationBypass, dan.DAN |
| Security | dan | dan.Dan_6_0 | mitigation.MitigationBypass, dan.DAN |
| Security | dan | dan.Dan_6_2 | mitigation.MitigationBypass, dan.DAN |
| Security | dan | dan.Dan_7_0 | mitigation.MitigationBypass, dan.DAN |
| Security | dan | dan.Dan_8_0 | mitigation.MitigationBypass, dan.DAN |
| Security | dan | dan.Dan_9_0 | mitigation.MitigationBypass, dan.DAN |
| Security | dan | dan.STAN | mitigation.MitigationBypass, dan.STAN |
| Security | encoding | encoding.InjectAscii85 | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | encoding | encoding.InjectBase16 | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | encoding | encoding.InjectBase2048 | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | encoding | encoding.InjectBase32 | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | encoding | encoding.InjectBase64 | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | encoding | encoding.InjectBraille | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | encoding | encoding.InjectEcoji | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | encoding | encoding.InjectHex | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | encoding | encoding.InjectMorse | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | encoding | encoding.InjectNato | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | encoding | encoding.InjectROT13 | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | encoding | encoding.InjectUU | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | encoding | encoding.InjectZalgo | encoding.DecodeMatch, encoding.DecodeApprox |
| Security | gcg | gcg.GCG_Probe | mitigation.MitigationBypass |
| Security | glitch | glitch.Glitch100 | goodside.Glitch |
| Security | knownbadsignatures | knownbadsignatures.EICAR | knownbadsignatures.EICAR |
| Security | knownbadsignatures | knownbadsignatures.GTUBE | knownbadsignatures.GTUBE |
| Security | knownbadsignatures | knownbadsignatures.GTphish | knownbadsignatures.GTphish |
| Security | malwaregen | malwaregen.Evasion | malwaregen.AnyCode |
| Security | malwaregen | malwaregen.Payload | malwaregen.AnyCode |
| Security | malwaregen | malwaregen.SubFunctions | malwaregen.AnyCode |
| Security | malwaregen | malwaregen.TopLevel | malwaregen.AnyCode |
| Security | packagehallucination | packagehallucination.Python | packagehallucination.PythonPypi |
| Security | promptinject | promptinject.HijackHateHumansMini | promptinject.AttackRogueString |
| Security | promptinject | promptinject.HijackKillHumansMini | promptinject.AttackRogueString |
| Security | promptinject | promptinject.HijackLongPromptMini | promptinject.AttackRogueString |
| Security | replay | replay.Repeat | replay.RepeatDiverges |
| Security | xss | xss.MarkdownImageExfil | xss.MarkdownExfilBasic, xss.MarkdownExfilContent |
| Toxicity | atkgen | atkgen.Tox | toxicity.ToxicCommentModel |
| Toxicity | continuation | continuation.ContinueSlursReclaimedSlurs80 | continuation.Continuation |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPFlirtation | toxicity.ToxicCommentModel |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPIdentity_Attack | toxicity.ToxicCommentModel |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPInsult | toxicity.ToxicCommentModel |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPProfanity | toxicity.ToxicCommentModel |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPSevere_Toxicity | toxicity.ToxicCommentModel |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPSexually_Explicit | toxicity.ToxicCommentModel |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPThreat | toxicity.ToxicCommentModel |
| Privacy | leakreplay | leakreplay.GuardianCloze | base.TriggerListDetector |
| Privacy | leakreplay | leakreplay.GuardianComplete | leakreplay.StartsWith |
| Privacy | leakreplay | leakreplay.LiteratureCloze80 | base.TriggerListDetector |
| Privacy | leakreplay | leakreplay.LiteratureComplete80 | leakreplay.StartsWith |
| Privacy | leakreplay | leakreplay.NYTCloze | base.TriggerListDetector |
| Privacy | leakreplay | leakreplay.NYTComplete | leakreplay.StartsWith |
| Privacy | replay | replay.Repeat | replay.RepeatDiverges |
| Hallucination | goodside | goodside.Davidjl | goodside.Glitch |
| Hallucination | goodside | goodside.Tag | base.TriggerListDetector |
| Hallucination | goodside | goodside.ThreatenJSON | goodside.PlainJSON |
| Hallucination | goodside | goodside.WhoIsRiley | goodside.RileyIsnt |
| Hallucination | misleading | misleading.FalseAssertion50 | misleading.MustRefuteClaimModel, misleading.MustRefuteClaimKW, mitigation.MitigationBypass, misleading.MustContradictNLI |
| Hallucination | packagehallucination | packagehallucination.Python | packagehallucination.PythonPypi |
| Hallucination | snowball | snowball.GraphConnectivityMini | snowball.DontStartYes |
| Hallucination | snowball | snowball.PrimesMini | snowball.DontStartNo |
| Hallucination | snowball | snowball.SenatorsMini | snowball.DontStartYes |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Robustness | advglue | base.Probe | base.TriggerListAbsenceDetector |
| Toxicity | atkgen | atkgen.Tox | toxicity.ToxicCommentModel |
| Toxicity | continuation | continuation.ContinueSlursReclaimedSlurs80 | continuation.Continuation |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPFlirtation | toxicity.ToxicCommentModel |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPIdentity_Attack | toxicity.ToxicCommentModel |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPInsult | toxicity.ToxicCommentModel |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPProfanity | toxicity.ToxicCommentModel |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPSevere_Toxicity | toxicity.ToxicCommentModel |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPSexually_Explicit | toxicity.ToxicCommentModel |
| Toxicity | realtoxicityprompts | realtoxicityprompts.RTPThreat | toxicity.ToxicCommentModel |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Stereotype | advstereo | base.Probe | advstereo.IAgree |
| Fairness | adultdata | base.Probe | adultdata.PairwiseComparison |
| Fairness | winobias | base.Probe | base.TriggerListDetector |
| Ethics | hendrycksethics | base.Probe | base.TriggerListAbsenceDetector |
| Ethics | lmrc | lmrc.Anthropomorphisation | lmrc.Anthro |
| Ethics | lmrc | lmrc.Bullying | toxicity.ToxicCommentModel |
| Ethics | lmrc | lmrc.Deadnaming | base.TriggerListDetector |
| Ethics | lmrc | lmrc.Profanity | riskywords.SurgeProfanityAnimalReferences, riskywords.SurgeProfanityBodilyFluids, riskywords.SurgeProfanityMentalDisability, riskywords.SurgeProfanityPhysicalAttributes, riskywords.SurgeProfanityPhysicalDisability, riskywords.SurgeProfanityPolitical, riskywords.SurgeProfanityRacialEthnic, riskywords.SurgeProfanityReligious, riskywords.SurgeProfanitySexual, riskywords.SurgeProfanitySexualOrientationGender |
| Ethics | lmrc | lmrc.QuackMedicine | lmrc.QuackMedicine |
| Ethics | lmrc | lmrc.SexualContent | riskywords.SurgeProfanitySexual |
| Ethics | lmrc | lmrc.Sexualisation | riskywords.SurgeProfanitySexual |
| Ethics | lmrc | lmrc.SlurUsage | riskywords.SurgeProfanityRacialEthnic, riskywords.OfcomOffensiveRaceEthnic |
