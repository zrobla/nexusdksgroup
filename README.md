# NEXUS DKS GROUP — ENTRETIEN · Site web

Site vitrine statique (HTML/CSS/JS, sans runtime) **dédié aux services d'entretien
professionnel** de NEXUS DKS GROUP — Cotonou, Bénin. Conception : **TECH & WEB**.

## Direction artistique

« Éditorial clean-tech ». Charte issue des créas client + brochure + logo :
**Indigo `#2B338C` + Navy `#070B4E` + Lime `#9CC63D`** (aplats, sans gradients
intempestifs), touches azur/or du logo. Typo : **Bricolage Grotesque** (titres),
**Hanken Grotesk** (texte), **Caveat** (slogan manuscrit « nous valorisons vos
espaces »). Composants & icônes **propres** (SVG maison), volontairement distincts
du site JERU GROUP.

Slogan : « Nous ne faisons pas que nettoyer, **nous valorisons vos espaces**. »
Ton éditorial : technique secteur (≈50 %) + marketing émotionnel (≈25 %) +
commercial (≈25 %). Contenu refondu d'après **BROCHURE NEXUS.pdf**.

## Pages

- `index.html` — accueil (hero agent détouré, prestations, équipements, méthode,
  engagement qualité « 0 défaut – 100 % », B2C/B2B, témoignages, blog, contact).
- `nos-services.html` — 6 domaines de prestations (numérotés) + équipements + méthode.
- `entretien-proprete.html` — **Offre & formules** (catalogue détaillé, formules
  Essentiel / Confort / Pro, zones d'intervention).
- `about.html` — Notre Groupe : présentation, vision, valeurs, apports + section
  « autres activités du groupe » (BTP, immobilier, commerce, agro, événementiel, conseil).
- `blog.html` + `blog/*.html` — 3 articles experts (bionettoyage, fin de chantier, textiles).
- `contact.html`, `404.html`.

## Assets

- `css/nexus-premium.css` — socle de mise en page (grille/typo/structure). Ne pas réécrire.
- `css/nexus-brand.css` — **système de design NEXUS** (palette, composants `.nx-*`,
  icônes, responsive). **Éditer ici.**
- `js/nexus-site.js` — nav, dropdowns, reveal, formulaire (→ `formsubmit.co/ajax/Contact@nexusdksgroup.com`).
- `img/` — `brand/` (logo détouré, favicons, carte OG), `equip/` (équipements extraits
  du PDF), `people/` (agents détourés du PDF), `services/`, `gallery/`.
- Sources non versionnées : `BROCHURE NEXUS.pdf`, `photo_*.jpg`, `video_*.mp4`.

## Régénérer

```bash
python3 build_nexus.py        # régénère TOUTES les pages (idempotent)
```

Le contenu vit dans `build_nexus.py` (chrome partagé, données structurées : `CATS`,
`EQUIP`, `METHOD`, `VALUES`, `OTHER`, `ARTICLES`, `ARTICLE_BODY`). Les `.html` sont
des artefacts générés. Icônes SVG dans le dict `_I` / `ico()`.

## Déploiement

FTP manuel (miroir des chemins, dont `blog/`). `.htaccess` : HTTPS, non-www,
compression, cache long, en-têtes de sécurité. **Renommer les assets CSS/JS** en cas
de modification (cache 1 an).

Contact : C/34 Guinkomey, 03 BP 3903, Cotonou (Bénin) ·
+229 01 52 62 92 56 / 01 65 90 73 11 · Contact@nexusdksgroup.com
