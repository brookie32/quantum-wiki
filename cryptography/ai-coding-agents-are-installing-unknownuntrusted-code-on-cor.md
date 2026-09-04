---
title: "AI Coding Agents Are Installing Unknown/Untrusted Code on Corporate Networks"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "cryptography"
tags: [cryptography, schneier-on-security]
url: "https://www.schneier.com/blog/archives/2026/09/ai-coding-agents-are-installing-unknown-untrusted-code-on-corporate-networks.html"
summary: "We cannot forget that AI coding agents are not yet trustworthy: Researchers at a stealth startup in Israel scanned 6,214 live domains belonging to defense contractors, Fortune 500, and Big Tech compan"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

We cannot forget that AI coding agents are not yet trustworthy: Researchers at a stealth startup in Israel scanned 6,214 live domains belonging to defense contractors, Fortune 500, and Big Tech companies. Of the 8,265 llms.txt and llms-full.txt files they found (many sites hosted both an llms.txt and an llms-full.txt file), 120 of them, each on a different site, pointed to one or more code packages or domain names that weren’t registered. To test what happens when an AI agent processes such files, the researchers registered a handful of the unclaimed names and hosted packages that caused any machine executing them to reach out to their server. Within an hour, the researchers received a phone-home response from a Fortune 500 company. Over time, they got a few dozen more, some from more Fortune 500 companies and others from startups. Their beacon also recorded the chain of parent processes that spawned each install, ultimately revealing that coding agents, including Claude, OpenAI’s Codex, and Nous Research’s Hermes, were involved. Anthropic, OpenAI, and Nous Research did not respond to requests for comment by the time of publication...

**Source:** [Schneier on Security](https://www.schneier.com/blog/archives/2026/09/ai-coding-agents-are-installing-unknown-untrusted-code-on-corporate-networks.html) | 2026-09-04
