#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : perl-Graph
Version  : 0.9734
Release  : 60
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETJ/Graph-0.9734.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETJ/Graph-0.9734.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Graph-perl = %{version}-%{release}
Requires: perl(Heap)
Requires: perl(Heap::Fibonacci)
BuildRequires : buildreq-cpan
BuildRequires : perl(Heap)
BuildRequires : perl(Heap::Fibonacci)
BuildRequires : perl(Set::Object)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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


%package perl
Summary: perl components for the perl-Graph package.
Group: Default
Requires: perl-Graph = %{version}-%{release}

%description perl
perl components for the perl-Graph package.


%prep
%setup -q -n Graph-0.9734
cd %{_builddir}/Graph-0.9734
pushd ..
cp -a Graph-0.9734 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
