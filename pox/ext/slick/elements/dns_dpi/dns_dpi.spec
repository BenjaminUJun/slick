{
    "dns_dpi": {
        "machine": "x86",
        "os": "Linux",
        "os_flavor": "Ubuntu",
        "software": "python",
        "inline": "no",
        "triggers": [
            "BadDomainEvent",
            "MultipleBadDomainRequestEvent",
            "DNSPacketSizeEvent",
            "DNSRequestExceedEvent",
            "IllegalDNSServer"
        ]
    }
}