Summary:	Conversation simulator
Summary(pl):	Symulator konwersacji
Name:		megahal
Version:	9.1.1
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/megahal/%{name}-%{version}.tar.gz
# Source0-md5:	acdca9ada85cb7fc49dbe2dd8e6b4fca
Source1:	%{name}-personal
Source2:	%{name}-personal.1
URL:		http://megahal.sourceforge.net/
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

%description -l pl
megahal jest symulatorem konwersacji, który uczy siê tego co do niego
mówisz. Symulatory konwersacji s± programami komputerowymi, które
symuluj± rozmowê z lud¼mi w jêzyku naturalnym. Megahal ró¿ni siê od
innych symulatorów takich jak Eliza tym, ¿e wykorzystuje model Markova
do nauki jak podtrzymaæ konwersacjê. Jest mo¿liwe nauczenie MegaHAL-a
rozmowy o nowych tematach oraz w innych jêzykach.

%package -n perl-Megahal
Summary:        perl module to megahal
Summary(pl):    Modu³ perla do korzystania z megahala
Group:          Development/Languages/Perl
Requires:       %{name} = %{version}-%{release}

%description -n perl-Megahal
perl module to megahal.

%description -n perl-Megahal -l pl
Modu³ perla do korzystania z megahala.

%package -n python-megahal
Summary:        python module to megahal
Summary(pl):    Modu³ pythona do korzystania z megahala
Group:          Libraries/Python
Requires:       %{name} = %{version}-%{release}

%description -n python-megahal
python module to megahal.

%description -n python-megahal -l pl
Modu³ pythona do korzystania z megahala.

%prep
%setup -q

%build
%{__make} all \
	CFLAGS="%{rpmcflags}" \
	INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/megahal,%{_mandir}/man{1,3}}

%{__make} pythonmodule-install perlmodule-install \
	DESTDIR=$RPM_BUILD_ROOT

install megahal %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}
install docs/megahal*.1 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/
install docs/megahal*.3 $RPM_BUILD_ROOT%{_mandir}/man3/
install megahal.aux megahal.ban megahal.grt megahal.swp megahal.trn \
	$RPM_BUILD_ROOT%{_libdir}/megahal/

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
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/Megahal
%{perl_vendorarch}/auto/Megahal/*.bs
%{perl_vendorarch}/auto/Megahal/*.so
%{_mandir}/man?/Megahal*

%files -n python-megahal
%attr(755,root,root) %{py_sitedir}/*.so
