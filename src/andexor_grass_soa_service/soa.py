from dataclasses import dataclass
import dns.resolver
import sys

@dataclass
class SOAReport:
    """ SOA DNS record, metadata, and errors """
    # resolver
    domain: str = None
    nameservers: list = None
    # query
    qname: str = None
    tcp: bool = False
    ttl: int = 0
    # errors
    error: str = None
    msg: str = None
    # SOA record
    master: str = None
    responsible: str = None
    serial: int = 0
    refresh: int = 0
    retry: int = 0
    expire: int = 0
    minimum: int = 0

def getSOAReport() -> SOAReport:
    """ Gets an SOA report """
    report: SOAReport = SOAReport()
    # resolver
    resolver = dns.resolver.Resolver()
    report.domain = resolver.domain.to_text()
    report.nameservers = resolver.nameservers
    # query
    qname: str = "andexor.net"
    rdtype: str = "SOA"
    tcp: bool = False
    ttl: float = 1.0
    report.qname = qname
    report.tcp = tcp
    report.ttl = ttl
    try:
        answers = resolver.resolve(qname = qname, rdtype = rdtype, tcp = tcp, lifetime = ttl)
        for rdata in answers:
            if rdata.rdtype.name != "SOA":
                report.error = "Error"
                report.msg = "SOA record not found"
                pass
            if rdata.rdclass != dns.rdataclass.IN:
                report.error = "Error"
                report.msg = "class is " + rdata.rdclass + " (not IN)"
                pass
            # SOA record
            report.master = rdata.mname.to_text()
            report.responsible = responsible = rdata.rname.to_text()
            report.serial = rdata.serial
            report.refresh = rdata.refresh
            report.retry = rdata.retry
            report.expire = rdata.expire
            report.minimum = rdata.minimum
    except dns.name.EmptyLabel as err:
        report.error = "EmptyLabel"
        report.msg = err.msg
    except dns.resolver.LifetimeTimeout as err:
        report.error = "LifetimeTimeout"
        report.msg = err.msg
    except dns.resolver.NoAnswer as err:
        report.error = "NoAnswer"
        report.msg = err.msg
    except dns.resolver.NoNameservers as err:
        report.error = "NoNameservers"
        report.msg = err.msg
    except dns.resolver.NXDOMAIN as err:
        report.error = "NXDOMAIN"
        report.msg = err.msg
    except dns.resolver.YXDOMAIN as err:
        report.error = "YXDOMAIN"
        report.msg = err.msg
    except:
        report.error = "Error"
        ex = sys.exception()
        args = ex.args
        if len(args) > 0:
            report.msg = args[0]
    return report
