#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Graph
Version  : 0.9722
Release  : 39
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETJ/Graph-0.9722.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETJ/Graph-0.9722.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libgraph-perl/libgraph-perl_0.96-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Graph-license = %{version}-%{release}
Requires: perl-Graph-perl = %{version}-%{release}
Requires: perl(Heap)
Requires: perl(Heap::Fibonacci)
BuildRequires : buildreq-cpan
BuildRequires : perl(Heap)
BuildRequires : perl(Heap::Fibonacci)
BuildRequires : perl(Set::Object)

%description
This is Graph, a Perl module for dealing with graphs, the abstract
data structures.  (If you were looking for pie charts, I'm sorry.)

%package dev
Summary: dev components for the perl-Graph package.
Group: Development
Provides: perl-Graph-devel = %{version}-%{release}
Requires: perl-Graph = %{version}-%{release}

%description dev
dev components for the perl-Graph package.


%package license
Summary: license components for the perl-Graph package.
Group: Default

%description license
license components for the perl-Graph package.


%package perl
Summary: perl components for the perl-Graph package.
Group: Default
Requires: perl-Graph = %{version}-%{release}

%description perl
perl components for the perl-Graph package.


%prep
%setup -q -n Graph-0.9722
cd %{_builddir}
tar xf %{_sourcedir}/libgraph-perl_0.96-2.debian.tar.xz
cd %{_builddir}/Graph-0.9722
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Graph-0.9722/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Graph
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Graph/aa4de88e127fdccdf8ffd510f46daa9344996b49
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Graph.3
/usr/share/man/man3/Graph::AdjacencyMap.3
/usr/share/man/man3/Graph::AdjacencyMatrix.3
/usr/share/man/man3/Graph::BitMatrix.3
/usr/share/man/man3/Graph::Directed.3
/usr/share/man/man3/Graph::Matrix.3
/usr/share/man/man3/Graph::TransitiveClosure.3
/usr/share/man/man3/Graph::TransitiveClosure::Matrix.3
/usr/share/man/man3/Graph::Traversal.3
/usr/share/man/man3/Graph::Traversal::BFS.3
/usr/share/man/man3/Graph::Traversal::DFS.3
/usr/share/man/man3/Graph::Undirected.3
/usr/share/man/man3/Graph::UnionFind.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Graph/aa4de88e127fdccdf8ffd510f46daa9344996b49

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Graph.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph.pod
/usr/lib/perl5/vendor_perl/5.34.0/Graph/AdjacencyMap.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/AdjacencyMap/Light.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/AdjacencyMatrix.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/Attribute.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/BitMatrix.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/Directed.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/MSTHeapElem.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/Matrix.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/SPTHeapElem.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/TransitiveClosure.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/TransitiveClosure/Matrix.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/Traversal.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/Traversal/BFS.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/Traversal/DFS.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/Undirected.pm
/usr/lib/perl5/vendor_perl/5.34.0/Graph/UnionFind.pm
