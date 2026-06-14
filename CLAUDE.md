# CLAUDE.md — Site NEXUS DKS GROUP (directives projet)

> Guidance pour Claude Code (terminal **et** extension VSCodium) sur ce dépôt.
> Les règles de sécurité globales (`~/.claude/CLAUDE.md`) et les standards agence (`~/CLAUDE.md`,
> §5.5 à §5.8) **s'appliquent et priment**. Ce fichier rappelle l'essentiel propre à NEXUS, au plus
> près du code.

## Nature du dépôt
Site **vitrine statique** de **NEXUS DKS GROUP** — entreprise d'entretien de **droit béninois**,
Cotonou (Bénin). Marque bleu indigo / navy / or / lime. Tout le HTML est produit par le script
`build_nexus.py` à partir de structures de données (pages, services, articles). Funnel **WhatsApp**
(`wa.me`) sans capture de lead ; devis en **FCFA** sous 24 h. Langue de sortie : **français**.

## 1) Build & cache-busting
- Régénérer le site avec `python3 build_nexus.py` (jamais éditer les `.html` générés à la main —
  modifier `build_nexus.py` puis rebuild).
- **Bumper `ASSETV`** à chaque déploiement d'assets (cache `.htaccess` 1 an) — sinon « les
  changements n'apparaissent pas » (faux bug récurrent).

## 2) SEO (cf. `~/CLAUDE.md` §5.5) — implémenté dans le balisage, vendu en bénéfices
1 seul `<h1>` par page ; JSON-LD valide (Organization, WebSite, BreadcrumbList, BlogPosting) ;
`og:type` correct ; canonical ; `sitemap.xml`, `robots.txt` (crawlers IA) et `llms.txt` générés
depuis les **mêmes données** que les pages. En communication client, parler **visibilité moteurs +
assistants IA**, pas artefacts.

## 3) Sécurité GPU mobile (≤ 991px) — anti-crash compositeur
Sur composants interactifs mobiles : **pas** de `backdrop-filter`, **pas** de `:has()` (utiliser des
classes JS), cases à cocher dessinées en CSS (pas `accent-color`), ombres/animations allégées.
Régression déjà corrigée — ne pas réintroduire.

## 4) Git / workflow
- **Ne pas committer/pousser automatiquement** : accumuler plusieurs implémentations puis demander
  validation avant commit (préférence utilisateur).
- Auteur = `zrobla` uniquement, **aucun** trailer `Co-Authored-By` ni mention IA
  (cf. `~/.claude/CLAUDE.md` §D). Pas de push/publication sans accord explicite.

## 5) Portfolio
Le travail livré pour NEXUS est référencé en étude de cas sur le **site Tech & Web**
(`~/Documents/GitRepo/'TECH & WEB'/portfolio/`) — voir la policy §5.7 de `~/CLAUDE.md` et le
`CLAUDE.md` de ce repo. À mettre à jour si NEXUS évolue significativement.
