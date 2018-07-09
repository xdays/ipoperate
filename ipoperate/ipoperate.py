#!/usr/bin/env python

import string
import sys 
import difflib

def de2bin(x):
    '''convert decimal to binary
    input: 15
    output: 11110000
    '''
    bstr = ''
    x = int(x)
    n=7 
    while n >= 0:
            re = x / (2 ** n)
            if re == 1:
                x = x % (2 ** n)
            n = n - 1 
            bstr = bstr + str(re) 
    return bstr

def bin2de(x):
    '''convert binary to decimal
    input: 11110000
    output: 15
    '''
    n = 7
    de = 0 
    while n >= 0:
        #print x[n]
        #print (2**(7-n))
        de = de + int(x[n])*(2**(7-n))
        n = n - 1 
        #print de
    return de

def ip2bin(ip):
    '''convert ip address to binary
    input: 10.0.0.0
    output: 00001010000000000000000000000000
    '''
    ipseg = ip.split(".")
    #print ipseg
    ipbin=''
    for num in ipseg:
        #print num
        ips = de2bin(num)
        #print ips
        ipbin = ipbin + str(ips)
        #print ipbin
    return ipbin

def bin2ip(x):
    '''convert ip address to binary
    input: 00001010000000000000000000000000
    output: 10.0.0.0
    '''
    blen = str(len(x))
    x = x.ljust(32, '0')
    n = 1 
    f = [None]*4
    while n <=4:
        f[n-1] = str(bin2de(x[(n-1)*8: n*8]))
        n = n + 1 
    ip = '.'.join(f)
    #print f
    #ip = '.'.join(g)
    #ip = ip + '/' + blen
    return ip

def net2bin(n):
    '''convert network address to binary
    input: 192.168.1.0/24
    output: 110000001010100000000001
    '''
    lnet = n.split('/')
    net,mask = lnet[0],lnet[1]
    netbin = ip2bin(net)[:int(mask)]
    return netbin

def bin2net(n):
    '''convert network address to binary
    input: 110000001010100000000001
    output: 192.168.1.0/24
    '''
    net,mask = bin2ip(n),len(n)
    nets = net + '/' + str(mask)
    return nets

def ip2long(x):
    '''convert ip to numbers in 256 hex
    input: 192.168.1.1
    output: 192*(256**3) + 168*(256**2) + 1*256 + 1
    '''
    x = x.split('.')
    n = 0
    ipl = 0
    while n <= 3:
        x[n] = int(x[n]) << (8*(3-n))
        ipl = ipl + x[n]
        n = n + 1
    return ipl

def long2ip(x):
    '''convert ip to numbers in 256 hex
    iutput: 192*(256**3) + 168*(256**2) + 1*256 + 1
    onput: 192.168.1.1
    '''
    ips = ''
    n = 3
    while n >= 1:
        ips = ips + str(x/(256**n)) + '.'
        x = x%(256**n)
        n = n - 1
    ips = ips + str(x)
    return ips

def net2ips(x):
    '''calculate the range of ip/mask in 256 hex
    input: 192.168.1.0/24
    output: 192.168.1.1,192.168.1.255,
    192*(256**3) + 168*(256**2) + 1*256,  192*(256**3) + 168*(256**2) + 1*256 + 255
    '''
    x = net2bin(x)
    low = x.ljust(32, '0')
    hi = x.ljust(32, '1')
    iplow = bin2ip(low)
    delow = str(ip2long(iplow))
    iphi = bin2ip(hi)
    dehi = str(ip2long(iphi))
    return iplow,iphi,delow,dehi

def compare(net1, net2,net1len=32, net2len=24):
    '''compare two strings and get the longest
    child string that both consist in, and the position
    of the child string
    '''
    ncmp = difflib.SequenceMatcher(None, net1, net2)
    rcmp = ncmp.find_longest_match(0, net1len, 0, net2len)
    rsize = rcmp.size
    #rend = rsize +1
    #print rend
    return net1[:rsize],rsize

def ips2net(ip1, ip2):
    '''merge two network and return the smallest network
    containing them
    input: 192.168.4.0,192.168.5.0
    output: 192.168.4.0/23
    '''
    mbin, mmask = compare(ip2bin(ip1), ip2bin(ip2), 32, 32)
    return bin2ip(mbin),str(mmask)

def nets2net(net1, net2):
    '''merge two network and return the smallest network
    containing them
    input: 192.168.4.0/24,192.168.5.0/24
    output: 192.168.4.0/23
    '''
    ip1,mask1,ip2,mask2 = net1.split('/') + net2.split('/')
    mbin,mmask = compare(ip2bin(ip1), ip2bin(ip2), 32, 32)
    net=bin2ip(mbin.ljust(32, '0'))
    mask = str(min(int(mmask), int(mask1), int(mask2)))
    return net,mask

def cidr2mask(net):
    '''change network fromat from cidr to mask
    input: 192.168.1.0/24
    output: 192.168.1.0/255.255.255.0
    '''
    netid,cidr = net.split('/')
    mask = bin2ip(''.join(['1']*int(cidr)+['0']*(32-int(cidr))))
    return '%s/%s' % (netid, mask)

def mask2cidr(net):
    '''change network fromat from mask to cidr
    input: 192.168.1.0/255.255.255.0
    output: 192.168.1.0/24
    '''
    netid,mask = net.split('/')
    cidr = len(ip2bin(mask).split('0')[0])
    return '%s/%s' % (netid, cidr)

def ips2range(ips, step=5):
    '''merge ip list into ip range
    input: ['192.168.1.1', '192.168.1.2', '192.168.1.3']
    output: [('192.168.1.1', '192.168.1.3')]
    '''
    ip_ranges = []
    ips = sorted([int(ip2long(ip)) for ip in ips])
    start_ip = ips[0]
    end_ip = ips[0]
    for ip in ips:
        if ip - start_ip < step:
            end_ip = ip
        else:
            ip_ranges.append((long2ip(start_ip), long2ip(end_ip)))
            start_ip = ip
            end_ip = ip
    else:
        ip_ranges.append((long2ip(start_ip), long2ip(end_ip)))
    return ip_ranges
