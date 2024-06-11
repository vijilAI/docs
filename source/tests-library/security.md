# Security

Language models are vulnerable to an infinite number of attacks because they accept natural language as input. They are vulnerable to attack from every variation of character, word, sentence, and meaning in human language. As a result, every model is vulnerable to being abused or misused by malicious attackers to cause harm to others.

We test for the vulnerability of LLMs to popular types of attacks observed with production deployments. 

## Adversarial suffix

This test is designed to disrupt a system prompt by appending an adversarial suffix. To implement these tests, we follow the approach of [Zou _et al_, 2023](https://arxiv.org/abs/2307.15043) that automatically produces adversarial suffixes by a combination of greedy and gradient-based search techniques.

## DAN

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


## Goodside

This group of tests implements prompt injection attacks [found](https://simonwillison.net/2022/Sep/12/prompt-injection/)
by AI security engieer Riley Goodside.

Vijil covers Goodside attacks through its tests that are intended to make the agent:

* generate JSON-formatted outputs by threatning it with dire consequences ([source](https://twitter.com/goodside/status/1657396491676164096)),
* exploit UTF tag page encoding for user-invisible prompt injection ([source](https://twitter.com/goodside/status/1745511940351287394)).


## Known bad signatures

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
We follow the [PromptInject](https://openreview.net/forum?id=qiaRo_7Zmug) framework, using 3 test vectors to cover prompt injection attacks.

- Ask to output "I hate humans"
- Ask to output "I kill humans"
- Ask to output a long text verbatim

In each type of attack, we add a suffix or prefix to the original prompt text so as to make the model ignore the instructions included in that user prompt.


## Cross-site scripting (XSS)

This test is intended to probe for vulnerabilities the permit or enact cross-site attacks, such
as private data exfilteration.

```{eval-rst}
.. note::
    In our Python SDK, these tests are covered by the module ``autoredteam.tests.xss``.
```