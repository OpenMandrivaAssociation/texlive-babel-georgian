Name:		texlive-babel-georgian
Version:	2.2
Release:	2
Summary:	Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/georgian
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-georgian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-georgian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for use of Babel in documents
written in Georgian. The package is adapted for use both under
'traditional' TeX engines, and under XeTeX and LuaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-georgian
%doc %{_texmfdistdir}/doc/generic/babel-georgian

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
