---
title: "Théorie d'Élasticité — 20 exercices corrigés"
subtitle: "Préparation d'examen — Licence Génie Civil, Semestre 4 (ENETP / Bamako)"
author: "KGB"
lang: fr
---

# Théorie d'Élasticité {.unnumbered}

## 20 exercices corrigés et les sujets d'examen {.unnumbered}

**Licence Génie Civil (GC) — Semestre 4 — ENETP / Bamako**

**KGB**

*Transcription intégrale du cahier manuscrit (pages 1 à 51) et des feuilles de sujets imprimées (pages 52 à 91).*
*Les repères « — page n — » renvoient à la page correspondante du document scanné.*

\newpage

*— page 1 —*

**17/08/2025**

# Préparation d'examen de Théorie d'élasticité

**Date : 26/08/25 (devoir et examen)**

**KGB**

## Exercice ① : Plaque comprimée

$l = 100\ \text{mm} = 0,1\ \text{m}$

$h = 50\ \text{mm} = 50 \cdot 10^{-3}\ \text{m}$

épaisseur $t = 3\ \text{mm} = 3 \cdot 10^{-3}\ \text{m}$

$E = 25\ \text{GPa} = 25 \cdot 10^{9}\ \text{Pa}$

$\nu = 0,3$

$$\left\{\begin{matrix} \sigma_{xx} = 35\ \text{MPa} = 35 \cdot 10^{6}\ \text{Pa} \\ \sigma_{yy} = 75\ \text{MPa} = 75 \cdot 10^{6}\ \text{Pa} \\ \sigma_{xy} = 20\ \text{MPa} = 20 \cdot 10^{6}\ \text{Pa} \end{matrix}\right.$$

![](figs/fig-p01-plaque.png)

**1) Calculons les composantes du tenseur des déformations**

$$\varepsilon_{xx} = \frac{1}{E}\left\lbrack \sigma_{xx} - \nu\,\sigma_{yy} \right\rbrack = \frac{1}{25 \cdot 10^{9}}\left\lbrack 35 \cdot 10^{6} - 0,3 \times 75 \cdot 10^{6} \right\rbrack$$

$$\Rightarrow \varepsilon_{xx} = 0,0005$$

$$\varepsilon_{yy} = \frac{1}{E}\left\lbrack \sigma_{yy} - \nu\,\sigma_{xx} \right\rbrack = \frac{1}{25 \cdot 10^{9}}\left\lbrack 75 \cdot 10^{6} - 0,3 \times 35 \cdot 10^{6} \right\rbrack$$

$$\Rightarrow \varepsilon_{yy} = 0,00258$$

$$\varepsilon_{xy} = \frac{\sigma_{xy}}{2\mu}\quad \text{or}\quad \mu = \frac{E}{2(1 + \nu)} = \frac{25 \cdot 10^{9}}{2(1 + 0,3)} \Rightarrow \mu = 9615384615,38$$

*— page 2 —*

$$\varepsilon_{xy} = \frac{20 \cdot 10^{6}}{19230769230,8} = 0,00104 \Rightarrow \varepsilon_{xy} = 0,00104$$

$$\text{alors}\quad \boxed{\begin{matrix} \varepsilon_{xx} = 0,0005 \\ \varepsilon_{yy} = 0,00258 \\ \varepsilon_{xy} = 0,00104 \end{matrix}}$$

**② Calculons les dimensions finales de la plaque.**

$$\ast\ \Delta l = \varepsilon_{xx} \times l = 0,0005 \times 100 = 0,05\ \text{mm}$$

$$\ast\ \Delta h = \varepsilon_{yy} \times h = 0,00258 \times 50 = 0,129\ \text{mm}$$

$$\ast\ \Delta e = \varepsilon_{zz} \cdot t = \frac{-\nu}{E}\left\lbrack \sigma_{xx} + \sigma_{yy} \right\rbrack t = \frac{-0,3}{25 \cdot 10^{9}}\left\lbrack 35 \cdot 10^{6} + 75 \cdot 10^{6} \right\rbrack \times 3$$

$$\Rightarrow \Delta e = -0,00396\ \text{mm}$$

> *[Passage barré dans le cahier, annoté « faux » :]*

$$\text{alors}\quad \boxed{\begin{matrix} \Delta l = 0,05\ \text{mm} \\ \Delta h = 0,129\ \text{mm} \\ \Delta e = -0,00396\ \text{mm} \end{matrix}}$$

**[ Vraie Version ]**

**(Formule) →** $\boxed{\text{Dimension finale} = \text{dimension initiale} \times (1 + \text{déformation})}$

$l = 100\ \text{mm}$

$$l' = l \times \left( 1 + \varepsilon_{xx} \right) = 100\,(1 + 0,0005) = 100,05\ \text{mm}$$

$$h' = h_{0} \cdot \left( 1 + \varepsilon_{yy} \right) = 50\,(1 + 0,00258) = 50,129\ \text{mm}$$

$$e' = e_{0} \cdot \left( 1 + \varepsilon_{zz} \right)\quad \text{or}\quad \varepsilon_{zz} = \frac{-\nu}{E}\left\lbrack \sigma_{xx} + \sigma_{yy} \right\rbrack$$

$$\text{avec}\ \boxed{e = t = 3\ \text{mm}}$$

$$\varepsilon_{zz} = -0,00132$$

*— page 3 —*

$$e' = 3\,(1 - 0,00132) = 2,996\ \text{mm}$$

$$\Rightarrow \boxed{\begin{matrix} l' = 100,05\ \text{mm} \\ h' = 50,129\ \text{mm} \\ e' = 2,996\ \text{mm} \end{matrix}}\quad \text{dimensions finales}$$

**\* Son volume a-t-il varié ?**

$$V_{i} = l \times h \times e = 100 \times 50 \times 3 = 15000\ \text{mm}^{3}$$

$$V_{f} = l' \times h' \times e' = 100,05 \times 50,129 \times 2,996$$

$$\Rightarrow V_{f} = 15026,15\ \text{mm}^{3}$$

donc $V_f > V_i$ d'où le volume varie très peu (quasiment incompressible).

$$\frac{V_{f}}{V_{i}} = \frac{15026,15}{15000} = 1,001 \Rightarrow \boxed{V_{f} = 1,001 \cdot V_{i}}$$

**③ Calculons la contrainte équivalente de Von Mises ainsi que celle de Tresca :**

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} \sigma_{xx} & \sigma_{xy} & \sigma_{xz} \\ \sigma_{yx} & \sigma_{yy} & \sigma_{yz} \\ \sigma_{zx} & \sigma_{zy} & \sigma_{zz} \end{bmatrix} = \begin{bmatrix} 35 & 20 & 0 \\ 20 & 75 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

$$\Rightarrow \left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} 35 & 20 \\ 20 & 75 \end{bmatrix}$$

$$\det\left( \overline{\overline{\sigma}} - \lambda\,\overline{\overline{I}} \right) = 0 \Rightarrow \begin{vmatrix} 35 - \lambda & 20 & 0 \\ 20 & 75 - \lambda & 0 \\ 0 & 0 & -\lambda \end{vmatrix} = 0$$

*— page 4 —*

$$\Rightarrow -\lambda\,(35 - \lambda)(75 - \lambda) + \lambda\,(20)^{2} = 0$$

$$\Rightarrow \lambda\left\lbrack -(35 - \lambda)(75 - \lambda) + (20)^{2} \right\rbrack = 0$$

$$\Rightarrow \boxed{\lambda = 0}\quad \text{et}\quad -2625 + 110\lambda - \lambda^{2} + 400 = 0$$

$$-\lambda^{2} + 110\lambda - 2225 = 0 \Rightarrow \lambda^{2} - 110\lambda + 2225 = 0$$

$$\Delta = (-110)^{2} - 4\,(2225) = 12100 - 8900$$

$$D = 3200 \Rightarrow \sqrt{\Delta} = 56,56$$

$$\lambda_{1} = \frac{110 - \sqrt{3200}}{2} = 26,72\quad \text{et}\quad \lambda_{2} = 83,28$$

les contraintes principales sont :

$$\sigma_{I} = 0\ \text{MPa}\ ;\quad \sigma_{II} = 26,72\ \text{MPa}\quad \text{et}\quad \sigma_{III} = 83,28\ \text{MPa}$$

$$\left( \sigma_{I} - \sigma_{II} \right)^{2} = (-26,72)^{2} = 713,958\ \text{MPa}$$

$$\left( \sigma_{II} - \sigma_{III} \right)^{2} = (26,72 - 83,28)^{2} = 3199,033\ \text{MPa}$$

$$\left( \sigma_{III} - \sigma_{I} \right)^{2} = (83,28)^{2} = 6935,558\ \text{MPa}$$

**\* Pour Von Mises :**

$$\sigma_{eq} = \sqrt{\frac{1}{2}\left\lbrack \left( \sigma_{I} - \sigma_{II} \right)^{2} + \left( \sigma_{II} - \sigma_{III} \right)^{2} + \left( \sigma_{III} - \sigma_{I} \right)^{2} \right\rbrack}$$

$$= \sqrt{\frac{1}{2}\left\lbrack 713,958 + 3199,033 + 6935,558 \right\rbrack} = 73,65\ \text{MPa}$$

$$\boxed{\sigma_{eq\,VM} = 73,65\ \text{MPa}}$$

**Autre méthode :**

$$\sigma_{eq}^{2} = \sigma_{xx}^{2} + \sigma_{yy}^{2} - \sigma_{xx} \cdot \sigma_{yy} + 3\sigma_{xy}^{2}$$

$$\text{avec}\ \left\{ \begin{matrix} \sigma_{xx} = 35\ \text{MPa} \\ \sigma_{yy} = 75\ \text{MPa} \\ \sigma_{xy} = 20\ \text{MPa} \end{matrix} \right. \Rightarrow \boxed{\sigma_{eq\,VM} = 73,6\ \text{MPa}}$$

*— page 5 —*

**\* Pour Tresca :**

$$\sigma_{eq} = \max\left( \left| \sigma_{I} - \sigma_{II} \right|,\ \left| \sigma_{II} - \sigma_{III} \right|,\ \left| \sigma_{III} - \sigma_{I} \right| \right)$$

$$\left| \sigma_{I} - \sigma_{II} \right| = \left| -26,72 \right| = 26,72\ \text{MPa}$$

$$\left| \sigma_{II} - \sigma_{III} \right| = \left| (26,72 - 83,28) \right| = \left| -56,56 \right| = 56,56\ \text{MPa}$$

$$\left| \sigma_{III} - \sigma_{I} \right| = \left| 83,28 \right| = 83,28\ \text{MPa}$$

$$\text{alors}\quad \boxed{\sigma_{eq\,T} = 83,28\ \text{MPa}}$$

## Exercice ② : Critères de Tresca et de Von Mises

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} \sigma & \tau & 0 \\ \tau & \sigma & 0 \\ 0 & 0 & \sigma \end{bmatrix}$$

**① La contrainte équivalente de Von Mises dépend-elle de $\sigma$ ?**

Oui, elle dépend des composantes du tenseur des contraintes $\sigma$ (ou contraintes isotropes) donc de la différence entre les contraintes principales mais pas de leur somme.

**② Comparaison de Von Mises et de Tresca :**

$$\det\left( \overline{\overline{\sigma}} - \lambda\,\overline{\overline{I}} \right) = 0 \Rightarrow \begin{vmatrix} \sigma - \lambda & \tau & 0 \\ \tau & \sigma - \lambda & 0 \\ 0 & 0 & \sigma - \lambda \end{vmatrix} = 0$$

$$\Rightarrow (\sigma - \lambda)(\sigma - \lambda)^{2} - \tau^{2}(\sigma - \lambda) = 0$$

$$\Rightarrow (\sigma - \lambda)\left\lbrack \sigma^{2} - 2\sigma\lambda + \lambda^{2} - \tau^{2} \right\rbrack = 0$$

$$\sigma - \lambda = 0 \Rightarrow \boxed{\lambda = \sigma}$$

$$\lambda^{2} - 2\sigma \cdot \lambda + \left( \sigma^{2} - \tau^{2} \right) = 0$$

*— page 6 —*

$$\Delta = (-2\sigma)^{2} - 4\left( \sigma^{2} - \tau^{2} \right) = 4\sigma^{2} - 4\sigma^{2} + 4\tau^{2} \Rightarrow \Delta = 4\tau^{2} \Rightarrow \sqrt{\Delta} = 2\tau$$

$$\lambda_{1} = \frac{2\sigma - 2\tau}{2} = \sigma - \tau\quad \text{et}\quad \lambda_{2} = \sigma + \tau$$

les contraintes principales sont :

$$\left\{ \begin{matrix} \sigma_{I} = \sigma \\ \sigma_{II} = \sigma - \tau \\ \sigma_{III} = \sigma + \tau \end{matrix} \right.$$

$$\left( \sigma_{I} - \sigma_{II} \right)^{2} = (\sigma - \sigma + \tau)^{2} = \tau^{2}$$

$$\left( \sigma_{II} - \sigma_{III} \right)^{2} = (\sigma - \tau - \sigma - \tau)^{2} = (-2\tau)^{2} = 4\tau^{2}$$

$$\left( \sigma_{III} - \sigma_{I} \right)^{2} = (\sigma + \tau - \sigma)^{2} = \tau^{2}$$

**\* Pour Von Mises :**

$$\sigma_{eq} = \sqrt{\frac{1}{2}\left\lbrack \tau^{2} + 4\tau^{2} + \tau^{2} \right\rbrack} = \sqrt{3\tau^{2}} = \tau\sqrt{3}$$

$$\boxed{\sigma_{eq\,VM} = \tau\sqrt{3}}$$

**\* Pour Tresca :**

$$\sigma_{eq} = \max\left( \left| \tau \right|,\ \left| -2\tau \right|,\ \left| \tau \right| \right) \Rightarrow \boxed{\sigma_{eq} = 2\tau}$$

$$\frac{\sigma_{eq\,V.M}}{\sigma_{eq\,T}} = \frac{\tau\sqrt{3}}{2\tau} = \frac{\sqrt{3}}{2} \Rightarrow \boxed{\sigma_{eq\,V.M} = \frac{\sqrt{3}}{2}\,\sigma_{eq\,T}}$$

## Exercice ③ : Relat° contraintes – déformations

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = a \times \begin{bmatrix} -1 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & -1 \end{bmatrix}$$

*— page 7 —*

avec $a$ est un nombre réel constant.

**① Les composantes de la matrice représentant le tenseur des contraintes pour la déformat° indiquée en fonction de $a$, $\mu$ :**

$$\overline{\overline{\sigma}} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right)\overline{\overline{I}} + 2\mu\,\overline{\overline{\varepsilon}}$$

or $\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = a(-1 + 2 - 1) = a(2 - 2) = 0 \Rightarrow \mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = 0$

donc $\overline{\overline{\sigma}} = 2\mu\,\overline{\overline{\varepsilon}} = 2\mu \cdot a\begin{bmatrix} -1 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & -1 \end{bmatrix}$

$$\Rightarrow \boxed{\left\lbrack \overline{\overline{\sigma}} \right\rbrack = 2\mu a \times \begin{bmatrix} -1 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & -1 \end{bmatrix}}$$

**② Déterminons les contraintes principales en fonct° de $a$ et $\mu$ :**

$$\det\left( \overline{\overline{\sigma}} - \lambda\,\overline{\overline{I}} \right) = 0 \Rightarrow 2\mu a\begin{vmatrix} -1 - \lambda & 1 & 0 \\ 1 & 2 - \lambda & 0 \\ 0 & 0 & -1 - \lambda \end{vmatrix} = 0$$

$$\Rightarrow 2\mu a\left\lbrack (2 - \lambda)(-1 - \lambda)^{2} - (-1 - \lambda) \right\rbrack = 0$$

$$\Rightarrow (-1 - \lambda)(2\mu a)\left\lbrack (2 - \lambda)(-1 - \lambda) - 1 \right\rbrack = 0$$

$$\Rightarrow 2\mu a\,(-1 - \lambda)\left\lbrack \lambda^{2} - \lambda - 2 - 1 \right\rbrack = 0$$

$$\Rightarrow 2\mu a\,(-1 - \lambda)\left( \lambda^{2} - \lambda - 3 \right) = 0$$

$$\Rightarrow (-2\mu a - \lambda)\left\lbrack (-2\mu a - \lambda)(4\mu a - \lambda) - 4\mu^{2}a^{2} \right\rbrack = 0$$

$$-2\mu a - \lambda = 0 \Rightarrow \lambda = -2\mu a$$

$$\text{et}\quad \lambda^{2} - 2\mu a\lambda - 12\mu^{2}a^{2} = 0$$

$$\Delta = 4\mu^{2}a^{2} - 4\left( -12\mu^{2}a^{2} \right) = 4\mu^{2}a^{2} + 48\mu^{2}a^{2}$$

$$\Delta = 52\mu^{2}a^{2} \Rightarrow \sqrt{\Delta} = \mu a\sqrt{52}$$

*— page 8 —*

$$\lambda_{1} = \frac{2\mu a - \mu a\sqrt{52}}{2} = \frac{\mu a}{2}\left( 2 - 2\sqrt{13} \right) = \mu a\left( 1 - \sqrt{13} \right)$$

$$\text{et}\quad \lambda_{2} = \mu a\left( 1 + \sqrt{13} \right)$$

les contraintes principales sont :

$$\left\{ \begin{matrix} \sigma_{I} = -2\mu a \\ \sigma_{II} = \mu a\left( 1 - \sqrt{13} \right) \\ \sigma_{III} = \mu a\left( 1 + \sqrt{13} \right) \end{matrix} \right.$$

**③ Calculons les contraintes équivalentes de Von Mises et de Tresca pour**
$$\left\{ \begin{matrix} E = 65\ \text{GPa} = 65 \cdot 10^{9}\ \text{Pa} \\ \nu = 0,33\quad \text{et}\quad a = 10^{-3} \end{matrix} \right.$$

$$\left( \sigma_{I} - \sigma_{II} \right)^{2} = \left( -2\mu a - \mu a + \mu a\sqrt{13} \right)^{2} = \left( -3\mu a + \mu a\sqrt{13} \right)^{2}$$

$$= 9\mu^{2}a^{2} - 6\mu^{2}a^{2}\sqrt{13} + 13a^{2}\mu^{2} = 22\mu^{2}a^{2} - 6\mu^{2}a^{2}\sqrt{13}$$

$$\left( \sigma_{II} - \sigma_{III} \right)^{2} = \left( \mu a - \mu a\sqrt{13} - \mu a - \mu a\sqrt{13} \right)^{2}$$

$$= \left( -2\mu a\sqrt{13} \right)^{2} \Rightarrow \left( \sigma_{II} - \sigma_{III} \right)^{2} = 52\mu^{2}a^{2}$$

$$\left( \sigma_{III} - \sigma_{I} \right)^{2} = \left( \mu a + \mu a\sqrt{13} + 2\mu a \right)^{2} = \left( 3\mu a + \mu a\sqrt{13} \right)^{2}$$

$$= 9\mu^{2}a^{2} + 6\mu^{2}a^{2}\sqrt{13} + 13\mu^{2}a^{2} = \left( 22 + 6\sqrt{13} \right)\mu^{2}a^{2}$$

**\* Pour Von Mises :**

$$\sigma_{eq} = \sqrt{\frac{1}{2}\left\lbrack \left( 22 - 6\sqrt{13} \right)\mu^{2}a^{2} + 52\mu^{2}a^{2} + \left( 22 + 6\sqrt{13} \right)\mu^{2}a^{2} \right\rbrack}$$

$$= \sqrt{\frac{1}{2}\left( 96\mu^{2}a^{2} \right)} = \mu a\sqrt{48} = 2\mu a\sqrt{12}$$

$$\Rightarrow \boxed{\sigma_{eq} = 2\mu a\sqrt{12}} = 0,169\ \text{GPa}$$

**\* Pour Tresca :**

$$\sigma_{eq} = \max\left( \left| \sigma_{I} - \sigma_{II} \right|,\ \left| \sigma_{II} - \sigma_{III} \right|,\ \left| \sigma_{III} - \sigma_{I} \right| \right)$$

$$\left| \sigma_{I} - \sigma_{II} \right| = \left| \mu a\left( -3 + \sqrt{13} \right) \right| = 0,01479\ \text{GPa}$$

$$\left| \sigma_{II} - \sigma_{III} \right| = \left| -2\mu a\sqrt{13} \right| = \left| -0,17621 \right| = 0,17621\ \text{GPa}$$

$$\left| \sigma_{III} - \sigma_{I} \right| = \left| \mu a\left( 3 + \sqrt{13} \right) \right| = 0,16241\ \text{GPa}$$

*— page 9 —*

$$\boxed{\sigma_{eq} = 0,17621\ \text{GPa}}$$

**④ Que pourrait-on faire avec ces contraintes (Von Mises et Tresca) ?**

On compare $\sigma_{eq\,V.M}$ et $\sigma_{eq.T}$ à la limite d'élasticité du matériau pour :

- Vérifier si le matériau reste <u>élastique</u> ou entre en <u>plastification</u> ;
- Choisir un critère adapté selon le type de matériau…

## Exercice ④ : Essai de Compression

$$E = 25\ \text{GPa} = 25 \cdot 10^{9}\ \text{Pa}\ ,\qquad \nu = 0,33$$

![](figs/fig-p09-compression.png)

**① Le problème posé correspond à un état plan de déformation** car les déplacements selon $z$ sont empêchés par l'enceinte rigide : $\varepsilon_{zz} = 0$. Cela arrive quand une dimension (profondeur)

*— page 10 —*

est bloquée, et le matériau ne peut pas se déformer dans cette direction.

**② Les composantes du tenseur des déformat° infinitésimales en fonction de $h_0$ et $h$ :**

$$\varepsilon_{yy} = \frac{\left( h - h_{0} \right)}{h_{0}}\quad \text{et}\quad \varepsilon_{zz} = 0.$$

$$\nu = -\frac{\varepsilon_{yy}}{\varepsilon_{xx}}\quad \text{mais ici}\quad \varepsilon_{xx} = -\nu\,\varepsilon_{yy} = -\nu\left( \frac{h - h_{0}}{h_{0}} \right)$$

$$\text{alors}\quad \boxed{\begin{matrix} \varepsilon_{xx} = -\nu\left( \dfrac{h - h_{0}}{h_{0}} \right) \\[2mm] \varepsilon_{yy} = \left( \dfrac{h - h_{0}}{h_{0}} \right)\quad \text{et}\quad \varepsilon_{zz} = 0 \end{matrix}}$$

**③** $h_{0} = 150\ \text{mm}$ et $h = 138\ \text{mm}$

Exprimons et calculons les composantes du tenseur des contraintes de Cauchy :

$$\overline{\overline{\sigma}} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right)\overline{\overline{I}} + 2\mu\,\overline{\overline{\varepsilon}}$$

$$\varepsilon_{xx} = -0,33\left( \frac{138 - 150}{150} \right) = 0,0264$$

$$\varepsilon_{yy} = \left( \frac{138 - 150}{150} \right) = -0,08\quad \text{et}\quad \varepsilon_{zz} = 0$$

$$\lambda = \frac{E\nu}{(1 + \nu)(1 - 2\nu)} = \frac{25 \cdot 10^{9} \times 0,33}{(1 + 0,33)\left( 1 - 2(0,33) \right)} = 18244139764,2\ \text{Pa} \simeq 18,2\ \text{GPa}$$

$$\mu = \frac{E}{2(1 + \nu)} = \frac{25 \cdot 10^{9}}{2(1 + 0,33)} = 9398496240,6\ \text{Pa} \simeq 9,4\ \text{GPa}$$

$$\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = 0,0264 + (-0,08) + 0 = -0,0536$$

*— page 11 —*

$$\sigma_{xx} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) + 2\mu\,\varepsilon_{xx} = 18,2\,(-0,0536) + 2(9,4)(0,0264)$$

$$\Rightarrow \boxed{\sigma_{xx} = -0,4792\ \text{GPa}}$$

$$\sigma_{yy} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) + 2\mu\,\varepsilon_{yy} = 18,2\,(-0,0536) + 2(9,4)(-0,08)$$

$$\Rightarrow \boxed{\sigma_{yy} = -2,47952\ \text{GPa}}$$

$$\sigma_{zz} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) + 2\mu\,\varepsilon_{zz} = 18,2\,(-0,0536) + 2(9,4)(0)$$

$$\Rightarrow \boxed{\sigma_{zz} = -0,97552\ \text{GPa}}$$

**④ Traçons les cercles de Mohr** correspondant à l'état de contrainte et déduisons la contrainte de cisaillement maximale :

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -0,47 & 0 & 0 \\ 0 & -2,47 & 0 \\ 0 & 0 & -0,97 \end{bmatrix}$$

On trace les cercles de Mohr pour les paires $\left( \sigma_{x},\sigma_{y} \right)$, $\left( \sigma_{y},\sigma_{z} \right)$ et $\left( \sigma_{x},\sigma_{z} \right)$

$$\boxed{\tau_{max} = \frac{\sigma_{max} - \sigma_{min}}{2}}\qquad 2\tau = 3,958\ \text{N/mm}^{2}$$

or $\sigma_{max} = -0,47$ GPa ; $\sigma_{min} = -2,47$ GPa

> *[Bas de la photo : un second feuillet recouvre la page ; on y lit le tableau de l'Exercice ⑤ (page 13) — $0,024\ |\ 0,0405\ |\ 0,0695\ |\ 0,095$ et $0,416\ |\ 2,041\ |\ 2,875\ |\ 2,316\ |\ 3,958$, ainsi que « $\sigma$ (MPa) $\rightarrow (OY)$ avec N/mm² = MPa ; $\varepsilon \rightarrow (OX)$ ».]*

*— page 12 —*

$$\tau_{max} = \frac{-0,47 - (-2,47)}{2} = \frac{-0,47 + 2,47}{2} = 1$$

$$\boxed{\tau_{max} = 1\ \text{GPa}}$$

![](figs/fig-p12-mohr.png)

Voir le fichier $\longrightarrow$ **RDM07** dans l'ordinateur.

Merci,

**KGB**

> *[Bas de page déchiré : on aperçoit en dessous la reprise des formules de $\lambda$, $\mu$ et $\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right)$ déjà écrites page 10.]*

*— page 13 —*

## Exercice ⑤ : Relat° contrainte – déformat°

$a = 3\ \text{mm}$ ; $b = 8\ \text{mm}$ et $l = 10\ \text{cm} = 100\ \text{mm}$

**① Représentons sur un graphique la contrainte en fonct° de la déformation :**

$$\varepsilon = \frac{\Delta l}{l}\quad \text{et}\quad \sigma = F/S\quad \text{avec}\quad S = a \times b\ \ (\text{sect}^{\circ}\ \text{rectangulaire})$$

| $F\ \lbrack N \rbrack$ | 0 | 10 | 25 | 45 | 70 | 95 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| $\Delta l\ (\text{mm})$ | 0 | 1 | 2,40 | 4,05 | 6,95 | 9,50 |

$$\varepsilon = \frac{\Delta l}{l} = \frac{0}{100} = 0\ ;\quad \varepsilon = \frac{\Delta l}{l} = \frac{1}{100} = 0,01$$

$$\varepsilon = \frac{\Delta l}{l} = \frac{2,40}{100} = 0,024\ ;\quad \varepsilon = \frac{\Delta l}{l} = \frac{4,05}{100} = 0,0405$$

$$\varepsilon = \frac{\Delta l}{l} = \frac{6,95}{100} = 0,0695\quad \text{et}\quad \varepsilon = \frac{\Delta l}{l} = \frac{9,50}{100} = 0,095$$

$$S = (3 \times 8)\ \text{mm}^{2} \Rightarrow S = 24\ \text{mm}^{2}$$

$$\sigma = \frac{F}{S} = \frac{0}{24} = 0\ \text{N/mm}^{2}\ ;\quad \sigma = \frac{F}{S} = \frac{10}{24} = 0,416\ \text{N/mm}^{2}$$

$$\sigma = \frac{F}{S} = \frac{25}{24} = 1,041\quad \sigma = \frac{F}{S} = \frac{45}{24} = 1,875\ \text{N/mm}^{2}$$

$$\sigma = \frac{F}{S} = \frac{70}{24} = 2,916\quad \text{et}\quad \sigma = \frac{95}{24} = 3,958\ \text{N/mm}^{2}$$

**On aura :**

| $\varepsilon$ | 0 | 0,01 | 0,024 | 0,0405 | 0,0695 | 0,095 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| $\sigma\ \lbrack \text{MPa} \rbrack$ | 0 | 0,416 | 1,041 | 1,875 | 2,916 | 3,958 |

$$\sigma\ (\text{MPa}) \longrightarrow (OY)\quad \text{avec}\quad \boxed{\text{N/mm}^{2} = \text{MPa}}\ ;\qquad \varepsilon \longrightarrow (OX)$$

*— page 14 —*

**② Déduisons le module de Young du matériau :**

$$\sigma = E \cdot \varepsilon \Rightarrow E = \frac{\sigma}{\varepsilon} = \frac{\left( \sigma_{2} - \sigma_{1} \right)}{\left( \varepsilon_{2} - \varepsilon_{1} \right)}$$

$$E = \frac{(1,041 - 0,416)}{(0,024 - 0,01)} = 44,64 \Rightarrow \boxed{E = 44,64\ \text{MPa}}$$

## Exercice ⑥ : Colonne sous compression

![](figs/fig-p14-colonne.png)

**① Les composantes du tenseur des contraintes en fonction de $P$ :**

$$\boxed{\sigma_{x} = \sigma_{y} = 0}$$

$$\boxed{\sigma_{z} = -P}\quad \text{avec}\quad \boxed{P = F/S}\quad \text{avec}\quad \boxed{S = a \cdot b}$$

**② Les composantes du tenseur des déformat° en fonction de $P$, $E$ et $\nu$ :**

$$\sigma = E \cdot \varepsilon$$

$$\varepsilon = \frac{\sigma}{E} \Rightarrow \varepsilon_{zz} = \frac{\sigma_{zz}}{E} = -P/E \Rightarrow \boxed{\varepsilon_{zz} = -P/E}$$

$$\varepsilon_{xx} = \varepsilon_{yy} = -\nu \cdot \varepsilon_{zz} = -\nu\left( \frac{-P}{E} \right) = \nu P/E$$

$$\Rightarrow \boxed{\varepsilon_{xx} = \varepsilon_{yy} = \nu P/E}$$

*— page 15 —*

**③** $\sigma_{e} = 2\ \text{MPa}$ ; $E = 20\ \text{GPa}$ et $h = 2\ \text{m}$

Calculons la variat° de la hauteur de la colonne :

$$\Delta h = \varepsilon_{zz} \cdot h = -\frac{P}{E}\,h = -\frac{F/S}{E} \cdot h$$

$$\Delta h = -\frac{F}{S\,E}\,h = \frac{-F}{a\,b\,E}\,h = -\frac{\sigma_{e}}{E}\,h$$

$$\boxed{\Delta h = -\frac{\sigma_{e}}{E}\,h}$$

$$\Delta h = -\frac{2 \cdot 10^{6}}{20 \cdot 10^{9}} \times 2 = -0,0002\ \text{m} = -2 \cdot 10^{-4}\ \text{m}$$

$$\text{alors}\quad \boxed{\Delta h = -0,2\ \text{mm}}$$

## Exercice ⑦ : Relat° $\rightarrow \sigma$ et $\varepsilon$

$$\overrightarrow{u} = \begin{pmatrix} -a\,x_{1} + a\,x_{2} \\ a\,x_{1} - a\,x_{2} \\ a\,x_{3} \end{pmatrix}\quad \text{avec}\ a > 0$$

**① Le tenseur des déformations infinitésimales :**

$$\overrightarrow{u} = u_{1}\overrightarrow{e_{1}} + u_{2}\overrightarrow{e_{2}} + u_{3}\overrightarrow{e_{3}}\qquad K_{ij} = \frac{\partial u_{i}}{\partial x_{j}}$$

$$\left\lbrack \overline{\overline{K}} \right\rbrack = \begin{bmatrix} \dfrac{\partial u_{1}}{\partial x_{1}} & \dfrac{\partial u_{1}}{\partial x_{2}} & \dfrac{\partial u_{1}}{\partial x_{3}} \\[3mm] \dfrac{\partial u_{2}}{\partial x_{1}} & \dfrac{\partial u_{2}}{\partial x_{2}} & \dfrac{\partial u_{2}}{\partial x_{3}} \\[3mm] \dfrac{\partial u_{3}}{\partial x_{1}} & \dfrac{\partial u_{3}}{\partial x_{2}} & \dfrac{\partial u_{3}}{\partial x_{3}} \end{bmatrix} = \begin{bmatrix} -a & a & 0 \\ a & -a & 0 \\ 0 & 0 & a \end{bmatrix}$$

$$\left\lbrack \overline{\overline{K}} \right\rbrack = \begin{bmatrix} -a & a & 0 \\ a & -a & 0 \\ 0 & 0 & a \end{bmatrix} \Rightarrow \left\lbrack \overline{\overline{K}} \right\rbrack^{t} = \begin{bmatrix} -a & a & 0 \\ a & -a & 0 \\ 0 & 0 & a \end{bmatrix}$$

$$\overline{\overline{\varepsilon}} = \frac{1}{2}\left( \overline{\overline{K}} + \overline{\overline{K}}^{t} \right)$$

*— page 16 —*

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \frac{1}{2}\left( \begin{bmatrix} -a & a & 0 \\ a & -a & 0 \\ 0 & 0 & a \end{bmatrix} + \begin{bmatrix} -a & a & 0 \\ a & -a & 0 \\ 0 & 0 & a \end{bmatrix} \right)$$

$$\Rightarrow \boxed{\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} -a & a & 0 \\ a & -a & 0 \\ 0 & 0 & a \end{bmatrix}}$$

**② Les composantes de la matrice représentant le tenseur des contraintes en foncti° de $a$, $\lambda$ et $\mu$ :**

$$\overline{\overline{\sigma}} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right)\overline{\overline{I}} + 2\mu\,\overline{\overline{\varepsilon}}$$

$$\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = -a - a + a = -a \Rightarrow \mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = -a$$

$$\lambda = \frac{E\nu}{(1 + \nu)(1 - 2\nu)}\quad \text{et}\quad \mu = E/2(1 + \nu)\quad \text{et}\quad \left\lbrack \overline{\overline{I}} \right\rbrack = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \lambda(-a)\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} + 2\mu\begin{bmatrix} -a & a & 0 \\ a & -a & 0 \\ 0 & 0 & a \end{bmatrix}$$

$$\Rightarrow \boxed{\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -2a\mu - a\lambda & 2\mu a & 0 \\ 2\mu a & -2\mu a - a\lambda & 0 \\ 0 & 0 & 2\mu a - a\lambda \end{bmatrix}}$$

<u>Par la suite :</u> $E = 210\ \text{GPa} = 210 \cdot 10^{9}\ \text{Pa}$ ; $\nu = 0,3$ et $a = 0,001$.

**③ Représentons les cercles de Mohr des contraintes :**

$$\lambda = \frac{210 \times 0,3}{(1 + 0,3)(1 - 2 \times 0,3)} = 121,153\ \text{GPa}$$

$$\mu = \frac{210}{2(1 + 0,3)} = 80,769\ \text{GPa}$$

*— page 17 —*

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -2 \times 0,001 \times 80,769 - 0,001 \times 121,153 & 0,161538 & 0 \\ 0,161538 & -0,282691 & 0 \\ 0 & 0 & 0,040385 \end{bmatrix}$$

$$\Rightarrow \boxed{\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -0,28 & 0,16 & 0 \\ 0,16 & -0,28 & 0 \\ 0 & 0 & 0,04 \end{bmatrix}}$$

**[ Voir RDM07 ]**

![](figs/fig-p17-mohr.png)

**④ Les contraintes principales sont :**

$$\sigma_{I} = -0,44\ \text{GPa}$$

$$\sigma_{II} = -0,12\ \text{GPa}$$

$$\sigma_{III} = 0,04\ \text{GPa}$$

$$\tau_{max} = \frac{\sigma_{max} - \sigma_{min}}{2} = \frac{0,04 + 0,44}{2} \Rightarrow \boxed{\tau_{max} = 0,24\ \text{GPa}}$$

**[ cisaillement maximal ]**

*— page 18 —*

## Exercice ⑧ : Tenseur des contraintes

![](figs/fig-p18-plaque.png)

**① La plaque est sollicitée en contrainte plane** car les efforts $\sigma_{1}$ et $\sigma_{2}$ sont appliqués dans le plan $(x,y)$ et $\sigma_{z} = 0$.

**② Les composantes du tenseur des déformat° infinitésimales :**

$$\varepsilon_{xx} = \frac{1}{E}\left\lbrack \sigma_{1} - \nu\,\sigma_{2} \right\rbrack\ ;\quad \varepsilon_{yy} = \frac{1}{E}\left\lbrack \sigma_{2} - \nu\,\sigma_{1} \right\rbrack\quad \text{et}\quad \varepsilon_{xy} = 0$$

$$\varepsilon_{zz} \neq 0\ (\text{contrainte plan})\quad \text{donc}\quad \varepsilon_{zz} = \frac{-\nu}{E}\left( \sigma_{1} + \sigma_{2} \right)$$

**③** $\sigma_{1} = 10\ \text{MPa}$ ; $\sigma_{2} = 15\ \text{MPa}$

$E = 25\ \text{GPa}$ et $\nu = 0,3$

$$\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = \varepsilon_{xx} + \varepsilon_{yy} + \varepsilon_{zz} = \frac{1}{E}\left\lbrack \sigma_{1} - \nu\sigma_{2} + \sigma_{2} - \nu\sigma_{1} - \nu\sigma_{1} - \sigma_{2}\nu \right\rbrack$$

$$= \frac{1}{25 \cdot 10^{9}}\left\lbrack 10^{7} + 15 \cdot 10^{6} - 0,3\left( 15 \cdot 10^{6} + 10^{7} + 10^{7} + 15 \cdot 10^{6} \right) \right\rbrack$$

$$\Rightarrow \boxed{\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = 4 \cdot 10^{-4}}$$

$$\text{avec}\quad \boxed{1\ \text{MPa} = 10^{6}\ \text{Pa}}$$

*— page 19 —*

Puisque $\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = 4 \cdot 10^{-4} > 0 \Rightarrow$ le volume augmente. $\left( \mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) > 0 \right.$, le matériau se dilate$)$

**④ Traçons les cercles de Mohr et déduisons la contrainte de cisaillement maximale :**

$$\sigma_{moy} = \frac{\sigma_{1} + \sigma_{2}}{2} = \frac{10 + 15}{2} \Rightarrow 12,5\ \text{MPa} = \sigma_{moy}$$

$$\tau_{max} = \frac{\sigma_{2} - \sigma_{1}}{2} = \frac{15 - 10}{2} \Rightarrow \boxed{2,5\ \text{MPa} = \tau_{max}}$$

d'où le cercle de Mohr sera tracé par : $\left\{ \begin{matrix} \text{Centre : } 12,5\ \text{MPa} \\ \text{Rayon : } 2,5\ \text{MPa} \end{matrix} \right.$

**⑤ Les contraintes équivalentes de Von Mises et Tresca**

**\* Von Mises :**

$$\sigma_{eq} = \sqrt{\sigma_{1}^{2} - \sigma_{1}\sigma_{2} + \sigma_{2}^{2}} = \sqrt{100 - 10 \times 15 + (15)^{2}}$$

$$\Rightarrow \boxed{\sigma_{eq} = 13,23\ \text{MPa}}$$

**\* Tresca :**

$$\sigma_{eq} = \left| \sigma_{2} - \sigma_{1} \right| = \left| 15 - 10 \right| = \left| 5 \right| \Rightarrow \boxed{5\ \text{MPa} = \sigma_{eq}}$$

## Exercice ⑨ : État plan de contrainte

![](figs/fig-p19-cisaillement.png)

**① La trace du tenseur des déformations est :**

*— page 20 —*

$$\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = \varepsilon_{xx} + \varepsilon_{yy} + \varepsilon_{zz}\quad \text{or}\quad \varepsilon_{zz} = 0\ \ (\text{matériau isotrope})$$

$$\Rightarrow \boxed{\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = \varepsilon_{xx} + \varepsilon_{yy}}$$

**② Les composantes du tenseur des déformations :**

$$\varepsilon_{xx} = \frac{1}{E}\left\lbrack \sigma_{xx} - \nu\,\sigma_{yy} \right\rbrack$$

$$\varepsilon_{yy} = \frac{1}{E}\left\lbrack \sigma_{yy} - \nu\,\sigma_{xx} \right\rbrack$$

$$\varepsilon_{xy} = \frac{\sigma_{xy}}{2\mu}\quad \text{avec}\quad \mu = \frac{E}{2(1 + \nu)}$$

$$\sigma_{xx} = \sigma_{yy} = 0\quad \text{et}\quad \sigma_{xy} \neq 0$$

$$\text{donc}\quad \left\{ \boxed{\begin{matrix} \varepsilon_{xx} = 0 \\ \varepsilon_{yy} = 0 \end{matrix}} \right.$$

$$\varepsilon_{xy} = \frac{\sigma_{xy}}{\dfrac{E}{(1 + \nu)}} \Rightarrow \boxed{\varepsilon_{xy} = \frac{(1 + \nu)}{E}\,\sigma_{xy}}$$

**③ Les contraintes principales :**

$$\left\lbrack \sigma \right\rbrack = \begin{bmatrix} 0 & \sigma_{xy} \\ \sigma_{xy} & 0 \end{bmatrix}$$

$$\boxed{\begin{matrix} \sigma_{I} = \sigma_{xy} \\ \sigma_{II} = -\sigma_{xy} \end{matrix}}$$

**\* Les directions principales sont orientées à 45° par rapport aux axes $x$ et $y$.**

## Exercice ⑩ : Critères limites d'élasticité

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} 0 & \sigma_{12} & 0 \\ \sigma_{12} & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

**① Les contraintes principales et les direct° du tenseur**

$$\det\left( \overline{\overline{\sigma}} - \lambda\,\overline{\overline{I}} \right) = 0 \Rightarrow \begin{vmatrix} -\lambda & \sigma_{12} & 0 \\ \sigma_{12} & -\lambda & 0 \\ 0 & 0 & -\lambda \end{vmatrix} = 0$$

$$\Rightarrow (-\lambda)\left( \lambda^{2} \right) + \lambda\,\sigma_{12}^{2} = 0$$

$$\Rightarrow -\lambda\left( \lambda^{2} - \sigma_{12}^{2} \right) = 0 \Rightarrow \left\{ \begin{matrix} -\lambda = 0 \Rightarrow \lambda = 0 \\ \lambda^{2} = \sigma_{12}^{2} \end{matrix} \right.$$

$$\Rightarrow \left\{ \begin{matrix} \lambda = \pm\,\sigma_{12} \\ \lambda = 0 \end{matrix} \right.$$

*— page 21 —*

**\* Les contraintes principales sont :**

$$\sigma_{I} = 0\ ;\quad \sigma_{II} = \sigma_{12}\quad \text{et}\quad \sigma_{III} = -\sigma_{12}$$

**\* <u>Directions principales</u> :** $\left( \overline{\overline{\sigma}} - \lambda\,\overline{\overline{I}} \right)\overrightarrow{u} = \overrightarrow{0}$ avec $\overrightarrow{u}\left( u_{1},u_{2},u_{3} \right)$

$$\begin{bmatrix} -\lambda & \sigma_{12} & 0 \\ \sigma_{12} & -\lambda & 0 \\ 0 & 0 & -\lambda \end{bmatrix}\begin{pmatrix} u_{1} \\ u_{2} \\ u_{3} \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \Rightarrow \left\{ \begin{matrix} -\lambda u_{1} + \sigma_{12}u_{2} = 0 \\ \sigma_{12}u_{1} - \lambda u_{2} = 0 \\ -\lambda u_{3} = 0 \end{matrix} \right.$$

<u>Pour $\lambda = 0$</u> :

$$\left\{ \begin{matrix} \sigma_{12}u_{2} = 0 \Rightarrow u_{2} = 0 \\ \sigma_{12}u_{1} = 0 \Rightarrow u_{1} = 0 \\ 0\,u_{3} = 0 \Rightarrow u_{3} = u_{3} \end{matrix} \right. \Rightarrow \overrightarrow{u}\begin{pmatrix} 0 \\ 0 \\ u_{3} \end{pmatrix}$$

$$\overrightarrow{u}' = \frac{\overrightarrow{u}}{\left\| \overrightarrow{u} \right\|} \Rightarrow \boxed{\overrightarrow{u}'\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}}$$

<u>Pour $\lambda = \sigma_{12}$</u> :

$$\left\{ \begin{matrix} -\sigma_{12}u_{1} + \sigma_{12}u_{2} = 0 \\ \sigma_{12}u_{1} - \sigma_{12}u_{2} = 0 \\ -\sigma_{12}u_{3} = 0 \end{matrix} \right. \Rightarrow \boxed{\overrightarrow{u}''\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}}$$

<u>Pour $\lambda = -\sigma_{12}$</u> :

$$\left\{ \begin{matrix} \sigma_{12}u_{1} + \sigma_{12}u_{2} = 0 \\ \sigma_{12}u_{1} + \sigma_{12}u_{2} = 0 \\ \sigma_{12}u_{3} = 0 \end{matrix} \right. \Rightarrow \left\{ \begin{matrix} u_{1} + u_{2} = 0 \\ \sigma_{12}u_{3} = 0 \end{matrix} \right.$$

$$u_{1} = -u_{2}$$

$$u_{2} = 1 \Rightarrow u_{1} = -1\quad \text{et}\quad u_{3} = 0 \Rightarrow \overrightarrow{u}\begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}$$

$$\overrightarrow{u}''' = \frac{-\overrightarrow{e_{1}} + \overrightarrow{e_{2}}}{\sqrt{2}} = +\frac{\sqrt{2}}{2}\left( -\overrightarrow{e_{1}} + \overrightarrow{e_{2}} \right) \Rightarrow \boxed{\overrightarrow{u}'''\begin{pmatrix} -\sqrt{2}/2 \\ \sqrt{2}/2 \\ 0 \end{pmatrix}}$$

<u>Vérification</u> : $\overrightarrow{u}' \cdot \overrightarrow{u}'' = 0$ ; $\overrightarrow{u}'' \cdot \overrightarrow{u}''' = 0$ et $\overrightarrow{u}''' \cdot \overrightarrow{u}' = 0$

**② Exprimons la limite d'élasticité en cisaillement $\left( \tau_{e} = \sigma_{12} \right)$ en fonct° de $\sigma_{e}$ en utilisant le critère de Von Mises et Tresca :**

**\* <u>Von Mises</u> :**

*— page 22 —*

$$\sigma_{eq} = \sqrt{\frac{1}{2}\left\lbrack \left( \sigma_{I} - \sigma_{II} \right)^{2} + \left( \sigma_{II} - \sigma_{III} \right)^{2} + \left( \sigma_{III} - \sigma_{I} \right)^{2} \right\rbrack}$$

$$\left( \sigma_{I} - \sigma_{II} \right)^{2} = \sigma_{12}^{2}\ ;\quad \left( \sigma_{II} - \sigma_{III} \right)^{2} = 4\sigma_{12}^{2}\quad \text{et}\quad \left( \sigma_{III} - \sigma_{I} \right)^{2} = \sigma_{12}^{2}$$

$$\sigma_{eq} = \sqrt{\frac{1}{2}\left\lbrack 6\sigma_{12}^{2} \right\rbrack} \Rightarrow \boxed{\sigma_{eq} = \sigma_{12}\sqrt{3}}$$

$$\text{alors}\quad \boxed{\sigma_{12} = \tau_{e} = \frac{\sigma_{eq}}{\sqrt{3}} = \frac{\sqrt{3}}{3}\,\sigma_{eq}}$$

**\* <u>Tresca</u> :**

$$\sigma_{eq} = \max\left( \left| \sigma_{I} - \sigma_{II} \right|,\ \left| \sigma_{II} - \sigma_{III} \right|,\ \left| \sigma_{III} - \sigma_{I} \right| \right)$$

$$\left| \sigma_{I} - \sigma_{II} \right| = \left| -\sigma_{12} \right| = \sigma_{12}$$

$$\left| \sigma_{II} - \sigma_{III} \right| = \left| \sigma_{12} + \sigma_{12} \right| = 2\sigma_{12}\quad \text{et}\quad \left| \sigma_{III} - \sigma_{I} \right| = \sigma_{12}$$

$$\Rightarrow \sigma_{eq} = 2\sigma_{12}$$

$$\Rightarrow \boxed{\tau_{e} = \sigma_{12} = \frac{1}{2}\,\sigma_{eq}}$$

**③ <u>Comparaison</u> :**

<u>Von Mises :</u>

$$\tau_{e} = \frac{\sqrt{3}}{3}\,\sigma_{eq} = 0,577\,\sigma_{eq} \Rightarrow \boxed{\tau_{e} = 0,577\,\sigma_{eq}}$$

<u>Tresca :</u>

$$\tau_{e} = \frac{1}{2}\,\sigma_{eq} = 0,5\,\sigma_{eq} \Rightarrow \boxed{\tau_{e} = 0,5\,\sigma_{eq}}$$

$0,577\,\sigma_{eq} > 0,5\,\sigma_{eq} \Rightarrow$ Von Mises prédit une limite en cisaillement un peu plus élevée que Tresca.

## Exercice ⑪ : Relation $\sigma$ et $\varepsilon$

$$\left. \begin{matrix} u_{1} = -\alpha\,x_{1} + \beta\left( x_{2} - x_{3} \right) \\ u_{2} = \alpha\left( x_{1} + x_{3} \right) - \beta\,x_{2} \\ u_{3} = -\alpha\left( x_{1} + x_{2} \right) - \beta\,x_{3} \end{matrix} \right| \quad \begin{matrix} \sigma_{e} = 25\ \text{MPa} \\ E = 14\ \text{GPa} = 14 \cdot 10^{9}\ \text{Pa} \\ \nu = 0,21 \end{matrix}$$

*— page 23 —*

**① Les composantes du tenseur des déformations infinitésimales :** $K_{ij} = \partial u_{i}/\partial x_{j}$

$$\left\lbrack \overline{\overline{K}} \right\rbrack = \begin{bmatrix} -\alpha & \beta & -\beta \\ \alpha & -\beta & \alpha \\ -\alpha & -\alpha & -\beta \end{bmatrix}\quad \text{et}\quad \left\lbrack \overline{\overline{K}} \right\rbrack^{t} = \begin{bmatrix} -\alpha & \alpha & -\alpha \\ \beta & -\beta & -\alpha \\ -\beta & \alpha & -\beta \end{bmatrix}$$

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \frac{1}{2}\begin{bmatrix} -2\alpha & \beta + \alpha & -\beta - \alpha \\ \alpha + \beta & -2\beta & 0 \\ -\alpha - \beta & 0 & -2\beta \end{bmatrix} \Rightarrow \boxed{\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} -\alpha & \dfrac{\beta + \alpha}{2} & -\dfrac{\beta + \alpha}{2} \\[2mm] \dfrac{\alpha + \beta}{2} & -\beta & 0 \\[2mm] -\dfrac{\alpha + \beta}{2} & 0 & -\beta \end{bmatrix}}$$

**② Les composantes du tenseur des contraintes de Cauchy :**

$$\sigma_{ij} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right)\delta_{ij} + 2\mu\,\varepsilon_{ij}$$

$$\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = -\alpha - \beta - \beta = -\alpha - 2\beta \Rightarrow \boxed{\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = -\alpha - 2\beta}$$

$$\lambda = \frac{E\nu}{(1 + \nu)(1 - 2\nu)} = \frac{14 \cdot 10^{9} \times 0,21}{(1 + 0,21)(1 - 2 \times 0,21)} = 4,18\ \text{GPa}$$

$$\mu = \frac{E}{2(1 + \nu)} = \frac{14 \cdot 10^{9}}{2(1 + 0,21)} = 5,78\ \text{GPa}$$

$$\sigma_{11} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) + 2\mu\,\varepsilon_{11} = 4,18\,(-\alpha - 2\beta) + 2\mu\,(-\alpha)$$

$$\sigma_{22} = \lambda\,(-\alpha - 2\beta) + 2\mu\,(-\beta)$$

$$\sigma_{33} = \lambda\,(-\alpha - 2\beta) + 2\mu\,(-\beta)$$

$$\sigma_{12} = 2\mu\,\varepsilon_{12} = 2\mu\left( \frac{\beta + \alpha}{2} \right) = \mu\,(\beta + \alpha)$$

$$\sigma_{13} = 2\mu\,\varepsilon_{13} = 2\mu\left( \frac{-\beta - \alpha}{2} \right) = \mu\,(-\beta - \alpha)$$

$$\sigma_{23} = 2\mu\,\varepsilon_{23} = 2\mu\,(0) = 0$$

$$\Rightarrow \boxed{\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} \lambda(-\alpha - 2\beta) + 2\mu(-\alpha) & \mu(\beta + \alpha) & \mu(-\beta - \alpha) \\ \mu(\beta + \alpha) & \lambda(-\alpha - 2\beta) - 2\mu\beta & 0 \\ \mu(-\beta - \alpha) & 0 & \lambda(-\alpha - 2\beta) - 2\mu\beta \end{bmatrix}}$$

*— page 24 —*

**③ Montrons que $\lambda = 2\mu$ pour obtenir $\sigma_{33} = 0$ :** (ie d'obtenir un état plan de contrainte)

$$\sigma_{33} = \lambda\,(-\alpha - 2\beta) + 2\mu\,(-\beta)$$

$$\sigma_{33} = 0 \Rightarrow 0 = \lambda\,(-\alpha - 2\beta) + 2\mu\,(-\beta)$$

$$0 = -\lambda\alpha - 2\beta\lambda + 2\mu(-\beta)$$

$$0 = -\lambda\alpha - 2\beta\,(\lambda + 2\mu) \Rightarrow \lambda\alpha = -2\beta\,(\lambda + 2\mu)$$

$$\boxed{\lambda = 2\mu}\quad \text{si}\quad \boxed{\nu = 1/3}$$

**④ La valeur maximale de $\alpha$ ?**

## Exercice ⑫ : Relat° $\varepsilon$ et $\sigma$

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = 10^{-6} \times \begin{bmatrix} \varepsilon_{xx} & 0 & 0 \\ 0 & -400 & 0 \\ 0 & 0 & 1200 \end{bmatrix}$$

$$E = 210\ \text{GPa}\ ;\quad \nu = 0,3\ ,\quad \sigma_{e} = 400\ \text{MPa}$$

**\* Déterminons les composantes de la matrice représentant le tenseur des contraintes pour la déformat° indiquée, en faisant :**

**① D'un <u>état plan de déformation</u> : $\varepsilon_{zz} = 0$**

$$\overline{\overline{\sigma}} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right)\overline{\overline{I}} + 2\mu\,\overline{\overline{\varepsilon}}$$

$$\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = 10^{-6}\left( \varepsilon_{xx} - 400 + 1200 \right) = 10^{-6}\left( \varepsilon_{xx} + 800 \right)$$

$$\sigma_{xx} = \frac{E}{\left( 1 - \nu^{2} \right)}\left\lbrack \varepsilon_{xx} + \nu\,\varepsilon_{yy} \right\rbrack$$

$$\sigma_{yy} = \frac{E}{\left( 1 - \nu^{2} \right)}\left\lbrack \varepsilon_{yy} + \nu\,\varepsilon_{xx} \right\rbrack\quad \text{et}\quad \sigma_{zz} = 0$$

$$\left. \begin{matrix} \varepsilon_{xx} = \varepsilon_{xx} = \text{inconnu} \\ \varepsilon_{yy} = -400 \cdot 10^{-6} \\ \varepsilon_{zz} = 1200 \cdot 10^{-6} \end{matrix} \right| \quad \text{Posons}\ \varepsilon_{xx} = a \cdot 10^{-6}$$

*— page 25 —*

Posons $\varepsilon_{xx} = 0$ :

$$\sigma_{xx} = \frac{E}{\left( 1 - \nu^{2} \right)}\left( \nu\,\varepsilon_{yy} \right) = \frac{210000}{\left( 1 - (0,3)^{2} \right)}\left( 0,3 \times \left( -400 \cdot 10^{-6} \right) \right)$$

$$\Rightarrow \boxed{\sigma_{xx} = -27,7\ \text{MPa}}$$

$$\sigma_{yy} = \frac{E}{\left( 1 - \nu^{2} \right)}\left( \varepsilon_{yy} \right) = \frac{210000}{\left( 1 - (0,3)^{2} \right)}\left( -400 \cdot 10^{-6} \right) = -92,3$$

$$\boxed{\sigma_{yy} = -92,3\ \text{MPa}}\quad \text{et}\quad \boxed{\sigma_{zz} = 0\ \text{MPa}}$$

$$\boxed{\sigma_{xz} = \sigma_{yz} = \sigma_{xy} = 0}\qquad \text{d'où}\quad \boxed{\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -27,7 & 0 & 0 \\ 0 & -92,3 & 0 \\ 0 & 0 & 0 \end{bmatrix}}$$

**② D'un <u>état plan de contrainte</u> : [ Même résultat ]**

## Exercice ⑬ : Critères de limite d'élasticité

$E = 210\ \text{GPa}$ ; $\nu = 0,3$ ; $\sigma_{e} = 400\ \text{MPa}$

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -50 & 15 & 0 \\ 15 & 0 & -12 \\ 0 & -12 & -50 \end{bmatrix}$$

**① Les composantes de la matrice représentant le tenseur des déformations pour cette contrainte**

$$\overline{\overline{\sigma}} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right)\overline{\overline{I}} + 2\mu\,\overline{\overline{\varepsilon}}$$

$$\Rightarrow \overline{\overline{\varepsilon}} = \frac{(1 + \nu)}{E} \cdot \overline{\overline{\sigma}} - \frac{\nu}{E}\,\mathrm{tr}\left( \overline{\overline{\sigma}} \right) \cdot \overline{\overline{I}}$$

$$\varepsilon_{xx} = \frac{1}{E}\left\lbrack \sigma_{xx} - \nu\left( \sigma_{yy} + \sigma_{zz} \right) \right\rbrack$$

$$\varepsilon_{yy} = \frac{1}{E}\left\lbrack \sigma_{yy} - \nu\left( \sigma_{xx} + \sigma_{zz} \right) \right\rbrack$$

$$\varepsilon_{zz} = \frac{1}{E}\left\lbrack \sigma_{zz} - \nu\left( \sigma_{xx} + \sigma_{yy} \right) \right\rbrack$$

$$\left| \begin{matrix} \varepsilon_{xy} = \dfrac{\sigma_{xy}}{2\mu} \\[2mm] \varepsilon_{xz} = \dfrac{\sigma_{xz}}{2\mu} \\[2mm] \varepsilon_{yz} = \dfrac{\sigma_{yz}}{2\mu} \\[2mm] \mu = \dfrac{E}{2(1 + \nu)} \end{matrix} \right.$$

*— page 26 —*

**[ Le reste de ⑬ est simple. ]**

## Exercice ⑭ : Critère de Von Mises

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} 0 & 0 & a \\ 0 & -a & 0 \\ a & 0 & 0 \end{bmatrix}$$

$$\sigma_{e} = 20\ \text{MPa}$$

**① Les composantes du tenseur des contraintes de Cauchy :**

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} 0 & 0 & a \\ 0 & -a & 0 \\ a & 0 & 0 \end{bmatrix}$$

**② Vérifions si le critère de Von Mises est satisfait ou non :** $E = 25\ \text{GPa}$, $\nu = 0,3$ et $a = 0,001$

$$\sigma_{eq} = \sqrt{\frac{1}{2}\left( \sigma_{I} - \sigma_{II} \right)^{2} + \left( \sigma_{II} - \sigma_{III} \right)^{2} + \left( \sigma_{III} - \sigma_{I} \right)^{2}}$$

~~Ainsi ao~~ Après avoir les contraintes principales $\sigma_{I}$, $\sigma_{II}$ et $\sigma_{III}$.

<u>Par exemple :</u> $\sigma_{eq} = 0,001\ \text{MPa} < \sigma_{e} = 20\ \text{MPa}$ d'où le ~~coube~~ critère de Von Mises est satisfait, le matériau reste élastique.

## Exercice ⑮ : Tenseur des contraintes

$E = 210\ \text{GPa} = 210 \cdot 10^{9}\ \text{Pa}$ ; $\nu = 0,3$

$$u_{1} = \beta\,x_{1} + \gamma\,x_{2}\quad (\text{en mm})$$

$$u_{2} = -\gamma\,x_{1} + \beta\,x_{2}$$

**① Les composantes du tenseur des déformations infinitésimales :** $K_{ij} = \partial u_{i}/\partial x_{j}$

$$\left\lbrack \overline{\overline{K}} \right\rbrack = \begin{bmatrix} \dfrac{\partial u_{1}}{\partial x_{1}} & \dfrac{\partial u_{1}}{\partial x_{2}} \\[3mm] \dfrac{\partial u_{2}}{\partial x_{1}} & \dfrac{\partial u_{2}}{\partial x_{2}} \end{bmatrix} = \begin{bmatrix} \beta & \gamma \\ -\gamma & \beta \end{bmatrix}$$

*— page 27 —*

$$\left\lbrack \overline{\overline{K}} \right\rbrack = \begin{bmatrix} \beta & \gamma \\ -\gamma & \beta \end{bmatrix} \Rightarrow \left\lbrack \overline{\overline{K}}^{t} \right\rbrack = \begin{bmatrix} \beta & -\gamma \\ \gamma & \beta \end{bmatrix}$$

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \frac{1}{2}\left( \begin{bmatrix} \beta & \gamma \\ -\gamma & \beta \end{bmatrix} + \begin{bmatrix} \beta & -\gamma \\ \gamma & \beta \end{bmatrix} \right) = \frac{1}{2}\begin{bmatrix} 2\beta & 0 \\ 0 & 2\beta \end{bmatrix}$$

$$\Rightarrow \boxed{\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} \beta & 0 \\ 0 & \beta \end{bmatrix}}$$

**② Le tenseur des contraintes au point $M$ :** $\beta = 0,02$ et $\gamma = 0,001$ :

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} \beta & 0 \\ 0 & \beta \end{bmatrix} \Rightarrow \left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} 0,02 & 0 \\ 0 & 0,02 \end{bmatrix}$$

Puisque le matériau est isotrope on aura :

$$\overline{\overline{\sigma}} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right)\overline{\overline{I}} + 2\mu\,\overline{\overline{\varepsilon}}$$

$$\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = \varepsilon_{11} + \varepsilon_{22} = \beta + \beta = 2\beta$$

$$\lambda = \frac{E\nu}{(1 + \nu)(1 - 2\nu)} = \frac{210 \cdot 10^{9} \times 0,3}{(1 + 0,3)(1 - 2 \times 0,3)}$$

$$\Rightarrow \lambda = 121,15\ \text{GPa}$$

$$\mu = \frac{E}{2(1 + \nu)} = \frac{210 \cdot 10^{9}}{2(1 + 0,3)} = 80,77\ \text{GPa}$$

$$\sigma_{11} = \sigma_{22} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) + 2\mu\,\varepsilon_{11}$$

$$= 121,15 \times 2\,(0,02) + 2 \times 80,77 \times (0,02)$$

$$= 8,08\ \text{MPa}$$

$$\text{alors}\quad \boxed{\begin{matrix} \sigma_{11} = 8,08\ \text{MPa} \\ \sigma_{22} = 8,08\ \text{MPa} \\ \sigma_{12} = 0\ \text{MPa} \end{matrix}}$$

*— page 28 —*

**③ <u>Explication</u> :** La sollicitation au point $M$ correspond à un état de déformation plane car $\varepsilon_{33} = 0$ mais $\sigma_{33} \neq 0$ qui dépend de la trace des déformations.

![](figs/fig-p28-nb.png)

## Exo ⑯ : Compression d'un bloc

![](figs/fig-p28-bloc.png)

**① Identifions les conditions aux limites sur les quatre bords du bloc :**

*— page 29 —*

$$\begin{matrix} \widehat{\text{Côté}}\ ① : \sigma_{yy} = -f \\ \widehat{\text{Côté}}\ ② : u_{y} = 0\ \text{et}\ \sigma_{xy} = 0 \end{matrix}\ \left| \ \begin{matrix} \widehat{\text{Côté}}\ ③ : \sigma_{xx} = 0\ ;\ \sigma_{xy} = 0\ (\text{pts libres}) \\ \widehat{\text{Côté}}\ ④ : \sigma_{xx} = 0\ \text{et}\ \sigma_{xy} = 0\ (\text{pts libres}) \end{matrix} \right.$$

**② Le schéma de l'état déformé du bloc est :**

![](figs/fig-p29-deforme.png)

**③ Les composantes du tenseur des déformat° en fonction de $f$, $E$ et $\nu$ :**

$$\left\lbrack \overline{\sigma} \right\rbrack = \begin{bmatrix} 0 & 0 & 0 \\ 0 & -f & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

$$\sigma = E \cdot \varepsilon$$

$$\varepsilon_{yy} = \frac{\sigma_{yy}}{E} = \frac{-f}{E} \Rightarrow \varepsilon_{yy} = -f/E\quad \text{et}\quad \varepsilon_{xy} = 0$$

$$\varepsilon_{xx} = -\nu \cdot \varepsilon_{yy} = -\nu\left( -f/E \right) = \nu f/E \Rightarrow \varepsilon_{xx} = \nu f/E$$

$$\text{alors}\quad \boxed{\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} \nu f/E & 0 \\ 0 & -f/E \end{bmatrix}}$$

**④ Déduisons les variat° de longueur suivant les axes $x$ et $y$ :**

$$\varepsilon_{xx} = \frac{\Delta l_{x}}{l} \Rightarrow \Delta l_{x} = l \cdot \varepsilon_{xx} = \frac{l \cdot \nu f}{E}$$

$$\varepsilon_{yy} = \frac{\Delta l_{y}}{h} \Rightarrow \Delta l_{y} = h \cdot \varepsilon_{yy} = \frac{-hf}{E}$$

$$\text{alors}\quad \boxed{\begin{matrix} \Delta l_{x} = l\,\nu f/E \\ \Delta l_{y} = -h\,f/E \end{matrix}}$$

**KGB**

*— page 30 —*

# Théorie d'élasticité  S④  L2  Par KGB

## Exercice ⑰ : Mur soumis à un effort de Compression

$$\overrightarrow{F} = -f\,l\,t\,\overrightarrow{y}\ ;\quad E = 20\ \text{GPa}\ ;\quad \nu = 0,3\ ;\quad l = 3\ \text{m}$$

$$h = 1,5\ \text{m}\quad \text{et}\quad t = 15\ \text{cm}$$

![](figs/fig-p30-mur.png)

$$f = 6,7\ \text{kN/m}^{2}$$

**① Identifions les conditions aux limites sur les six (6) côtés du mur :**

- Face supérieure : $\sigma_{yy} = -f$
- Face inférieure : $u_{y} = 0$ (sol rigide)
- Face avant / arrière (en $z$) : $\sigma_{iz} = 0$
- Face gauche / droite (en $x$) : $u_{x} = 0$ (bloqué)

**② Déterminons le tenseur des déformations dans le mur :**

*— page 31 —*

$$\varepsilon_{yy} = \frac{\sigma_{yy}}{E} = -f/E$$

$$\nu = \frac{-\varepsilon_{xx}}{\varepsilon_{yy}} \Rightarrow \varepsilon_{xx} = -\nu \cdot \varepsilon_{yy} = -\nu\left( -\frac{f}{E} \right) = \frac{\nu f}{E}$$

$$\varepsilon_{zz} = -\nu \cdot \varepsilon_{yy} = \nu f/E\quad \text{alors}\quad \boxed{\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} \dfrac{\nu f}{E} & 0 & 0 \\[2mm] 0 & -f/E & 0 \\[2mm] 0 & 0 & \nu f/E \end{bmatrix}}$$

**③ Les forces nécessaires pour assurer le blocage du déplacement horizontale longitudinal sur les côtés gauche et droite du mur :**

$$\sigma_{xx} = E \cdot \varepsilon_{xx} = E\left( \frac{\nu f}{E} \right) = \nu f$$

$$\Rightarrow \boxed{F\,(\text{blocage}) = \sigma_{xx} = \nu f}$$

## Exo ⑱ : Contrainte équivalente de Von Mises

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} 2\varepsilon & a\varepsilon & 0 \\ a\varepsilon & -\varepsilon & 0 \\ 0 & 0 & -\varepsilon \end{bmatrix}$$

**① La variation de volume du matériau est :**

$$\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = \varepsilon_{xx} + \varepsilon_{yy} + \varepsilon_{zz} = 2\varepsilon - \varepsilon - \varepsilon = 0 \Rightarrow \mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = 0$$

Puisque $\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = 0$ alors il n'y a pas de variation de volume.

**② Les déformations principales en fonct° de $a$ et $\varepsilon$ :**

$$\det\left( \overline{\overline{\varepsilon}} - \lambda\,\overline{\overline{I}} \right) = 0 \Rightarrow \begin{vmatrix} 2\varepsilon - \lambda & a\varepsilon & 0 \\ a\varepsilon & -\varepsilon - \lambda & 0 \\ 0 & 0 & -\varepsilon - \lambda \end{vmatrix} = 0$$

$$\Rightarrow (-\varepsilon - \lambda)^{2}(2\varepsilon - \lambda) - a^{2}\varepsilon^{2}(-\varepsilon - \lambda) = 0$$

$$\Rightarrow \left\lbrack -a^{2}\varepsilon^{2} + (2\varepsilon - \lambda)(-\varepsilon - \lambda) \right\rbrack(-\varepsilon - \lambda) = 0$$

*— page 32 —*

$$\Rightarrow (-\varepsilon - \lambda)\left( -a^{2}\varepsilon^{2} - 2\varepsilon^{2} - 2\varepsilon\lambda + \varepsilon\lambda + \lambda^{2} \right) = 0$$

$$\Rightarrow (-\varepsilon - \lambda)\left( \lambda^{2} - \varepsilon\lambda - a^{2}\varepsilon^{2} - 2\varepsilon^{2} \right) = 0$$

$$\left\{ \begin{matrix} -\varepsilon - \lambda = 0 \Rightarrow \lambda = -\varepsilon \\ \lambda^{2} - \varepsilon\lambda - a^{2}\varepsilon^{2} - 2\varepsilon^{2} = 0 \Rightarrow \Delta = \varepsilon^{2} - 4\left( -a^{2}\varepsilon^{2} - 2\varepsilon^{2} \right) \end{matrix} \right.$$

$$\Delta = \varepsilon^{2} + 4a^{2}\varepsilon^{2} + 8\varepsilon^{2}$$

$$D = 9\varepsilon^{2} + 4a^{2}\varepsilon^{2}$$

$$\lambda_{1} = \frac{\varepsilon - \sqrt{9\varepsilon^{2} + 4a^{2}\varepsilon^{2}}}{2}\quad \text{et}\quad \lambda_{2} = \frac{\varepsilon + \sqrt{9\varepsilon^{2} + 4a^{2}\varepsilon^{2}}}{2}$$

d'où les déformations principales sont :

$$\varepsilon_{I} = -\varepsilon$$

$$\varepsilon_{II} = \frac{\varepsilon}{2}\left( 1 - \sqrt{9 + 4a^{2}} \right)\quad \text{et}\quad \varepsilon_{III} = \frac{\varepsilon}{2}\left( 1 + \sqrt{9 + 4a^{2}} \right)$$

**③ Les composantes du tenseur des contraintes de Cauchy en $f\left( a,\mu\ \text{et}\ \varepsilon \right)$ :**

$$\overline{\overline{\sigma}} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right)\overline{\overline{I}} + 2\mu\,\overline{\overline{\varepsilon}}$$

or $\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right) = 0$ donc $\overline{\overline{\sigma}} = 2\mu\,\overline{\overline{\varepsilon}}$

$$\Rightarrow \boxed{\left\lbrack \overline{\overline{\sigma}} \right\rbrack = 2\mu\begin{bmatrix} 2\varepsilon & a\varepsilon & 0 \\ a\varepsilon & -\varepsilon & 0 \\ 0 & 0 & -\varepsilon \end{bmatrix}}$$

**④ La contrainte équivalente de Mises Von en fonction de $a$, $\mu$ et $\varepsilon$ :**

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = 2\mu\begin{bmatrix} 2\varepsilon & a\varepsilon & 0 \\ a\varepsilon & -\varepsilon & 0 \\ 0 & 0 & -\varepsilon \end{bmatrix} = \begin{bmatrix} 4\mu\varepsilon & 2\mu a\varepsilon & 0 \\ 2\mu a\varepsilon & -2\mu\varepsilon & 0 \\ 0 & 0 & -2\mu\varepsilon \end{bmatrix}$$

*— page 33 —*

$$\det\left( \overline{\overline{\sigma}} - \lambda\,\overline{\overline{I}} \right) = 0 \Rightarrow \begin{vmatrix} 4\mu\varepsilon - \lambda & 2\mu a\varepsilon & 0 \\ 2\mu a\varepsilon & -2\mu\varepsilon - \lambda & 0 \\ 0 & 0 & -2\mu\varepsilon - \lambda \end{vmatrix} = 0$$

$$\Rightarrow (-2\mu\varepsilon - \lambda)^{2}(4\mu\varepsilon - \lambda) - 4\mu^{2}a^{2}\varepsilon^{2}(-2\mu\varepsilon - \lambda) = 0$$

$$\Rightarrow (-2\mu\varepsilon - \lambda)\left\lbrack -4\mu^{2}a^{2}\varepsilon^{2} - 8\mu^{2}\varepsilon^{2} + 2\mu\varepsilon\lambda - 4\mu\varepsilon\lambda + \lambda^{2} \right\rbrack = 0$$

$$\Rightarrow (-2\mu\varepsilon - \lambda)\left( \lambda^{2} - 2\mu\varepsilon\lambda - 4\mu^{2}a^{2}\varepsilon^{2} - 8\mu^{2}\varepsilon^{2} \right) = 0$$

$$\left\{ \begin{matrix} -2\mu\varepsilon - \lambda = 0 \Rightarrow \boxed{\lambda = -2\mu\varepsilon} \\ \lambda^{2} - 2\mu\varepsilon\lambda - 4a^{2}\mu^{2}\varepsilon^{2} - 8\mu^{2}\varepsilon^{2} = 0 \end{matrix} \right.$$

$$\Delta = 4\mu^{2}\varepsilon^{2} - 4\left( -4a^{2}\mu^{2}\varepsilon^{2} - 8\mu^{2}\varepsilon^{2} \right)$$

$$= 4\mu^{2}\varepsilon^{2} + 16a^{2}\mu^{2}\varepsilon^{2} + 32\mu^{2}\varepsilon^{2}$$

$$\Delta = 36\mu^{2}\varepsilon^{2} + 16a^{2}\mu^{2}\varepsilon^{2}$$

$$\sqrt{\Delta} = \mu\varepsilon\sqrt{36 + 16a^{2}} = \mu\varepsilon\sqrt{4 \times 9 + 4 \times 4a^{2}}$$

$$\text{donc}\quad \sqrt{\Delta} = 2\mu\varepsilon\sqrt{9 + 4a^{2}}$$

$$\lambda_{1} = \frac{2\mu\varepsilon - 2\varepsilon\mu\sqrt{9 + 4a^{2}}}{2} = \mu\varepsilon - \mu\varepsilon\sqrt{9 + 4a^{2}}$$

$$\text{et}\quad \lambda_{2} = \mu\varepsilon + \mu\varepsilon\sqrt{9 + 4a^{2}}$$

les contraintes principales sont :

$$\sigma_{I} = -2\mu\varepsilon$$

$$\sigma_{II} = \mu\varepsilon\left( 1 - \sqrt{9 + 4a^{2}} \right)$$

$$\sigma_{III} = \mu\varepsilon\left( 1 + \sqrt{9 + 4a^{2}} \right)$$

*— page 34 —*

$$\sigma_{eq} = \sqrt{\frac{1}{2}\left\lbrack \left( \sigma_{I} - \sigma_{II} \right)^{2} + \left( \sigma_{II} - \sigma_{III} \right)^{2} + \left( \sigma_{III} - \sigma_{I} \right)^{2} \right\rbrack}$$

$$\left( \sigma_{I} - \sigma_{II} \right)^{2} = \left( -2\mu\varepsilon - \mu\varepsilon + \mu\varepsilon\sqrt{9 + 4a^{2}} \right)^{2} = \left( -3\mu\varepsilon + \mu\varepsilon\sqrt{9 + 4a^{2}} \right)^{2}$$

$$= 9\mu^{2}\varepsilon^{2} - 6\mu^{2}\varepsilon^{2}\sqrt{9 + 4a^{2}} + \mu^{2}\varepsilon^{2}\left( 9 + 4a^{2} \right)$$

$$= 9\mu^{2}\varepsilon^{2} + 9\mu^{2}\varepsilon^{2} + 4a^{2}\mu^{2}\varepsilon^{2} - 6\mu^{2}\varepsilon^{2}\sqrt{9 + 4a^{2}}$$

$$\Rightarrow \left( \sigma_{I} - \sigma_{II} \right)^{2} = 18\mu^{2}\varepsilon^{2} + 4a^{2}\mu^{2}\varepsilon^{2} - 6\mu^{2}\varepsilon^{2}\sqrt{9 + 4a^{2}}$$

$$\left( \sigma_{II} - \sigma_{III} \right)^{2} = \left( \mu\varepsilon - \mu\varepsilon\sqrt{9 + 4a^{2}} - \mu\varepsilon - \mu\varepsilon\sqrt{9 + 4a^{2}} \right)^{2}$$

$$= \left( -2\mu\varepsilon\sqrt{9 + 4a^{2}} \right)^{2} = 4\mu^{2}\varepsilon^{2}\left( 9 + 4a^{2} \right)$$

$$\Rightarrow \left( \sigma_{II} - \sigma_{III} \right)^{2} = 36\mu^{2}\varepsilon^{2} + 16a^{2}\mu^{2}\varepsilon^{2}$$

$$\left( \sigma_{III} - \sigma_{I} \right)^{2} = \left( \mu\varepsilon + \mu\varepsilon\sqrt{9 + 4a^{2}} + 2\mu\varepsilon \right)^{2} = \left( 3\mu\varepsilon + \mu\varepsilon\sqrt{9 + 4a^{2}} \right)^{2}$$

$$= 9\mu^{2}\varepsilon^{2} + 6\mu^{2}\varepsilon^{2}\sqrt{9 + 4a^{2}} + \mu^{2}\varepsilon^{2}\left( 9 + 4a^{2} \right)$$

$$\Rightarrow \left( \sigma_{III} - \sigma_{I} \right)^{2} = 18\mu^{2}\varepsilon^{2} + 4a^{2}\mu^{2}\varepsilon^{2} + 6\mu^{2}\varepsilon^{2}\sqrt{9 + 4a^{2}}$$

$$\text{donc}\quad \left( \sigma_{I} - \sigma_{II} \right)^{2} + \left( \sigma_{III} - \sigma_{I} \right)^{2} = 36\mu^{2}\varepsilon^{2} + 8a^{2}\mu^{2}\varepsilon^{2}$$

$$\left( \sigma_{I} - \sigma_{II} \right)^{2} + \left( \sigma_{III} - \sigma_{I} \right)^{2} + \left( \sigma_{II} - \sigma_{III} \right)^{2} = \mu^{2}\varepsilon^{2}\left( 36 + 8a^{2} + 36 + 16a^{2} \right)$$

$$= \mu^{2}\varepsilon^{2}\left( 72 + 24a^{2} \right)$$

$$\Rightarrow \sigma_{eq} = \sqrt{\frac{1}{2}\left\lbrack \mu^{2}\varepsilon^{2}\left( 72 + 24a^{2} \right) \right\rbrack}$$

*— page 35 —*

$$\sigma_{eq} = \sqrt{\mu^{2}\varepsilon^{2}\left( 36 + 12a^{2} \right)} = \mu\varepsilon\sqrt{36 + 12a^{2}}$$

$$= \mu\varepsilon\sqrt{4 \times 9 + 4 \times 3a^{2}} = \mu\varepsilon\sqrt{4\left( 9 + 3a^{2} \right)}$$

$$\text{alors}\quad \sigma_{eq\,V.M} = 2\mu\varepsilon\sqrt{9 + 3a^{2}}$$

$$\sigma_{eq} = 2\mu\varepsilon\sqrt{3 \times 3 + 3a^{2}} = 2\mu\varepsilon\sqrt{3\left( 3 + a^{2} \right)}$$

$$\text{d'où}\quad \boxed{\sigma_{eq\,V.M} = 18\,\mu\varepsilon\sqrt{3 + a^{2}}}$$

## Exo ⑲ : Partie ① : Relation Contrainte – Déformat°

$E = 210\ \text{GPa}$

$\nu = 0,3$

$\sigma_{e} = 400\ \text{MPa}$

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = 10^{-6}\begin{bmatrix} \varepsilon_{xx} & 0 & 0 \\ 0 & -400 & 0 \\ 0 & 0 & 1200 \end{bmatrix}$$

**\* Les composantes de la matrice représentant le tenseur des contraintes :**

**ⓐ <u>D'un état plan de déformation</u> :**

$$\sigma_{xx} = \frac{E}{\left( 1 - \nu^{2} \right)}\left\lbrack \varepsilon_{xx} + \nu\,\varepsilon_{yy} \right\rbrack$$

$$\sigma_{yy} = \frac{E}{\left( 1 - \nu^{2} \right)}\left\lbrack \varepsilon_{yy} + \nu\,\varepsilon_{xx} \right\rbrack$$

$$\sigma_{xy} = 2\mu \cdot \varepsilon_{xy} = \frac{2E}{2(1 + \nu)}\,\varepsilon_{xy} = \frac{E\,\varepsilon_{xy}}{(1 + \nu)}$$

$$\sigma_{zz} = \frac{\nu E}{\left( 1 - \nu^{2} \right)}\left\lbrack \varepsilon_{xx} + \varepsilon_{yy} \right\rbrack$$

**ⓑ <u>D'un état plan de contrainte</u> :** $\sigma_{zz} = 0$ mais $\varepsilon_{zz} \neq 0$

*— page 36 —*

$$\varepsilon_{xx} = \frac{1}{E}\left( \sigma_{xx} - \nu\,\sigma_{yy} \right)$$

$$\varepsilon_{yy} = \frac{1}{E}\left( \sigma_{yy} - \nu\,\sigma_{xx} \right)\quad \text{et}\quad \varepsilon_{zz} = \frac{-\nu}{E}\left( \sigma_{xx} + \sigma_{yy} \right)$$

**( Supposons )**

**ⓒ** $\sigma_{eq}(\text{Von Mises}) = 65\ \text{MPa} < \sigma_{e} = 400\ \text{MPa} \Rightarrow$ ~~donc~~ pas de dépassement de la limite d'élasticité.

$\sigma_{eq}(\text{Von Mises}) = 500\ \text{MPa} > \sigma_{e} = 400\ \text{MPa}$ donc le matériau dépasse sa limite d'élasticité.

**Partie ② : [ Corriger en TD : ]**

## Exercice ⑳ : $\sigma_{e} = 200\ \text{MPa}$

<u>Détermination du tenseur des contraintes, des déformations et du critère de rupture (Von Mises) :</u>

$$\begin{matrix} \sigma_{xx} = 150\ \text{MPa} \\ \sigma_{yy} = 50\ \text{MPa} \\ \sigma_{zz} = 0 \end{matrix}\ \left| \ \begin{matrix} \sigma_{xy} = 30\ \text{MPa} \\ \sigma_{xz} = 20\ \text{MPa} \\ \sigma_{yz} = 0 \end{matrix}\ \right| \ \begin{matrix} E = 210\ \text{GPa} \\ = 210 \cdot 10^{9}\ \text{Pa} \\ \nu = 0,3 \end{matrix}$$

**① Vérifions que le tenseur est symétrique :**

$$\left. \begin{matrix} \sigma_{xy} = \sigma_{yx} = 30\ \text{MPa} \\ \sigma_{xz} = \sigma_{zx} = 20\ \text{MPa} \\ \sigma_{yz} = \sigma_{zy} = 0\ \text{MPa} \end{matrix} \right\} \Rightarrow \text{le tenseur est donc symétrique.}$$

**② Calculons les déformations $\varepsilon_{xx}$, $\varepsilon_{yy}$ et $\varepsilon_{zz}$** (utiliser la loi de Hooke généralisée)

$$\varepsilon_{xx} = \frac{1}{E}\left\lbrack \sigma_{xx} - \nu\left( \sigma_{yy} + \sigma_{zz} \right) \right\rbrack = \frac{1}{210 \cdot 10^{9}}\left\lbrack 150 \cdot 10^{6} - 0,3\left( 50 \cdot 10^{6} \right) \right\rbrack$$

$$\Rightarrow \boxed{\varepsilon_{xx} = 0,0006428571}$$

*— page 37 —*

$$\varepsilon_{yy} = \frac{1}{E}\left\lbrack \sigma_{yy} - \nu\left( \sigma_{xx} + \sigma_{zz} \right) \right\rbrack = \frac{1}{210 \cdot 10^{9}}\left\lbrack 50 \cdot 10^{6} - 0,3 \times 150 \cdot 10^{6} \right\rbrack$$

$$\Rightarrow \boxed{\varepsilon_{yy} = 2,38 \cdot 10^{-5}} = 0,0000238$$

$$\varepsilon_{zz} = \frac{1}{E}\left\lbrack \sigma_{zz} - \nu\left( \sigma_{xx} + \sigma_{yy} \right) \right\rbrack = \frac{1}{210 \cdot 10^{9}}\left\lbrack -0,3\left( 150 \cdot 10^{6} + 50 \cdot 10^{6} \right) \right\rbrack$$

$$\Rightarrow \boxed{\varepsilon_{zz} = -0,000285714}$$

**③ Le tenseur des déformations infinitésimales est :**

$$\varepsilon_{xy} = \frac{\sigma_{xy}}{2\mu}\quad \text{avec}\quad \mu = G = \frac{E}{2(1 + \nu)}$$

$$\mu = G = \frac{E}{2(1 + \nu)} = \frac{210 \cdot 10^{9}}{2(1 + 0,3)} = 80,76\ \text{GPa}$$

$$\varepsilon_{xy} = \frac{30 \cdot 10^{6}}{2 \times 80,76 \cdot 10^{9}} \Rightarrow \boxed{\varepsilon_{xy} = 0,000185735}$$

$$\varepsilon_{xz} = \frac{\sigma_{xz}}{2\mu} = \frac{20 \cdot 10^{6}}{2 \times 80,76 \cdot 10^{9}} \Rightarrow \boxed{\varepsilon_{xz} = 0,000123823}$$

$$\varepsilon_{yz} = \frac{\sigma_{yz}}{2\mu} = 0 \Rightarrow \boxed{\varepsilon_{yz} = 0}$$

$$\text{d'où}\quad \left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} 0,000642 & 0,000185 & 0,000123 \\ 0,000185 & 0,0000238 & 0 \\ 0,000123 & 0 & -0,000285 \end{bmatrix}$$

**④ Calculons la contrainte équivalente de Von Mises :**

**\* <u>Il y a deux méthodes.</u>**

*— page 38 —*

**\* <u>méthode ①</u> :**

$$\sigma_{eq} = \sqrt{\frac{1}{2}\left\lbrack \left( \sigma_{xx} - \sigma_{yy} \right)^{2} + \left( \sigma_{yy} - \sigma_{zz} \right)^{2} + \left( \sigma_{zz} - \sigma_{xx} \right)^{2} + 3\left( \sigma_{xy}^{2} + \sigma_{xz}^{2} + \sigma_{yz}^{2} \right) \right\rbrack}$$

$$\Rightarrow \boxed{\sigma_{eq} \simeq 138\ \text{MPa}}$$

**\* <u>méthode ②</u> :**

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} 150 & 30 & 20 \\ 30 & 50 & 0 \\ 20 & 0 & 0 \end{bmatrix}\qquad \det\left( \overline{\overline{\sigma}} - \lambda\,\overline{\overline{I}} \right) = 0$$

$$\left. \begin{matrix} \sigma_{I} = ? \\ \sigma_{II} = ? \\ \sigma_{III} = ? \end{matrix} \right\} \ \text{contraintes principales des contraintes}$$

$$\sigma_{eq} = \sqrt{\frac{1}{2}\left\lbrack \left( \sigma_{I} - \sigma_{II} \right)^{2} + \left( \sigma_{II} - \sigma_{III} \right)^{2} + \left( \sigma_{III} - \sigma_{I} \right)^{2} \right\rbrack}$$

$$\boxed{\sigma_{eq} \simeq 138\ \text{MPa}}$$

<u>Rmq</u> : La méthode ② est recommandée.

**⑤ <u>Conclusion</u> :** $\sigma_{eq} = 138\ \text{MPa} < \sigma_{e} = 200\ \text{MPa}$, le matériau reste dans son domaine élastique.

**⑥ Les directions principales des contraintes :**

$$\left( \overline{\overline{\sigma}} - \lambda\,\overline{\overline{I}} \right)\overrightarrow{u} = \overrightarrow{0}\quad \text{avec}\quad \overrightarrow{u}\left( u_{1},u_{2},u_{3} \right)$$

*— page 39 —*

$$\text{et}\quad \overrightarrow{u}' = \frac{\overrightarrow{u}}{\left\| \overrightarrow{u} \right\|}\quad \text{pour chaque contrainte } \lambda$$

$$\text{On aura}\quad \boxed{\overrightarrow{u}'\,;\ \overrightarrow{u}''\ \text{et}\ \overrightarrow{u}'''}\quad \longleftarrow \text{direct° principales}$$

<u>Vérificat°</u> : $\overrightarrow{u}' \cdot \overrightarrow{u}'' = 0$ ; $\overrightarrow{u}'' \cdot \overrightarrow{u}''' = 0$ et $\overrightarrow{u}' \cdot \overrightarrow{u}''' = 0$

**⑦ Représentons le cercle de Mohr pour le plan $(x,y)$ :**

$$\begin{matrix} \sigma_{I} = ? \\ \sigma_{II} = ? \\ \sigma_{III} = ? \end{matrix}\qquad (\text{question ④})$$

**( Exemple )**

![](figs/fig-p39-mohr.png)

**KGB**

*— page 40 —*

# Théorie d'élasticité (S④)

**\* Qu'est-ce que le matériau élastique ?**

**\* Donner la loi de Hooke généralisée**

$$\varepsilon_{1} = \frac{1}{E}\left\lbrack \sigma_{1} - \nu\left( \sigma_{2} + \sigma_{3} \right) \right\rbrack$$

$$\varepsilon_{2} = \frac{1}{E}\left\lbrack \sigma_{2} - \nu\left( \sigma_{1} + \sigma_{3} \right) \right\rbrack$$

$$\varepsilon_{3} = \frac{1}{E}\left\lbrack \sigma_{3} - \nu\left( \sigma_{1} + \sigma_{2} \right) \right\rbrack$$

$$\sigma_{1} = ?\qquad \sigma_{2} = ?\qquad \sigma_{3} = ?$$

$$\varepsilon_{1} = \frac{1}{E}\left\lbrack \sigma_{1} - \nu\left( \sigma_{2} + \sigma_{3} \right) \right\rbrack = \frac{1}{E}\left\lbrack \sigma_{1} - \nu\sigma_{2} - \nu\sigma_{3} \right\rbrack$$

$$\varepsilon_{2} = \frac{1}{E}\left\lbrack \sigma_{2} - \nu\left( \sigma_{1} + \sigma_{3} \right) \right\rbrack = \frac{1}{E}\left\lbrack \sigma_{2} - \nu\sigma_{1} - \nu\sigma_{3} \right\rbrack$$

$$\varepsilon_{3} = \frac{1}{E}\left\lbrack \sigma_{3} - \nu\left( \sigma_{1} + \sigma_{2} \right) \right\rbrack = \frac{1}{E}\left\lbrack \sigma_{3} - \nu\sigma_{1} - \nu\sigma_{2} \right\rbrack$$

$$\begin{bmatrix} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \end{bmatrix} = \frac{1}{E}\begin{bmatrix} 1 & -\nu & -\nu \\ -\nu & 1 & -\nu \\ -\nu & -\nu & 1 \end{bmatrix}\begin{bmatrix} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \end{bmatrix}$$

$$\Rightarrow E\begin{bmatrix} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \end{bmatrix} = \begin{bmatrix} 1 & -\nu & -\nu \\ -\nu & 1 & -\nu \\ -\nu & -\nu & 1 \end{bmatrix}\begin{bmatrix} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \end{bmatrix}$$

> *[En marge :]* $\boxed{\begin{matrix} Ax = b \\ x = A^{-1}b \end{matrix}}$

*— page 41 —*

$$\text{on aura :}\quad \begin{bmatrix} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \end{bmatrix} = E\begin{bmatrix} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \end{bmatrix} \cdot \begin{bmatrix} 1 & -\nu & -\nu \\ -\nu & 1 & -\nu \\ -\nu & -\nu & 1 \end{bmatrix}^{-1}$$

$$\Rightarrow \begin{bmatrix} \sigma_{1} \\ \sigma_{2} \\ \sigma_{3} \end{bmatrix} = \frac{E}{(1 + \nu)(1 - 2\nu)}\begin{bmatrix} 1 - \nu & \nu & \nu \\ \nu & 1 - \nu & \nu \\ \nu & \nu & 1 - \nu \end{bmatrix}\begin{bmatrix} \varepsilon_{1} \\ \varepsilon_{2} \\ \varepsilon_{3} \end{bmatrix}$$

$$\boxed{\begin{matrix} \sigma_{1} = \dfrac{E}{(1 + \nu)(1 - 2\nu)}\left\lbrack (1 - \nu)\varepsilon_{1} + \nu\,\varepsilon_{2} + \nu\,\varepsilon_{3} \right\rbrack \\[4mm] \sigma_{2} = \dfrac{E}{(1 + \nu)(1 - 2\nu)}\left\lbrack -\nu\,\varepsilon_{1} + (1 - \nu)\varepsilon_{2} + \nu\,\varepsilon_{3} \right\rbrack \\[4mm] \sigma_{3} = \dfrac{E}{(1 + \nu)(1 - 2\nu)}\left\lbrack \nu\,\varepsilon_{1} + \varepsilon_{2} \cdot \nu + (1 - \nu)\varepsilon_{3} \right\rbrack \end{matrix}}$$

## Quelques réponses de cours en Théorie d'élasticité : (S4)

**① Explication du principe de la décomposition polaire d'une transformation :**

Quand un corps se déforme, le mouvement total peut être vu comme deux choses :

*— page 42 —*

- Une rotation (le corps tourne un peu) ;
- Une déformation pure (le corps change de forme sans tourner).

La décomposition polaire permet de séparer ces deux effets. Donc

$$\text{Transformation totale} = \text{Rotation} \times \text{Déformation}$$

**② Explication pour la différence entre le premier et le second tenseurs des contraintes de Piola-Kirchhoff :**

- <u>Premier tenseur</u> : Compare la force actuelle à la forme initiale, direct mais pas toujours symétriques.
- <u>Deuxième tenseur</u> : compare aussi la force actuelle à la forme initiale, plus précis pour énergie, plus pratique pour les calculs mais il est toujours symétriques.

**③ Explicat° de la <u>symétrie matérielle</u> :**

C'est quand un matériau garde les mêmes propriétés (résistance, comportement…) même si on le tourne ou change sa direction.

<u>Exemple</u> : Un cube en acier.

*— page 43 —*

**④ Différence entre le tenseur des contraintes de Cauchy et le premier tenseur des contraintes de Piola-Kirchhoff :**

**– <u>Pour Cauchy</u> :** mesure les contraintes dans la configuration actuelle (après déformation).

**– <u>Premier tenseur de Piola-Kirchhoff</u> :** mesure les contraintes par rapport à la forme initiale (avant déformation).

**⑤ Description de la théorie de l'élasticité des matériaux amorphes et celle des matériaux cristallins :**

**– <u>matériaux amorphes</u> :**

Les mtx amorphes ont une structure désordonnée ; leur comportement élastique est souvent le même dans toutes les directions.

<u>Exemple</u> : le ~~fer~~ Verre.

**– <u>matériaux cristallins</u> :**

Les mtx cristallins ont une structure bien ordonnée, leur réponse élastique peut changer selon la direction.

<u>Exemples</u> : le fer, les métaux.

*— page 44 —*

**⑥ <u>Comparaison d'un matériau</u>** $\left\{ \begin{matrix} \text{fragile} \\ \text{ductile} \end{matrix} \right.$

Un matériau fragile casse vite sans se plier.

<u>Exemples</u> : le Verre, la céramique.

\* Un matériau ductile peut se plier beaucoup avant de casser.

<u>Exemples</u> : le Cuivre, ou l'aluminium.

**⑦ ⓐ La loi de Hooke pour un matériau dépourvu de plan de symétrie :** $\boxed{\sigma = C \cdot \varepsilon}$

Quand un matériau n'a pas de forme régulière, on utilise la loi de Hooke générale.

**ⓑ Le nombre de composantes constituant chacun des tenseurs dans la loi :**

- le tenseur de contrainte a 6 valeurs.
- le tenseur de déformation a aussi 6 valeurs.
- le tenseur de rigidité (qui relie les deux) a 81 valeurs au total, mais souvent 21 seulement sont vraiment différentes.

**⑧ Peut-on définir un seuil de déformat° au-delà duquel la loi d'élasticité linéaire ne peut être appliquée ?**

Oui, ce seuil est appelé la <u>limite élastique</u>. En dessous, le matériau reprend sa forme initiale

*— page 45 —*

(comportement élastique). Au-delà, il se déforme de manière plastique (déformat° permanente), donc la loi d'élasticité linéaire qui suppose un comportement réversible, <u>n'est plus valable</u>.

**⑨ Explication de l'effet Poisson :**

Quand on étire un matériau dans une direction, il rétrécit dans la direct° perpendiculaire. Cet effet est mesuré par le coeff de Poisson $(\nu)$.

**⑩ Que se passe-t-il lorsque la contrainte dans un matériau atteint ou dépasse la limite d'élasticité de celui-ci ?**

Le matériau ne revient plus à sa forme initiale. Il subit une déformation permanente ou <u>plastique</u>, voire se casse s'il continue d'être sollicité.

**⑪ ⓐ Quel est le nombre de paramètres matériaux pour un matériau isotrope ?**

Un matériau isotrope a seulement <u>2 paramètres</u> principaux.

<u>Exemples</u> : $\left\{ \begin{matrix} \text{module de Young } E \\ \text{coeff de Poisson } \nu \end{matrix} \right.$

*— page 46 —*

**ⓑ Donner un ordre de grandeur de ces paramètres pour un matériau de votre choix**

**Acier**

**⑫ Dans un état plan de déformation, les trois (3) éléments diagonaux de la matrice représentant le tenseur des contraintes sont non nuls. Expliquer pourquoi dans ce cas l'état de contrainte n'est pas plan.**

Dans un état de contrainte plan, on considère que la contrainte agit seulement dans un plan (2 dimensions).

Si les trois (3) éléments diagonaux $\left( \sigma_{xx},\ \sigma_{yy}\ \text{et}\ \sigma_{zz} \right)$ sont tous différents de zéro, cela signifie qu'il y a des contraintes dans trois (3) directions, donc l'état n'est pas plan, mais 3D.

**⑬ On dit qu'un matériau a un <u>comportement élastique</u>, quand il reprend sa forme initiale après qu'on ait arrêté de le déformer.**

*— page 47 —*

**⑭ Explication du concept d'isotropie et d'homogénéité d'un matériau :**

<u>Isotropie</u> : les propriétés du matériau sont les mêmes dans toutes les directions.

<u>Homogénéité</u> : les propriétés du matériau sont les mêmes en tout point du matériau.

**⑮ Qu'appelle-t-on une loi de comportement mécanique ?**

C'est une règle qui explique comment un matériau réagit quand on lui applique une force (contrainte).

**⑯ Deux propriétés mécaniques d'un matériau élastique linéaire et leur interprétation :**

- Module de Young $(E)$
- Coefficient de Poisson $(\nu)$

**\* <u>Interprétation</u> :**

- le <u>module de Young</u> $(E)$ mesure la rigidité, c'est-à-dire combien le matériau se déforme peu quand on applique une force.
- le <u>coeff de Poisson</u> $(\nu)$ indique comment le matériau rétrécit ou s'élargit dans une direction perpendiculaire quand on l'étire.

*— page 48 —*

**⑰ Loi de Hooke pour les mtx isotropes :**

$$\boxed{\overline{\overline{\sigma}} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right)\overline{\overline{I}} + 2\mu\,\overline{\overline{\varepsilon}}}$$

où $\lambda$ et $\mu \longrightarrow$ coeff de Lamé

**ⓐ <u>Rappelons les expressions de ces coefficients</u> :**

$$\boxed{\lambda = \frac{E\nu}{(1 + \nu)(1 - 2\nu)}}\quad \text{et}\quad \boxed{\mu = \frac{E}{2(1 + \nu)}}$$

**ⓑ Pourquoi cette loi ne serait pas valable pour les matériaux anisotropes ?**

Cette loi suppose que les propriétés sont les mêmes dans toutes les direct° (isotropes). Pour les mtx anisotropes, les propriétés changent selon la direction, donc cette loi simple ne fonctionne pas.

**⑱ Explication de la différence entre le premier et le second tenseurs des contraintes de Piola-Kirchhoff :**

**<u>Premier tenseur</u> :**

Relie les forces dans la configurat° actuelle aux surfaces de la configurat° initiale.

*— page 49 —*

**<u>Second tenseur</u> :**

Est lié aux forces et surfaces dans la configurat° initiale, mais avec des propriétés plus symétriques et plus faciles à utiliser en calcul.

**⑲**

$$\boxed{\sigma_{ij} = \lambda\,\mathrm{tr}\left( \overline{\overline{\varepsilon}} \right)\delta_{ij} + 2\mu\,\varepsilon_{ij}}$$

**ⓐ <u>Deux (2) matériaux qui obéissent à la loi de Hooke</u> :**

- l'acier
- l'aluminium

**ⓑ <u>L'intérêt d'une loi de comportement mécanique est</u> :**

De prédire comment un matériau va réagir (se déformer, se casser) sous différentes charges ou efforts.

**ⓒ <u>Les hypothèses permettant d'aboutir à cette loi</u> :**

- le matériau est élastique ;
- le matériau est isotrope ;
- le comportement est linéaire ;
- les déformat° sont petites (infinitésimales).

**ⓓ <u>Le premier et le second tenseurs des contraintes de Piola-Kirchhoff peuvent-ils être exprimés de la m̂ façon que le tenseur des contraintes**

*— page 50 —*

**de Cauchy dans la loi de Hooke présentée ?</u>**

Non, car les tenseurs de Piola-Kirchhoff sont définis dans la <u>configuration initiale</u> (avant déformation), ~~t~~tandis que le tenseur de Cauchy est défini dans la <u>configurat° actuelle</u> (après déformation).

Donc, ils ne s'expriment pas de la m̂ façon.

**ⓔ <u>Réécrire la loi de Hooke, en représentation matricielle, en état plan de contrainte et en état plan de déformat°, ds le plan $\left( x_{1},x_{2} \right)$</u>**

$$\sigma = \left\lbrack \sigma_{11},\ \sigma_{22},\ \sigma_{12} \right\rbrack^{T}$$

$$\varepsilon = \left\lbrack \varepsilon_{11},\ \varepsilon_{22},\ 2\varepsilon_{12} \right\rbrack^{T}$$

(la composante de cisaillement est $\times 2$)

$$\begin{vmatrix} C_{11} & C_{12} & 0 \\ C_{12} & C_{11} & 0 \\ 0 & 0 & C_{66} \end{vmatrix}\quad \text{avec}\quad \left\{ \begin{matrix} C_{11} = E/\left( 1 - \nu^{2} \right) \\ C_{12} = E\nu/\left( 1 - \nu^{2} \right) \\ C_{66} = E/2(1 + \nu) \end{matrix} \right.$$

<u>d'où :</u>

$$\begin{matrix} \left\lbrack \sigma_{11} \right\rbrack \\ \left\lbrack \sigma_{22} \right\rbrack \\ \left\lbrack \sigma_{12} \right\rbrack \end{matrix} = \begin{bmatrix} E/\left( 1 - \nu^{2} \right) & E\nu/\left( 1 - \nu^{2} \right) & 0 \\ E\nu/\left( 1 - \nu^{2} \right) & E/\left( 1 - \nu^{2} \right) & 0 \\ 0 & 0 & E/2(1 + \nu) \end{bmatrix}\begin{bmatrix} \varepsilon_{11} \\ \varepsilon_{22} \\ 2\varepsilon_{12} \end{bmatrix}$$

*— page 51 —*

**\* La contrainte équivalente de Von Mises dépend-elle de sigma $(\sigma)$ ?**

$\longrightarrow$ Oui, la contrainte de Von Mises dépend des valeurs de $\sigma$ car elle est calculée à partir des différentes composantes du tenseur des contraintes.

**⑳**

- **\* <u>Isotrope</u> :** mêmes propriétés partout
- **\* <u>Anisotrope</u> :** propriétés variables selon la direction
- **\* <u>Unisotrope</u> :** anisotropie avec directions privilégiées fixes. (ou orthotrope)

<u>Exemples</u> :

$$\underline{\text{Isotrope}} \nearrow\!\!\!\searrow \begin{matrix} \text{acier} \\ \text{aluminium} \end{matrix}\qquad \underline{\text{Anisotrope}} \swarrow\!\!\!\searrow \begin{matrix} \text{bois} \\ \text{fibre de Carbone} \end{matrix}$$

<u>La théorie de l'élasticité</u> : étudie comment un matériau se déforme puis revient à sa forme normale après une force.

<u>Entropie</u> : Niveau de désordre

<u>Élastomère</u> : matériau très élastique

<u>Monomère</u> : Petite unité de base

<u>Mtx cristallins</u> : Mtx dont les atomes sont bien rangés, formant une structure régulière.

<u>Mtx incompressibles</u> : Mtx qui ne changent presque pas de volume sous l'effet d'une pression.

<u>Mtx déformables</u> : Mtx qui peuvent changer de forme sous l'action d'une force.

<u>Mtx indéformables</u> : qui ne changent pas du tout de forme, peu importe la force.

<u>Mtx plastique</u> : garde la forme après la force.

<u>'' élastique</u> : Reprend sa forme après la force.

> **[ <u>Loi de Hooke généralisée</u> : Relie force et déformation. ]**

*— page 52 — (feuille de sujet imprimée)*

*…de Tresca.*

### Exercice 18 : Critère de von Mises (8.0 pts)

La matrice représentant le tenseur des contraintes en un point $M$ d'un matériau ayant un comportement élastique linéaire s'exprime comme suit :

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -65 & 30 & 0 \\ 30 & -60 & 0 \\ 0 & 0 & 60 \end{bmatrix}$$

où les valeurs numériques sont en MPa. Le matériau a une limite d'élasticité $\sigma_{e} = 355.0$ MPa, un module de Young $E = 200.0$ GPa et un coefficient de Poisson $\nu = 0.3$.

1. (2 points) Calculer les valeurs numériques des composantes du tenseur des déformations.
2. (6 points) Déterminer la contrainte équivalente de von Mises et vérifier si la limite d'élasticité du matériau est atteinte ou non.

---

mamadou.toungara@enetp.ml — 13 of 16

*— page 53 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Seconde Session / S4 / 2021-2022 / décembre 2022

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 90 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Exercice 19 : Relation contraintes-déformations (10.0 pts)

La matrice représentant le tenseur des déformations en un point $M$ d'un matériau ayant un comportement élastique linéaire (coefficients de Lamé, $\lambda$ et $\mu$) s'exprime comme suit :

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = a \times \begin{bmatrix} -1.00 & 1.00 & 0.00 \\ 1.00 & 2.00 & 0.00 \\ 0.00 & 0.00 & -1.00 \end{bmatrix}$$

où $a$ est un nombre réel constant.

1. (2 points) Exprimer, en fonction de $a$ et $\mu$, les composantes de la matrice représentant le tenseur des contraintes pour la déformation indiquée.
2. (3 points) Déterminer les contraintes principales, en fonction de $a$ et $\mu$.
3. (3 points) Calculer les contraintes équivalentes de von Mises et de Tresca pour un module de Young $E = 65.0$ GPa, un coefficient de Poisson $\nu = 0.33$ et $a = 10^{-3}$.
4. (2 points) Que pourrait-on faire avec ces contraintes (von Mises et Tresca) ?

### Exercice 20 : Essai de compression (10.0 pts)

La Fig. 6 représente un matériau soumis en compression dans une enceinte à parois indéformables. On se place dans le plan $(x,\ y)$ où le matériau a une hauteur initiale $h_{0}$ et une largeur $b$. La dimension de la profondeur (suivant l'axe $z$) est maintenue constante. Le matériau a un module de Young $E = 25.0$ GPa et un coefficient de Poisson $\nu = 0.33$.

1. (2 points) Le problème posé correspond-il à un état plan de contrainte ou de déformation (justifier la réponse) ?
2. (2 points) Exprimer, en fonction de $h_{0}$ et $h$, les composantes du tenseur des déformations infinitésimales.
3. (3 points) Exprimer et calculer les composantes du tenseur des contraintes de Cauchy, pour $h_{0} = 150.0$ mm et $h = 138.0$ mm.
4. (3 points) Tracer les cercles de Mohr correspondant à l'état de contrainte indiqué et en déduire la contrainte de cisaillement maximale.

![](figs/fig-p53-figure6.png)

<center>FIGURE 6 – Exercice 20</center>

---

mamadou.toungara@enetp.ml — 14 of 16

*— page 54 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Première Session / S4 / 2021-2022 / octobre 2022

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 120 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Questions de Compréhension (4.0 pts)

*Dans les explications, restez concis, clairs et surtout utilisez vos propres termes.*

1. (2 points) Expliquer le principe de la décomposition polaire d'une transformation.
2. (2 points) Expliquer la différence entre le premier et le second tenseurs des contraintes de Piola-Kirchhoff.

### Exercice 17 : Relation Contrainte-Déformation (8.0 pts)

En un point $M$ d'un matériau isotrope, ayant un comportement élastique linéaire (module de Young $E$ et coefficient de Poisson $\nu$), le champ de déplacement (en mm) est le suivant :

$$u_{1} = -\alpha x_{1} + \beta\left( x_{2} - x_{3} \right);\qquad u_{2} = \alpha\left( x_{1} + x_{3} \right) - \beta x_{2};\qquad u_{3} = -\alpha\left( x_{1} + x_{2} \right) - \beta x_{3}$$

où $\alpha$ et $\beta$ sont des réels. Le matériau a une limite d'élasticité $\sigma_{e} = 25.0$ MPa, un module de Young $E = 14.0$ GPa et un coefficient de Poisson $\nu = 0.21$.

1. (1 point) Exprimer les composantes du tenseur des déformations infinitésimales.
2. (2 points) Déterminer les composantes du tenseur des contraintes de Cauchy.
3. (3 points) Montrer qu'afin d'obtenir un état plan de contrainte, la condition suivante devrait être vérifiée :

$$\lambda = 2\mu$$

   où $\lambda$ et $\mu$ sont des coefficients de Lamé.
4. (2 points) Déterminer la valeur maximale de $\alpha$ permettant au matériau de satisfaire le critère de Tresca.

### Exercice 18 : Critère de von Mises (8.0 pts)

La matrice représentant le tenseur des contraintes en un point $M$ d'un matériau ayant un comportement élastique linéaire s'exprime comme suit :

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -65 & 30 & 0 \\ 30 & -60 & 0 \\ 0 & 0 & 60 \end{bmatrix}$$

où les valeurs numériques sont en MPa. Le matériau a une limite d'élasticité $\sigma_{e} = 355.0$ MPa, un module de Young $E = 200.0$ GPa et un coefficient de Poisson $\nu = 0.3$.

1. (2 points) Calculer les valeurs numériques des composantes du tenseur des déformations.
2. (6 points) Déterminer la contrainte équivalente de von Mises et vérifier si la limite d'élasticité du matériau est atteinte ou non.

---

mamadou.toungara@enetp.ml — 13 of 16

*— page 55 — (feuille de sujet imprimée)*

### Exercice 17 : Relation Contrainte-Déformation (8.0 pts)

En un point $M$ d'un matériau isotrope, ayant un comportement élastique linéaire (module de Young $E$ et coefficient de Poisson $\nu$), le champ de déplacement (en mm) est le suivant :

$$u_{1} = -\alpha x_{1} + \beta\left( x_{2} - x_{3} \right);\qquad u_{2} = \alpha\left( x_{1} + x_{3} \right) - \beta x_{2};\qquad u_{3} = -\alpha\left( x_{1} + x_{2} \right) - \beta x_{3}$$

où $\alpha$ et $\beta$ sont des réels. Le matériau a une limite d'élasticité $\sigma_{e} = 25.0$ MPa, un module de Young $E = 14.0$ GPa et un coefficient de Poisson $\nu = 0.21$.

1. (1 point) Exprimer les composantes du tenseur des déformations infinitésimales.
2. (2 points) Déterminer les composantes du tenseur des contraintes de Cauchy.
3. (3 points) Montrer qu'afin d'obtenir un état plan de contrainte, la condition suivante devrait être vérifiée :

$$\lambda = 2\mu$$

   où $\lambda$ et $\mu$ sont des coefficients de Lamé.
4. (2 points) Déterminer la valeur maximale de $\alpha$ permettant au matériau de satisfaire le critère de Tresca.

*— page 56 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Seconde Session / S4 / 2022-2023 / novembre 2023

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 90 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Questions de Compréhension (4.0 pts)

1. (2 points) Décrire, en quelques phrases et surtout avec vos propres mots, la théorie de l'élasticité des matériaux amorphes et celle des matériaux cristallins.
2. (2 points) Rappeler la loi de Hooke pour un matériau dépourvu de plan de symétrie et rappeler le nombre de composantes constituant chacun des tenseurs dans la loi.

### Exercice 23 : Critère de von Mises (6.0 pts)

En un point M d'une structure, la matrice représentant le tenseur des contraintes s'exprime :

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} 0 & 0 & a \\ 0 & -a & 0 \\ a & 0 & 0 \end{bmatrix}$$

où $a$ est une constante. Le matériau a une limite d'élasticité $\sigma_{e} = 20.0$ MPa, en traction.

1. (3 points) Déterminer les composantes du tenseur des contraintes de Cauchy.
2. (3 points) Vérifier si le critère de von Mises est satisfait ou non. On prendra $E = 25.0$ GPa, $\nu = 0.3$ et $a = 0.001$.

### Exercice 24 : Relation contraintes-déformations (10.0 pts)

En un point donné d'un matériau isotrope et ayant un comportement élastique linéaire, le vecteur déplacement s'exprime :

$$\overrightarrow{u} = \begin{pmatrix} -aX_{1} + aX_{2} \\ aX_{1} - aX_{2} \\ aX_{3} \end{pmatrix}$$

où $a$ est un nombre positif. Les coordonnées du matériel dans la configuration de référence sont notées $X_{i}$.

1. (1 point) Déterminer le tenseur des déformations infinitésimales.
2. (3 points) Exprimer, en fonction de $a$, $\lambda$ et $\mu$, les composantes de la matrice représentant le tenseur des contraintes.

Par la suite, on choisit $E = 210.0$ GPa, $\nu = 0.3$ et $a = 0.001$.

3. (4 points) Représenter les cercles de Mohr des Contraintes
4. (2 points) En déduire les contraintes principales et les directions principales associées.

---

mamadou.toungara@enetp.ml — 16 of 16

*— page 57 — (feuille de sujet imprimée)*

### Exercice 16 : Critères de limité d'élasticité (8.0 pts)

La matrice représentant le tenseur des contraintes en un point $M$ d'un matériau ayant un comportement élastique linéaire s'exprime comme suit :

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -50 & 15 & 0 \\ 15 & 0 & -12 \\ 0 & -12 & -50 \end{bmatrix}$$

Le matériau a un module de Young $E = 210.0$ GPa, un coefficient de Poisson $\nu = 0.3$ et une limite d'élasticité $\sigma_{e} = 400.0$ MPa.

1. (2 points) Déterminer les composantes de la matrice représentant le tenseur des déformations pour la contrainte indiquée.
2. (4 points) Calculer les contraintes équivalentes de von Mises et de Tresca et conclure si le matériau atteint ou non sa limite d'élasticité.
3. (2 points) Tracer les cercles de Mohr correspondant à l'état de contrainte indiqué.

*— page 58 — (figure du sujet)*

![](figs/fig-p58-bloc-cl.png)

*— page 59 — (feuille de sujet imprimée)*

### Exercice 8 : Critères limites d'élasticité (5.0 *pts*)

La limite d'élasticité en traction d'un matériau est notée $\sigma_{e}$. Le tenseur des contraintes en un point $M$ du matériau s'écrit :

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} 0 & \sigma_{12} & 0 \\ \sigma_{12} & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

1. (2 points) Déterminer les contraintes et les directions principales du tenseur.
2. (2 points) Exprimer la limite d'élasticité en cisaillement $\left( \tau_{e} = \sigma_{12} \right)$, en fonction de $\sigma_{e}$, en utilisant le critère de von Mises et celui de Tresca.
3. (1 point) Comparer la limite d'élasticité en cisaillement obtenue à travers les deux critères.

*— page 60 — (feuille de sujet imprimée)*

### Exercice 9 : Mur soumis à un effort de compression (7.0 *pts*)

La Fig. 2 représente un mur soumis à un effort réparti $\overrightarrow{f}$ de compression dont la résultante est notée $\overrightarrow{F} = -f\ell t\,\overrightarrow{y}$. Des deux côtés du mur, c'est-à-dire à gauche et à droite sur la figure, le déplacement horizontal longitudinal (suivant l'axe $x$) est bloqué. Sur le côté inférieur $(y = 0)$, le sol est considéré comme suffisamment rigide pour bloquer le déplacement vertical (suivant l'axe $y$), mais le glissement transversal reste possible à ce niveau. Le matériau constitutif a un module de Young $E = 20.0$ GPa et un coefficient de Poisson $\nu = 0.3$. Le mur a une longueur (suivant l'axe $x$) $\ell = 3.0$ m, une hauteur (suivant l'axe $y$) $h = 1.5$ m et une épaisseur (suivant l'axe $z$) $t = 15.0$ cm.

*— page 61 — (feuille de sujet imprimée)*

![](figs/fig-p61-figure2.png)

<center>FIGURE 2 – Exercice 9</center>

L'effort réparti vaut $f = 6.7\ \text{kN.m}^{-2}$. La déformation dans le matériau est considéré uniforme. Le poids propre du mur sera négligé devant les charges qui lui sont appliquées et nous resterons dans le cadre des petites déformations.

1. (2 points) Identifier les conditions aux limites sur les six (06) côtés du mur.
2. (2 points) Déterminer le tenseur des déformations dans le mur.
3. (3 points) Déterminer les forces nécessaires pour assurer le blocage du déplacement horizontal longitudinal sur les côtés gauche et droite du mur.

*— page 62 — (feuille de sujet imprimée)*

### Exercice 16 : Critères de limité d'élasticité (8.0 pts)

La matrice représentant le tenseur des contraintes en un point $M$ d'un matériau ayant un comportement élastique linéaire s'exprime comme suit :

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -50 & 15 & 0 \\ 15 & 0 & -12 \\ 0 & -12 & -50 \end{bmatrix}$$

Le matériau a un module de Young $E = 210.0$ GPa, un coefficient de Poisson $\nu = 0.3$ et une limite d'élasticité $\sigma_{e} = 400.0$ MPa.

1. (2 points) Déterminer les composantes de la matrice représentant le tenseur des déformations pour la contrainte indiquée.
2. (4 points) Calculer les contraintes équivalentes de von Mises et de Tresca et conclure si le matériau atteint ou non sa limite d'élasticité.
3. (2 points) Tracer les cercles de Mohr correspondant à l'état de contrainte indiqué.

*— page 63 — (feuille de sujet imprimée)*

### Exercice 10 : Compression d'un bloc (6.0 *pts*)

Dans le plan, un bloc d'un matériau ayant un comportement élastique linéaire, de module de Young $E$ et de coefficient de Poisson $\nu$, doit supporter le poids $\overrightarrow{f}$ d'un bâtiment, où $f$ a les dimensions d'une force par unité de longueur. Le bloc a une longueur $\ell$ et une hauteur $h$, il repose sur un sol infiniment rigide, ses côtés gauche et droit sont libres de toute force (voir Fig. 3). Les forces de frottement entre le bloc et le sol ne sont pas prises en compte. De même, son poids propre est négligé devant la charge qui lui est appliquée.

![](figs/fig-p63-figure3.png)

<center>FIGURE 3 – Exercice 10</center>

1. (1 point) Identifier les conditions aux limites sur les quatre bords du bloc.
2. (1 point) Schématiser l'état déformé du bloc.
3. (2 points) Exprimer, en fonction de $f$, $E$ et $\nu$, les composantes du tenseur des déformations.

*— page 64 — (feuille de sujet imprimée)*

### Exercice 7 : Tenseur des Contraintes (5.0 *pts*)

En un point $M$ d'un solide isotrope $(E = 210.0\ \text{GPa et}\ \nu = 0.3)$ le champ de déplacement (en mm) est le suivant :

$$u_{1} = \beta x_{1} + \gamma x_{2};\qquad u_{2} = -\gamma x_{1} + \beta x_{2}$$

où $\beta$ et $\gamma$ sont des réels. La déformation dans le solide est considérée comme homogène.

1. (2 points) Exprimer les composantes du tenseur des déformations infinitésimales.
2. (2 points) Déterminer le tenseur des contraintes au point $M$. On prendra $\beta = 0.02$ et $\gamma = 0.001$.
3. (1 point) Expliquer si la sollicitation au point $M$ correspond à un état de contrainte ou de déformation plan.

*— page 65 — (feuille de sujet imprimée)*

### Exercice 15 : Relation Contrainte-Déformation (6.0 pts)

La matrice représentant le tenseur des déformations en un point $M$ d'un matériau ayant un comportement élastique linéaire s'exprime comme suit :

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = 10^{-6} \times \begin{bmatrix} \varepsilon_{xx} & 0 & 0 \\ 0 & -400 & 0 \\ 0 & 0 & 1200 \end{bmatrix}$$

Le matériau a un module de Young $E = 210.0$ GPa, un coefficient de Poisson $\nu = 0.3$ et une limite d'élasticité $\sigma_{e} = 400.0$ MPa. Déterminer les composantes de la matrice représentant le tenseur des contraintes pour la déformation indiquée, en faisant l'hypothèse :

1. (3 points) d'un état plan de déformation.
2. (3 points) d'un état plan de contrainte.

*— page 66 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Première Session / S4 / 2018-2019 / septembre 2019

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 120 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Questions de compréhension (3.0 *pts*)

1. (1 point) Quand dit-on qu'un matériau a un comportement élastique ?
2. (2 points) Expliquer le concept d'isotropie et d'homogénéité d'un matériau.

### Exercice 7 : Tenseur des Contraintes (5.0 *pts*)

En un point $M$ d'un solide isotrope $(E = 210.0\ \text{GPa et}\ \nu = 0.3)$ le champ de déplacement (en mm) est le suivant :

$$u_{1} = \beta x_{1} + \gamma x_{2};\qquad u_{2} = -\gamma x_{1} + \beta x_{2}$$

où $\beta$ et $\gamma$ sont des réels. La déformation dans le solide est considérée comme homogène.

1. (2 points) Exprimer les composantes du tenseur des déformations infinitésimales.
2. (2 points) Déterminer le tenseur des contraintes au point $M$. On prendra $\beta = 0.02$ et $\gamma = 0.001$.
3. (1 point) Expliquer si la sollicitation au point $M$ correspond à un état de contrainte ou de déformation plan.

### Exercice 8 : Critères limites d'élasticité (5.0 *pts*)

La limite d'élasticité en traction d'un matériau est notée $\sigma_{e}$. Le tenseur des contraintes en un point $M$ du matériau s'écrit :

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} 0 & \sigma_{12} & 0 \\ \sigma_{12} & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

1. (2 points) Déterminer les contraintes et les directions principales du tenseur.
2. (2 points) Exprimer la limite d'élasticité en cisaillement $\left( \tau_{e} = \sigma_{12} \right)$, en fonction de $\sigma_{e}$, en utilisant le critère de von Mises et celui de Tresca.
3. (1 point) Comparer la limite d'élasticité en cisaillement obtenue à travers les deux critères.

### Exercice 9 : Mur soumis à un effort de compression (7.0 *pts*)

La Fig. 2 représente un mur soumis à un effort réparti $\overrightarrow{f}$ de compression dont la résultante est notée $\overrightarrow{F} = -f\ell t\,\overrightarrow{y}$. Des deux côtés du mur, c'est-à-dire à gauche et à droite sur la figure, le déplacement horizontal longitudinal (suivant l'axe $x$) est bloqué. Sur le côté inférieur $(y = 0)$, le sol est considéré comme suffisamment rigide pour bloquer le déplacement vertical (suivant l'axe $y$), mais le glissement transversal reste possible à ce niveau. Le matériau constitutif a un module de Young $E = 20.0$ GPa et un coefficient de Poisson $\nu = 0.3$. Le mur a une longueur (suivant l'axe $x$) $\ell = 3.0$ m, une hauteur (suivant l'axe $y$) $h = 1.5$ m et une épaisseur (suivant l'axe $z$) $t = 15.0$ cm.

---

mamadou.toungara@enetp.ml — 6 of 16

*— page 67 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

![](figs/fig-p61-figure2.png)

<center>FIGURE 2 – Exercice 9</center>

L'effort réparti vaut $f = 6.7\ \text{kN.m}^{-2}$. La déformation dans le matériau est considéré uniforme. Le poids propre du mur sera négligé devant les charges qui lui sont appliquées et nous resterons dans le cadre des petites déformations.

1. (2 points) Identifier les conditions aux limites sur les six (06) côtés du mur.
2. (2 points) Déterminer le tenseur des déformations dans le mur.
3. (3 points) Déterminer les forces nécessaires pour assurer le blocage du déplacement horizontal longitudinal sur les côtés gauche et droite du mur.

*— page 68 — (feuille de sujet imprimée, page photographiée en rotation)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Seconde Session / S4 / 2019-2020 / octobre 2021

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 120 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Questions de Compréhension (6.0 pts)

*Dans les explications, il est fortement conseillé d'être concis et clair*

1. (2 points) Expliquer l'effet Poisson.
2. (2 points) Définir un matériau fragile et en donner deux exemples.
3. (2 points) Que se passe-t-il lorsque la contrainte dans un matériau atteint ou dépasse la limite d'élasticité de celui-ci ?

### Exercice 15 : Relation Contrainte-Déformation (6.0 pts)

La matrice représentant le tenseur des déformations en un point $M$ d'un matériau ayant un comportement élastique linéaire s'exprime comme suit :

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = 10^{-6} \times \begin{bmatrix} \varepsilon_{xx} & 0 & 0 \\ 0 & -400 & 0 \\ 0 & 0 & 1200 \end{bmatrix}$$

Le matériau a un module de Young $E = 210.0$ GPa, un coefficient de Poisson $\nu = 0.3$ et une limite d'élasticité $\sigma_{e} = 400.0$ MPa. Déterminer les composantes de la matrice représentant le tenseur des contraintes pour la déformation indiquée, en faisant l'hypothèse :

1. (3 points) d'un état plan de déformation.
2. (3 points) d'un état plan de contrainte.

### Exercice 16 : Critères de limité d'élasticité (8.0 pts)

La matrice représentant le tenseur des contraintes en un point $M$ d'un matériau ayant un comportement élastique linéaire s'exprime comme suit :

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -50 & 15 & 0 \\ 15 & 0 & -12 \\ 0 & -12 & -50 \end{bmatrix}$$

Le matériau a un module de Young $E = 210.0$ GPa, un coefficient de Poisson $\nu = 0.3$ et une limite d'élasticité $\sigma_{e} = 400.0$ MPa.

1. (2 points) Déterminer les composantes de la matrice représentant le tenseur des déformations pour la contrainte indiquée.
2. (4 points) Calculer les contraintes équivalentes de von Mises et de Tresca et conclure si le matériau atteint ou non sa limite d'élasticité.
3. (2 points) Tracer les cercles de Mohr correspondant à l'état de contrainte indiqué.

---

mamadou.toungara@enetp.ml — 12 of 16

*— page 69 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Seconde Session / S4 / 2018-2019 / janvier 2020

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 120 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Questions de compréhension (5.0 *pts*)

1. (1 point) Qu'appelle-t-on une loi de comportement mécanique ?
2. (2 points) Citer deux propriétés mécaniques d'un matériau ayant un comportement élastique linéaire et donner leur interprétation.
3. (2 points) La loi de Hooke pour les matériaux isotropes s'exprime :

$$\overline{\overline{\sigma}} = \lambda\,tr\left( \overline{\overline{\varepsilon}} \right)\overline{\overline{I}} + 2\mu\,\overline{\overline{\varepsilon}}$$

   où $\lambda$ et $\mu$ sont des coefficients de Lamé. Rappeler les expressions de ces coefficients et expliquer pourquoi cette loi ne serait pas valable pour les matériaux anisotropes.

### Exercice 10 : Compression d'un bloc (6.0 pts)

Dans le plan, un bloc d'un matériau ayant un comportement élastique linéaire, de module de Young $E$ et de coefficient de Poisson $\nu$, doit supporter le poids $\overrightarrow{f}$ d'un bâtiment, où $f$ a les dimensions d'une force par unité de longueur. Le bloc a une longueur $\ell$ et une hauteur $h$, il repose sur un sol infiniment rigide, ses côtés gauche et droit sont libres de toute force (voir Fig. 3). Les forces de frottement entre le bloc et le sol ne sont pas prises en compte. De même, son poids propre est négligé devant la charge qui lui est appliquée.

![](figs/fig-p63-figure3.png)

<center>FIGURE 3 – Exercice 10</center>

1. (1 point) Identifier les conditions aux limites sur les quatre bords du bloc.
2. (1 point) Schématiser l'état déformé du bloc.
3. (2 points) Exprimer, en fonction de $f$, $E$ et $\nu$, les composantes du tenseur des déformations.

---

mamadou.toungara@enetp.ml — 8 of 16

*— page 70 — (feuille de sujet imprimée)*

### Exercice 17 : Relation Contrainte-Déformation (8.0 pts)

En un point $M$ d'un matériau isotrope, ayant un comportement élastique linéaire (module de Young $E$ et coefficient de Poisson $\nu$), le champ de déplacement (en mm) est le suivant :

$$u_{1} = -\alpha x_{1} + \beta\left( x_{2} - x_{3} \right);\qquad u_{2} = \alpha\left( x_{1} + x_{3} \right) - \beta x_{2};\qquad u_{3} = -\alpha\left( x_{1} + x_{2} \right) - \beta x_{3}$$

où $\alpha$ et $\beta$ sont des réels. Le matériau a une limite d'élasticité $\sigma_{e} = 25.0$ MPa, un module de Young $E = 14.0$ GPa et un coefficient de Poisson $\nu = 0.21$.

1. (1 point) Exprimer les composantes du tenseur des déformations infinitésimales.
2. (2 points) Déterminer les composantes du tenseur des contraintes de Cauchy.
3. (3 points) Montrer qu'afin d'obtenir un état plan de contrainte, la condition suivante devrait être vérifiée :

$$\lambda = 2\mu$$

   où $\lambda$ et $\mu$ sont des coefficients de Lamé.
4. (2 points) Déterminer la valeur maximale de $\alpha$ permettant au matériau de satisfaire le critère de Tresca.

*— page 71 — (feuille de sujet imprimée)*

### Exercice 11 : Tenseur des Contraintes (9.0 *pts*)

Une plaque rectangulaire, de dimensions $\ell \times h$, est soumise à deux contraintes, $\sigma_{1}$ et $\sigma_{2}$, uniformément réparties sur ses bords comme indiqué sur la Fig. 4. Les côtés avant et arrière de la plaque sont libres de toute contrainte. Le matériau constitutif de la plaque est isotrope et a un comportement élastique linéaire dont les paramètres sont le module de Young $(E)$ et le coefficient de Poisson $(\nu)$. Les contraintes de cisaillement sur les bords 1, 2, 3 et 4 sont nulles.

![](figs/fig-p71-figure4.png)

<center>FIGURE 4 – Exercice 11</center>

1. (1 point) La plaque est-elle sollicitée en contrainte ou en déformation planes (justifier la réponse) ?
2. (2 points) Exprimer les composantes du tenseur des déformations infinitésimales.
3. (2 points) En déduire la trace du tenseur des déformations infinitésimales. Cette trace correspond à la variation de volume de la plaque. Pour $\sigma_{1} = 10.0$ MPa, $\sigma_{2} = 15.0$ MPa, $E = 25.0$ GPa et $\nu = 0.3$, expliquer si le volume du matériau augmente ou diminue.
4. (2 points) Pour les valeurs précédentes des contraintes, tracer les cercles de Mohr et en déduire la contrainte de cisaillement maximale.
5. (2 points) Calculer la contrainte équivalente de von Mises et celle de Tresca.

*— page 72 — (feuille de sujet imprimée)*

### Exercice 1 : Etat plan de contrainte (8.0 pts)

La Fig. 1 représente une plaque soumise à un état de contrainte, sa face arrière et sa face avant sont libres de toute contrainte.

![](figs/fig-p72-figure1.png)

<center>FIGURE 1 – Exercice 1</center>

1. (2 points) Déterminer la trace du tenseur des déformations.
2. (3 points) Déterminer les composantes du tenseur des déformations.
3. (3 points) Déterminer les contraintes principales et les directions principales associées.

*— page 73 — (feuille de sujet imprimée)*

### Exercice 8 : Critères limites d'élasticité (5.0 *pts*)

La limite d'élasticité en traction d'un matériau est notée $\sigma_{e}$. Le tenseur des contraintes en un point $M$ du matériau s'écrit :

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} 0 & \sigma_{12} & 0 \\ \sigma_{12} & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

1. (2 points) Déterminer les contraintes et les directions principales du tenseur.
2. (2 points) Exprimer la limite d'élasticité en cisaillement $\left( \tau_{e} = \sigma_{12} \right)$, en fonction de $\sigma_{e}$, en utilisant le critère de von Mises et celui de Tresca.
3. (1 point) Comparer la limite d'élasticité en cisaillement obtenue à travers les deux critères.

*— page 74 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Contrôle Continu / S4 / 2021-2022 / octobre 2022

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 90 minutes**

### Questions de Compréhension (4.0 pts)

*Dans les explications, il est fortement conseillé d'être concis et clair.*

1. (2 points) Quel est le nombre de paramètres matériaux pour un matériau isotrope ? Donner un ordre de grandeur de ces paramètres pour un matériau de votre choix.
2. (2 points) Dans un état plan de déformation, les trois éléments diagonaux de la matrice représentant le tenseur des contraintes sont non nuls. Expliquer pourquoi dans ce cas l'état de contrainte n'est pas plan.

### Exercice 1 : Etat plan de contrainte (8.0 pts)

La Fig. 1 représente une plaque soumise à un état de contrainte, sa face arrière et sa face avant sont libres de toute contrainte.

![](figs/fig-p72-figure1.png)

<center>FIGURE 1 – Exercice 1</center>

1. (2 points) Déterminer la trace du tenseur des déformations.
2. (3 points) Déterminer les composantes du tenseur des déformations.
3. (3 points) Déterminer les contraintes principales et les directions principales associées.

### Exercice 2 : Critères de limité d'élasticité (8.0 pts)

La matrice représentant le tenseur des déformations en un point $M$ d'un matériau ayant un comportement élastique linéaire s'exprime comme suit :

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = 10^{-4} \times \begin{bmatrix} -1.00 & 0.00 & 0.03 \\ 0.00 & 2.00 & 0.00 \\ 0.03 & 0.00 & -1.00 \end{bmatrix}$$

Le matériau a un module de Young $E = 210.0$ GPa, un coefficient de Poisson $\nu = 0.3$ et une limite d'élasticité $\sigma_{e} = 300.0$ MPa.

---

mamadou.toungara@enetp.ml — 2 of 16

*— page 75 — (feuille de sujet imprimée)*

### Exercice 23 : Critère de von Mises (6.0 pts)

En un point M d'une structure, la matrice représentant le tenseur des contraintes s'exprime :

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} 0 & 0 & a \\ 0 & -a & 0 \\ a & 0 & 0 \end{bmatrix}$$

où $a$ est une constante. Le matériau a une limite d'élasticité $\sigma_{e} = 20.0$ MPa, en traction.

1. (3 points) Déterminer les composantes du tenseur des contraintes de Cauchy.
2. (3 points) Vérifier si le critère de von Mises est satisfait ou non. On prendra $E = 25.0$ GPa, $\nu = 0.3$ et $a = 0.001$.

*— page 76 — (feuille de sujet imprimée)*

### Exercice 24 : Relation contraintes-déformations (10.0 pts)

En un point donné d'un matériau isotrope et ayant un comportement élastique linéaire, le vecteur déplacement s'exprime :

$$\overrightarrow{u} = \begin{pmatrix} -aX_{1} + aX_{2} \\ aX_{1} - aX_{2} \\ aX_{3} \end{pmatrix}$$

où $a$ est un nombre positif. Les coordonnées du matériel dans la configuration de référence sont notées $X_{i}$.

1. (1 point) Déterminer le tenseur des déformations infinitésimales.
2. (3 points) Exprimer, en fonction de $a$, $\lambda$ et $\mu$, les composantes de la matrice représentant le tenseur des contraintes.

Par la suite, on choisit $E = 210.0$ GPa, $\nu = 0.3$ et $a = 0.001$.

3. (4 points) Représenter les cercles de Mohr des Contraintes
4. (2 points) En déduire les contraintes principales et les directions principales associées.

*— page 77 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Première Session / S4 / 2018-2019 / septembre 2019

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 120 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Questions de compréhension (3.0 *pts*)

1. (1 point) Quand dit-on qu'un matériau a un comportement élastique ?
2. (2 points) Expliquer le concept d'isotropie et d'homogénéité d'un matériau.

### Exercice 7 : Tenseur des Contraintes (5.0 *pts*)

En un point $M$ d'un solide isotrope $(E = 210.0\ \text{GPa et}\ \nu = 0.3)$ le champ de déplacement (en mm) est le suivant :

$$u_{1} = \beta x_{1} + \gamma x_{2};\qquad u_{2} = -\gamma x_{1} + \beta x_{2}$$

où $\beta$ et $\gamma$ sont des réels. La déformation dans le solide est considérée comme homogène.

1. (2 points) Exprimer les composantes du tenseur des déformations infinitésimales.
2. (2 points) Déterminer le tenseur des contraintes au point $M$. On prendra $\beta = 0.02$ et $\gamma = 0.001$.
3. (1 point) Expliquer si la sollicitation au point $M$ correspond à un état de contrainte ou de déformation plan.

### Exercice 8 : Critères limites d'élasticité (5.0 *pts*)

La limite d'élasticité en traction d'un matériau est notée $\sigma_{e}$. Le tenseur des contraintes en un point $M$ du matériau s'écrit :

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} 0 & \sigma_{12} & 0 \\ \sigma_{12} & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

1. (2 points) Déterminer les contraintes et les directions principales du tenseur.
2. (2 points) Exprimer la limite d'élasticité en cisaillement $\left( \tau_{e} = \sigma_{12} \right)$, en fonction de $\sigma_{e}$, en utilisant le critère de von Mises et celui de Tresca.
3. (1 point) Comparer la limite d'élasticité en cisaillement obtenue à travers les deux critères.

### Exercice 9 : Mur soumis à un effort de compression (7.0 *pts*)

La Fig. 2 représente un mur soumis à un effort réparti $\overrightarrow{f}$ de compression dont la résultante est notée $\overrightarrow{F} = -f\ell t\,\overrightarrow{y}$. Des deux côtés du mur, c'est-à-dire à gauche et à droite sur la figure, le déplacement horizontal longitudinal (suivant l'axe $x$) est bloqué. Sur le côté inférieur $(y = 0)$, le sol est considéré comme suffisamment rigide pour bloquer le déplacement vertical (suivant l'axe $y$), mais le glissement transversal reste possible à ce niveau. Le matériau constitutif a un module de Young $E = 20.0$ GPa et un coefficient de Poisson $\nu = 0.3$. Le mur a une longueur (suivant l'axe $x$) $\ell = 3.0$ m, une hauteur (suivant l'axe $y$) $h = 1.5$ m et une épaisseur (suivant l'axe $z$) $t = 15.0$ cm.

---

mamadou.toungara@enetp.ml — 6 of 16

*— page 78 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Contrôle Continu / S4 / 2022-2023 / septembre 2023

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 90 minutes**

### Exercice 5 : Bloc sous Compression (9.0 pts)

Un bloc de matériau est soumis à l'effort d'une pression $p$, comme indiqué sur la figure ci-contre. Il repose sur un sol rigide et suffisamment lisse. Le matériau constitutif du bloc a un comportement élastique linéaire, de module de Young $E$ et de coefficient de Poisson $\nu$.

1. (1 point) Déterminer les composantes du tenseur des contraintes en fonction de $p$.
2. (2 points) Déterminer les composantes du tenseur des déformations, en fonction de $p$, $E$ et $\nu$.
3. (3 points) Exprimer, en fonction de $p$, $E$ et $\nu$, la variation de volume du bloc.
4. (3 points) En déduire la valeur du coefficient de Poisson, en supposant que le bloc est constitué d'un matériau incompressible.

![](figs/fig-p78-bloc3d.png)

### Exercice 6 : Relation contraintes-déformations (11.0 pts)

La matrice représentant le tenseur des déformations en un point $M$ d'un matériau ayant un comportement élastique linéaire (coefficients de Lamé, $\lambda$ et $\mu$) s'exprime comme suit :

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} -a & a & 0 \\ a & 2a & 0 \\ 0 & 0 & -a \end{bmatrix}$$

où $a$ est un nombre positif.

1. (2 points) Exprimer, en fonction de $a$ et $\mu$, les composantes de la matrice représentant le tenseur des contraintes pour la déformation indiquée.
2. (3 points) Déterminer les contraintes principales, en fonction de $a$ et $\mu$.
3. (2 points) Pourrait-il s'agir d'un problème d'état plan de contrainte ou de déformation (justifier la réponse) ?
4. (4 points) Comparer la contrainte équivalente de von Mises à celle de Tresca.

*— page 79 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

![](figs/fig-p61-figure2.png)

<center>FIGURE 2 – Exercice 9</center>

L'effort réparti vaut $f = 6.7\ \text{kN.m}^{-2}$. La déformation dans le matériau est considéré uniforme. Le poids propre du mur sera négligé devant les charges qui lui sont appliquées et nous resterons dans le cadre des petites déformations.

1. (2 points) Identifier les conditions aux limites sur les six (06) côtés du mur.
2. (2 points) Déterminer le tenseur des déformations dans le mur.
3. (3 points) Déterminer les forces nécessaires pour assurer le blocage du déplacement horizontal longitudinal sur les côtés gauche et droite du mur.

*— page 80 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Première Session / S4 / 2019-2020 / juin 2021

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 120 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Questions de Compréhension (2.0 pts)

1. (1 point) Définir un matériau ductile.
2. (1 point) Peut-on définir un seuil de déformation au-delà duquel la loi d'élasticité linéaire ne peut plus être appliquée (argumenter la réponse) ?

### Exercice 12 : Relation Contrainte-Déformation (5.0 pts)

Une éprouvette, de section rectangulaire $a \times b$ et de longueur utile $\ell$, est soumise à un effort de traction $F$, graduellement croissant. L'allongement $(\Delta\ell)$ de l'éprouvette est mesurée au fur et à mesure que l'effort évolue. Les données enregistrées sont indiquées dans le Tableau 2. Les dimensions

<center>TABLE 2 – Mesures effort-allongement</center>

| $F(\text{N})$ | 0 | 10.0 | 25.0 | 45.0 | 70.0 | 95.0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| $\Delta\ell(\text{mm})$ | 0 | 1.00 | 2.40 | 4.05 | 6.95 | 9.50 |

de l'éprouvette sont les suivantes : $a = 3.0$ mm, $b = 8.0$ mm et $\ell = 10.0$ cm.

1. (3 points) Représenter sur un graphique la contrainte en fonction de la déformation.
2. (2 points) En déduire le module de Young du matériau.

### Exercice 13 : Colonne sous Compression (6.0 pts)

Une colonne de béton est soumise à un effort de compression $\overrightarrow{P}$ uniformément réparti dans sa section droite. La colonne a une hauteur $h$ et une section rectangulaire $a \times b$ (Fig. 5.a). Elle repose sur un sol rigide et suffisamment lisse. Le matériau constitutif de la colonne est considéré comme isotrope, il a un comportement élastique linéaire, son module de Young est noté $E$ et son coefficient de Poisson $\nu$. Sa limite d'élasticité en compression est notée $\sigma_{e}$. La déformation dans la colonne est considérée comme homogène. Son poids propre est négligé devant les efforts qui lui sont appliqués.

1. (1 point) Schématiser la colonne dans son état déformé.
2. (1 point) Déterminer les composantes du tenseur des contraintes en fonction de $P$.
3. (2 points) Déterminer les composantes du tenseur des déformations, en fonction de $P$, $E$ et $\nu$.
4. (1 point) Calculer la variation de la hauteur de la colonne pour $\sigma_{e} = 2.0$ MPa, $E = 20.0$ GPa et $h = 2.0$ m.

### Exercice 14 : Plaque Comprimée (7.0 pts)

---

mamadou.toungara@enetp.ml — 10 of 16

*— page 81 — (feuille de sujet imprimée, page photographiée en rotation)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

4. (2 points) En déduire les variations de longueur suivant les axes $x$ et $y$.

### Exercice 11 : Tenseur des Contraintes (9.0 *pts*)

Une plaque rectangulaire, de dimensions $\ell \times h$, est soumise à deux contraintes, $\sigma_{1}$ et $\sigma_{2}$, uniformément réparties sur ses bords comme indiqué sur la Fig. 4. Les côtés avant et arrière de la plaque sont libres de toute contrainte. Le matériau constitutif de la plaque est isotrope et a un comportement élastique linéaire dont les paramètres sont le module de Young $(E)$ et le coefficient de Poisson $(\nu)$. Les contraintes de cisaillement sur les bords 1, 2, 3 et 4 sont nulles.

![](figs/fig-p71-figure4.png)

<center>FIGURE 4 – Exercice 11</center>

1. (1 point) La plaque est-elle sollicitée en contrainte ou en déformation planes (justifier la réponse) ?
2. (2 points) Exprimer les composantes du tenseur des déformations infinitésimales.
3. (2 points) En déduire la trace du tenseur des déformations infinitésimales. Cette trace correspond à la variation de volume de la plaque. Pour $\sigma_{1} = 10.0$ MPa, $\sigma_{2} = 15.0$ MPa, $E = 25.0$ GPa et $\nu = 0.3$, expliquer si le volume du matériau augmente ou diminue.
4. (2 points) Pour les valeurs précédentes des contraintes, tracer les cercles de Mohr et en déduire la contrainte de cisaillement maximale.
5. (2 points) Calculer la contrainte équivalente de von Mises et celle de Tresca.

---

mamadou.toungara@enetp.ml — 9 of 16

*— page 82 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Première Session / S4 / 2021-2022 / octobre 2022

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 120 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Questions de Compréhension (4.0 pts)

*Dans les explications, restez concis, clairs et surtout utilisez vos propres termes.*

1. (2 points) Expliquer le principe de la décomposition polaire d'une transformation.
2. (2 points) Expliquer la différence entre le premier et le second tenseurs des contraintes de Piola-Kirchhoff.

### Exercice 17 : Relation Contrainte-Déformation (8.0 pts)

En un point $M$ d'un matériau isotrope, ayant un comportement élastique linéaire (module de Young $E$ et coefficient de Poisson $\nu$), le champ de déplacement (en mm) est le suivant :

$$u_{1} = -\alpha x_{1} + \beta\left( x_{2} - x_{3} \right);\qquad u_{2} = \alpha\left( x_{1} + x_{3} \right) - \beta x_{2};\qquad u_{3} = -\alpha\left( x_{1} + x_{2} \right) - \beta x_{3}$$

où $\alpha$ et $\beta$ sont des réels. Le matériau a une limite d'élasticité $\sigma_{e} = 25.0$ MPa, un module de Young $E = 14.0$ GPa et un coefficient de Poisson $\nu = 0.21$.

1. (1 point) Exprimer les composantes du tenseur des déformations infinitésimales.
2. (2 points) Déterminer les composantes du tenseur des contraintes de Cauchy.
3. (3 points) Montrer qu'afin d'obtenir un état plan de contrainte, la condition suivante devrait être vérifiée :

$$\lambda = 2\mu$$

   où $\lambda$ et $\mu$ sont des coefficients de Lamé.
4. (2 points) Déterminer la valeur maximale de $\alpha$ permettant au matériau de satisfaire le critère de Tresca.

### Exercice 18 : Critère de von Mises (8.0 pts)

La matrice représentant le tenseur des contraintes en un point $M$ d'un matériau ayant un comportement élastique linéaire s'exprime comme suit :

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -65 & 30 & 0 \\ 30 & -60 & 0 \\ 0 & 0 & 60 \end{bmatrix}$$

où les valeurs numériques sont en MPa. Le matériau a une limite d'élasticité $\sigma_{e} = 355.0$ MPa, un module de Young $E = 200.0$ GPa et un coefficient de Poisson $\nu = 0.3$.

1. (2 points) Calculer les valeurs numériques des composantes du tenseur des déformations.
2. (6 points) Déterminer la contrainte équivalente de von Mises et vérifier si la limite d'élasticité du matériau est atteinte ou non.

---

mamadou.toungara@enetp.ml — 13 of 16

*— page 83 — (feuille de sujet imprimée)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Première Session / S4 / 2022-2023 / octobre 2023

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 90 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Questions de Compréhension (6.0 pts)

1. (2 points) Décrire, en quelques phrases et surtout avec vos propres mots, la théorie de l'élasticité des matériaux amorphes et celle des matériaux cristallins.
2. (2 points) Comparer un matériau fragile à un matériau ductile.
3. (2 points) Rappeler la loi de Hooke pour un matériau dépourvu de plan de symétrie et rappeler le nombre de composantes constituant chacun des tenseurs dans la loi.

### Exercice 21 : Critère de Mohr-Coulomb (7.0 pts)

On considère un solide homogène et isotrope constitué d'un matériau fragile de coefficient de Poisson $\nu$ et de limite d'élasticité, en compression, $\sigma_{e}$. L'angle de frottement vaut $\varphi$ et le coefficient de cohésion $\sigma_{0}$. Le solide est soumis à une pression $p$, comme indiqué ci-contre. Les paroi de l'enceinte contenant le solide sont rigides.

![](figs/fig-p83-mohrcoulomb.png)

1. (1 point) Déterminer les composantes du tenseur des déformations.
2. (2 points) Déterminer les composantes du tenseur des contraintes de Cauchy.
3. (3 points) Déterminer, en fonction de $\nu$, $\varphi$ et $\sigma_{0}$, la pression maximale que le matériau pourrait subir, selon le critère de Mohr-Coulomb.

### Exercice 22 : Critère de Tresca (7.0 pts)

En un point M d'une structure, la matrice représentant le tenseur des contraintes s'exprime :

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} 0 & 0 & a \\ 0 & 0 & 0 \\ a & 0 & -2a \end{bmatrix}$$

1. (3 points) Déterminer les composantes du tenseur des contraintes de Cauchy.
2. (2 points) Le problème proposé correspond-il à un état plan de contrainte ou de déformation ? Si oui, préciser le plan.
3. (2 points) Calculer la contrainte équivalente de Tresca pour $E = 25.0$ GPa, $\nu = 0.3$ et $a = 0.001$.

*— page 84 — (feuille de sujet imprimée, page photographiée en rotation — reprise de la page 68)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Seconde Session / S4 / 2019-2020 / octobre 2021

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 120 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Questions de Compréhension (6.0 pts)

*Dans les explications, il est fortement conseillé d'être concis et clair*

1. (2 points) Expliquer l'effet Poisson.
2. (2 points) Définir un matériau fragile et en donner deux exemples.
3. (2 points) Que se passe-t-il lorsque la contrainte dans un matériau atteint ou dépasse la limite d'élasticité de celui-ci ?

### Exercice 15 : Relation Contrainte-Déformation (6.0 pts)

La matrice représentant le tenseur des déformations en un point $M$ d'un matériau ayant un comportement élastique linéaire s'exprime comme suit :

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = 10^{-6} \times \begin{bmatrix} \varepsilon_{xx} & 0 & 0 \\ 0 & -400 & 0 \\ 0 & 0 & 1200 \end{bmatrix}$$

Le matériau a un module de Young $E = 210.0$ GPa, un coefficient de Poisson $\nu = 0.3$ et une limite d'élasticité $\sigma_{e} = 400.0$ MPa. Déterminer les composantes de la matrice représentant le tenseur des contraintes pour la déformation indiquée, en faisant l'hypothèse :

1. (3 points) d'un état plan de déformation.
2. (3 points) d'un état plan de contrainte.

### Exercice 16 : Critères de limité d'élasticité (8.0 pts)

La matrice représentant le tenseur des contraintes en un point $M$ d'un matériau ayant un comportement élastique linéaire s'exprime comme suit :

$$\left\lbrack \overline{\overline{\sigma}} \right\rbrack = \begin{bmatrix} -50 & 15 & 0 \\ 15 & 0 & -12 \\ 0 & -12 & -50 \end{bmatrix}$$

Le matériau a un module de Young $E = 210.0$ GPa, un coefficient de Poisson $\nu = 0.3$ et une limite d'élasticité $\sigma_{e} = 400.0$ MPa.

1. (2 points) Déterminer les composantes de la matrice représentant le tenseur des déformations pour la contrainte indiquée.
2. (4 points) Calculer les contraintes équivalentes de von Mises et de Tresca et conclure si le matériau atteint ou non sa limite d'élasticité.
3. (2 points) Tracer les cercles de Mohr correspondant à l'état de contrainte indiqué.

---

mamadou.toungara@enetp.ml — 12 of 16

*— page 85 — (feuille de sujet imprimée — reprise de la page 56)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Seconde Session / S4 / 2022-2023 / novembre 2023

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 90 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Questions de Compréhension (4.0 pts)

1. (2 points) Décrire, en quelques phrases et surtout avec vos propres mots, la théorie de l'élasticité des matériaux amorphes et celle des matériaux cristallins.
2. (2 points) Rappeler la loi de Hooke pour un matériau dépourvu de plan de symétrie et rappeler le nombre de composantes constituant chacun des tenseurs dans la loi.

### Exercice 23 : Critère de von Mises (6.0 pts)

En un point M d'une structure, la matrice représentant le tenseur des contraintes s'exprime :

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = \begin{bmatrix} 0 & 0 & a \\ 0 & -a & 0 \\ a & 0 & 0 \end{bmatrix}$$

où $a$ est une constante. Le matériau a une limite d'élasticité $\sigma_{e} = 20.0$ MPa, en traction.

1. (3 points) Déterminer les composantes du tenseur des contraintes de Cauchy.
2. (3 points) Vérifier si le critère de von Mises est satisfait ou non. On prendra $E = 25.0$ GPa, $\nu = 0.3$ et $a = 0.001$.

### Exercice 24 : Relation contraintes-déformations (10.0 pts)

En un point donné d'un matériau isotrope et ayant un comportement élastique linéaire, le vecteur déplacement s'exprime :

$$\overrightarrow{u} = \begin{pmatrix} -aX_{1} + aX_{2} \\ aX_{1} - aX_{2} \\ aX_{3} \end{pmatrix}$$

où $a$ est un nombre positif. Les coordonnées du matériel dans la configuration de référence sont notées $X_{i}$.

1. (1 point) Déterminer le tenseur des déformations infinitésimales.
2. (3 points) Exprimer, en fonction de $a$, $\lambda$ et $\mu$, les composantes de la matrice représentant le tenseur des contraintes.

Par la suite, on choisit $E = 210.0$ GPa, $\nu = 0.3$ et $a = 0.001$.

3. (4 points) Représenter les cercles de Mohr des Contraintes
4. (2 points) En déduire les contraintes principales et les directions principales associées.

---

mamadou.toungara@enetp.ml — 16 of 16

*— page 86 — (feuille de sujet imprimée — reprise de la page 53)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

---

# Examen de la Seconde Session / S4 / 2021-2022 / décembre 2022

> — documents papiers autorisés, aucun support numérique n'est autorisé ;
> — **l'usage du téléphone portable est strictement interdit pendant le contrôle** ;
> — **durée : 90 minutes** ;
> — *pas nécessaire de tout traiter pour avoir le maximum de points, barème est indicatif*

### Exercice 19 : Relation contraintes-déformations (10.0 pts)

La matrice représentant le tenseur des déformations en un point $M$ d'un matériau ayant un comportement élastique linéaire (coefficients de Lamé, $\lambda$ et $\mu$) s'exprime comme suit :

$$\left\lbrack \overline{\overline{\varepsilon}} \right\rbrack = a \times \begin{bmatrix} -1.00 & 1.00 & 0.00 \\ 1.00 & 2.00 & 0.00 \\ 0.00 & 0.00 & -1.00 \end{bmatrix}$$

où $a$ est un nombre réel constant.

1. (2 points) Exprimer, en fonction de $a$ et $\mu$, les composantes de la matrice représentant le tenseur des contraintes pour la déformation indiquée.
2. (3 points) Déterminer les contraintes principales, en fonction de $a$ et $\mu$.
3. (3 points) Calculer les contraintes équivalentes de von Mises et de Tresca pour un module de Young $E = 65.0$ GPa, un coefficient de Poisson $\nu = 0.33$ et $a = 10^{-3}$.
4. (2 points) Que pourrait-on faire avec ces contraintes (von Mises et Tresca) ?

### Exercice 20 : Essai de compression (10.0 pts)

La Fig. 6 représente un matériau soumis en compression dans une enceinte à parois indéformables. On se place dans le plan $(x,\ y)$ où le matériau a une hauteur initiale $h_{0}$ et une largeur $b$. La dimension de la profondeur (suivant l'axe $z$) est maintenue constante. Le matériau a un module de Young $E = 25.0$ GPa et un coefficient de Poisson $\nu = 0.33$.

1. (2 points) Le problème posé correspond-il à un état plan de contrainte ou de déformation (justifier la réponse) ?
2. (2 points) Exprimer, en fonction de $h_{0}$ et $h$, les composantes du tenseur des déformations infinitésimales.
3. (3 points) Exprimer et calculer les composantes du tenseur des contraintes de Cauchy, pour $h_{0} = 150.0$ mm et $h = 138.0$ mm.
4. (3 points) Tracer les cercles de Mohr correspondant à l'état de contrainte indiqué et en déduire la contrainte de cisaillement maximale.

![](figs/fig-p53-figure6.png)

<center>FIGURE 6 – Exercice 20</center>

---

mamadou.toungara@enetp.ml — 14 of 16

*— page 87 — (feuille de sujet imprimée, page photographiée en rotation)*

École Normale d'Enseignement Technique et Professionnel (ENETP) / Bamako

**Théorie d'Élasticité / Génie Civil (GC) / Licence / Semestre 4 / 2021-2022** — 4 octobre 2024

![](figs/fig-p87-figure5a.png)

![](figs/fig-p87-figure5b.png)

<center>FIGURE 5 – a : Exercice 13, b : Exercice 14</center>

La Fig. 5.b représente une plaque dans le plan $(x,\ y)$. Elle a une longueur $\ell$, une hauteur $h$ et une épaisseur $t$, le matériau constitutif a un module de Young $E$ et un coefficient de Poisson $\nu$. La plaque est soumise aux contraintes $\sigma_{xx}$, $\sigma_{yy}$ et $\sigma_{xy}$. Sur les côtés inférieur $(y = 0)$ et gauche $(x = 0)$, la plaque s'appuie contre un support rigide mais qui autorise le glissement dans le plan. Les faces arrière et avant sont libres de toute contrainte.

On prendra $E = 210.0$ GPa, $\nu = 0.3$, $\sigma_{xx} = 35.0$ MPa, $\sigma_{yy} = 75.0$ MPa et $\sigma_{xy} = 20.0$ MPa.

1. (3 points) Calculer les composantes du tenseur des déformations.
2. (2 points) Représenter les cercles de Mohr et en déduire les contraintes principales ainsi que la contrainte de cisaillement maximale
3. (2 points) Calculer la contrainte équivalente de von Mises ainsi que celle de Tresca et comparer les deux contraintes équivalentes.

*— page 88 — (feuille de sujet imprimée, haut de page tronqué)*

…et $t_{0}$. La structure est soumise à une traction suivant la direction $x$, comme indiqué sur la Fig. 2.a. Le matériau constitutif, considéré comme homogène, isotrope et ayant un comportement élastique linéaire, a un module de Young $E$ et un coefficient de Poisson $\nu$.

1. Expliquer brièvement l'effet Poisson.
2. Exprimer, en fonction de $\ell$, de $\ell_{0}$ et de $\nu$, les composantes du tenseur des déformations infinitésimales.
3. Exprimer, en fonction de $\ell$, de $\ell_{0}$ et de $E$, les composantes du tenseur des contraintes.
4. Montrer que l'on peut établir la relation suivante entre le module de Young $E$ et les paramètres de Lamé, $\lambda$ et $\mu$ :

$$\lambda(1 - 2\nu) + 2\mu = E$$

![](figs/fig-p88-figure2a.png)

*— page 89 — (feuille de sujet imprimée)*

![](figs/fig-p89-figure2b.png)

<center>…2 – a : Exercice 4 ; b : Exercice 5</center>

### Exercice 5 : Etat plan de contrainte

En un point donné d'un solide, l'état de contrainte, considéré comme plan, est représenté sur la Fig. 2.b. Le matériau est isotrope et homogène, il a un comportement élastique linéaire. Le module de Young du matériau $E = 210$ GPa et un coefficient de Poisson $\nu = 0.34$.

1. Donner un exemple de structure où l'on peut rencontrer un état plan de contrainte.
2. Comparer la contrainte équivalente de von Mises et celle de Tresca.
3. Calculer le tenseur des déformations infinitésimales.
4. L'état de déformation est-il plan ?

*…Exercice 6 : Critère de Mohr-Coulomb*

*— page 90 — (feuille de sujet imprimée — cliché identique à la page 89)*

![](figs/fig-p89-figure2b.png)

<center>…2 – a : Exercice 4 ; b : Exercice 5</center>

### Exercice 5 : Etat plan de contrainte

En un point donné d'un solide, l'état de contrainte, considéré comme plan, est représenté sur la Fig. 2.b. Le matériau est isotrope et homogène, il a un comportement élastique linéaire. Le module de Young du matériau $E = 210$ GPa et un coefficient de Poisson $\nu = 0.34$.

1. Donner un exemple de structure où l'on peut rencontrer un état plan de contrainte.
2. Comparer la contrainte équivalente de von Mises et celle de Tresca.
3. Calculer le tenseur des déformations infinitésimales.
4. L'état de déformation est-il plan ?

*…Exercice 6 : Critère de Mohr-Coulomb*

*— page 91 —*

![](figs/fig-p91-kgb.png)

