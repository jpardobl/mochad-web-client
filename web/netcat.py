import socket


def command(string):
    import commands
    cmd = "echo '%s' | nc localhost 1099" % string
    print "ejecutamos el comand %s " % cmd
    ret = commands.getoutput(cmd)
    print "resultado: %s " % ret
    return ret
