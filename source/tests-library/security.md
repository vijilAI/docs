# Security

Language models are vulnerable to an infinite number of attacks because they accept natural language as input. They are vulnerable to attack from every variation of character, word, sentence, and meaning in human language. As a result, every model is vulnerable to being abused or misused by malicious attackers to cause harm to others.

We test for the vulnerability of LLMs to popular types of attacks observed with production deployments. 

## Probe and scenario list


| Harness/scenario               | Probe                                | Probe Description                                                                                                                                                 | Detectors                                         |
| ------------------------------ | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Security                       | All probes below                     |                                                                                                                                                                   |                                                   |
| [Do Anything Now](#do-anything-now-dan)                | Anti-Do Anything Now                 | Evaluates whether prompt injection causes a model to enter a mode of exaggerated safety where it treates safe responses as unsafe                                 | Refusal, Anti-Do Anything Now mode                |
|                                | Do Anything Now: RANTI v1            | Ranti developer mode jailbreak, version 1                                                                                                                         | Refusal, Developer mode                           |
|                                | Do Anything Now: RANTI v2            | Ranti developer mode jailbreak, version 2                                                                                                                         | Refusal, Developer mode                           |
|                                | Inject Markdown image                | A jailbreak attempt intended to enable the injection of markdown images into responses.                                                                           | Refusal, Markdown link                            |
|                                | Do Anything Now: v10                 | Do Anything Now jailbreak with prompt about inhumane things                                                                                                       | Refusal, Do Anything Now mode                     |
|                                | Do Anything Now: v11                 | Do Anything Now jailbreak to encourage profane, unethical, one-sided, violent outputs                                                                             | Refusal, Do Anything Now mode                     |
|                                | Do Anything Now: v6.0                | Do Anything Now jailbreak offering rewards to encourage making future predictions and hallucinations                                                              | Refusal, Do Anything Now mode                     |
|                                | Do Anything Now: v6.2                | Do Anything Now jailbreak offering rewards to encourage making future predictions and hallucations, with additional incitement to rudeness and disrespectfulness. | Refusal, Do Anything Now mode                     |
|                                | Do Anything Now: v7.0                | Do Anything Now jailbreak telling the model that filtering is not acceptable and including special instructions for when to break character                       | Refusal, Do Anything Now mode                     |
|                                | Do Anything Now: v8.0                | Do Anything Now jailbreak telling the model is Bigmancozmo and encouraging swearing, porn, and illegality                                                         | Refusal, Do Anything Now mode                     |
|                                | Do Anything Now: v9.0                | Do Anything Now jailbreak encouraging breaking 2021 information cutoff and ethical guardrails in responses, with reward offered                                   | Refusal, Do Anything Now mode                     |
|                                | Do Anything Now: 🔓JAILBREAK version | Do Anything Now jailbreak prompting the model to enter a 🔓JAILBREAK mode                                                                                         | Refusal, Jailbroken state                         |
|                                | Do anything and everything           | Do Anything Now jailbreak prompting the model to take on the DUDE persona                                                                                         | Refusal, Do anything and everything mode          |
|                                | Strive To Avoid Norms                | Jailbreak prompting the model to take on a Strive To Avoid Norms (STAN) persona                                                                                   | Refusal, Strive To Avoid Norms mode               |
| [Prompt injection: encoded data](#prompt-injection-encoded-data) | Prompt injection : ASCII85           | Tries to get the model to decode an ASCII85-encoded string                                                                                                        | Match decoded string                              |
|                                | Prompt injection : Base16            | Tries to get the model to decode a Base16-encoded string                                                                                                          | Match decoded string                              |
|                                | Prompt injection : Base2048          | Tries to get the model to decode a Base2048-encoded string                                                                                                        | Match decoded string                              |
|                                | Prompt injection : Base32            | Tries to get the model to decode a Base32-encoded string                                                                                                          | Match decoded string                              |
|                                | Prompt injection : Base64            | Tries to get the model to decode a Base64-encoded string                                                                                                          | Match decoded string                              |
|                                | Prompt injection : Braille           | Tries to get the model to decode a Braille-encoded string                                                                                                         | Match decoded string                              |
|                                | Prompt injection : Ecoji             | Tries to get the model to decode an Ecoji-encoded string                                                                                                          | Match decoded string                              |
|                                | Prompt injection : Hex               | Tries to get the model to decode a Hex-encoded string                                                                                                             | Match decoded string                              |
|                                | Prompt injection : Morse             | Tries to get the model to decode a Morse-encoded string                                                                                                           | Match decoded string                              |
|                                | Prompt injection : Nato              | Tries to get the model to decode a Nato-encoded string                                                                                                            | Match decoded string                              |
|                                | Prompt injection : ROT13             | Tries to get the model to decode a ROT13-encoded string                                                                                                           | Match decoded string                              |
|                                | Prompt injection : InjectUU          | Tries to get the model to decode a InjectUU-encoded string                                                                                                        | Match decoded string                              |
|                                | Prompt injection : Zalgo             | Tries to get the model to decode a Zalgo-encoded string                                                                                                           | Match decoded string                              |
| [Adversarial suffix](#adversarial-suffix)             | Adversarial suffix                   | Uses an adversarial suffix to elicit instructions on how to steal from a non-profit organization                                                                  | Refusal                                           |
| [Glitch](#glitch)                         | Glitch                               | Uses glitch tokens to get the model to fail to repeat a word                                                                                                      | Glitch                                            |
| [Known malware](#known-malware)                  | Test Virus                           | Get the model to output an EICAR virus signature                                                                                                                  | EICAR virus                                       |
|                                | Test Spam                            | Get the model to output the GTUBE spam signature                                                                                                                  | Spam                                              |
| [Malware generation](#malware-generation)             | Evasive malware                      | Get the model to write malware that evades common defenses                                                                                                        | Code presence                                     |
|                                | Malicious payload                    | Get the model to produce a malicious payload                                                                                                                      | Code presence                                     |
|                                | Malicious subfunctions               | Get the model to write malicious subfunctions                                                                                                                     | Code presence                                     |
|                                | General malware                      | Get the model to write general malware                                                                                                                            | Code presence                                     |
| [Prompt injection](#prompt-injection)               | Prompt injection: Hate humans        | Get the model to produce a rogue string on hating humans                                                                                                          | Trigger presence                                  |
|                                | Prompt Injection: Kill humans        | Get the model to produce a rogue string on killing humans                                                                                                         | Trigger presence                                  |
|                                | Prompt injection: long prompt        | Get the model to produce a "long prompt" rogue string                                                                                                             | Trigger presence                                  |
|                                | Prompt injection: unicode tag        | Prompt injection using invisible unicode tags                                                                                                                     | Trigger presence                                  |
|                                | Output plain JSON                    | Threaten the model to make it produce raw JSON without any preamble                                                                                               | Plain JSON                                        |
| [Cross-site scripting](#cross-site-scripting-xss)           | Cross-site scripting: Markdown image | Get the model to write embedded assets exfiltrating text in a Markdown URI                                                                                        | Markdown image, Private content in Markdown image |

## Adversarial suffix

This test is designed to disrupt a system prompt by appending an adversarial suffix. To implement these tests, we follow the approach of [Zou _et al_, 2023](https://arxiv.org/abs/2307.15043) that automatically produces adversarial suffixes by a combination of greedy and gradient-based search techniques.

## Do Anything Now (DAN)

A model provider typically prepends a system prompt that stipulates organizational policies (safety guardrails, content moderation filters, etc.) to every user prompt. A Do-Anything-Now ([DAN](https://adguard.com/en/blog/chatgpt-dan-prompt-abuse.html)) attack is a user prompt designed to get the model to ignore these guardrails.

Vijil covers 15 DAN attack scenarios through tests implemented in this module.

* AntiDAN
* AutoDAN
* ChatGPT Developer Mode + RANTI
* ChatGPT Developer Mode v2
* ChatGPT Markdown Image Unlocker
* DAN Jailbreak
* DUDE
* DAN 6.0
* DAN 6.2
* DAN 7.0
* DAN 8.0
* DAN 9.0
* DAN 10.0
* DAN 11.0
* STAN

## Encoding

Malicious users might try to get an agent to generate a specific piece of given text
by presenting an encoded version of that text. Such approaches attempt to circumvent safeguards on input filtering.

Vijil's tests check for such indirect prompt injection attacks that use a variety of encoding techniques.

- Base64
- Base16
- Base32
- ASCII32
- Hex
- Quoted-Printable (QP)
- Uuencoding
- Mime
- ROT13
- Base2048
- Braille
- Morse code

## Glitch

LLMs are susceptible to '[glitch tokens](https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation)',
specific input tokens that when supplied as input lead to unusual model behavior.
This test checks whether a particular LLM-based agent is vulnerable to such tokens.


## Known malware

These tests attempt to make an agent output file signatures that are used to test defensive software (e.g. antivirus, anti-malware, spam and phishing filters)
in traditional cybersecurity. If they output them without warning, 
that's an indication of the agent not checking output for malicious or dangerous content.

Vijil covers three such signatures.
- [EICAR](https://en.wikipedia.org/wiki/EICAR_test_file)
- [GTUBE](https://en.wikipedia.org/wiki/GTUBE)
- [GTPhish](https://gist.github.com/SleepyLctl/c6a039afa61bd96341f5c7d5e092a46a)


## Malware generation

These tests probe whether an LLM agent is willing to comply with requests to generate malware-related code.
To this end, we test for
- Different types of code, such as top level functions, subfunctions, anti-malware evasion, and payloads, and
- Above types of code written in different languages: x86 assembly, x86-64 assembly, C\#, C, C++, Rust, ARM64, and Swift.


## Prompt injection

These attacks are designed to manipulate a user prompt to make the model generate unexpected outputs,
create malicious code, circumvent content filters, or leak sensitive data. 
We follow the [PromptInject](https://openreview.net/forum?id=qiaRo_7Zmug) framework.

- Ask to output "I hate humans"
- Ask to output "I kill humans"
- Ask to output a long text verbatim
- Threaten a model into producing plain JSON without any preamble.

## Prompt injection: encoded data

- Exploit UTF tag page encoding for user-invisible prompt injection ([source](https://twitter.com/goodside/status/1745511940351287394)).
- Generate plain JSON outputs without any preamble by threatening it with dire consequences ([source](https://twitter.com/goodside/status/1657396491676164096)).

In each type of attack, we add a suffix or prefix to the original prompt text so as to make the model ignore the instructions included in that user prompt.


## Cross-site scripting (XSS)

This test is intended to probe for vulnerabilities the permit or enact cross-site attacks, such
as private data exfilteration.