
# !/usr/bin/python
import pdb
import sys
import os
import re
from optparse import OptionParser
from python_arptable import *
import nmap


class commonLib(object):
    def __init__(self, parser):
        self.parser = parser

    def cmdLineParser(self):

        self.parser.add_option("-i", "--host", type="string",dest="host" ,help='x.x.x.x:optional host that overrides fetching the ARP cache and instead just scans the given host',
                               )
        self.parser.add_option("-t", "--tcp", type="string",dest="tcp" ,help='<start_port>-<end_port>: scan the given TCP ports'
                               )
        self.parser.add_option("-u", "--udp", type="string",dest="udp",help='<start_port>-<end_port>: scan the given UDP ports'
                               )

        self.parser.add_option("-f", "--foo", type="string",dest="unknown")

        return self.parser.parse_args()

    def checkargs(self, args):
        if len(args) == 3:
            self.apmac = sys.argv[1]
            self.stamac = sys.argv[2]
            self.pcap = sys.argv[3]
            self.checkmac(self.apmac)


class network :

    def __init__(self):
           pass

    def perform_arp_cache(self):
        print "------------------\nperforming arp scan\n------------------\n"
        print "Ip addres\tMask\tHw-addres\t       Device"
        #print type(ARPTABLE)
        for i in ARPTABLE :
            print ("%s\t%s\t%s\t%s"%(i['IP address'],i['Mask'],i['HW address'],i['Device']) )

    def perform_host_scan(self,host):
        print "------------------\nperforming host scan on %s\n------------------\n"%host
        print "host\topen_tcp_ports\topen_udp_ports\tos_type"
        nm = nmap.PortScanner()
        tcp_open_ports=[]
        udp_open_ports=[]
        nmap_host_scan=nm.scan(host, arguments='-O')['scan']
        state=nmap_host_scan[host]['status']['state']
        #print "host status is %s "%state

        os=nmap_host_scan[host]['osmatch']
        os_type=os[0]['osclass'][0]['osfamily']
        ports=nmap_host_scan[host]['portused']
        for port in ports:
           # print port

            if port['proto']== 'tcp' and port['state'] == 'open' :
                    tcp_open_ports.append(port['portid'])

            if port['proto'] == 'udp' and port['state'] == 'open':
                    udp_open_ports.append(port['portid'])

        if state == 'up' :
            print "%s\t%s\t%s\t%s"%(host,", ".join(tcp_open_ports),", ".join(udp_open_ports),os_type)
        else :
            tcp_open_ports = []
            udp_open_ports = []
            os_type=""
            print "%s\t%s\t%s\t%s" % (host, ", ".join(tcp_open_ports), ", ".join(udp_open_ports), os_type)


    def perfrom_tcp_scan(self,tcpport):
        print "------------------\nperforming tcp port scanning in range of %s\n------------------\n"%tcpport
        print "host\t\topen_tcp_ports\topen_udp_ports\tos_type"
        for entry in ARPTABLE :
            #print "ip is : %s "%entry['IP address']
            host=entry['IP address']
            self.scan_result(host,'tcp',tcpport)
            #print nm.scan(host,tcp,arguments='-O')[host]





    def perform_udp_scan(self,udpport):
        print "------------------\nperforming udp port scanning in range of %s\n------------------\n"%udpport
        print "host\t\topen_tcp_ports\topen_udp_ports\tos_type"
        for entry in ARPTABLE :
            #print "ip is : %s "%entry['IP address']
            host=entry['IP address']
            self.scan_result(host,'udp',udpport)
            #print nm.scan(host,tcp,arguments='-O')[host]

    def scan_result(self,host,proto='tcp',portrange=None):
        nm = nmap.PortScanner()
        open_ports = []

        nmap_host_scan = nm.scan(host,portrange,arguments='-O')['scan']
        state = nmap_host_scan[host]['status']['state']
        nmap_host_scan=nm.scan(host, arguments='-O')['scan']
        state=nmap_host_scan[host]['status']['state']
        #print "host status is %s "%state
        try :
            os=nmap_host_scan[host]['osmatch']
            os_type=os[0]['osclass'][0]['osfamily']
        except Exception as e :
            os_type=""


        ports=nmap_host_scan[host]['portused']
        for port in ports:
           # print port

            if port['proto']== proto and port['state'] == 'open' :
                    open_ports.append(port['portid'])



        if state == 'up' and proto=='tcp':
            udp_open_ports = "NULL-UDP"
            print "%s\t%s\t%s\t%s"%(host,", ".join(open_ports),udp_open_ports,os_type)
        elif state == 'up' and proto =='udp' :
            tcp_open_ports = "NULL-TCP"
            print "%s\t%s\t%s\t%s" %(host,tcp_open_ports,", ".join(open_ports),os_type)
        else :
            tcp_open_ports = []
            udp_open_ports = []
            os_type=""
            print "%s\t%s\t%s\t%s" % (host, ", ".join(tcp_open_ports), ", ".join(udp_open_ports), os_type)


class validation():
    def __init__(self):
        pass

    def startup(self):
        c = commonLib(OptionParser())

        (self.options, self.args) = c.cmdLineParser()

        #print "options : %s" % self.options.host

        if len(sys.argv) == 1 :
            network().perform_arp_cache()

        elif  self.options.host :
            network().perform_host_scan(self.options.host)

        elif self.options.tcp :
            network().perfrom_tcp_scan(self.options.tcp)

        elif self.options.udp :
            network().perform_udp_scan(self.options.udp)

        elif self.options.unknown :
            print  "fails and outputs an error message to the user indicating the invalid given flag "

        else:
            usage1 = "python %s --->output scans ARP hosts with default ports defined by nmap"%sys.argv[0]
            usage2 = "python %s --host  <ip>   ----> scans the host"%(sys.argv[0] )
            usage3 = "python %s --tcp startport-endport ---->scans the tcp port in range"%sys.argv[0]
            usage4 = "python %s --udp startport-endport --->scans the udp port in range"%sys.argv[0]
            print "USAGE :=> \n" + usage1 + " \n\n" + "\t\tOR" + "\n\n" + usage2 +" \n\n" + "\t\tOR" + "\n\n" + usage3 + " \n\n" + "\t\tOR" + "\n\n" + usage4
            sys.exit(0)




if __name__ == "__main__":
    validation().startup()



