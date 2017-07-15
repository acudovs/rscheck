# RSCheck - Real Server health Check

RSCheck is a simple daemon for checking a Real Server health before adding it to
a Load Balancing cluster.

It is very dangerous to add misconfigured Real Server to a Load Balancing
cluster especially when using least connection scheduler (lesser extent
but still affects other schedulers). Missing virtual IP address or rp_filter
enabled on a Real Server network interface leads to site downtime by directing
all new connections to the misconfigured server.

## Building RSCheck RPM package

You should always create RPM packages in a clean environment and preferably on a
separate machine or in container!

```shell
yum -y update
yum -y install @Development\ Tools

git clone https://github.com/AlekseyChudov/rscheck.git

cd rscheck
rpmbuild -bb rscheck.spec
```

## RSCheck usage example

```shell
yum -y update
yum -y install epel-release
yum -y install rscheck

cp /usr/share/doc/rscheck*/rscheck.conf /etc/rscheck/primary-site.conf
vi /etc/rscheck/primary-site.conf

systemctl enable rscheck@primary-site
systemctl start rscheck@primary-site
systemctl status rscheck@primary-site

cp /usr/share/doc/rscheck*/rscheck.conf /etc/rscheck/dns-server.conf
vi /etc/rscheck/dns-server.conf

systemctl enable rscheck@dns-server
systemctl start rscheck@dns-server
systemctl status rscheck@dns-server

curl -v 'http://localhost:81/getstatus'
curl -v 'http://localhost:81/getstatus' -X HEAD

curl -v 'http://localhost:81/getstatus?virtual_if=tunl0&virtual_ip=1.1.1.1'
curl -v 'http://localhost:81/getstatus?virtual_if=tunl0&virtual_ip=1.1.1.1,2.2.2.2'

curl -v 'http://localhost:81/getstatus?exclude=dns-example.com,interfaces,http,tcp-443,sysclt'
```
