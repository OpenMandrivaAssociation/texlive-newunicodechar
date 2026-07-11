%global tl_name newunicodechar
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Definitions of the meaning of Unicode characters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newunicodechar
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newunicodechar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newunicodechar.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newunicodechar.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a friendly interface for defining the meaning of
Unicode characters. The document should be processed by (pdf)LaTeX with
the unicode option of inputenc or inputenx, or by XeLaTeX/LuaLaTeX. The
command provided is \newunicodechar{<char>}{<code>} where <char> is a
directly-typed Unicode character, and <code> is its replacement.

