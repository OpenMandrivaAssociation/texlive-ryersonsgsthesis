%global tl_name ryersonsgsthesis
%global tl_revision 50119

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.3
Release:	%{tl_revision}.1
Summary:	Ryerson School of Graduate Studies thesis template
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ryersonsgsthesis
License:	apache2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ryersonsgsthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ryersonsgsthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX class and template files for Ryerson
School of Graduate Studies (SGS) theses.

