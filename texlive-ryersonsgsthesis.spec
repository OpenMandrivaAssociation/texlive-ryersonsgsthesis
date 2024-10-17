Name:		texlive-ryersonsgsthesis
Version:	50119
Release:	2
Summary:	Ryerson School of Graduate Studies thesis template
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ryersonsgsthesis
License:	apache2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ryersonsgsthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ryersonsgsthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX class and template files for
Ryerson School of Graduate Studies (SGS) theses.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ryersonsgsthesis
%doc %{_texmfdistdir}/doc/latex/ryersonsgsthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
