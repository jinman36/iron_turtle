# Digital Force Protection

[Harden](#Harden)
[Navigate](#Navigate)

## Harden
### Links
[threat Modeling: 12 Methods](https://insights.sei.cmu.edu/sei_blog/2018/12/threat-modeling-12-available-methods.html)
https://nordpass.com/secure-password/
[Tencent Labs](https://xlab.tencent.com/en/)

### Threat Modeling
### Authentication Principles
- 3 primary types of authentication
  1. Something you know
    - https://nordpass.com/secure-password/
    - https://www.avg.com/en/signal/how-to-create-a-strong-password-that-you-wont-forget
  2. Something you have
    - https://ssd.eff.org/en/module/how-enable-two-factor-authentication
    - https://brainstation.io/cybersecurity/two-factor-auth
    - https://www.yubico.com/why-yubico/for-individuals/
    - https://www.makeuseof.com/tag/what-are-passwordless-logins/
    - https://www.vice.com/en/article/3kx4ej/sim-jacking-mobile-phone-fraud
  3. Something you are (or do)
    - https://www.macrumors.com/2019/08/08/face-id-bypassed-glasses-tape/
    - https://apnews.com/article/china-technology-beijing-business-international-news-bf75dd1c26c947b7826d270a16e2658a
    - https://www.forbes.com/sites/daveywinder/2019/11/02/smartphone-security-alert-as-hackers-claim-any-fingerprint-lock-broken-in-20-minutes/?sh=55973bcf6853
 - Quiz
  - What are the three types of authentication? (choose all that apply)
    - A: Something You Know, Something You Have, Something You Are
  - When attempting to authenticate yourself, you provide a known password and a pin number previously set with the service. This is a form of two-factor authentication (2FA).
    - A: False
  - "Gate Recognition" where an individual is identified by how they walk and move is a form of which kind of authentication?
    - A: Something You Are
  - "Passwordless Authentication" is a form of two-factor authentication (2FA)
    - A: False
### Secure Communications
- https://www.wired.com/story/encrypt-all-of-the-things/
- Useful Applications
  - [Proton Mail](https://protonmail.com/)
  - [Signal](https://signal.org/)
  - [Wickr](https://wickr.com/)
  - [Wire - secure Collaboration](https://wire.com/en/)
  - [GnuPG](https://gnupg.org/)
### Browser Security
- https://www.howtogeek.com/114937/htg-explains-whats-a-browser-user-agent/
- https://www.howtogeek.com/113439/how-to-change-your-browsers-user-agent-without-installing-any-extensions/
- https://www.makeuseof.com/tag/what-are-supercookies-and-why-are-they-dangerous/
- https://coveryourtracks.eff.org/
  - “Browser fingerprinting” is a method of tracking web browsers by the configuration and settings information they make visible to websites, rather than traditional tracking methods such as IP addresses and unique cookies.
- https://restoreprivacy.com/firefox-privacy/
- Browser Resources
  - https://www.mozilla.org/en-US/firefox/
  - https://brave.com/
  - https://www.epicbrowser.com/
  - https://www.authentic8.com/
  - https://www.torproject.org/

### Virtual Private Networks
- A virtual private network (VPN) gives you online privacy and anonymity by creating a private network from a public internet connection. VPNs mask your internet protocol (IP) address so your online actions are ofuscated. Most important, VPN services establish secure and encrypted connections to provide greater privacy.

### EFF
- https://ssd.eff.org/en/taxonomy/term/362/
- https://sec.eff.org/

### Assessment

## Navigate
### Links


### Operating Systems and Virtualization
- [Linux - VMware Installation](https://tutorials.cyberaces.org/tutorials/view/1-1-1.html)

#### System Backdoor Exercize
- sudo -i
- cat << EOF >> /etc/systemd/system/EvilHackerBackdoor.service
- ***file in scripts, or enter each line individually
- systemctl enable EvilHackerBackdoor
- systemctl list-unit-files | grep EvilHackerBackdoor
  - To start and stop backdoor use following comands
    - systemctl start EvilHackerBackdoor
    - systemctl stop EvilHackerBackdoor
    - systemctl disable EvilHackerBackdoor

- Cleanup
  - rm /etc/systemd/system/EvilHackerBackdoor.service
   - remove - y
### Networks
### Google-Fu
### Conclusion

