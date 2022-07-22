- Helpful command links (powershell)
  - https://gist.github.com/HarmJ0y/184f9822b195c52dd50c379ed3117993

# Active Directory 
- is a collection of machines and servers connected inside of domains, that are a collective part of a bigger forest of domains, that make up the Active Directory network.
  - Domain Controllers
  - Forests, Trees, Domains
  - Users + Groups 
  - Trusts
  - Policies 
  - Domain Services

## Domain Controllers
- A domain controller is a Windows server that has Active Directory Domain Services (AD DS) installed and has been promoted to a domain controller in the forest.

## Active Directory Data Store (AS DS)
- Contains the NTDS.dit - a database that contains all of the information of an Active Directory domain controller as well as password hashes for domain users
- Stored by default in %SystemRoot%\NTDS
- accessible only by the domain controller

## AD Users
- Domain Admins
- Service Accounts (Domain Admins)
- Local Administrators
- Domain Users

## AD Groups
- Security Groups
- Distribution Groups

## Domain trusts
- Directional
- Transitive

