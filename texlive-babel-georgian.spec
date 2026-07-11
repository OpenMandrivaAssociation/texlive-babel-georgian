%global tl_name babel-georgian
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Babel support for Georgian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/georgian
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-georgian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-georgian.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for use of Babel in documents written in
Georgian. The package is adapted for use both under 'traditional' TeX
engines, and under XeTeX and LuaTeX.

