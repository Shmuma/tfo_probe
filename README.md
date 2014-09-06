TCP Fast Open is an TCP extension proposed by Google aiming at combining 3-way
handshake with data retrieveing.

Original paper: 
http://static.googleusercontent.com/external_content/untrusted_dlcp/research.google.com/en/us/pubs/archive/37517.pdf

# Setup

On modern linux kernels it's required to just turn it on:
    echo 3 > /proc/sys/net/ipv4/tcp_fastopen

