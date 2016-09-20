# D-ITG-rpm

D-ITG supports both IPv4 and IPv6 traffic generation and it is capable to generate traffic at network, transport, and application layer.

With this solution you can create rpm package from D-ITG source. 

After checking out, use the following commands to build.

```
rpmbuild --define "_topdir ${HOME}/rpmbuild" -ba SPECS/D-ITG.spec
```
