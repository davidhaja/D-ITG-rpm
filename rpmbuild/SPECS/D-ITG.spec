Name:           D-ITG
Version:        2.8.1
Release:        0
Summary:        Distributed Internet Traffic Generator
Group:          Applications/Generator/Measure
License:        GPL
URL:            http://traffic.comics.unina.it/software/ITG/
Vendor:         COMICS (COMputer for Interaction and CommunicationS) Group Department of Electrical Engineering and Information Technologies University of Napoli "Federico II" ditg@comics.unina.it
Source:         %{name}-%{version}.tar.gz
Packager: 	David Haja (david.haja@gmail.com)
Patch0:         patch-check_uid
%description

D-ITG is a platform capable to produce traffic at packet level accurately 
replicating appropriate stochastic processes for both IDT (Inter Departure 
Time) and PS (Packet Size) random variables (exponential, uniform, cauchy, 
normal, pareto, ...). 
D-ITG supports both IPv4 and IPv6 traffic generation and it is capable to 
generate traffic at network, transport, and application layer. 
We believe that D-ITG shows interesting properties when compared to other 
traffic generators.

%prep
%setup 

%patch0

%build
cd src/
make

%install
rm -rf $RPM_BUILD_ROOT
cd src/
make install PREFIX=$RPM_BUILD_ROOT/usr

%files
%{_bindir}/*
%{_libdir}/*
%doc README
