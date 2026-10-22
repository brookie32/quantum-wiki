---
title: "New Serious PHP Vulnerabilities Released and Patched"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "cryptography"
tags: [cryptography, schneier-on-security]
url: "https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html"
summary: "PHP maintainers have released two critical vulnerabilities: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical vulnerabilities that can allow unauthenticated remote code execution. All PHP users a"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

PHP maintainers have released two critical vulnerabilities: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical vulnerabilities that can allow unauthenticated remote code execution. All PHP users are strongly encouraged to update immediately. Who is at risk: all PHP installations serving web requests, including PHP-FPM, Apache with mod_php, php-cgi, FrankenPHP and LiteSpeed. We consider the risk highest for mod_php, with a demonstrated exploit where an unauthenticated request can trigger the attack before any application code runs. The vulnerabilities:...

**Source:** [Schneier on Security](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html) | 2026-10-22
