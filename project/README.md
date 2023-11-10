# SurfSentry

Surfsentry is a Windows application developed to protect users against malicious websites. It retrieves a list of malicious links from USOM (Ulusal Siber Olaylara Müdahale Merkezi - National Cyber Incident Response Center) and writes them to the hosts file. This ensures a secure internet experience for users.

## Blocking CNC Server IPs

Surfsentry not only blocks domain connections by writing them to the hosts file, but also identifies IP addresses associated with Command and Control (CNC) servers provided by USOM. It adds firewall rules to block communication with these IPs, providing an additional layer of protection against malicious activity.

## Installation

To use Surfsentry, follow these steps:

1. Clone the project repository or download the ZIP file.
2. Navigate to the project/dist folder and run the `surfsentry.exe` application (you should run with administration permissions for blocking operations).
4. Start using the application.

## Usage

Surfsentry is easy to use. When you run the application, it retrieves a list of malicious website links from USOM and writes them to the hosts file. This helps users have a secure internet experience and safeguards against malicious websites. The application features a user-friendly interface with additional instructions.

## Disclaimer

This project no longer performs DNS resolution. Instead, it retrieves malicious website links from USOM and writes them to the hosts file and firewall rule for protection.
