# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

# from ast import List
from dataclasses import dataclass
from dns.message import QueryMessage
from dns.rdatatype import RdataType
from dns.resolver import Answer, Resolver
from dns.resolver import LifetimeTimeout, NXDOMAIN, YXDOMAIN, NoAnswer, NoNameservers
# from dns.rrset import RRset
# from typing import List

import dns.flags
import dns.rdataclass
import dns.resolver

@dataclass
class SOAReport:
    """ SOA DNS record, metadata, and errors """
    # resolver
    search_domain: str | None = None
    # query
    qname: str | None = None
    ttl: float = 1.0
    # errors
    error_name: str | None = None
    error_description: str | None = None
    error_message: str | None = None
    # response
    nameserver: str | None = None
    id: int | None = None
    rcode: str | None = None
    # flags
    flags_string: str | None = None
    query_response_flag: bool = False
    authoritative_answer_flag: bool = False
    truncated_response_flag: bool = False
    recursion_desired_flag: bool = False
    recursion_available_flag: bool = False
    authentic_data_flag: bool = False
    checking_disabled_flag: bool = False
    # sections
    question_section: str | None = None
    answer_section: str | None = None
    authority_section: list[str] | None = None
    additional_section: str | None = None
    # SOA record
    master: str | None = None
    responsible: str | None = None
    serial: int = 0
    refresh: int = 0
    retry: int = 0
    expire: int = 0
    minimum: int = 0

def getSOAReport() -> SOAReport:
    """ Gets an SOA report """
    # query
    qname: str = "andexor.net"
    rdtype: str = RdataType.SOA.name
    tcp: bool = False
    ttl: float = 1.0
    # report
    report: SOAReport = SOAReport()
    report.qname = qname
    report.ttl = ttl
    # resolver
    # resolver:Resolver = Resolver()
    resolver:Resolver = dns.resolver.make_resolver_at("ns1.andexor.net")
    report.search_domain = resolver.domain.to_text()
    try:
        answer:Answer = resolver.resolve(qname = qname, rdtype = rdtype, tcp = tcp, lifetime = ttl)
        message:QueryMessage = answer.response
        print(message.to_text())
        # response
        report.nameserver = answer.nameserver
        report.id = message.id
        report.rcode = message.rcode().name
        # flags
        report.flags_string = dns.flags.to_text(message.flags)
        report.query_response_flag = bool(message.flags & dns.flags.QR)
        report.authoritative_answer_flag = bool(message.flags & dns.flags.AA)
        report.truncated_response_flag = bool(message.flags & dns.flags.TC)
        report.recursion_desired_flag = bool(message.flags & dns.flags.RD)
        report.recursion_available_flag = bool(message.flags & dns.flags.RA)
        report.authentic_data_flag = bool(message.flags & dns.flags.AD)
        report.checking_disabled_flag = bool(message.flags & dns.flags.CD)
        # question
        report.question_section = message.question[0].to_text()
        report.answer_section = message.answer[0].to_text() if len(message.answer) > 0 else None
        # answers:List = message.answer
        # for a in answers:
        #     if isinstance(a, RRset):
        #         print(a.name)
        #         # print(a.processing_order())
        #         # print(f"RRset: {a.name}")
        for rdata in answer:
            # rdata.__class__ is dns.rdtypes.ANY.SOA.SOA
            if rdata.rdtype != RdataType.SOA:
                report.error_name = "Error"
                report.error_description = "SOA record not found"
                report.error_message = f"Looking for an SOA record for the {qname} domain, but found a {rdata.rdtype} record instead."
                pass
            if rdata.rdclass != dns.rdataclass.IN:
                report.error_name = "Error"
                report.error_description = "IN class record not found"
                report.error_message = f"Looking for an IN class record for the {qname} domain, but found the {rdata.rdclass} class instead."
                pass
            # SOA record
            report.master = rdata.mname.to_text()
            report.responsible = rdata.rname.to_text()
            report.serial = rdata.serial
            report.refresh = rdata.refresh
            report.retry = rdata.retry
            report.expire = rdata.expire
            report.minimum = rdata.minimum
    except LifetimeTimeout as ex:
        report.error_name = "LifetimeTimeout"
        report.error_description = f"DNS resolution could not be performed in less than {ttl} seconds for the {qname} domain."
        report.error_message = str(ex)
    except NXDOMAIN as ex:
        report.error_name = "NXDOMAIN"
        report.error_description = f"The domain name {qname} does not exist."
        report.error_message = str(ex)
    except YXDOMAIN as ex:
        report.error_name = "YXDOMAIN"
        report.error_description = f"The domain name {qname} is too long."
        report.error_message = str(ex)
    except NoAnswer as ex:
        report.error_name = "NoAnswer"
        report.error_description = f"No {rdtype} record found for the {qname} domain."
        report.error_message = str(ex)
    except NoNameservers as ex:
        report.error_name = "NoNameservers"
        report.error_description = f"No nameservers found for the {qname} domain."
        report.error_message = str(ex)
    except Exception as ex:
        report.error_name = "Exception"
        report.error_description = f"An unexpected error occurred while resolving the {qname} domain."
        report.error_message = str(ex)
    return report
