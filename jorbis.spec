Name:			jorbis
Summary:		JOrbis - Pure Java Ogg Vorbis Decoder
URL:			http://www.jcraft.com/jorbis/index.html
Group:			Development/Java
Version:		0.0.17
Release:		4
License:		LGPL
BuildRequires:	ant
BuildRequires:	jpackage-utils
BuildRequires:	java-rpmbuild >= 1.5
BuildRequires:	unzip
BuildRequires:	update-alternatives
BuildRequires:	xml-commons-apis
BuildRequires:	xml-commons-resolver
Requires:		java >= 1.5
BuildArch:		noarch
Source0:		%{name}-%{version}.zip

%description
JOrbis is a pure Java Ogg Vorbis decoder.
JOrbis accepts Ogg Vorbis bitstreams and decodes them to raw PCMs.

JOrbis is copyrighted by JCraft Inc. and is licensed through the
GNU Lesser General Public License.

Read the COPYING.LIB file for the complete license.

%package javadoc
Summary:	Javadoc for jorbis
Group:		Development/Java

%description javadoc
Javadoc for jorbis.

%package -n jorbis-player
Summary:	JOrbisPlayer - a ogg player using %{name}
Group:		Development/Java
Requires:	%{name} = %{version}

%description -n jorbis-player
JOrbisPlayer is a simple ogg-Player.

%package -n jorbis-comment
Summary:	JOrbisComment is a simple comment editor for Ogg Vorbis
Group:		Development/Java
Requires:	%{name} = %{version}

%description -n jorbis-comment
JOrbisComment is a simple comment editor for Ogg Vorbis.

This program is just provided here for setting an example, how to
use JOrbis for editing comments.

%prep
%setup -q -n %{name}-%{version}

%build
%javac \
	`find ./ -name '*.java'`
%jar cf jorbis.jar \
	com/jcraft/jogg/*.class \
	com/jcraft/jorbis/*.class
%jar cf JOrbisPlayer.jar \
	player/*.class
%jar cf JOrbisComment.jar \
	comment_editor/*.class

%javadoc \
	-d doc -public \
	`find ./ -name '*.java'`

%install
# jars
%__install -dm 755 %{buildroot}%{_javadir}
%__install -pm 644 jorbis.jar \
	%{buildroot}%{_javadir}/jorbis-%{version}.jar
%__install -pm 644 JOrbisPlayer.jar \
	%{buildroot}%{_javadir}/JOrbisPlayer-%{version}.jar
%__install -pm 644 JOrbisComment.jar \
	%{buildroot}%{_javadir}/JOrbisComment-%{version}.jar
pushd %{buildroot}%{_javadir}
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd

# javadoc
%__install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr doc/* \
	%{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(-,root,root)
%doc COPYING.LIB ChangeLog README
%{_javadir}/%{name}*.jar

%files javadoc
%defattr(-,root,root)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files -n jorbis-player
%defattr(-,root,root)
%doc player/JOrbisPlayer.html
#%doc player/*.ogg player/playlist
%{_javadir}/JOrbisPlayer*.jar

%files -n jorbis-comment
%defattr(-,root,root)
%doc comment_editor/README
%{_javadir}/JOrbisComment*.jar



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.17-0.0.3mdv2011.0
+ Revision: 619832
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.0.17-0.0.2mdv2010.0
+ Revision: 429645
- rebuild

* Mon Sep 22 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0.0.17-0.0.1mdv2009.0
+ Revision: 286737
- remove unneeded PreReq
- import jorbis


