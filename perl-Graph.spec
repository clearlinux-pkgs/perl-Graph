#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Graph
Version  : 0.9704
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/J/JH/JHI/Graph-0.9704.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JH/JHI/Graph-0.9704.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libgraph-perl/libgraph-perl_0.96-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Graph-man

%description
This is Graph, a Perl module for dealing with graphs, the abstract
data structures.  (If you were looking for pie charts, I'm sorry.)

%package man
Summary: man components for the perl-Graph package.
Group: Default

%description man
man components for the perl-Graph package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Graph-0.9704
mkdir -p %{_topdir}/BUILD/Graph-0.9704/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Graph-0.9704/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Graph.pm
/usr/lib/perl5/site_perl/5.26.1/Graph.pod
/usr/lib/perl5/site_perl/5.26.1/Graph/AdjacencyMap.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/AdjacencyMap/Heavy.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/AdjacencyMap/Light.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/AdjacencyMap/Vertex.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/AdjacencyMatrix.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/Attribute.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/BitMatrix.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/Directed.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/MSTHeapElem.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/Matrix.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/SPTHeapElem.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/TransitiveClosure.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/TransitiveClosure/Matrix.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/Traversal.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/Traversal/BFS.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/Traversal/DFS.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/Undirected.pm
/usr/lib/perl5/site_perl/5.26.1/Graph/UnionFind.pm
/usr/lib/perl5/site_perl/5.26.1/Heap071/Elem.pm
/usr/lib/perl5/site_perl/5.26.1/Heap071/Fibonacci.pm
/usr/lib/perl5/site_perl/5.26.1/auto/Heap071/Elem/autosplit.ix
/usr/lib/perl5/site_perl/5.26.1/auto/Heap071/Fibonacci/autosplit.ix

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Graph.3
/usr/share/man/man3/Graph::AdjacencyMap.3
/usr/share/man/man3/Graph::AdjacencyMap::Vertex.3
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
/usr/share/man/man3/Heap071::Elem.3
/usr/share/man/man3/Heap071::Fibonacci.3
