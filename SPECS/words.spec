Summary: A dictionary of English words for the /usr/share/dict directory
Name: words
Version: 3.0
Release: 28%{?dist}
License: Public Domain
Group: System Environment/Libraries
# Note that Moby Project officially does not exist any more. The most complete
# information about the project is in Wikipedia.
URL: http://en.wikipedia.org/wiki/Moby_Project
Source: http://web.archive.org/web/20060527013227/http://www.dcs.shef.ac.uk/research/ilash/Moby/mwords.tar.Z

BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: dos2unix
BuildRequires: grep

#428582 - linux.words contains misspelled word "flourescent"
#440146 - misspelled word in /usr/share/dict/words (architecure)
#457309 - contains both 'unnecessary' and 'unneccesary'
Patch0: words-3.0-typos.patch
#470921 -"Barack" and "Obama" are not in /usr/share/dict/words
Patch1: words-3.0-presidents.patch

%description
The words file is a dictionary of English words for the
/usr/share/dict directory. Some programs use this database of
words to check spelling. Password checkers use it to look for bad
passwords.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
cd mwords
dos2unix -o *; chmod a+r *
cat [1-9]*.??? | egrep --invert-match "'s$" | egrep  "^[[:alnum:]'&!,./-]+$" | sort --ignore-case --dictionary-order | uniq > moby

cat <<EOF >license.txt
***
    The license in the readme.txt file is original and DEPRECATED
    license of The Moby lexicon project.
***

On June 1, 1996 Grady Ward announced that the fruits of
the Moby project were being placed in the public domain:

The Moby lexicon project is complete and has
been place into the public domain. Use, sell,
rework, excerpt and use in any way on any platform.

Placing this material on internal or public servers is
also encouraged. The compiler is not aware of any
export restrictions so freely distribute world-wide.

You can verify the public domain status by contacting

Grady Ward
3449 Martha Ct.
Arcata, CA  95521-4884

daedal@myrealbox.com
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/dict
install -m644 mwords/moby $RPM_BUILD_ROOT%{_datadir}/dict/linux.words
ln -sf linux.words $RPM_BUILD_ROOT%{_datadir}/dict/words

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc mwords/readme.txt mwords/license.txt
%{_datadir}/dict/linux.words
%{_datadir}/dict/words

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 23 2012 Karel Zak <kzak@redhat.com> - 3.0-19
- fix #746416 - words contains "unltraconservative"

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 12 2009 Karel Zak <kzak@redhat.com> - 3.0-14
- fix #457309 - contains both 'unnecessary' and 'unneccesary'
- fix #470921 -"Barack" and "Obama" are not in /usr/share/dict/words
- update spec file (#226542 - Merge Review)

* Mon Jun 23 2008 Karel Zak <kzak@redhat.com> - 3.0-13
- fix #428582 - linux.words contains misspelled word "flourescent"
- fix #440146 - misspelled word in /usr/share/dict/words (architecure)

* Mon Apr  2 2007 Karel Zak <kzak@redhat.com> - 3.0-12
- fix #226542 - Merge Review: words

* Mon Apr  2 2007 Karel Zak <kzak@redhat.com> - 3.0-11
- cleanup spec file
- fix #227216 - Unnecessary BuildRequirement to ncompress

* Wed Jan 24 2007 Karel Zak <kzak@redhat.com> - 3.0-10
- fix regex that removes possessives ('s)

* Wed Jul 19 2006 Karel Zak <kzak@redhat.com> - 3.0-9
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.0-8.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 21 2005  Karel Zak <kzak@redhat.com> 3-8
- rebuilt

* Mon May  2 2005  Karel Zak <kzak@redhat.com> 3-7
- sort with --dictionary-order
- remove words with possessives ('s)

* Mon Apr  4 2005 Karel Zak <kzak@redhat.com> 3-6
- fix uniq command usage

* Tue Mar 29 2005 Karel Zak <kzak@redhat.com> 3-5
- replace word list with much better Moby Project words list (#61395)
- revise %%description; ispell/aspell no longer uses words

* Mon Sep 27 2004 Adrian Havill <havill@redhat.com> 2-23
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb  5 2003 Nalin Dahyabhai <nalin@redhat.com> 2-21
- rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Apr  3 2002 Trond Eivind Glomsrod <teg@redhat.com> 2-18
- Bump.

* Mon Mar 18 2002 Trond Eivind Glomsrod <teg@redhat.com> 2-17
- s/Copyright/License/
- add gullible and facetious (#60166, #60173)

* Fri Apr  6 2001 Trond Eivind Glomsrod <teg@redhat.com>
- Add carnivore (#35031)

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 13 2000 Trond Eivind Glomsrod <teg@redhat.com>
- use %%{_tmppath}

* Thu Apr 13 2000 Nalin Dahyabhai <nalin@redhat.com>
- add some words: some food additives, dinosaurs, atmospheric terms

* Fri Apr 07 2000 Trond Eivind Glomsrod <teg@redhat.com>
- update description
- moved it to /usr/share/dict
- updated URL

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 12)

* Wed Sep 30 1998 Bill Nottingham <notting@redhat.com>
- take out extra.words (they're all in linux.words)

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- correct desiccate (problem #794)

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Tue Sep 23 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
