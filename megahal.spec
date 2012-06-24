Summary:	Conversation simulator
Summary(pl):	Symulator konwersacji
Name:		megahal
Version:	9.0.3
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://download.sourceforge.net/megahal/%{name}-%{version}.tar.gz
# Source0-md5:	435774dbe112dc514546cbe11d85b9f2
URL:		http://megahal.sourceforge.net/
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
megahal jest symulatorem konwersacji, kt�ry uczy si� tego co do niego
m�wisz. Symulatory konwersacji s� programami komputerowymi, kt�re
symuluj� rozmow� z lud�mi w j�zyku naturalnym. Megahal r�ni si� od
innych symulator�w takich jak Eliza tym, �e wykorzystuje model Markova
do nauki jak podtrzyma� konwersacj�. Jest mo�liwe nauczenie MegaHAL-a
rozmowy o nowych tematach oraz w innych j�zykach.

%prep
%setup -q -n %{name}

%build
%{__make} all CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/megahal,%{_mandir}/man1}

install megahal debian/megahal-personal $RPM_BUILD_ROOT%{_bindir}
install docs/megahal.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install megahal.aux megahal.ban megahal.grt megahal.swp megahal.trn \
	$RPM_BUILD_ROOT%{_libdir}/megahal/

mv -f docs/paper.txt docs/README.TXT debian/README.* debian/*.p* .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc paper.txt README.* hal.pl Hal.pm
%attr(755,root,root) %{_bindir}/*
%{_libdir}/megahal
%{_mandir}/man?/*
