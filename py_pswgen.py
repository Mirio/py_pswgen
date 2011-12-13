#                                    LICENSE BSD 2 CLAUSE                                       #
#   Copyright 2011 Mirio. All rights reserved.                                                  #
#   Redistribution and use in source and binary forms, with or without modification, are        #
#   permitted provided that the following conditions are met:                                   #
#       1. Redistributions of source code must retain the above copyright notice, this list of  #
#      conditions and the following disclaimer.                                                 #
#       2. Redistributions in binary form must reproduce the above copyright notice, this list  #
#      of conditions and the following disclaimer in the documentation and/or other materials   #
#      provided with the distribution.                                                          #
#                                                                                               #
#   THIS SOFTWARE IS PROVIDED BY Mirio ''AS IS'' AND ANY EXPRESS OR IMPLIED                     #
#   WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND    #
#   FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR    #
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
#   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR    #
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON    #
#   ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING          #
#   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF        #
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                                  #
#                                                                                               #
#   The views and conclusions contained in the software and documentation are those of the      #
#   authors and should not be interpreted as representing official policies, either expressed   #
#   or implied, of Mirio                                                                        # 


import random
import sys

__version__ = "1.0"

def genera(width,cycles):
    dictionary = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y',
                'z','A','B','C','D','E','F','G','H','I','J','K',
                'L','M','N','O','P','Q','R','S','T','U','V','W',
                'X','Y','Z','1','2','3','4','5','6','7','8','9']
    x = 0
    outlist = []
    outlist_tmp = []
    while x < cycles:
        x=x+1
        outlist_tmp.append(random.sample(dictionary, width))
        for item in outlist_tmp:
            for x in item:
                outlist.append(x)
    return "".join(outlist)
print "\nPy_pswgen = " + __version__
print "\n" * 3
try:
    w = int(raw_input("Width?\n----> "))
    c = int(raw_input("Cycles?\n----> "))
except ValueError:
    print "Wrong digits. Try again."
    sys.exit(0)
print "\n" * 2
print "==== PASSWORD ====\n"
try:
    print genera(w,c)
except ValueError:
    print "Password Limit is 61. Try Again"
    sys.exit(0)
print "\n" * 2
