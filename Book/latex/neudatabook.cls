% ---------------------------------------------------------------------------
% neudatabook.cls — Neudata Consulting Ltd book class
% Books and long training texts in the Neudata house style (the "style 1" look of
% neudata.cls: teal strip, navy cover band, navy headings over teal rules).
% Compile with LuaLaTeX (Overleaf: Menu > Compiler > LuaLaTeX) or XeLaTeX, and biber.
%
% \documentclass[options]{neudatabook}
%   en | vi     language of the fixed labels (Chapter / Chương, Contents / Mục lục ...)
%   draft       adds a DRAFT watermark
% ---------------------------------------------------------------------------
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{neudatabook}[2026/10/04 Neudata Consulting Ltd book class]

\newif\ifnb@vi
\newif\ifnb@draft
\DeclareOption{en}{\nb@vifalse}
\DeclareOption{vi}{\nb@vitrue}
\DeclareOption{draft}{\nb@drafttrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptions\relax
\LoadClass[11pt, a4paper, oneside, openany]{book}

% ----- Fonts (XeLaTeX / LuaLaTeX) --------------------------------------------------
% TeX Gyre Heros (Helvetica/Arial look) and TeX Gyre Adventor (Century Gothic look) ship
% with TeX Live and Overleaf and cover Vietnamese; Source Code Pro for code and R output.
\RequirePackage{fontspec}
\RequirePackage{unicode-math}
\setmainfont{texgyreheros}[Extension=.otf, UprightFont=*-regular, BoldFont=*-bold,
  ItalicFont=*-italic, BoldItalicFont=*-bolditalic]
\setsansfont{texgyreheros}[Extension=.otf, UprightFont=*-regular, BoldFont=*-bold,
  ItalicFont=*-italic, BoldItalicFont=*-bolditalic]
\newfontfamily\nb@display{texgyreadventor}[Extension=.otf, UprightFont=*-regular,
  BoldFont=*-bold, ItalicFont=*-italic, BoldItalicFont=*-bolditalic]
\setmonofont{SourceCodePro}[Extension=.otf, UprightFont=*-Regular, BoldFont=*-Semibold,
  ItalicFont=*-RegularIt, BoldItalicFont=*-SemiboldIt, Scale=0.88]
\setmathfont{texgyredejavu-math.otf}

\RequirePackage{microtype}
\RequirePackage[a4paper, top=2.6cm, bottom=2.5cm, left=2.3cm, right=2.3cm,
                headheight=1.2cm, headsep=0.6cm, footskip=1.1cm]{geometry}
\RequirePackage[table]{xcolor}
\RequirePackage{graphicx}
\RequirePackage{tikz}
\RequirePackage{fancyhdr}
\RequirePackage{titlesec}
\RequirePackage{titletoc}
\RequirePackage{booktabs}
\RequirePackage{array}
\RequirePackage{tabularx}
\RequirePackage{longtable}
\RequirePackage{enumitem}
\RequirePackage[most]{tcolorbox}
\RequirePackage{etoolbox}
\RequirePackage{amsmath}
\RequirePackage{fvextra}
\RequirePackage{csquotes}
\RequirePackage{xurl}

% ----- Colours (same as neudata.cls) --------------------------------------------------
\definecolor{NeudataDeepTeal}{HTML}{055F56}
\definecolor{NeudataPPTTeal}{HTML}{0D7377}
\definecolor{NeudataBlue}{HTML}{0070C0}
\definecolor{NeudataNavy}{HTML}{04242F}
\definecolor{NeudataLogoBlue}{HTML}{0B376C}
\definecolor{NeudataMist}{HTML}{EAF2F5}
\definecolor{NeudataGrey}{HTML}{8A99A3}
\definecolor{NeudataInk}{HTML}{1F2D33}
\definecolor{NeudataSeafoam}{HTML}{9FD3CB}
\definecolor{NeudataCode}{HTML}{F3F7F8}
\definecolor{NeudataRed}{HTML}{B23B2E}
\definecolor{NeudataAmber}{HTML}{B5651D}
\colorlet{NeudataTeal}{NeudataDeepTeal}
\colorlet{NeudataHeading}{NeudataNavy}
\colorlet{NeudataSubheading}{NeudataLogoBlue}

\RequirePackage[font={small}, labelfont={bf, color=NeudataTeal}, skip=6pt]{caption}
\RequirePackage[hidelinks]{hyperref}
\hypersetup{colorlinks=true, linkcolor=NeudataHeading, urlcolor=NeudataLogoBlue,
  citecolor=NeudataTeal, bookmarksnumbered=true}
\color{NeudataInk}

% ----- Language of fixed labels --------------------------------------------------------
\ifnb@vi
  \newcommand{\nb@chaptername}{Chương}
  \newcommand{\nb@appendixname}{Phụ lục}
  \renewcommand{\contentsname}{Mục lục}
  \renewcommand{\figurename}{Hình}
  \renewcommand{\tablename}{Bảng}
  \renewcommand{\bibname}{Tài liệu tham khảo}
  \newcommand{\nb@objectives}{Mục tiêu học tập}
  \newcommand{\nb@note}{Diễn giải lâm sàng}
  \newcommand{\nb@tip}{Thực hành tốt}
  \newcommand{\nb@warning}{Lỗi thường gặp}
  \newcommand{\nb@important}{Điểm chính}
  \newcommand{\nb@authorsby}{Tác giả}
  \newcommand{\nb@editionline}{Ấn bản thứ nhất}
  % Vietnamese is not hyphenated: set ragged-right paragraphs instead
  \hyphenpenalty=10000 \exhyphenpenalty=10000
  \AtBeginDocument{\RaggedRight}
\else
  \newcommand{\nb@chaptername}{Chapter}
  \newcommand{\nb@appendixname}{Appendix}
  \renewcommand{\contentsname}{Contents}
  \renewcommand{\bibname}{References}
  \newcommand{\nb@objectives}{Learning objectives}
  \newcommand{\nb@note}{Clinical interpretation}
  \newcommand{\nb@tip}{Good practice}
  \newcommand{\nb@warning}{Common mistake}
  \newcommand{\nb@important}{Key points}
  \newcommand{\nb@authorsby}{Authors}
  \newcommand{\nb@editionline}{First edition}
\fi
\RequirePackage{ragged2e}

% ----- Metadata -------------------------------------------------------------------------
\newcommand{\nb@subtitle}{}
\newcommand{\nb@authorlist}{}
\newcommand{\nb@edition}{\nb@editionline}
\newcommand{\nb@logo}{figures/neudata-logo.png}
\newcommand{\subtitle}[1]{\renewcommand{\nb@subtitle}{#1}}
\newcommand{\authorlist}[1]{\renewcommand{\nb@authorlist}{#1}}   % one author per line: A \\ B
\newcommand{\edition}[1]{\renewcommand{\nb@edition}{#1}}
\newcommand{\logo}[1]{\renewcommand{\nb@logo}{#1}}

% ----- Headings ---------------------------------------------------------------------------
\setcounter{secnumdepth}{2}
\setcounter{tocdepth}{1}
\titleformat{\chapter}[display]
  {\normalfont\color{NeudataHeading}\raggedright\hyphenpenalty=10000}
  {\nb@display\large\bfseries\color{NeudataTeal}\MakeUppercase{\ifnb@inappendix\nb@appendixname\else\nb@chaptername\fi}\
   \fontsize{40}{40}\selectfont\thechapter}
  {1.2ex}
  {\nb@display\fontsize{26}{31}\selectfont\bfseries}
  [{\color{NeudataTeal}\vspace{1.2ex}\titlerule[1.6pt]}]
\titleformat{name=\chapter, numberless}[display]
  {\normalfont\color{NeudataHeading}\raggedright\hyphenpenalty=10000}{}{0pt}
  {\nb@display\fontsize{26}{31}\selectfont\bfseries}
  [{\color{NeudataTeal}\vspace{1.2ex}\titlerule[1.6pt]}]
\titlespacing*{\chapter}{0pt}{0pt}{3.2ex}
\titleformat{\section}
  {\Large\bfseries\color{NeudataHeading}}{\thesection}{0.6em}{}
  [{\color{NeudataTeal}\vspace{-0.5ex}\titlerule[0.9pt]}]
\titleformat{\subsection}
  {\large\bfseries\color{NeudataSubheading}}{\thesubsection}{0.6em}{}
\titleformat{\subsubsection}
  {\normalsize\bfseries\color{NeudataTeal}}{\thesubsubsection}{0.5em}{}
\titlespacing*{\section}{0pt}{3ex plus .6ex minus .2ex}{1.4ex}
\titlespacing*{\subsection}{0pt}{2.2ex plus .4ex minus .2ex}{0.8ex}
\titlespacing*{\subsubsection}{0pt}{1.8ex plus .4ex minus .2ex}{0.5ex}

\newif\ifnb@inappendix
\g@addto@macro\appendix{\nb@inappendixtrue}

% Table of contents
\titlecontents{chapter}[0pt]{\addvspace{0.9em}\bfseries\color{NeudataHeading}}
  {\contentslabel[\thecontentslabel]{1.8em}}{}{\hfill\contentspage}
\dottedcontents{section}[4.2em]{\color{NeudataInk}}{2.4em}{0.6pc}

% Lists and paragraphs
\setlist[itemize,1]{label={\color{NeudataTeal}\textbullet}, leftmargin=1.4em, itemsep=0.15em}
\setlist[itemize,2]{label={\color{NeudataSubheading}\textendash}}
\setlist[enumerate,1]{label={\color{NeudataTeal}\bfseries\arabic*.}, itemsep=0.15em}
\setlength{\parskip}{0.55em}
\setlength{\parindent}{0pt}
\linespread{1.06}

% ----- Header and footer ------------------------------------------------------------
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrule}{{\color{NeudataTeal}\hrule height 0.6pt}}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
\fancyhead[L]{\footnotesize\color{NeudataNavy}\nouppercase{\leftmark}}
\fancyhead[R]{\includegraphics[height=0.8cm]{\nb@logo}}
\fancyfoot[L]{\scriptsize\color{NeudataGrey}\@title\ \textperiodcentered\ Neudata Consulting Ltd}
\fancyfoot[R]{\small\color{NeudataNavy}\thepage}
\fancypagestyle{plain}{\fancyhf{}\renewcommand{\headrule}{}%
  \fancyfoot[R]{\small\color{NeudataNavy}\thepage}}

% ----- Cover, title page and copyright page ------------------------------------------
\renewcommand{\maketitle}{%
  \begin{titlepage}
    \begin{tikzpicture}[remember picture, overlay]
      \fill[NeudataDeepTeal] (current page.north west) rectangle ([yshift=-0.35cm]current page.north east);
      \node[anchor=north west, inner sep=0] at ([xshift=2.3cm, yshift=-2.0cm]current page.north west)
        {\includegraphics[width=4.6cm]{\nb@logo}};
      \fill[NeudataNavy] ([yshift=-9.2cm]current page.north west) rectangle ([yshift=-18.6cm]current page.north east);
      \fill[NeudataDeepTeal] ([yshift=-18.6cm]current page.north west) rectangle ([yshift=-18.85cm]current page.north east);
      % Fonts are set with the node's font= key: switching font inside an aligned TikZ
      % node keeps the default font's word spacing and squeezes the words together.
      \node[anchor=south west, text width=16.4cm, align=left, inner sep=0, text=white,
            font={\nb@display\fontsize{34}{41}\selectfont\bfseries}]
        at ([xshift=2.3cm, yshift=-14.3cm]current page.north west) {\@title};
      \ifx\nb@subtitle\@empty\else
      \node[anchor=north west, text width=16.4cm, align=left, inner sep=0, text=NeudataSeafoam,
            font={\nb@display\fontsize{17}{22}\selectfont}]
        at ([xshift=2.3cm, yshift=-15.1cm]current page.north west) {\nb@subtitle};
      \fi
      \node[anchor=north west, text width=16.4cm, align=left, inner sep=0, text=NeudataNavy]
        at ([xshift=2.3cm, yshift=-20.4cm]current page.north west) {%
          {\large\bfseries\nb@authorlist\par}};
      \node[anchor=south west, text width=16.4cm, align=left, inner sep=0, font=\small, text=NeudataGrey]
        at ([xshift=2.3cm, yshift=2.0cm]current page.south west) {%
          Neudata Consulting Ltd \textperiodcentered\ www.neu-data.com \textperiodcentered\ \textit{Insight. Impact. Innovation.}};
      \fill[NeudataDeepTeal] (current page.south west) rectangle ([yshift=0.35cm]current page.south east);
    \end{tikzpicture}
  \end{titlepage}
  % Title page
  \thispagestyle{empty}
  \vspace*{3cm}
  {\raggedright\hyphenpenalty=10000\exhyphenpenalty=10000
   {\nb@display\fontsize{28}{34}\selectfont\bfseries\color{NeudataHeading}\@title\par}
   \vspace{0.8em}
   {\nb@display\Large\color{NeudataTeal}\nb@subtitle\par}}
  \vspace{1.6em}{\color{NeudataTeal}\rule{\textwidth}{1.2pt}}\par
  \vspace{2.2em}
  {\large\nb@authorlist\par}
  \vfill
  \includegraphics[height=2.2cm]{\nb@logo}\par\vspace{0.6em}
  {\small\color{NeudataGrey}Neudata Consulting Ltd \textperiodcentered\ \@date\par}
  \clearpage}

\newcommand{\copyrightpage}[1]{%
  \thispagestyle{empty}
  \vspace*{\fill}
  {\small
  {\bfseries\@title}\\ \nb@subtitle\par\medskip
  \nb@edition, \@date\par\medskip
  #1\par\bigskip
  {\bfseries\color{NeudataNavy}Copyright \textcopyright\ Neudata, \the\year}\par\smallskip
  {\footnotesize All property rights and copyright are reserved. This book contains proprietary
  information and materials developed by Neudata and may not be copied, reproduced, distributed,
  published or cited, in whole or in part, without the prior written consent of Neudata. Where
  explicit written permission has been granted, appropriate attribution must be included,
  followed by ``by courtesy of Neudata''.\par}
  \medskip
  Neudata Consulting Ltd \textperiodcentered\ www.neu-data.com \textperiodcentered\ contact@neu-data.com\par}
  \clearpage}

% ----- Draft watermark ------------------------------------------------------------------
\ifnb@draft
  \AddToHook{shipout/background}{%
    \put(0,0){\begin{tikzpicture}[remember picture, overlay]
      \node[rotate=45, text=NeudataGrey!25, font=\fontsize{90}{90}\selectfont\bfseries]
        at (current page.center) {DRAFT};
    \end{tikzpicture}}}
\fi

% ----- Boxes ------------------------------------------------------------------------------
\tcbset{nb/base/.style={enhanced, breakable, arc=2pt, outer arc=2pt, boxrule=0pt,
  left=9pt, right=9pt, top=6pt, bottom=6pt, before skip=10pt, after skip=10pt,
  fonttitle=\bfseries\small, titlerule=0pt}}
% Callouts: \begin{nbcallout}{note|tip|warning|important}{Optional title}
\colorlet{nbc@note}{NeudataLogoBlue}
\colorlet{nbc@tip}{NeudataDeepTeal}
\colorlet{nbc@warning}{NeudataRed}
\colorlet{nbc@important}{NeudataNavy}
\newcommand{\nb@deftitle@note}{\nb@note}
\newcommand{\nb@deftitle@tip}{\nb@tip}
\newcommand{\nb@deftitle@warning}{\nb@warning}
\newcommand{\nb@deftitle@important}{\nb@important}
\newenvironment{nbcallout}[2]{%
  \colorlet{nbcc}{nbc@#1}%
  \def\nb@ct{#2}\ifx\nb@ct\@empty\def\nb@ct{\csname nb@deftitle@#1\endcsname}\fi
  \begin{tcolorbox}[nb/base, colback=nbcc!6, colframe=nbcc, leftrule=4pt,
    coltitle=nbcc, colbacktitle=nbcc!6, title={\nb@ct}]}
  {\end{tcolorbox}}
% Learning objectives
\newenvironment{objectives}{%
  \begin{tcolorbox}[nb/base, colback=NeudataMist, colframe=NeudataDeepTeal, boxrule=0.8pt,
    coltitle=white, colbacktitle=NeudataDeepTeal, title={\nb@objectives}]}
  {\end{tcolorbox}}
% Exercises: \begin{exercise}{Exercise 3.1}
\newenvironment{exercise}[1]{%
  \begin{tcolorbox}[nb/base, colback=white, colframe=NeudataNavy, boxrule=0.6pt,
    coltitle=NeudataNavy, colbacktitle=NeudataMist, title={#1}]}
  {\end{tcolorbox}}

% ----- R code and output ----------------------------------------------------------------
% Code: highlighted by the converter with the macros below inside an fvextra Verbatim.
\newcommand{\RComment}[1]{\textcolor{NeudataDeepTeal}{\textit{#1}}}
\newcommand{\RString}[1]{\textcolor{NeudataAmber}{#1}}
\newcommand{\RNumber}[1]{\textcolor{NeudataLogoBlue}{#1}}
\newcommand{\RFunction}[1]{\textcolor{NeudataNavy}{\textbf{#1}}}
\newcommand{\ROperator}[1]{\textcolor{NeudataRed}{#1}}
\newcommand{\RKeyword}[1]{\textcolor{NeudataLogoBlue}{\textbf{#1}}}
\DefineVerbatimEnvironment{RCodeV}{Verbatim}{commandchars=\\\{\}, fontsize=\small,
  breaklines=true, breakanywhere=false, breaksymbolleft={}, baselinestretch=1.05}
\DefineVerbatimEnvironment{ROutputV}{Verbatim}{fontsize=\small, breaklines=true,
  breakanywhere=true, breaksymbolleft={}, baselinestretch=1.0, formatcom=\color{NeudataInk!85}}
\newtcolorbox{rcode}{enhanced, breakable, colback=NeudataCode, colframe=NeudataCode,
  boxrule=0pt, arc=2pt, left=7pt, right=7pt, top=3pt, bottom=3pt,
  before skip=8pt, after skip=2pt,
  overlay unbroken and first={\node[anchor=north east, font=\tiny\bfseries, text=NeudataGrey,
    inner sep=3pt] at (frame.north east) {R};}}
\newtcolorbox{routput}{enhanced, breakable, colback=white, colframe=NeudataGrey!45,
  boxrule=0pt, leftrule=2.5pt, arc=0pt, outer arc=0pt, left=7pt, right=7pt, top=2pt,
  bottom=2pt, before skip=2pt, after skip=8pt}

% Inline code
\newcommand{\code}[1]{\texttt{\color{NeudataNavy}#1}}

% ----- Tables -------------------------------------------------------------------------
\newcommand{\nbheader}{\rowcolor{NeudataNavy}}
\newcommand{\nbth}[1]{\textcolor{white}{\textbf{#1}}}
\renewcommand{\arraystretch}{1.18}
\newcolumntype{Y}{>{\RaggedRight\arraybackslash}X}

\endinput
