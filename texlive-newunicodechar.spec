# revision 21463
# category Package
# catalog-ctan /macros/latex/contrib/newunicodechar
# catalog-date 2011-02-18 20:19:38 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-newunicodechar
Version:	1.0
Release:	1
Summary:	Definitions of the meaning of Unicode characters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/newunicodechar
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newunicodechar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newunicodechar.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newunicodechar.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a friendly interface for defining the
meaning of Unicode characters. The document should be processed
by (pdf)LaTeX with \usepackage[utf8]{inputenc} or by
XeLaTeX/LuaLaTeX. The command provided is
\newunicodechar{<char>}{<code>} where <char> is a directly-
typed Unicode character, and <code> is its replacement.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/newunicodechar/newunicodechar.sty
%doc %{_texmfdistdir}/doc/latex/newunicodechar/README
%doc %{_texmfdistdir}/doc/latex/newunicodechar/newunicodechar.pdf
#- source
%doc %{_texmfdistdir}/source/latex/newunicodechar/newunicodechar.dtx
%doc %{_texmfdistdir}/source/latex/newunicodechar/newunicodechar.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
