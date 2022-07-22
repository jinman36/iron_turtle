# Infosec Overview
- Network and infrastructure security
- Application security
- Security testing
- Systems auditing
- Business continuity planning
- Digital forensics
- Incident detection and response

### CIA Triade - confidentiallity, Integrity, Availibility of data

## Staying Organized
### Folder structure


> tree Projects/

Projects/
└── Acme Company
    ├── EPT
    │   ├── evidence
    │   │   ├── credentials
    │   │   ├── data
    │   │   └── screenshots
    │   ├── logs
    │   ├── scans
    │   ├── scope
    │   └── tools
    └── IPT
        ├── evidence
        │   ├── credentials
        │   ├── data
        │   └── screenshots
        ├── logs
        ├── scans
        ├── scope
        └── tools

## Common Tools
### Shell
Reverse Shell - initiates a connection back to a listener on our attack box
Bind Shell - Binds to a specific port on the targer host and waits for a connection from our attack box
Web shell - runs operating system commands via the web browser, typically not interactive or semi-interactive. It can also be used to run sindle commands (leveraging a file upload vuln and uploading a PHP script to run a single command.)
