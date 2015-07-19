# revision 28253
# category Package
# catalog-ctan /macros/latex/contrib/newunicodechar
# catalog-date 2012-11-13 18:34:11 +0100
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-newunicodechar
Version:	1.1
Release:	9
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

%description
The package provides a friendly interface for defining the
meaning of Unicode characters. The document should be processed
by (pdf)LaTeX with the unicode option of inputenc or inputenx,
or by XeLaTeX/LuaLaTeX. The command provided is
\newunicodechar{<char>}{<code>} where <char> is a directly-
typed Unicode character, and <code> is its replacement.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/newunicodechar/newunicodechar.sty
%doc %{_texmfdistdir}/doc/latex/newunicodechar/README
%doc %{_texmfdistdir}/doc/latex/newunicodechar/newunicodechar.pdf
#- source
%doc %{_texmfdistdir}/source/latex/newunicodechar/newunicodechar.dtx
%doc %{_texmfdistdir}/source/latex/newunicodechar/newunicodechar.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
