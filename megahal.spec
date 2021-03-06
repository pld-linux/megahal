Summary:	Conversation simulator
Summary(pl.UTF-8):	Symulator konwersacji
Name:		megahal
Version:	9.1.1
Release:	3
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/megahal/%{name}-%{version}.tar.gz
# Source0-md5:	acdca9ada85cb7fc49dbe2dd8e6b4fca
Source1:	%{name}-personal
Source2:	%{name}-personal.1
URL:		http://megahal.alioth.debian.org/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
megahal is a conversation simulator that can learn as you talk to it
Conversation simulators are computer programs which give the
appearance of conversing with a user in natural language. Such
programs are effective because they exploit the fact that human beings
tend to read much more meaning into what is said than is actually
there; we are fooled into reading structure into chaos, and we
interpret non-sequitur as valid conversation. MegaHAL differs from
conversation simulators such as Eliza in that it uses a Markov Model
to learn how to hold a conversation. It is possible to teach MegaHAL
to talk about new topics, and in different languages.

%description -l pl.UTF-8
megahal jest symulatorem konwersacji, który uczy się tego co do niego
mówisz. Symulatory konwersacji są programami komputerowymi, które
symulują rozmowę z ludźmi w języku naturalnym. Megahal różni się od
innych symulatorów takich jak Eliza tym, że wykorzystuje model Markova
do nauki jak podtrzymać konwersację. Jest możliwe nauczenie MegaHAL-a
rozmowy o nowych tematach oraz w innych językach.

%package -n perl-Megahal
Summary:	Perl module for megahal
Summary(pl.UTF-8):	Moduł Perla do korzystania z megahala
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-Megahal
Perl module for megahal.

%description -n perl-Megahal -l pl.UTF-8
Moduł Perla do korzystania z megahala.

%package -n python-megahal
Summary:	python module for megahal
Summary(pl.UTF-8):	Moduł pythona do korzystania z megahala
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-megahal
python module for megahal.

%description -n python-megahal -l pl.UTF-8
Moduł pythona do korzystania z megahala.

%prep
%setup -q
%{__sed} -i 's@gcc@$(CC)@' Makefile

%build
%{__make} all \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/megahal,%{_mandir}/man{1,3}}

%{__make} pythonmodule-install perlmodule-install \
	DESTDIR=$RPM_BUILD_ROOT

install megahal %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}
install docs/megahal*.1 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1
install docs/megahal*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install megahal.aux megahal.ban megahal.grt megahal.swp megahal.trn \
	$RPM_BUILD_ROOT%{_libdir}/megahal

mv -f docs/paper.txt docs/README.TXT .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc paper.txt README.*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/megahal
%{_mandir}/man?/megahal*

%files -n perl-Megahal
%defattr(644,root,root,755)
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/Megahal
%{perl_vendorarch}/auto/Megahal/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Megahal/*.so
%{_mandir}/man?/Megahal*

%files -n python-megahal
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
