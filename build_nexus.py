# -*- coding: utf-8 -*-
"""
Générateur du site NEXUS DKS GROUP — ENTRETIEN (TECH & WEB).
Site statique FR centré sur les services d'entretien professionnel.
Design "éditorial clean-tech" : indigo + navy + lime (aplats), icônes & cartes
propres (distinctes de JERU). Contenu rehaussé : technique (50%) + émotionnel
(25%) + commercial (25%). Régénère toutes les pages : python3 build_nexus.py
"""
import os
import json
from urllib.parse import quote

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE = {
    "name": "NEXUS DKS GROUP",
    "domain": "https://nexusdksgroup.com",
    "email": "Contact@nexusdksgroup.com",
    "tel1_disp": "+229 01 52 62 92 56",
    "tel1_href": "+2290152629256",
    "tel2_disp": "+229 01 65 90 73 11",
    "tel2_href": "+2290165907311",
    "wa": "2290152629256",
    "addr": "C/34 Guinkomey, 03 BP 3903, Cotonou (Bénin)",
    "year": "2026",
}

# Version des assets (cache-busting) — à incrémenter à chaque modif CSS/JS.
ASSETV = "20260606t"

# ---------------------------------------------------------------- Icônes SVG
_I = {
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "send": '<path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7z"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 2 .7 2.9a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.1-1.1a2 2 0 0 1 2.1-.5c.9.3 1.9.6 2.9.7A2 2 0 0 1 22 16.9z"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 "pin": '<path d="M12 21s-7-5.5-7-11a7 7 0 0 1 14 0c0 5.5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "message": '<path d="M21 11.5a8.5 8.5 0 0 1-12.3 7.6L3 21l1.9-5.7A8.5 8.5 0 1 1 21 11.5z"/>',
 "building": '<path d="M3 21h18M6 21V4h9v17M15 9h3v12"/><path d="M9 8h2M9 12h2M9 16h2"/>',
 "hardhat": '<path d="M2 18h20M4 18a8 8 0 0 1 16 0"/><path d="M10 6a2 2 0 0 1 4 0v3M8 9.2V7M16 9.2V7"/>',
 "home": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M9.5 21v-6h5v6"/>',
 "utensils": '<path d="M5 3v7a2 2 0 0 0 4 0V3M7 11v10M16 3c-1.5 0-3 1.5-3 4s1.5 4 3 4v10"/>',
 "film": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M3 15h18M8 4v16M16 4v16"/>',
 "sofa": '<path d="M5 11V8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v3"/><path d="M3 12a2 2 0 0 1 2 2v3h14v-3a2 2 0 0 1 2-2 2 2 0 0 0-2 2v1H5v-1a2 2 0 0 0-2-2z"/><path d="M6 17v2M18 17v2"/>',
 "wind": '<path d="M3 8h11a3 3 0 1 0-3-3M3 16h15a3 3 0 1 1-3 3M3 12h7"/>',
 "droplet": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
 "disc": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="2.5"/>',
 "spray": '<path d="M9 11h6l1 9a2 2 0 0 1-2 2h-4a2 2 0 0 1-2-2l1-9z"/><path d="M9 11V7h5"/><path d="M14 4h2M17 6h1.5M16 8.2h2"/>',
 "flask": '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/><path d="M7.5 15h9"/>',
 "broom": '<path d="m13 11 6-6"/><path d="M4 20c3 0 5-1 6-4l3 1c-1 3-3 5-6 5l-3-2z"/><path d="m10 13 3 3"/>',
 "shield": '<path d="M12 3 5 6v6c0 4 3 7 7 9 4-2 7-5 7-9V6l-7-3z"/><path d="m9 12 2 2 4-4"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "star": '<path d="m12 3 2.6 5.5 6 .8-4.4 4.2 1.1 6L12 16.8 6.7 19.5l1.1-6L3.4 9.3l6-.8L12 3z"/>',
 "smile": '<circle cx="12" cy="12" r="9"/><path d="M8 14a4 4 0 0 0 8 0"/><path d="M9 9.5h.01M15 9.5h.01"/>',
 "leaf": '<path d="M11 20A7 7 0 0 1 4 13c0-5 4-9 16-9 0 10-5 16-11 16z"/><path d="M9 18c2-5 5-7 8-8"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
 "clipboard": '<rect x="6" y="4" width="12" height="17" rx="2"/><path d="M9 4V3h6v1"/><path d="M9 10h6M9 14h6M9 18h3"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 5.5a3.5 3.5 0 0 1 0 7M22 20a6.5 6.5 0 0 0-5-6.3"/>',
 "badge": '<circle cx="12" cy="9" r="6"/><path d="m9.2 9 2 2 3.6-3.6"/><path d="M8 14l-1 7 5-3 5 3-1-7"/>',
 "thumb": '<path d="M7 11v9H4a1 1 0 0 1-1-1v-7a1 1 0 0 1 1-1h3z"/><path d="M7 11l4-8a2 2 0 0 1 3 2l-1 4h5a2 2 0 0 1 2 2.4l-1.5 7A2 2 0 0 1 17 21H7"/>',
 "sparkle": '<path d="M12 3v6M9 6h6M5 13v4M3 15h4M16 11l1.5 3.5L21 16l-3.5 1.5L16 21l-1.5-3.5L11 16l3.5-1.5L16 11z"/>',
 "cart": '<circle cx="9" cy="20" r="1.4"/><circle cx="17" cy="20" r="1.4"/><path d="M3 4h2l2.4 12.4a1 1 0 0 0 1 .8h8.7a1 1 0 0 0 1-.8L21 8H6"/>',
 "tower": '<path d="M12 2 8 6v15h8V6l-4-4z"/><path d="M8 21V11l-3 2v8M16 21V11l3 2v8"/>',
 "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 9h18M8 3v4M16 3v4"/>',
 "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 12h18"/>',
 "target": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="0.6"/>',
 "refresh": '<path d="M3 12a9 9 0 0 1 15-6.7L21 8M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-15 6.7L3 16M3 21v-5h5"/>',
 "down": '<path d="m6 9 6 6 6-6"/>',
 "scale": '<path d="M12 3v18M5 7h14M7 7l-3 7a3 3 0 0 0 6 0L7 7zM17 7l-3 7a3 3 0 0 0 6 0l-3-7z"/>',
 "link": '<path d="M10 13a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 11a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/>',
 "download": '<path d="M12 3v12m0 0 4-4m-4 4-4-4"/><path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2"/>',
 "rocket": '<path d="M5 15c-1.5 1-2 4-2 4s3-.5 4-2a2.8 2.8 0 0 0-2-2z"/><path d="M9 15l-3-3c1-5 5-9 11-9 0 6-4 10-9 11z"/><circle cx="14.5" cy="9.5" r="1.5"/>',
 "heart": '<path d="M12 20S4 14.5 4 9a4 4 0 0 1 8-1 4 4 0 0 1 8 1c0 5.5-8 11-8 11z"/>',
 "graduation": '<path d="M2 9l10-4 10 4-10 4z"/><path d="M6 11v4c0 1.5 2.7 3 6 3s6-1.5 6-3v-4"/>',
}
def ico(name, cls=""):
    c = "nx-svg" + ((" " + cls) if cls else "")
    return '<svg class="%s" viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % (c, _I.get(name, _I["check"]))

SOCIAL = {
 "facebook": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 22v-8.1h2.7l.4-3.2h-3.1V8.7c0-.9.2-1.6 1.6-1.6H17V4.2c-.4-.1-1.5-.2-2.8-.2-2.8 0-4.7 1.7-4.7 4.8v2H6.8v3.2h2.7V22h4Z"/></svg>',
 "instagram": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5Zm0 2.3A2.7 2.7 0 0 0 4.3 7v10A2.7 2.7 0 0 0 7 19.7h10a2.7 2.7 0 0 0 2.7-2.7V7A2.7 2.7 0 0 0 17 4.3H7Zm10.2 1.5a1.1 1.1 0 1 1 0 2.2 1.1 1.1 0 0 1 0-2.2ZM12 7a5 5 0 1 1 0 10 5 5 0 0 1 0-10Zm0 2.3A2.7 2.7 0 1 0 12 14.7 2.7 2.7 0 0 0 12 9.3Z"/></svg>',
 "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.9 8.1A1.9 1.9 0 1 1 4.9 4a1.9 1.9 0 0 1 0 4.1ZM3.2 9.6h3.3V20H3.2V9.6Zm5.1 0h3.2V11h.1c.4-.8 1.6-1.7 3.4-1.7 3.6 0 4.3 2.4 4.3 5.5V20H16v-4.6c0-1.1 0-2.6-1.6-2.6s-1.8 1.2-1.8 2.5V20H8.3V9.6Z"/></svg>',
 "whatsapp": '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C9 3 3.3 8.7 3.3 15.7c0 2.4.7 4.7 1.9 6.7L3 29l6.8-2.1c1.9 1 4 1.6 6.2 1.6 7 0 12.7-5.7 12.7-12.7S23 3 16 3Zm0 23c-1.9 0-3.7-.5-5.3-1.5l-.4-.2-3.9 1.2 1.2-3.8-.3-.4c-1.1-1.7-1.6-3.6-1.6-5.6C5.7 10 10.3 5.4 16 5.4S26.3 10 26.3 15.7 21.7 26 16 26Zm5.7-7.5c-.3-.2-1.8-.9-2.1-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.2-1.3-.5-2.5-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.5-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.4s1.1 2.8 1.2 3c.2.2 2.1 3.2 5 4.5.7.3 1.2.5 1.7.6.7.2 1.3.2 1.8.1.6-.1 1.8-.7 2-1.4.3-.7.3-1.3.2-1.4-.1-.1-.3-.2-.6-.4Z"/></svg>',
}

# ---------------------------------------------------------------- Données
# Catégories de prestations (issues de la brochure, contenu rehaussé)
CATS = [
 ("entreprises-bureaux", "Entreprises & Bureaux", "building",
  "Des environnements de travail sains, valorisants et propices à la performance — entretien régulier piloté par un plan de propreté.",
  ["Bionettoyage des plans de travail et surfaces partagées",
   "Désinfection ciblée des points de contact à fort passage",
   "Sanitaires, parties communes et réassort des consommables",
   "Plan de propreté contractuel et passages planifiés"]),
 ("fin-de-chantier", "Fin de Chantier", "hardhat",
  "La remise en état post-travaux qui transforme un chantier livré en espace prêt à occuper, sans la moindre trace.",
  ["Dépose et évacuation des résidus de construction",
   "Décollage de films, traces de peinture, laitance et poussières fines",
   "Nettoyage approfondi des vitrages, sols et menuiseries",
   "Réception « prête à occuper » avant remise des clés"]),
 ("residences", "Résidences & Appartements", "home",
  "Votre intérieur soigné comme il le mérite — la sérénité d'un refuge impeccable, sans y penser.",
  ["Nettoyage complet ou grand ménage de remise à neuf",
   "Entretien ponctuel ou récurrent selon votre rythme de vie",
   "Sols, sanitaires, cuisine, vitrerie intérieure",
   "Réservation simple par téléphone ou WhatsApp"]),
 ("restaurants-lounges", "Restaurants & Lounges", "utensils",
  "L'hygiène irréprochable qui protège votre réputation et celle de vos clients, dans le respect des bonnes pratiques alimentaires.",
  ["Dégraissage des surfaces, plans et équipements de cuisine",
   "Entretien des salles, terrasses et espaces d'accueil",
   "Protocoles d'hygiène compatibles avec les normes du secteur",
   "Interventions en horaires décalés, hors service"]),
 ("espaces-specifiques", "Espaces Spécifiques", "film",
  "Des lieux à forte fréquentation entretenus avec des protocoles dédiés : confort, sécurité et image au rendez-vous.",
  ["Salles de cinéma, de conférence et de spectacle",
   "Salles de fête et espaces événementiels",
   "Protocoles adaptés aux établissements recevant du public (ERP)",
   "Remise en état express entre deux événements"]),
 ("textiles-surfaces", "Textiles & Surfaces", "sofa",
  "La technicité du nettoyage en profondeur : redonner éclat et hygiène à vos textiles et revêtements.",
  ["Shampouinage et détachage des canapés et fauteuils",
   "Traitement des moquettes par injection-extraction",
   "Désinfection et assainissement des matelas",
   "Traitement des surfaces dures et cristallisation des sols"]),
]
CATMAP = {c[0]: c for c in CATS}

EQUIP = [
 ("aspirateur.jpg", "Aspirateur industriel", "wind", "Aspiration puissante poussières & liquides."),
 ("injecteur.jpg", "Injecteur / extracteur", "droplet", "Nettoyage en profondeur des textiles."),
 ("monobrosse.jpg", "Monobrosse professionnelle", "disc", "Décapage, lustrage et cristallisation."),
 ("haute-pression.jpg", "Nettoyeur haute pression", "spray", "Façades, sols extérieurs et zones techniques."),
 ("produits.jpg", "Produits spécialisés", "flask", "Gammes pro adaptées à chaque support."),
 ("accessoires.jpg", "Accessoires & consommables", "broom", "Matériel d'appoint et équipements de protection."),
]

METHOD = [
 ("Analyse du besoin", "search", "Écoute, qualification et lecture fine de vos contraintes d'exploitation."),
 ("Visite du site", "pin", "Diagnostic terrain, métrage et repérage des points sensibles."),
 ("Proposition personnalisée", "clipboard", "Cahier des charges, protocoles et devis transparent en FCFA."),
 ("Intervention encadrée", "users", "Équipe formée, matériel professionnel, horaires adaptés à votre activité."),
 ("Contrôle qualité", "badge", "Auto-contrôle rigoureux et vérification après chaque passage."),
 ("Validation client", "thumb", "Suivi de satisfaction, traçabilité et amélioration continue."),
]

VALUES = [
 ("Professionnalisme", "briefcase"), ("Rigueur", "target"), ("Discipline", "shield"),
 ("Respect du client", "users"), ("Sens du détail", "sparkle"),
 ("Formation continue", "refresh"), ("Contrôle interne", "clipboard"),
]

# Autres activités du groupe (page Notre Groupe uniquement)
OTHER = [
 ("BTP & Travaux Publics", "tower", "Bâtiment, gros œuvre, second œuvre et travaux publics, pilotés du terrassement à la finition."),
 ("Rénovation & Immobilier", "home", "Rénovation, promotion et gestion immobilière, mise à disposition et valorisation de biens."),
 ("Commerce & Import-Export", "cart", "Commerce général, négoce, import-export et approvisionnement sécurisé."),
 ("Agro, Élevage & Alimentation", "leaf", "Exploitation agricole, élevage, poissonnerie, restauration et tourisme."),
 ("Événementiel & Logistique", "calendar", "Ingénierie événementielle, logistique, transport et gestion de manifestations."),
 ("Conseil & Business", "scale", "Conseil en gestion, finance, marketing, intermédiation et création de marque de mode."),
]

# Articles de blog
ARTICLES = [
 ("bionettoyage-bureaux", "Hygiène pro",
  "Bionettoyage en entreprise : pourquoi les points de contact changent tout",
  "Poignées, interrupteurs, claviers, ascenseurs… Ces surfaces invisibles concentrent l'essentiel des transmissions. Décryptage d'une approche qui dépasse le simple nettoyage.",
  "img/services/blog-bionettoyage.jpg", "8 min"),
 ("fin-de-chantier-checklist", "Chantier",
  "Réussir le nettoyage de fin de chantier : la checklist d'une remise en état impeccable",
  "Entre la dernière finition et la remise des clés se joue la première impression. Voici la méthode pour livrer un espace « prêt à occuper », sans reprise.",
  "img/services/blog-fin-chantier.jpg", "7 min"),
 ("moquettes-injection-extraction", "Techniques",
  "Moquettes & textiles : injection-extraction ou shampouinage, que choisir ?",
  "Deux techniques, deux résultats. Comprendre leurs principes pour préserver vos revêtements et prolonger leur durée de vie.",
  "img/services/blog-textiles.jpg", "6 min"),
 ("hygiene-restaurants-argument", "Restauration",
  "Restaurants & lounges : l'hygiène, votre meilleur argument commercial",
  "En salle comme en cuisine, la propreté se voit, se sent et se raconte. Comment en faire un levier de réputation et de fidélité.",
  "img/services/blog-restaurants-hygiene.jpg", "6 min"),
 ("externaliser-entretien-entreprise", "Conseil",
  "Externaliser l'entretien de votre entreprise : 6 bénéfices concrets",
  "Temps gagné, image soignée, coûts maîtrisés : pourquoi confier sa propreté à un prestataire structuré change la donne.",
  "img/services/blog-externalisation.jpg", "7 min"),
 ("proximite-technologie-nexus", "Innovation",
  "Au plus proche de vos espaces : quand la technologie réduit les distances",
  "Contact de proximité, demandes pré-qualifiées, pilotage interne informatisé : comment NEXUS raccourcit le chemin entre votre besoin et l'intervention.",
  "img/services/blog-tech-proximite.jpg", "8 min"),
]

# ---------------------------------------------------------------- Chrome
def head(title, desc, path, page_class, prefix=""):
    canonical = SITE["domain"] + "/" + (path if path != "index.html" else "")
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="author" content="NEXUS DKS GROUP">
<meta name="designer" content="Tech &amp; Web — tech-and-web.com">
<link rel="author" href="https://tech-and-web.com">
<meta name="format-detection" content="telephone=no">
<meta name="theme-color" content="#070b4e">
<link rel="canonical" href="__CANON__">
<link rel="icon" href="__P__favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="__P__favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="__P__apple-touch-icon.png">
<link rel="manifest" href="__P__site.webmanifest">
<meta property="og:site_name" content="NEXUS DKS GROUP">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_BJ">
<meta property="og:title" content="__TITLE__">
<meta property="og:description" content="__DESC__">
<meta property="og:url" content="__CANON__">
<meta property="og:image" content="__DOMAIN__/img/brand/nexus-og-card.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="__DOMAIN__/img/brand/nexus-og-card.jpg">
<link href="__P__vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
<link href="__P__css/nexus-premium.css?v=__V__" rel="stylesheet">
<link href="__P__css/nexus-brand.css?v=__V__" rel="stylesheet">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":["Organization","ProfessionalService"],"name":"NEXUS DKS GROUP","alternateName":"NEXUS DKS GROUP - ENTRETIEN","url":"__DOMAIN__/","logo":"__DOMAIN__/img/brand/nexus-logo.png","image":"__DOMAIN__/img/brand/nexus-og-card.jpg","email":"__EMAIL__","telephone":"__TEL__","slogan":"Nous ne faisons pas que nettoyer, nous valorisons vos espaces.","description":"Entreprise de droit béninois spécialisée dans les services d'entretien professionnel, basée à Cotonou et intervenant à Cotonou, ses environs et dans tout le Bénin : entreprises, commerces, résidences et chantiers.","address":{"@type":"PostalAddress","streetAddress":"C/34 Guinkomey, 03 BP 3903","addressLocality":"Cotonou","addressCountry":"BJ"},"areaServed":"Bénin"}
</script>
</head>
""".replace("__TITLE__", title).replace("__DESC__", desc).replace("__CANON__", canonical)\
   .replace("__DOMAIN__", SITE["domain"]).replace("__EMAIL__", SITE["email"])\
   .replace("__TEL__", "+" + SITE["tel1_href"].lstrip("+")).replace("__V__", ASSETV).replace("__P__", prefix)

def header(active, prefix=""):
    cat_items = ""
    for slug, label, *_ in CATS:
        cat_items += '<li role="none"><a class="nav-dropdown-link" href="%sservices/%s.html" role="menuitem">%s</a></li>\n' % (prefix, slug, label)
    cat_items += '<li role="none"><a class="nav-dropdown-link" href="%sentretien-proprete.html" role="menuitem">Offre &amp; formules &rarr;</a></li>\n' % prefix
    a = lambda k: " is-active" if active == k else ""
    serv = " is-active" if active in ("services", "offre") else ""
    return """<body class="__PC__">
<a class="skip-link" href="#main">Aller au contenu</a>
<header class="site-header">
  <div class="container">
    <div class="header-inner">
      <a class="site-brand" href="__P__index.html" aria-label="NEXUS DKS GROUP — accueil">
        <img class="site-logo-full" src="__P__img/brand/nexus-logo.png" alt="NEXUS DKS GROUP — Entretien" width="230" height="52">
      </a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Ouvrir la navigation"><span></span><span></span><span></span></button>
      <nav class="site-nav" id="site-nav" aria-label="Navigation principale">
        <a class="nav-link__HOME__" href="__P__index.html">Accueil</a>
        <a class="nav-link__ABOUT__" href="__P__about.html">Notre Groupe</a>
        <div class="nav-dropdown nav-dropdown-split">
          <div class="nav-dropdown-head">
            <a class="nav-link nav-link-parent__SERV__" href="__P__nos-services.html">Nos Services</a>
            <button class="nav-link nav-dropdown-toggle nav-dropdown-toggle-icon" type="button" aria-expanded="false" aria-controls="serv-menu" aria-haspopup="true" aria-label="Afficher les services">__DOWN__</button>
          </div>
          <ul class="nav-dropdown-menu nav-dropdown-menu-list" id="serv-menu" role="menu">
__ITEMS__          </ul>
        </div>
        <a class="nav-link__BLOG__" href="__P__blog.html">Blog</a>
        <a class="nav-link__CONTACT__" href="__P__contact.html">Contact</a>
        <a class="nav-cta" href="__P__contact.html">__SEND__ Devis gratuit</a>
      </nav>
    </div>
  </div>
</header>
<main id="main">
""".replace("__PC__", "").replace("__P__", prefix).replace("__ITEMS__", cat_items)\
   .replace("__HOME__", a("home")).replace("__ABOUT__", a("about")).replace("__SERV__", serv)\
   .replace("__BLOG__", a("blog")).replace("__CONTACT__", a("contact"))\
   .replace("__DOWN__", ico("down")).replace("__SEND__", ico("send"))

def footer(prefix=""):
    cat_links = "".join('<a href="%sservices/%s.html">%s</a>\n' % (prefix, s, l) for s, l, *_ in CATS)
    return """</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a class="site-brand" href="__P__index.html" aria-label="NEXUS DKS GROUP"><img class="site-logo-full" src="__P__img/brand/nexus-logo.png" alt="NEXUS DKS GROUP" width="250" height="58"></a>
        <p>Entretien professionnel à Cotonou et ses environs. Nous accompagnons entreprises, commerces, résidences et chantiers vers des espaces propres, sains et valorisés.</p>
        <p class="nx-script">Nous valorisons vos espaces.</p>
        <div class="footer-social">
          <a href="https://wa.me/__WA__" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">__S_WA__</a>
          <a href="#" aria-label="Facebook">__S_FB__</a>
          <a href="#" aria-label="Instagram">__S_IG__</a>
          <a href="#" aria-label="LinkedIn">__S_LI__</a>
        </div>
      </div>
      <div class="footer-nav-group">
        <div class="footer-nav"><h4>Nos services</h4>
__CATS__          <a href="__P__entretien-proprete.html">Offre &amp; formules</a>
        </div>
        <div class="footer-nav"><h4>Le groupe</h4>
          <a href="__P__about.html">Notre Groupe</a>
          <a href="__P__carrieres.html">Carrières</a>
          <a href="__P__blog.html">Blog</a>
          <a href="__P__contact.html">Contact</a>
          <a href="__P__nexus-dks-group-presentation.pdf" download>__I_DL__ Brochure (PDF)</a>
        </div>
        <div class="footer-nav"><h4>Contact</h4>
          <a href="tel:__T1H__">__I_PH__ __T1D__</a>
          <a href="tel:__T2H__">__I_PH__ __T2D__</a>
          <a href="mailto:__EMAIL__">__I_ML__ __EMAIL__</a>
          <span class="footer-address">__I_PIN__ __ADDR__</span>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; __YEAR__ NEXUS DKS GROUP — ENTRETIEN · Cotonou, Bénin</span>
      <a class="site-credit" href="https://tech-and-web.com" target="_blank" rel="noopener noreferrer">Conception : TECH &amp; WEB</a>
    </div>
  </div>
</footer>
<a class="whatsapp-float" href="https://wa.me/__WA__" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">__S_WA__</a>
<button class="scroll-top-btn" aria-label="Retour en haut" type="button"><svg viewBox="0 0 24 24"><polyline points="18 15 12 9 6 15"></polyline></svg></button>
<script src="__P__js/nexus-site.js?v=__V__" defer></script>
</body></html>""".replace("__V__", ASSETV).replace("__P__", prefix).replace("__WA__", SITE["wa"]).replace("__CATS__", cat_links)\
   .replace("__S_WA__", SOCIAL["whatsapp"]).replace("__S_FB__", SOCIAL["facebook"]).replace("__S_IG__", SOCIAL["instagram"]).replace("__S_LI__", SOCIAL["linkedin"])\
   .replace("__T1H__", SITE["tel1_href"]).replace("__T1D__", SITE["tel1_disp"]).replace("__T2H__", SITE["tel2_href"]).replace("__T2D__", SITE["tel2_disp"])\
   .replace("__EMAIL__", SITE["email"]).replace("__ADDR__", SITE["addr"]).replace("__YEAR__", SITE["year"])\
   .replace("__I_PH__", ico("phone")).replace("__I_ML__", ico("mail")).replace("__I_PIN__", ico("pin")).replace("__I_DL__", ico("download"))

# ---------------------------------------------------------------- Sections réutilisables
def cta(prefix="", title="Confiez-nous vos espaces dès aujourd'hui",
        text="Décrivez votre besoin : nous réalisons un diagnostic et vous adressons une proposition claire, chiffrée en FCFA, sous 24&nbsp;heures."):
    return """<section class="section">
  <div class="container">
    <div class="nx-cta reveal">
      <span class="nx-eyebrow">Passons à l'action</span>
      <h2>%s</h2>
      <p>%s</p>
      <div class="nx-cta-row">
        <a class="btn-lime" href="%scontact.html">%s Demander un devis</a>
        <a class="btn-secondary" href="https://wa.me/%s" target="_blank" rel="noopener noreferrer">%s WhatsApp</a>
      </div>
    </div>
  </div>
</section>""" % (title, text, prefix, ico("send"), SITE["wa"], ico("message"))

def contact_section(prefix="", title="Parlons de vos espaces"):
    opts = "".join('<option>%s</option>' % l for _, l, *_ in CATS)
    return """<section id="contact" class="section section-dark">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Contact &amp; devis</span>
      <h2 class="section-title">__TITLE__</h2>
      <p class="section-copy">Un devis, un rappel, une visite de diagnostic ? Renseignez le formulaire ou joignez-nous directement. Réponse rapide, proposition claire en FCFA.</p>
    </div></div>
    <div class="contact-layout">
      <div class="form-shell reveal">
        <form id="contact-brief">
          <div class="form-grid">
            <div class="form-group"><label class="form-label" for="full-name">Nom complet</label><input class="form-control" id="full-name" name="full_name" type="text" placeholder="Vos nom et prénom"></div>
            <div class="form-group"><label class="form-label" for="company-name">Entreprise / structure</label><input class="form-control" id="company-name" name="company_name" type="text" placeholder="Société, résidence ou particulier"></div>
            <div class="form-group"><label class="form-label" for="phone-number">Téléphone</label><input class="form-control" id="phone-number" name="phone_number" type="text" placeholder="+229"></div>
            <div class="form-group"><label class="form-label" for="email-address">Email</label><input class="form-control" id="email-address" name="email_address" type="email" placeholder="nom@domaine.com"></div>
            <div class="form-group"><label class="form-label" for="client-type">Vous êtes</label><select class="form-control" id="client-type" name="client_type"><option value="">Choisir…</option><option>Particulier (B2C)</option><option>Entreprise / Institution (B2B)</option></select></div>
            <div class="form-group"><label class="form-label" for="project-type">Type de prestation</label><select class="form-control" id="project-type" name="project_type"><option value="">Choisir un service</option>__OPTS__<option>Autre besoin d'entretien</option></select></div>
            <div class="form-group full"><label class="form-label" for="project-message">Votre besoin</label><textarea class="form-control" id="project-message" name="project_message" placeholder="Lieu, surface approximative, fréquence souhaitée, échéance…"></textarea></div>
          </div>
          <p class="form-note">Plus votre demande est précise (surface, fréquence, contraintes d'accès), plus votre devis sera juste.</p>
          <div class="nx-cta-row"><button class="btn-lime" type="submit">__SEND__ Envoyer ma demande</button></div>
          <div class="form-success" hidden>Merci ! Votre demande est bien reçue. L'équipe NEXUS DKS GROUP vous recontacte rapidement.</div>
          <div class="form-error" hidden style="color:#ff9b9b;margin-top:12px;font-weight:600;"></div>
        </form>
      </div>
      <aside class="summary-card contact-summary reveal d1">
        <h3>Coordonnées directes</h3>
        <p>Pour une demande urgente, un seul réflexe : appelez ou écrivez-nous.</p>
        <div class="contact-points">
          <a class="contact-point" href="tel:__T1H__">__I_PH__<div><strong>Ligne principale</strong><span>__T1D__</span></div></a>
          <a class="contact-point" href="tel:__T2H__">__I_PH__<div><strong>Ligne secondaire</strong><span>__T2D__</span></div></a>
          <a class="contact-point" href="https://wa.me/__WA__" target="_blank" rel="noopener noreferrer">__I_MSG__<div><strong>WhatsApp</strong><span>Réponse rapide</span></div></a>
          <a class="contact-point" href="mailto:__EMAIL__">__I_ML__<div><strong>Email</strong><span>__EMAIL__</span></div></a>
          <div class="contact-point">__I_PIN__<div><strong>Adresse</strong><span>__ADDR__</span></div></div>
        </div>
        <div class="pill-row"><span class="pill">Cotonou</span><span class="pill">Bénin</span><span class="pill">B2C &amp; B2B</span></div>
      </aside>
    </div>
  </div>
</section>""".replace("__OPTS__", opts).replace("__TITLE__", title).replace("__SEND__", ico("send"))\
   .replace("__I_PH__", ico("phone")).replace("__I_ML__", ico("mail")).replace("__I_PIN__", ico("pin")).replace("__I_MSG__", ico("message"))\
   .replace("__T1H__", SITE["tel1_href"]).replace("__T1D__", SITE["tel1_disp"]).replace("__T2H__", SITE["tel2_href"]).replace("__T2D__", SITE["tel2_disp"])\
   .replace("__WA__", SITE["wa"]).replace("__EMAIL__", SITE["email"]).replace("__ADDR__", SITE["addr"])

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True) if os.path.dirname(path) else None
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("écrit:", path, "(%d Ko)" % (len(content) // 1024))


# ---------------------------------------------------------- Sections partagées
def section_method():
    steps = ""
    for i, (t, icon, d) in enumerate(METHOD):
        steps += '<div class="nx-step reveal%s"><span class="nx-step-num"></span><h4>%s</h4><p>%s</p></div>\n' % (" d%d" % (i % 3) if i % 3 else "", t, d)
    return """<section class="section">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Notre méthode</span>
      <h2 class="section-title">Chaque intervention suit un processus structuré</h2>
    </div></div>
    <div class="nx-method">%s</div>
  </div>
</section>""" % steps

def section_engage():
    return """<section class="section section-dark">
  <div class="container">
    <div class="nx-split">
      <div class="reveal">
        <span class="nx-eyebrow">Engagement qualité</span>
        <h2 class="section-title">Objectif : <span class="nx-mark">0 défaut, 100% de satisfaction</span></h2>
        <p class="section-copy">La qualité est au cœur de notre service. Nous ne livrons pas un passage, nous livrons une exigence — vérifiée, suivie et améliorée en continu.</p>
        <ul class="nx-list" style="margin-top:18px">
          <li>__CK__<span>Personnel formé en continu aux protocoles métier</span></li>
          <li>__CK__<span>Politique de contrôle interne des travaux après exécution</span></li>
          <li>__CK__<span>Suivi de la satisfaction client et traçabilité des passages</span></li>
          <li>__CK__<span>Démarche d'amélioration continue</span></li>
        </ul>
      </div>
      <div class="reveal d1">
        <div class="nx-grid cols-2" style="gap:16px">
          <div class="nx-card" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.1)"><span class="nx-ico is-navy">__I_CLOCK__</span><h3 style="color:#fff">Gain de temps</h3><p style="color:rgba(255,255,255,.74)">Vous vous concentrez sur votre cœur de métier.</p></div>
          <div class="nx-card" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.1)"><span class="nx-ico is-navy">__I_STAR__</span><h3 style="color:#fff">Meilleure image</h3><p style="color:rgba(255,255,255,.74)">Des espaces qui valorisent votre marque.</p></div>
          <div class="nx-card" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.1)"><span class="nx-ico is-navy">__I_LEAF__</span><h3 style="color:#fff">Environnement sain</h3><p style="color:rgba(255,255,255,.74)">Hygiène et bien-être au quotidien.</p></div>
          <div class="nx-card" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.1)"><span class="nx-ico is-navy">__I_SMILE__</span><h3 style="color:#fff">Tranquillité d'esprit</h3><p style="color:rgba(255,255,255,.74)">Un partenaire fiable, vraiment.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>""".replace("__CK__", ico("check")).replace("__I_CLOCK__", ico("clock")).replace("__I_STAR__", ico("star")).replace("__I_LEAF__", ico("leaf")).replace("__I_SMILE__", ico("smile"))


# ============================================================ ACCUEIL
def build_home():
    hero = """<section class="nx-hero nx-hero-slider" aria-roledescription="carrousel" aria-label="NEXUS DKS GROUP — présentation">
  <div class="container">
    <div class="nx-hero-track">

      <!-- Diapo 1 : image de marque / valorisation (tous publics) -->
      <article class="nx-hero-slide is-active" data-hero-slide aria-hidden="false">
        <div class="nx-hero-grid">
          <div>
            <span class="nx-eyebrow">NEXUS DKS GROUP — Entretien</span>
            <h1>L'entretien professionnel au service de votre <span class="accent">image</span>.</h1>
            <p class="lead">Entreprises, commerces, résidences et chantiers : nous garantissons des espaces propres, sains et valorisés, grâce à des équipes encadrées et un matériel de niveau professionnel.</p>
            <div class="nx-hero-cta">
              <a class="btn-lime" href="contact.html">__SEND__ Devis gratuit sous 24&nbsp;h</a>
              <a class="btn-secondary" href="nos-services.html">Découvrir nos services</a>
            </div>
            <div class="nx-hero-note"><span>__CK__ 0 défaut, 100% satisfaction</span><span>__CK__ Cotonou &amp; environs</span><span>__CK__ B2C &amp; B2B</span></div>
          </div>
          <div class="nx-hero-figure">
            <div class="nx-blob"></div>
            <img src="img/people/agent-homme.png" alt="Agent d'entretien professionnel NEXUS DKS GROUP" width="699" height="1018">
            <div class="nx-hero-chip tl"><span class="nx-ico is-lime">__I_SPARK__</span><div><strong>Espaces valorisés</strong><small>pas seulement nettoyés</small></div></div>
            <div class="nx-hero-chip br"><span class="nx-ico is-navy">__I_SHIELD__</span><div><strong>Équipe encadrée</strong><small>matériel professionnel</small></div></div>
          </div>
        </div>
      </article>

      <!-- Diapo 2 : entreprises &amp; institutions (B2B, partenaires) — layout immersif -->
      <article class="nx-hero-slide" data-hero-slide aria-hidden="true">
        <div class="nx-hero-immersive is-entreprises">
          <img class="nx-hero-immersive-bg" src="img/services/hero-entreprises.jpg" alt="" aria-hidden="true">
          <div class="nx-hero-immersive-copy">
            <span class="nx-eyebrow">Entreprises · Institutions · Partenaires</span>
            <h1>Des espaces sains, des équipes <span class="accent">performantes</span>.</h1>
            <p class="lead">Bureaux, sièges sociaux et établissements recevant du public : nos protocoles de bionettoyage et nos contrats d'entretien récurrent protègent la santé de vos collaborateurs — et l'image de votre marque.</p>
            <div class="nx-hero-cta">
              <a class="btn-lime" href="contact.html">__SEND__ Devis entreprise</a>
              <a class="btn-secondary" href="entretien-proprete.html">Nos formules pro</a>
            </div>
          </div>
          <div class="nx-hero-kpis">
            <div class="nx-kpi"><span class="nx-ico is-lime">__I_BLDG__</span><div><strong>B2B &amp; institutions</strong><small>contrats sur-mesure</small></div></div>
            <div class="nx-kpi"><span class="nx-ico is-navy">__I_USERS__</span><div><strong>Équipes encadrées</strong><small>agents formés &amp; assurés</small></div></div>
            <div class="nx-kpi"><span class="nx-ico is-gold">__I_TARGET__</span><div><strong>0 défaut</strong><small>100% satisfaction visée</small></div></div>
          </div>
        </div>
      </article>

      <!-- Diapo 3 : expertise &amp; bionettoyage (techniciens, pro, chantiers) — immersif premium -->
      <article class="nx-hero-slide" data-hero-slide aria-hidden="true">
        <div class="nx-hero-immersive is-expertise">
          <img class="nx-hero-immersive-bg" src="img/services/hero-bionettoyage.jpg" alt="" aria-hidden="true">
          <div class="nx-hero-immersive-copy">
            <span class="nx-eyebrow">Expertise technique · Chantiers</span>
            <h1>La <span class="accent">technicité</span> du propre, du détail à la finition.</h1>
            <p class="lead">Bionettoyage, injection-extraction, haute pression, nettoyage fin de chantier : des gestes encadrés et un matériel de niveau professionnel, pour des résultats que l'on voit… et que l'on mesure.</p>
            <div class="nx-hero-cta">
              <a class="btn-lime" href="nos-services.html">__ARR__ Nos équipements</a>
              <a class="btn-secondary" href="entretien-proprete.html">Offre &amp; formules</a>
            </div>
          </div>
          <div class="nx-hero-kpis">
            <div class="nx-kpi"><span class="nx-ico is-lime">__I_DROP__</span><div><strong>Bionettoyage</strong><small>désinfection des surfaces</small></div></div>
            <div class="nx-kpi"><span class="nx-ico is-navy">__I_SPRAY__</span><div><strong>Haute pression</strong><small>sols &amp; façades</small></div></div>
            <div class="nx-kpi"><span class="nx-ico is-gold">__I_SHIELD__</span><div><strong>Gestes encadrés</strong><small>protocoles &amp; EPI</small></div></div>
          </div>
        </div>
      </article>

    </div>

    <div class="nx-hero-controls">
      <button type="button" class="nx-hero-arrow is-prev" data-hero-prev aria-label="Diapositive précédente">__ARR__</button>
      <div class="nx-hero-dots" role="tablist" aria-label="Choisir une diapositive">
        <button type="button" class="nx-hero-dot is-active" data-hero-dot aria-label="Diapositive 1 : image de marque"></button>
        <button type="button" class="nx-hero-dot" data-hero-dot aria-label="Diapositive 2 : entreprises &amp; institutions"></button>
        <button type="button" class="nx-hero-dot" data-hero-dot aria-label="Diapositive 3 : expertise &amp; équipements"></button>
      </div>
      <button type="button" class="nx-hero-arrow is-next" data-hero-next aria-label="Diapositive suivante">__ARR__</button>
    </div>
  </div>
</section>""".replace("__SEND__", ico("send")).replace("__CK__", ico("check")).replace("__I_SPARK__", ico("sparkle")).replace("__I_SHIELD__", ico("shield")).replace("__I_BLDG__", ico("building")).replace("__I_USERS__", ico("users")).replace("__I_TARGET__", ico("target")).replace("__I_DROP__", ico("droplet")).replace("__I_SPRAY__", ico("spray")).replace("__I_DISC__", ico("disc")).replace("__ARR__", ico("arrow"))

    STATS = [
        ("briefcase", "is-lime", "6+", "axes d'interventions"),
        ("target",    "is-navy", "0&nbsp;défaut", "objectif qualité"),
        ("clock",     "is-gold", "24&nbsp;h", "votre devis en FCFA"),
        ("users",     "is-lime", "50+", "employés formés &amp; encadrés"),
    ]
    statbar = "".join('<div class="nx-statbar-item"><span class="nx-ico %s nx-ico-sm">%s</span><div><strong>%s</strong><span>%s</span></div></div>' % (cls, ico(name), num, lab) for name, cls, num, lab in STATS)
    pitch = """<section class="section compact">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Présentation</span>
      <h2 class="section-title">Nous ne faisons pas que nettoyer, <span class="nx-mark">nous valorisons vos espaces.</span></h2>
      <p class="section-copy">NEXUS DKS GROUP — ENTRETIEN est une entreprise spécialisée dans les services d'entretien professionnel à Cotonou et ses environs. <span class="nx-conv">Notre conviction : faire de l'entretien professionnel une norme, et non un luxe. Un environnement propre, c'est une image renforcée, une santé préservée et une tranquillité retrouvée.</span></p>
    </div></div>
    <div class="nx-statbar reveal">__STATBAR__</div>
    <div class="nx-split nx-why-inline">
      <div class="nx-figure reveal">
        <img src="img/people/agente-cover.jpg" alt="Agente d'entretien NEXUS DKS GROUP">
        <span class="nx-figure-tag">__SPK__ Au service de votre image</span>
      </div>
      <div class="reveal d1">
        <span class="nx-eyebrow">Pourquoi nous</span>
        <h2 class="section-title">Choisir NEXUS DKS GROUP, c'est&hellip;</h2>
        <p class="section-copy">Bien plus qu'un prestataire : un partenaire qui comprend que la propreté est un levier d'image, de bien-être et de productivité.</p>
        <ul class="nx-list" style="margin-top:18px">
          <li>__CK__<span><strong>Améliorer l'image de vos espaces</strong> — des lieux qui inspirent confiance, dès le premier regard.</span></li>
          <li>__CK__<span><strong>Offrir un environnement sain et agréable</strong> — pour vos collaborateurs, vos clients, vos proches.</span></li>
          <li>__CK__<span><strong>Gagner du temps et de l'efficacité</strong> — vous vous concentrez sur votre activité, nous gérons le reste.</span></li>
          <li>__CK__<span><strong>Bénéficier d'un service professionnel structuré</strong> — protocoles, encadrement et contrôle qualité.</span></li>
        </ul>
        <div class="nx-hero-cta" style="margin-top:26px"><a class="btn-main" href="about.html">Découvrir notre méthode</a></div>
      </div>
    </div>
  </div>
</section>""".replace("__CK__", ico("check")).replace("__SPK__", ico("sparkle")).replace("__STATBAR__", statbar)

    # prestations (6 catégories) — cartes photo immersives (image dédiée par service)
    SERVICE_IMG = {
        "entreprises-bureaux":  "svc-bureaux.jpg",
        "fin-de-chantier":      "svc-fin-chantier.jpg",
        "residences":           "svc-residences.jpg",
        "restaurants-lounges":  "svc-restaurants.jpg",
        "espaces-specifiques":  "svc-espaces.jpg",
        "textiles-surfaces":    "svc-textiles.jpg",
    }
    cards = ""
    for i, (slug, label, icon, desc, bullets) in enumerate(CATS):
        d = " d%d" % (i % 3) if i % 3 else ""
        img = SERVICE_IMG.get(slug, "entretien.jpg")
        cards += """<article class="nx-card-photo reveal%s" id="%s">
  <img class="nx-card-photo-bg" src="img/services/%s" alt="" aria-hidden="true" loading="lazy">
  <div class="nx-card-photo-body">
    <h3>%s</h3>
    <p>%s</p>
    <span class="nx-card-photo-link">En savoir plus %s</span>
  </div>
  <a class="nx-card-photo-cover" href="services/%s.html" aria-label="En savoir plus : %s"></a>
</article>
""" % (d, slug, img, label, desc, ico("arrow"), slug, label)
    prestations = """<section id="services" class="section section-soft">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Nos prestations</span>
      <h2 class="section-title">Une large gamme de services d'entretien professionnel</h2>
      <p class="section-copy">Du bureau au chantier, de la résidence au lounge : six expertises pour répondre à chaque exigence, avec le même niveau de rigueur.</p>
    </div></div>
    <div class="nx-grid cols-3">%s</div>
    <div style="text-align:center;margin-top:34px"><a class="btn-main" href="nos-services.html">Voir le détail des services %s</a></div>
  </div>
</section>""" % (cards, ico("arrow"))

    # équipements
    eq = ""
    for (img, name, icon, d) in EQUIP:
        eq += '<article class="nx-marquee-card"><div class="nx-marquee-media"><img src="img/equip/%s" alt="%s" loading="lazy"></div><div class="nx-marquee-cap"><span class="nx-ico is-lime nx-ico-sm">%s</span><span>%s</span></div></article>\n' % (img, name, ico(icon), name)
    equip = """<section class="section section-soft">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Nos équipements</span>
      <h2 class="section-title">Un matériel professionnel pour un résultat professionnel</h2>
      <p class="section-copy">Aspiration industrielle, injection-extraction, monobrosse, haute pression et gammes de produits spécialisés : chaque support reçoit le traitement qu'il mérite.</p>
    </div></div>
    <div class="nx-marquee" data-partners-carousel role="list" aria-label="Nos équipements professionnels">%s</div>
  </div>
</section>""" % eq

    # audience B2C/B2B
    audience = """<section class="section section-soft nx-tuck-b">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">À qui nous nous adressons</span>
      <h2 class="section-title">Pensé pour les particuliers comme pour les professionnels</h2>
    </div></div>
    <div class="nx-audience">
      <article class="nx-aud b2c reveal"><span class="nx-aud-tag">__I_HOME__ Particuliers · B2C</span><h3>Votre intérieur, soigné comme il le mérite</h3><p>Résidences et appartements : grand ménage, entretien régulier ou ponctuel, textiles et surfaces. Simple, flexible, sans engagement lourd.</p><ul class="nx-list"><li>__CK__<span>Nettoyage complet &amp; entretien récurrent</span></li><li>__CK__<span>Canapés, moquettes, matelas</span></li><li>__CK__<span>Réservation rapide par WhatsApp</span></li></ul></article>
      <article class="nx-aud b2b reveal d1"><span class="nx-aud-tag">__I_BRIEF__ Entreprises &amp; institutions · B2B</span><h3>Des contrats fiables, un interlocuteur unique</h3><p>Bureaux, commerces, restaurants, chantiers et ERP : des engagements de service, une facturation claire et un reporting qualité.</p><ul class="nx-list"><li>__CK__<span>Contrats d'entretien sur mesure</span></li><li>__CK__<span>Protocoles &amp; plan de prévention</span></li><li>__CK__<span>Interlocuteur dédié &amp; reporting</span></li></ul></article>
    </div>
  </div>
</section>""".replace("__CK__", ico("check")).replace("__I_HOME__", ico("home")).replace("__I_BRIEF__", ico("briefcase"))

    # témoignages
    quotes = [
        ("Des bureaux impeccables chaque matin. L'équipe est discrète, ponctuelle et le contrôle qualité se voit vraiment.", "Direction", "PME de services, Cotonou", "PS"),
        ("Remise en état de fin de chantier parfaite : nous avons livré l'appartement le jour même, sans la moindre reprise.", "Maître d'ouvrage", "Programme résidentiel, Calavi", "MA"),
        ("Nos canapés et moquettes ont retrouvé une seconde vie. Service professionnel, résultat bluffant.", "Cliente particulière", "Résidence, Cotonou", "AK"),
    ]
    def quote_card(txt, who, role, ini, clone=False):
        cls = "nx-quote is-clone" if clone else "nx-quote reveal"
        hid = ' aria-hidden="true"' if clone else ""
        return '<article class="%s"%s><p>« %s »</p><div class="nx-quote-by"><span class="nx-avatar">%s</span><div><strong>%s</strong><br><span>%s</span></div></div></article>\n' % (cls, hid, txt, ini, who, role)
    qc = "".join(quote_card(t, w, r, i) for (t, w, r, i) in quotes)
    qc_clone = "".join(quote_card(t, w, r, i, clone=True) for (t, w, r, i) in quotes)
    testi = """<section class="section section-soft nx-tuck-t">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Ils nous font confiance</span>
      <h2 class="section-title">La satisfaction, notre meilleure référence</h2>
    </div></div>
    <div class="nx-mrail-wrap"><div class="nx-grid cols-3 nx-mrail nx-mrail-rev">%s%s</div></div>
  </div>
</section>""" % (qc, qc_clone)

    # blog teaser
    def blog_card(art, clone=False):
        slug, catg, ttl, exc, img, rt = art
        cls = "nx-blog-card is-clone" if clone else "nx-blog-card reveal"
        hid = ' aria-hidden="true"' if clone else ""
        return """<article class="%s"%s>
  <a class="nx-blog-media" href="blog/%s.html"><span class="nx-blog-cat">%s</span><img src="%s" alt="%s" loading="lazy"></a>
  <div class="nx-blog-body"><div class="nx-blog-meta">Lecture %s</div><h3>%s</h3><p>%s</p><a class="nx-blog-link" href="blog/%s.html">Lire l'article %s</a></div>
</article>
""" % (cls, hid, slug, catg, img, ttl, rt, ttl, exc, slug, ico("arrow"))
    teaser = ARTICLES[:3]  # l'accueil ne met en avant que les 3 articles phares
    bc = "".join(blog_card(a) for a in teaser)
    bc_clone = "".join(blog_card(a, clone=True) for a in teaser)
    blog = """<section class="section section-soft">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Le blog</span>
      <h2 class="section-title">Conseils &amp; expertise du secteur de l'entretien</h2>
      <p class="section-copy">Des analyses utiles pour les clients, les professionnels et les partenaires : hygiène, techniques, organisation.</p>
    </div></div>
    <div class="nx-mrail-wrap"><div class="nx-grid cols-3 nx-mrail">%s%s</div></div>
    <div style="text-align:center;margin-top:34px"><a class="btn-main" href="blog.html">Tous les articles %s</a></div>
  </div>
</section>""" % (bc, bc_clone, ico("arrow"))

    body = hero + pitch + prestations + audience + testi + equip + blog + contact_section(title="Confiez-nous vos espaces dès aujourd'hui")
    title = "NEXUS DKS GROUP — Entretien professionnel à Cotonou (Bénin)"
    desc = "Entreprise de droit béninois d'entretien professionnel à Cotonou, ses environs et dans tout le Bénin : bureaux, commerces, résidences, chantiers. Devis FCFA sous 24 h."
    write("index.html", head(title, desc, "index.html", "page-home") + header("home") + body + footer())


# ============================================================ NOS SERVICES
def build_services():
    banner = """<section class="page-banner" style="--banner-image:url('img/services/bandeau-supplies.jpg')">
  <div class="container"><div class="banner-shell reveal">
    <span class="nx-eyebrow">Nos services</span>
    <h1>Une large gamme de services d'entretien professionnel</h1>
    <p class="lead">Six domaines d'expertise, des protocoles adaptés à chaque environnement, un seul niveau d'exigence : l'excellence.</p>
    <div class="nx-hero-cta"><a class="btn-lime" href="contact.html">__SEND__ Demander un devis</a><a class="btn-secondary" href="entretien-proprete.html">Offre &amp; formules</a></div>
  </div></div>
  <span class="nx-banner-rule"></span>
</section>""".replace("__SEND__", ico("send"))

    # 6 prestations détaillées (numérotées)
    presta = ""
    for i, (slug, label, icon, desc, bullets) in enumerate(CATS):
        bl = "".join('<li>%s<span>%s</span></li>' % (ico("check"), b) for b in bullets)
        presta += """<article class="nx-presta reveal%s" id="%s">
  <div class="nx-presta-head"><span class="nx-ico is-lime">%s</span><span class="nx-num">%02d</span></div>
  <h3>%s</h3><p>%s</p>
  <ul class="nx-list">%s</ul>
  <a class="nx-blog-link" href="services/%s.html">Découvrir ce service %s</a>
</article>
""" % (" d%d" % (i % 3) if i % 3 else "", slug, ico(icon), i + 1, label, desc, bl, slug, ico("arrow"))
    prestations = """<section class="section">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Prestations</span>
      <h2 class="section-title">Ce que nous prenons en charge</h2>
      <p class="section-copy">Chaque catégorie répond à des contraintes propres. Nous y répondons par des protocoles, un matériel et des équipes adaptés.</p>
    </div></div>
    <div class="nx-grid cols-3">%s</div>
  </div>
</section>""" % presta

    # équipements (grille complète avec desc)
    eq = ""
    for i, (img, name, icon, d) in enumerate(EQUIP):
        eq += '<article class="nx-equip reveal%s"><div class="nx-equip-media"><img src="img/equip/%s" alt="%s" loading="lazy"></div><div class="nx-equip-cap">%s</div></article>\n' % (" d%d" % (i % 3) if i % 3 else "", img, name, name)
    equip = """<section class="section section-soft">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Nos équipements professionnels</span>
      <h2 class="section-title">Un matériel professionnel pour un résultat professionnel</h2>
    </div></div>
    <div class="nx-grid cols-3">%s</div>
  </div>
</section>""" % eq

    # méthode (6) + engagement
    steps = "".join('<div class="nx-step reveal"><span class="nx-step-num"></span><h4>%s</h4><p>%s</p></div>\n' % (t, d) for t, icon, d in METHOD)
    method = """<section class="section">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Notre méthode de travail</span>
      <h2 class="section-title">Un processus structuré, du diagnostic à la validation</h2>
    </div></div>
    <div class="nx-method">%s</div>
  </div>
</section>""" % steps

    body = banner + prestations + equip + method + cta(title="Un besoin d'entretien précis ?", text="Confiez-nous votre cahier des charges : nous concevons un protocole sur mesure et un devis clair en FCFA, sous 24&nbsp;heures.") + contact_section()
    title = "Nos services d'entretien | NEXUS DKS GROUP — Cotonou"
    desc = "Services d'entretien NEXUS DKS GROUP : entreprises & bureaux, fin de chantier, résidences, restaurants & lounges, espaces spécifiques, textiles & surfaces. Cotonou, Bénin."
    write("nos-services.html", head(title, desc, "nos-services.html", "page-services") + header("services") + body + footer())


# ============================================================ OFFRE & FORMULES (entretien-proprete)
def build_offre():
    banner = """<section class="page-banner" style="--banner-image:url('img/equip/injecteur.jpg')">
  <div class="container"><div class="banner-shell reveal">
    <span class="nx-eyebrow">Offre professionnelle &amp; formules</span>
    <h1>Une offre d'entretien à large éventail et à forte valeur</h1>
    <p class="lead">Du passage ponctuel au contrat multi-sites, nous structurons une réponse complète, traçable et chiffrée — adaptée à votre réalité et à votre budget.</p>
    <div class="nx-hero-cta"><a class="btn-lime" href="contact.html">__SEND__ Obtenir mon devis</a><a class="btn-secondary" href="tel:__T1H__">__PH__ __T1D__</a></div>
  </div></div>
  <span class="nx-banner-rule"></span>
</section>""".replace("__SEND__", ico("send")).replace("__PH__", ico("phone")).replace("__T1H__", SITE["tel1_href"]).replace("__T1D__", SITE["tel1_disp"])

    intro = """<section class="section">
  <div class="container">
    <div class="nx-split">
      <div class="reveal">
        <span class="nx-eyebrow">Une offre, toute la chaîne</span>
        <h2 class="section-title">De l'entretien courant aux interventions techniques</h2>
        <p class="section-copy">Notre catalogue couvre l'ensemble du cycle de propreté de vos espaces : entretien récurrent, remise en état, bionettoyage, traitement des textiles et des surfaces, jusqu'aux opérations spécialisées (cristallisation, haute pression, désinfection). Une couverture pensée pour les exigences réelles des particuliers, des entreprises et des institutions.</p>
        <ul class="nx-list" style="margin-top:18px">
          <li>__CK__<span><strong>Entretien courant &amp; récurrent</strong> — plan de propreté contractuel, passages planifiés.</span></li>
          <li>__CK__<span><strong>Opérations ponctuelles</strong> — grand nettoyage, remise en état, fin de chantier.</span></li>
          <li>__CK__<span><strong>Prestations techniques</strong> — injection-extraction, monobrosse, cristallisation, haute pression.</span></li>
          <li>__CK__<span><strong>Hygiène &amp; désinfection</strong> — points de contact, sanitaires, zones sensibles.</span></li>
        </ul>
      </div>
      <div class="reveal d1"><div class="nx-figure wide"><img src="img/services/bandeau-accessoires.jpg" alt="Matériel et produits d'entretien NEXUS DKS GROUP"><span class="nx-figure-tag">__SPK__ Couverture complète</span></div></div>
    </div>
  </div>
</section>""".replace("__CK__", ico("check")).replace("__SPK__", ico("sparkle"))

    # prestations détaillées réutilisées
    presta = ""
    for i, (slug, label, icon, desc, bullets) in enumerate(CATS):
        bl = "".join('<li>%s<span>%s</span></li>' % (ico("check"), b) for b in bullets)
        presta += '<article class="nx-card reveal%s"><span class="nx-ico is-lime">%s</span><h3>%s</h3><p>%s</p><ul class="nx-list">%s</ul></article>\n' % (" d%d" % (i % 3) if i % 3 else "", ico(icon), label, desc, bl)
    detail = """<section class="section section-soft">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Le détail de l'offre</span>
      <h2 class="section-title">Six domaines, une exigence constante</h2>
    </div></div>
    <div class="nx-grid cols-3">%s</div>
  </div>
</section>""" % presta

    # formules
    formulas = [
        ("Essentiel", "Particuliers · Résidences", "à partir de", "25 000", "FCFA / intervention",
         ["Intervention ponctuelle", "Pièces de vie &amp; sanitaires", "Sols, surfaces, dépoussiérage", "Produits &amp; matériel fournis"], False),
        ("Confort", "Particuliers &amp; petits bureaux", "à partir de", "60 000", "FCFA / mois",
         ["Passages réguliers (hebdomadaires)", "Entretien complet des espaces", "Vitrerie intérieure", "Suivi qualité &amp; ajustements"], True),
        ("Pro / Contrat", "Entreprises &amp; institutions", "sur", "devis", "selon site, surface &amp; fréquence",
         ["Plan de propreté dédié", "Équipe &amp; planning sur mesure", "Consommables &amp; reporting", "Interlocuteur unique"], False),
    ]
    fc = ""
    for i, (name, target, pre, price, unit, feats, feat) in enumerate(formulas):
        li = "".join('<li>%s<span>%s</span></li>' % (ico("check"), x) for x in feats)
        btn = "btn-lime" if feat else "btn-main"
        fc += """<article class="nx-formula%s reveal%s">
  <div class="nx-f-name">%s</div><div class="nx-f-target">%s</div>
  <div class="nx-f-price"><small>%s</small><strong>%s</strong><span>%s</span></div>
  <ul class="nx-list">%s</ul>
  <a class="%s" href="contact.html">Choisir cette formule</a>
</article>
""" % (" featured" if feat else "", " d%d" % (i % 3) if i % 3 else "", name, target, pre, price, unit, li, btn)
    formules = """<section class="section">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Formules</span>
      <h2 class="section-title">Des formules lisibles, ajustées à chaque espace</h2>
      <p class="section-copy">Tarifs indicatifs en FCFA, affinés après un diagnostic gratuit selon la surface, la fréquence et le niveau d'exigence.</p>
    </div></div>
    <div class="nx-formulas">%s</div>
    <p class="form-note" style="text-align:center;margin-top:20px">Besoin d'une réponse multi-sites ou d'un contrat annuel ? <a href="contact.html" style="color:var(--indigo);font-weight:800">Parlons-en &rarr;</a></p>
  </div>
</section>""" % fc

    # zones
    zones = """<section class="section section-dark">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Zones d'intervention</span>
      <h2 class="section-title">Cotonou et tout le Bénin</h2>
      <p class="section-copy">Nous intervenons à Cotonou et dans les principales agglomérations du pays. Une adresse hors zone ? Parlons-en.</p>
    </div></div>
    <div class="nx-grid cols-4">
      __Z__ Cotonou __ZE__ __Z__ Calavi __ZE__ __Z__ Porto-Novo __ZE__ __Z__ Sèmè-Kpodji __ZE__
      __Z__ Ouidah __ZE__ __Z__ Abomey-Calavi __ZE__ __Z__ Parakou __ZE__ __Z__ &amp; au-delà __ZE__
    </div>
  </div>
</section>""".replace("__Z__", '<div class="nx-card reveal" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.1);flex-direction:row;align-items:center;gap:12px;padding:18px 20px"><span class="nx-ico is-navy nx-ico-sm">' + ico("pin") + '</span><h3 style="color:#fff;font-size:1.05rem">').replace("__ZE__", "</h3></div>")

    body = banner + intro + detail + formules + zones + cta(title="Construisons votre contrat d'entretien", text="Un diagnostic gratuit, une proposition claire, un engagement de qualité. Démarrons dès cette semaine.") + contact_section()
    title = "Offre & formules d'entretien | NEXUS DKS GROUP — Cotonou"
    desc = "Offre d'entretien professionnel NEXUS DKS GROUP : entretien courant, remise en état, prestations techniques, hygiène. Formules Essentiel, Confort, Pro/Contrat en FCFA."
    write("entretien-proprete.html", head(title, desc, "entretien-proprete.html", "page-offre") + header("offre") + body + footer())


# ============================================================ NOTRE GROUPE
def build_about():
    banner = """<section class="page-banner" style="--banner-image:url('img/people/agente-cover.jpg')">
  <div class="container"><div class="banner-shell reveal">
    <span class="nx-eyebrow">Notre groupe</span>
    <h1>NEXUS DKS GROUP</h1>
    <p class="lead">Une entreprise d'entretien professionnel à Cotonou — adossée à un groupe aux activités complémentaires. Notre raison d'être : faire de la propreté une norme accessible, et de chaque espace une fierté.</p>
    <div class="nx-hero-cta"><a class="btn-lime" href="contact.html">__SEND__ Travailler avec nous</a><a class="btn-secondary" href="nos-services.html">Nos services</a></div>
  </div></div>
  <span class="nx-banner-rule"></span>
</section>""".replace("__SEND__", ico("send"))

    presentation = """<section class="section">
  <div class="container">
    <div class="nx-split">
      <div class="reveal">
        <span class="nx-eyebrow">Présentation</span>
        <h2 class="section-title">Spécialistes de l'entretien, au service de votre image</h2>
        <p class="section-copy">NEXUS DKS GROUP — ENTRETIEN accompagne entreprises, commerces, résidences et chantiers à Cotonou et ses environs, en leur offrant des prestations de qualité, adaptées à leurs besoins. Notre objectif est sans ambiguïté : <strong>garantir des espaces propres, sains et valorisés.</strong></p>
        <h3 style="font-family:'Bricolage Grotesque';color:var(--indigo);margin:24px 0 8px;font-size:1.2rem">Notre vision</h3>
        <p class="section-copy">Faire de l'entretien professionnel une norme, et non un luxe. Permettre aux entreprises comme aux particuliers d'accéder à un service d'entretien de qualité, pour améliorer leur environnement et leur image.</p>
      </div>
      <div class="reveal d1"><div class="nx-figure tall"><img src="img/people/agente-cover.jpg" alt="NEXUS DKS GROUP — entretien professionnel"><span class="nx-figure-tag">__SPK__ Une nouvelle norme</span></div></div>
    </div>
  </div>
</section>""".replace("__SPK__", ico("sparkle"))

    # valeurs
    vc = "".join('<article class="nx-card reveal" style="flex-direction:row;align-items:center;gap:14px;padding:22px 24px"><span class="nx-ico is-lime nx-ico-sm">%s</span><h3 style="font-size:1.1rem">%s</h3></article>\n' % (ico(icon), name) for name, icon in VALUES)
    valeurs = """<section class="section section-soft">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Nos valeurs</span>
      <h2 class="section-title">Ce qui guide chacune de nos interventions</h2>
    </div></div>
    <div class="nx-grid cols-3">%s</div>
  </div>
</section>""" % vc

    # autres activités du groupe
    oc = "".join('<article class="nx-card reveal"><span class="nx-ico">%s</span><h3>%s</h3><p>%s</p></article>\n' % (ico(icon), name, d) for name, icon, d in OTHER)
    other = """<section class="section section-dark">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">L'écosystème NEXUS DKS GROUP</span>
      <h2 class="section-title">Au-delà de l'entretien, un groupe multiservices</h2>
      <p class="section-copy">L'entretien est notre signature et notre site lui est dédié. Mais NEXUS DKS GROUP, c'est aussi un ensemble d'activités complémentaires — un seul groupe, plusieurs solutions.</p>
    </div></div>
    <div class="nx-grid cols-3">%s</div>
    <p class="form-note" style="text-align:center;color:rgba(255,255,255,.7);margin-top:22px">Un besoin sur l'une de ces activités ? <a href="contact.html" style="color:var(--lime-bright);font-weight:800">Contactez le groupe &rarr;</a></p>
  </div>
</section>""" % oc

    body = banner + presentation + valeurs + section_engage() + section_method() + other + cta()
    title = "Notre Groupe | NEXUS DKS GROUP — Entretien & multiservices, Cotonou"
    desc = "NEXUS DKS GROUP : spécialiste de l'entretien professionnel à Cotonou, adossé à un groupe multiservices (BTP, immobilier, commerce, agro, événementiel, conseil)."
    write("about.html", head(title, desc, "about.html", "page-about") + header("about") + body + footer())


# ============================================================ BLOG (index)
def build_blog():
    # catégories uniques (filtre)
    cats = []
    for a in ARTICLES:
        if a[1] not in cats:
            cats.append(a[1])
    filters = '<button type="button" class="nx-chip is-active" data-filter="all">Tous</button>'
    filters += "".join('<button type="button" class="nx-chip" data-filter="%s">%s</button>' % (c, c) for c in cats)

    bc = ""
    for i, (slug, catg, ttl, exc, img, rt) in enumerate(ARTICLES):
        bc += """<article class="nx-blog-card reveal%s" data-cat="%s">
  <a class="nx-blog-media" href="blog/%s.html"><span class="nx-blog-cat">%s</span><img src="%s" alt="%s" loading="lazy"></a>
  <div class="nx-blog-body"><div class="nx-blog-meta">Lecture %s</div><h3>%s</h3><p>%s</p><a class="nx-blog-link" href="blog/%s.html">Lire l'article %s</a></div>
</article>
""" % (" d%d" % (i % 3) if i % 3 else "", catg, slug, catg, img, ttl, rt, ttl, exc, slug, ico("arrow"))

    hero = """<section class="svc-hero">
  <img class="svc-hero-bg" src="img/services/bandeau-accessoires.jpg" alt="" aria-hidden="true">
  <div class="container">
    <span class="nx-eyebrow">Le blog</span>
    <h1>Le journal de la propreté professionnelle</h1>
    <p class="lead">Hygiène, techniques, organisation et bonnes pratiques : des contenus utiles pour les clients, les professionnels et les partenaires du secteur de l'entretien.</p>
  </div>
</section>"""
    grid = """<section class="section">
  <div class="container">
    <div class="nx-blog-filter reveal" role="tablist" aria-label="Filtrer les articles par thème">%s</div>
    <div class="nx-grid cols-3" data-blog-grid>%s</div>
    <p class="nx-blog-empty" hidden>Aucun article dans cette catégorie pour le moment.</p>
  </div>
</section>""" % (filters, bc)
    body = hero + grid + cta(title="Un sujet d'entretien à approfondir ?", text="Nos experts répondent à vos questions et conçoivent la solution adaptée à vos espaces.")
    title = "Blog entretien & propreté | NEXUS DKS GROUP"
    desc = "Articles d'experts sur l'entretien professionnel : bionettoyage, fin de chantier, traitement des textiles, hygiène des espaces. NEXUS DKS GROUP, Cotonou."
    write("blog.html", head(title, desc, "blog.html", "page-blog") + header("blog") + body + footer())


# ============================================================ ARTICLES
ARTICLE_BODY = {
 "bionettoyage-bureaux": """
<p class="nx-article-lead">On croit nettoyer un bureau ; en réalité, on gère un réseau de surfaces de contact. C'est précisément là — sur quelques centimètres carrés invisibles — que se jouent la santé des équipes et l'image de l'organisation.</p>
<p>Dans un environnement de travail, l'œil juge le sol, les vitres et les corbeilles. Pourtant, l'essentiel des transmissions microbiennes se concentre sur des zones discrètes : poignées de portes, interrupteurs, boutons d'ascenseur, claviers, téléphones, rampes d'escalier, machines à café. Ces « points de contact » sont touchés des dizaines de fois par jour, par des dizaines de mains différentes. Les ignorer, c'est nettoyer ce qui se voit en laissant intact ce qui contamine.</p>
<h2>Nettoyage, désinfection, bionettoyage : trois niveaux à ne pas confondre</h2>
<p>Ces trois termes sont souvent employés comme synonymes. Ils décrivent en réalité des opérations distinctes, et les confondre installe un faux sentiment de sécurité.</p>
<h3>Le nettoyage</h3>
<p>Il retire les salissures visibles et une partie des micro-organismes, par action mécanique et détergence. Indispensable, mais insuffisant à lui seul dans les zones sensibles.</p>
<h3>La désinfection</h3>
<p>Elle réduit la charge microbienne à l'aide de produits actifs (bactéricides, virucides). Son efficacité dépend d'un paramètre trop souvent négligé : le <strong>temps de contact</strong>.</p>
<h3>Le bionettoyage</h3>
<p>Il combine les deux dans un ordre précis — détergence <em>puis</em> désinfection — avec un protocole écrit, un temps de contact respecté et une traçabilité des passages. C'est le standard des environnements exigeants.</p>
<blockquote>Un point de contact désinfecté sans avoir été nettoyé au préalable n'est pas réellement assaini : la salissure protège le micro-organisme du produit actif.</blockquote>
<h2>Une méthode qui se voit dans les résultats</h2>
<p>Le bionettoyage n'est pas affaire de produit miracle, mais de méthode rigoureuse, reproductible et contrôlée :</p>
<ul>
  <li><strong>Cartographie des points de contact</strong>, zone par zone, selon leur fréquence d'usage et leur niveau de risque.</li>
  <li><strong>Choix des produits selon le support</strong> : inox, plastique, bois et écrans tactiles n'appellent pas la même chimie.</li>
  <li><strong>Respect du temps de contact</strong> et du sens de passage, toujours du propre vers le sale et du haut vers le bas.</li>
  <li><strong>Microfibre code-couleur</strong> : une couleur par zone (sanitaires, bureaux, cuisine) pour éliminer les contaminations croisées.</li>
  <li><strong>Traçabilité</strong> : fiches de passage et contrôle après intervention, pour prouver — et améliorer — la qualité.</li>
</ul>
<h2>À quelle fréquence intervenir ?</h2>
<p>La bonne fréquence dépend du trafic et de la vocation des locaux. Un plateau de bureaux classique se traite efficacement par un passage quotidien et une désinfection ciblée des points de contact ; un espace recevant du public, ou une période épidémique, justifient des repasses en cours de journée. Le principe : ajuster l'effort au risque réel, ni plus, ni moins.</p>
<h2>Pourquoi cela change tout pour votre entreprise</h2>
<p>Moins d'arrêts maladie et donc moins d'absentéisme, des collaborateurs qui se sentent considérés, des visiteurs rassurés dès l'accueil : l'hygiène des points de contact agit directement sur la productivité et sur la perception de votre marque. Ce n'est pas une dépense de confort, c'est un investissement dans la continuité de votre activité.</p>
<div class="nx-article-keys">
  <h3>À retenir</h3>
  <ul>
    <li>Le risque sanitaire se concentre sur les points de contact, pas sur les surfaces visibles.</li>
    <li>Bionettoyage = nettoyer <em>puis</em> désinfecter, avec temps de contact et traçabilité.</li>
    <li>Microfibre code-couleur et plan de propreté garantissent un résultat reproductible.</li>
  </ul>
</div>
""",
 "fin-de-chantier-checklist": """
<p class="nx-article-lead">Entre la dernière finition et la remise des clés se joue la première impression. Un nettoyage de fin de chantier réussi transforme un ouvrage livré en espace « prêt à occuper » — sans la moindre reprise.</p>
<p>Le nettoyage de fin de chantier n'a rien d'un grand ménage classique. Il s'attaque à des salissures spécifiques — laitance de ciment, traces de peinture et d'enduit, colles, films de protection, poussières fines incrustées dans les menuiseries et les bouches de ventilation — qui exigent des techniques, des produits et un matériel adaptés. Bâclé, il retarde une livraison ; maîtrisé, il la sécurise.</p>
<h2>Comprendre les salissures de chantier</h2>
<p>Avant de nettoyer, il faut identifier. Chaque résidu appelle un traitement précis :</p>
<ul>
  <li><strong>Laitance et voiles de ciment</strong> : déposés sur sols et faïences, ils ternissent durablement s'ils ne sont pas décapés.</li>
  <li><strong>Films de protection et adhésifs</strong> : à retirer sans rayer les supports (vitres, profilés, inox).</li>
  <li><strong>Traces de peinture et d'enduit</strong> : projections sur sols, vitres et menuiseries.</li>
  <li><strong>Poussières fines</strong> : les plus sournoises, logées dans les gaines, plinthes, luminaires et VMC.</li>
</ul>
<h2>La séquence qui évite les reprises</h2>
<p>Un fin de chantier efficace se déroule en passes successives, du plus grossier au plus fin.</p>
<h3>1. Évacuation &amp; dégrossissage</h3>
<p>Retrait des gravats résiduels, dépose des protections, aspiration industrielle des poussières en hauteur comme au sol.</p>
<h3>2. Traitement des salissures techniques</h3>
<p>Décapage de la laitance, retrait des résidus de peinture et de colle, nettoyage des menuiseries et des huisseries.</p>
<h3>3. Vitrerie &amp; surfaces</h3>
<p>Nettoyage des vitrages intérieurs et extérieurs accessibles, détachage des encadrements, lustrage des surfaces.</p>
<h3>4. Finition &amp; contrôle</h3>
<ul>
  <li>Nettoyage approfondi des sanitaires et de la robinetterie.</li>
  <li>Traitement adapté du revêtement de sol (cristallisation, lustrage, protection).</li>
  <li>Contrôle qualité pièce par pièce, à la lumière rasante, pour traquer la moindre trace.</li>
</ul>
<blockquote>Un chantier mal nettoyé peut retarder une livraison de plusieurs jours. Un chantier bien nettoyé se livre le jour même.</blockquote>
<h2>Le bon matériel, le bon dosage</h2>
<p>Aspiration industrielle eau et poussières, monobrosse, raclettes professionnelles, décapants adaptés au support : le fin de chantier est un métier d'équipement. Le surdosage de produit, lui, laisse des films collants qui re-fixent la poussière — d'où l'importance d'un personnel formé.</p>
<h2>Le réflexe gagnant</h2>
<p>Intégrer le nettoyage de fin de chantier au planning <em>dès l'amont</em>, et non comme une étape subie en dernière minute. C'est la garantie d'une réception fluide, d'un procès-verbal sans réserve et d'un client conquis.</p>
<div class="nx-article-keys">
  <h3>À retenir</h3>
  <ul>
    <li>Le fin de chantier est une prestation technique, distincte du ménage courant.</li>
    <li>On travaille en passes : gravats → salissures techniques → vitrerie → finition &amp; contrôle.</li>
    <li>Anticiper l'étape dans le planning évite les reprises et sécurise la livraison.</li>
  </ul>
</div>
""",
 "moquettes-injection-extraction": """
<p class="nx-article-lead">Vos textiles concentrent poussières, allergènes et taches. Deux grandes techniques s'offrent à vous pour leur redonner vie : le shampouinage et l'injection-extraction. Comment choisir la bonne ?</p>
<p>Canapés, fauteuils, moquettes, tapis et matelas sont de véritables éponges à particules. Un entretien périodique prolonge leur durée de vie, assainit l'air intérieur — un enjeu réel pour les personnes sensibles ou allergiques — et préserve l'aspect d'origine. Encore faut-il employer la bonne méthode sur la bonne fibre.</p>
<h2>Pourquoi entretenir ses textiles</h2>
<p>Au-delà de l'esthétique, un textile encrassé dégrade la qualité de l'air : acariens, pollens et poussières fines s'y accumulent et se redispersent à chaque usage. Un traitement professionnel régulier réduit cette charge et évite l'incrustation définitive des taches.</p>
<h2>Le shampouinage</h2>
<p>Une solution moussante est appliquée puis travaillée mécaniquement (brosse rotative ou monobrosse) pour décoller les salissures, avant aspiration. Rapide et économique, il convient au rafraîchissement régulier de surfaces peu à moyennement encrassées. Ses limites : un temps de séchage plus long et un risque de résidus moussants si le rinçage est insuffisant.</p>
<h2>L'injection-extraction</h2>
<p>Le procédé injecte sous pression une solution détergente au cœur de la fibre, puis l'<strong>extrait</strong> immédiatement — avec les salissures dissoutes — par une aspiration puissante. Résultat : un nettoyage en profondeur, très peu de résidus et un séchage maîtrisé. C'est la référence pour les encrassements importants et les exigences sanitaires.</p>
<h2>Quelle technique pour quel besoin ?</h2>
<ul>
  <li><strong>Encrassement léger à moyen, entretien courant</strong> → shampouinage.</li>
  <li><strong>Encrassement profond, taches anciennes, exigence sanitaire</strong> → injection-extraction.</li>
  <li><strong>Matelas &amp; literie</strong> → injection-extraction complétée d'une désinfection.</li>
  <li><strong>Fibres délicates ou cuir</strong> → traitement doux spécifique, jamais d'eau en excès.</li>
</ul>
<blockquote>La bonne technique, c'est celle qui correspond à la fibre, au niveau de salissure et à l'usage réel du textile.</blockquote>
<h2>Le séchage, étape décisive</h2>
<p>Un textile mal séché, c'est la porte ouverte aux odeurs et aux moisissures. Maîtriser l'humidité résiduelle — par l'extraction et la ventilation — fait partie intégrante d'un traitement réussi, et conditionne une remise en service rapide.</p>
<h2>Notre approche</h2>
<p>Nous diagnostiquons la nature du textile et le degré d'encrassement avant d'engager le traitement le plus pertinent, avec un matériel professionnel et des produits adaptés à chaque support. Objectif : un résultat visible, durable et sans mauvaise surprise.</p>
<div class="nx-article-keys">
  <h3>À retenir</h3>
  <ul>
    <li>Entretenir ses textiles, c'est aussi assainir l'air intérieur.</li>
    <li>Shampouinage pour l'entretien courant ; injection-extraction pour le nettoyage en profondeur.</li>
    <li>Le diagnostic de la fibre et la maîtrise du séchage font la différence.</li>
  </ul>
</div>
""",
 "hygiene-restaurants-argument": """
<p class="nx-article-lead">En restauration, la propreté n'est pas un détail d'arrière-cuisine : c'est un argument commercial qui se voit, se sent et se raconte. Un client rassuré revient — et en parle autour de lui.</p>
<p>Avant même la première bouchée, le client juge. Une vitre nette, des sanitaires impeccables, une salle sans trace : autant de signaux qui installent la confiance. À l'inverse, une seule table collante ou un coin négligé suffit à entacher une réputation patiemment construite.</p>
<h2>L'hygiène, premier avis client</h2>
<p>À l'ère des avis en ligne, la propreté est l'un des critères les plus commentés. Elle pèse sur la note, donc sur la visibilité, donc sur le chiffre d'affaires. Soigner l'entretien, c'est protéger sa réputation numérique autant que sa salle.</p>
<h2>Cuisine : la rigueur invisible</h2>
<p>Derrière le service se joue l'essentiel : dégraissage des plans, des équipements et des hottes, désinfection des surfaces en contact alimentaire, traitement des sols antidérapants, gestion des zones froides. Des protocoles alignés sur les bonnes pratiques d'hygiène (HACCP) protègent vos clients — et votre responsabilité.</p>
<blockquote>En salle, la propreté se voit ; en cuisine, elle se prouve. Les deux racontent la même exigence.</blockquote>
<h2>Intervenir sans perturber le service</h2>
<p>La clé d'un entretien réussi en restauration : des interventions en horaires décalés — la nuit, après le service ou avant l'ouverture. Vos équipes retrouvent des locaux prêts, sans jamais voir leur exploitation ralentie.</p>
<h2>Faire de la propreté un récit de marque</h2>
<p>Un établissement qui assume son exigence d'hygiène se distingue. C'est un argument à revendiquer, sur place comme en ligne : il rassure, fidélise et justifie votre positionnement.</p>
<div class="nx-article-keys">
  <h3>À retenir</h3>
  <ul>
    <li>La propreté est un critère d'avis client majeur — donc commercial.</li>
    <li>Cuisine : protocoles alignés HACCP ; salle : zéro trace visible.</li>
    <li>Interventions en horaires décalés pour ne jamais gêner le service.</li>
  </ul>
</div>
""",
 "externaliser-entretien-entreprise": """
<p class="nx-article-lead">Gérer soi-même le ménage de ses locaux semble économique. En réalité, le « système D » coûte souvent plus cher — en temps, en qualité et en sérénité — qu'un prestataire structuré.</p>
<p>Confier l'entretien à un professionnel, ce n'est pas déléguer une corvée : c'est s'offrir un cadre, une régularité et un résultat mesurable. Voici six bénéfices concrets.</p>
<h2>1. Du temps recentré sur votre métier</h2>
<p>Chaque heure passée à organiser, contrôler ou rattraper le nettoyage est une heure volée à votre cœur d'activité. L'externalisation vous rend ce temps.</p>
<h2>2. Une qualité constante et contrôlée</h2>
<p>Plan de propreté, protocoles écrits, contrôle qualité après passage : la régularité ne dépend plus de la disponibilité d'un salarié, mais d'un engagement de service.</p>
<h2>3. Des coûts maîtrisés et lisibles</h2>
<p>Plus de gestion de matériel, de produits, de remplacements ni de turnover : un budget clair, chiffré en FCFA, sans mauvaise surprise.</p>
<h2>4. Un matériel professionnel</h2>
<p>Aspiration industrielle, injection-extraction, monobrosse, haute pression : un équipement que peu d'entreprises rentabiliseraient en interne.</p>
<h2>5. Une image qui inspire confiance</h2>
<p>Des espaces impeccables valorisent votre marque auprès des clients, des partenaires et des collaborateurs — dès le premier regard.</p>
<h2>6. La conformité et la traçabilité</h2>
<p>Personnel formé et encadré, protocoles documentés, suivi des passages : autant de garanties utiles, notamment pour les institutions et les établissements recevant du public.</p>
<blockquote>Externaliser, ce n'est pas dépenser plus : c'est payer le juste prix d'un résultat fiable et reproductible.</blockquote>
<div class="nx-article-keys">
  <h3>À retenir</h3>
  <ul>
    <li>Le « système D » coûte en temps, en qualité et en sérénité.</li>
    <li>Un prestataire structuré apporte régularité, matériel pro et budget lisible.</li>
    <li>Personnel encadré et traçabilité = conformité, utile pour les institutions.</li>
  </ul>
</div>
""",
 "proximite-technologie-nexus": """
<p class="nx-article-lead">Entre votre besoin et l'intervention, chaque étape de trop fait perdre du temps. NEXUS DKS GROUP a fait un choix clair : rapprocher la relation client grâce à des outils simples, et piloter ses opérations par des systèmes informatisés.</p>
<p>La propreté est un métier de terrain. Mais la qualité du service se joue aussi — et de plus en plus — dans la fluidité de la relation : la facilité à demander un devis, à suivre une intervention, à obtenir une réponse. C'est là que la technologie, bien employée, fait la différence.</p>
<h2>Le contact de proximité, augmenté par la technologie</h2>
<p>Réduire la distance entre le client et l'équipe, c'est réduire le temps d'intervention. Nos canaux de contact directs (WhatsApp, configurateurs de demande) permettent de :</p>
<ul>
  <li><strong>Pré-qualifier la demande</strong> en quelques secondes — surface, fréquence, contraintes — pour un devis plus juste et plus rapide.</li>
  <li><strong>Supprimer les allers-retours</strong> : la bonne information est transmise du premier coup.</li>
  <li><strong>Répondre au plus près du besoin</strong>, sur le canal que le client utilise déjà au quotidien.</li>
  <li><strong>Tracer chaque échange</strong> pour un suivi clair et une relation de confiance.</li>
</ul>
<blockquote>Moins d'étapes entre le besoin et l'action, c'est plus de réactivité pour le client — et plus d'efficacité pour nos équipes.</blockquote>
<h2>En interne : un pilotage informatisé</h2>
<p>La même exigence s'applique en coulisses. NEXUS DKS GROUP s'appuie sur des systèmes de gestion informatisés pour suivre et traiter ses processus, mais aussi pour <strong>encadrer et accompagner son personnel et sa cheville ouvrière</strong> : planification des interventions, traçabilité des passages, contrôle qualité, suivi des équipes et de leur formation. La technologie ne remplace pas l'humain : elle le soutient et le valorise.</p>
<h2>Déjà en place sur ce site</h2>
<p>Ce site n'est pas une vitrine figée, c'est un outil de service. Plusieurs fonctionnalités sont déjà actives :</p>
<ul>
  <li>Des <strong>configurateurs de demande</strong> qui génèrent un message pré-rempli en un clic.</li>
  <li>Un <strong>devis express</strong> et une <strong>candidature en ligne</strong> via WhatsApp.</li>
  <li>Une expérience <strong>pensée pour le mobile</strong>, rapide et accessible.</li>
</ul>
<h2>Et ce n'est qu'un début</h2>
<p>D'autres innovations suivront sur ce site pour rapprocher encore davantage NEXUS de ses clients et fluidifier le traitement des demandes — toujours dans la même logique : moins de friction, plus de proximité.</p>
<h2>Un partenaire technologique : Tech &amp; Web</h2>
<p>Cette feuille de route digitale est conçue et déployée avec notre partenaire et prestataire technologique <strong>Tech &amp; Web</strong> — conception de sites, applications métier et solutions numériques sur mesure. C'est cette alliance entre expertise terrain et savoir-faire technologique qui permet à NEXUS DKS GROUP d'innover au service de sa clientèle.</p>
<p><a href="https://tech-and-web.com" target="_blank" rel="noopener" title="Tech &amp; Web — conception de sites web, applications et solutions digitales sur mesure">Découvrir Tech &amp; Web, notre partenaire technologique &rarr;</a></p>
<div class="nx-article-keys">
  <h3>À retenir</h3>
  <ul>
    <li>Le contact de proximité (WhatsApp, configurateurs) réduit le temps d'intervention.</li>
    <li>En interne, des systèmes informatisés pilotent les process et encadrent les équipes.</li>
    <li>D'autres innovations suivront, avec notre partenaire technologique Tech &amp; Web.</li>
  </ul>
</div>
""",
}

def build_articles():
    n = len(ARTICLES)
    for idx, (slug, catg, ttl, exc, img, rt) in enumerate(ARTICLES):
        # liens articles connexes
        related = ""
        for j in range(1, 3):
            r = ARTICLES[(idx + j) % n]
            related += '<article class="nx-blog-card reveal"><a class="nx-blog-media" href="%s.html"><span class="nx-blog-cat">%s</span><img src="../%s" alt="%s" loading="lazy"></a><div class="nx-blog-body"><h3>%s</h3><a class="nx-blog-link" href="%s.html">Lire %s</a></div></article>\n' % (r[0], r[1], r[4], r[2], r[2], r[0], ico("arrow"))
        banner = """<div class="nx-read-progress" aria-hidden="true"><span data-read-bar></span></div>
<section class="svc-hero svc-hero-article">
  <img class="svc-hero-bg" src="../%s" alt="" aria-hidden="true">
  <div class="container">
    <nav class="svc-crumb" aria-label="Fil d'Ariane"><a href="../index.html">Accueil</a><span>/</span><a href="../blog.html">Blog</a><span>/</span><b>%s</b></nav>
    <span class="nx-eyebrow">%s · Lecture %s</span>
    <h1 style="font-size:clamp(2rem,3.6vw,3.1rem);max-width:24ch">%s</h1>
  </div>
</section>""" % (img, catg, catg, rt, ttl)
        url = SITE["domain"] + "/blog/" + slug + ".html"
        wa_share = "https://wa.me/?text=" + quote(ttl + " — " + url)
        article = """<section class="section"><div class="container">
  <div class="nx-article-layout">
    <article class="nx-article reveal">%s
      <div class="nx-article-sign">
        <span class="nx-avatar">N</span>
        <div><strong>Équipe NEXUS DKS GROUP</strong><span>Experts de l'entretien professionnel — Cotonou, Bénin</span></div>
      </div>
      <div class="nx-article-nav">
        <a class="btn-secondary" href="../blog.html">%s Tous les articles</a>
        <a class="btn-lime" href="../contact.html">%s Demander un devis</a>
      </div>
    </article>
    <aside class="nx-article-aside">
      <div class="nx-aside-card reveal">
        <span class="nx-aside-cat">%s</span>
        <div class="nx-aside-meta">%s Lecture %s</div>
        <div class="nx-aside-share">
          <span>Partager</span>
          <a class="nx-share-btn" href="%s" target="_blank" rel="noopener noreferrer" aria-label="Partager sur WhatsApp">%s</a>
          <button type="button" class="nx-share-btn" data-copy="%s" aria-label="Copier le lien de l'article">%s</button>
        </div>
      </div>
      <div class="nx-aside-cta reveal d1">
        <h3>Un besoin d'entretien ?</h3>
        <p>Diagnostic sur site et devis clair en FCFA sous 24&nbsp;h.</p>
        <a class="btn-lime" href="../contact.html">%s Demander un devis</a>
      </div>
    </aside>
  </div>
</div></section>""" % (ARTICLE_BODY[slug], ico("arrow"), ico("send"), catg, ico("clock"), rt, wa_share, ico("message"), url, ico("link"), ico("send"))
        # injecter les icônes check dans les <li> de l'article
        article = article.replace("<li>", "<li>" + ico("check"))
        rel = '<section class="section section-soft"><div class="container"><div class="section-header reveal"><div class="section-heading"><span class="nx-eyebrow">À lire aussi</span><h2 class="section-title">Articles connexes</h2></div></div><div class="nx-grid cols-2">%s</div></div></section>' % related
        # données structurées (SEO + chatbots) : BlogPosting
        ld_obj = {
            "@context": "https://schema.org", "@type": "BlogPosting",
            "headline": ttl, "description": exc,
            "image": SITE["domain"] + "/" + img,
            "author": {"@type": "Organization", "name": "NEXUS DKS GROUP"},
            "publisher": {"@type": "Organization", "name": "NEXUS DKS GROUP",
                          "logo": {"@type": "ImageObject", "url": SITE["domain"] + "/img/brand/nexus-logo.png"}},
            "mainEntityOfPage": SITE["domain"] + "/blog/" + slug + ".html",
            "articleSection": catg, "inLanguage": "fr-BJ",
        }
        ld = '<script type="application/ld+json">' + json.dumps(ld_obj, ensure_ascii=False) + '</script>\n'
        body = ld + banner + article + rel
        title = "%s | Blog NEXUS DKS GROUP" % ttl
        desc = exc[:155]
        ld_path = "blog/%s.html" % slug
        write("blog/%s.html" % slug, head(title, desc, ld_path, "page-article", prefix="../") + header("blog", prefix="../") + body + footer(prefix="../"))


# ============================================================ CONTACT
def build_contact():
    banner = """<section class="contact-hero">
  <div class="container">
    <div class="contact-hero-grid">
      <div class="reveal">
        <span class="nx-eyebrow">Contact &amp; devis</span>
        <h1>Demandez votre devis gratuit</h1>
        <p class="lead">Un besoin d'entretien ponctuel ou un contrat régulier ? Décrivez-nous vos espaces : nous revenons vers vous sous 24&nbsp;heures.</p>
        <div class="nx-hero-cta"><a class="btn-lime" href="tel:__T1H__">__PH__ __T1D__</a><a class="btn-secondary" href="https://wa.me/__WA__" target="_blank" rel="noopener noreferrer">__MSG__ WhatsApp</a></div>
        <div class="nx-hero-note"><span>__CK__ Réponse sous 24&nbsp;h</span><span>__CK__ Devis en FCFA</span><span>__CK__ Cotonou &amp; tout le Bénin</span></div>
      </div>
      <figure class="contact-hero-card reveal d1">
        <img src="img/brand/nexus-contact-card.jpg" alt="NEXUS DKS GROUP — matériel professionnel et coordonnées de contact" width="1100" height="1100">
      </figure>
    </div>
  </div>
  <span class="nx-banner-rule"></span>
</section>""".replace("__T1H__", SITE["tel1_href"]).replace("__T1D__", SITE["tel1_disp"]).replace("__WA__", SITE["wa"]).replace("__PH__", ico("phone")).replace("__MSG__", ico("message")).replace("__CK__", ico("check"))
    body = banner + contact_section()
    title = "Contact &amp; devis | NEXUS DKS GROUP — Cotonou"
    desc = "Contactez NEXUS DKS GROUP à Cotonou pour un devis d'entretien : téléphone, WhatsApp, email. Réponse sous 24 h. C/34 Guinkomey, Cotonou (Bénin)."
    write("contact.html", head(title, desc, "contact.html", "page-contact") + header("contact") + body + footer())


# ============================================================ CARRIÈRES
def build_carrieres():
    hero = """<section class="svc-hero svc-hero-article">
  <img class="svc-hero-bg" src="img/services/hero-entreprises.jpg" alt="" aria-hidden="true">
  <div class="container">
    <span class="nx-eyebrow">Carrières · Recrutement</span>
    <h1>Construisons ensemble la nouvelle norme du propre</h1>
    <p class="lead">NEXUS DKS GROUP recrute des profils rigoureux, fiers du travail bien fait. Formation continue, encadrement et matériel professionnel : ici, l'entretien est un véritable métier d'expertise.</p>
    <div class="nx-hero-cta"><a class="btn-lime" href="#postuler">__RKT__ Postuler en 1 minute</a><a class="btn-secondary" href="nexus-dks-group-presentation.pdf" download>__DL__ La brochure</a></div>
  </div>
</section>""".replace("__RKT__", ico("rocket")).replace("__DL__", ico("download"))

    JOIN = [
        ("graduation", "Formation continue", "Montée en compétence sur nos protocoles métier : bionettoyage, injection-extraction, HACCP, ERP."),
        ("users", "Équipes encadrées", "Un cadre clair, des chefs d'équipe, des consignes précises — et le respect de chacun."),
        ("spray", "Matériel professionnel", "Vous travaillez avec un équipement de niveau pro, pas avec les moyens du bord."),
        ("target", "Évolution au mérite", "Le sérieux et la régularité ouvrent l'accès à des postes d'encadrement et de spécialiste."),
    ]
    feats = "".join('<article class="nx-feature reveal%s"><span class="nx-ico is-lime">%s</span><div><h3>%s</h3><p>%s</p></div></article>' % (" d%d" % (i % 3) if i % 3 else "", ico(ic), t, d) for i, (ic, t, d) in enumerate(JOIN))
    why = """<section class="section">
  <div class="container">
    <div class="svc-split">
      <div class="reveal">
        <span class="nx-eyebrow">Pourquoi nous rejoindre</span>
        <h2 class="section-title">Un métier d'expertise, un cadre qui fait grandir</h2>
        <p class="section-copy">Chez NEXUS DKS GROUP, la propreté n'est pas un petit boulot : c'est une discipline. Nous formons, encadrons et équipons nos équipes pour qu'elles livrent une exigence — et en soient fières.</p>
      </div>
      <div class="nx-feature-list reveal d1">%s</div>
    </div>
  </div>
</section>""" % feats

    ROLES = [
        ("Agent d'entretien", "broom", "Nettoyage courant et bionettoyage, sens du détail, ponctualité et discrétion."),
        ("Chef d'équipe", "users", "Encadrement terrain, contrôle qualité et relation client de proximité."),
        ("Technicien spécialisé", "droplet", "Injection-extraction, monobrosse, haute pression, nettoyage fin de chantier."),
        ("Superviseur qualité", "badge", "Contrôle interne après exécution, traçabilité et amélioration continue."),
        ("Commercial · Développement", "briefcase", "Prospection B2B, devis, suivi de comptes et partenariats institutionnels."),
        ("Candidature spontanée", "heart", "Un autre profil fiable et motivé ? Présentez-vous : nous cherchons des talents."),
    ]
    rc = "".join('<article class="nx-card reveal%s"><span class="nx-ico is-lime">%s</span><h3>%s</h3><p>%s</p></article>\n' % (" d%d" % (i % 3) if i % 3 else "", ico(ic), t, d) for i, (t, ic, d) in enumerate(ROLES))
    roles = """<section class="section section-soft">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Profils recherchés</span>
      <h2 class="section-title">Les talents qui font la différence</h2>
      <p class="section-copy">Du terrain à l'encadrement, nous recrutons des personnes fiables, ponctuelles et exigeantes sur la qualité.</p>
    </div></div>
    <div class="nx-grid cols-3">%s</div>
  </div>
</section>""" % rc

    fields = [
        ("select", "Poste visé", ["Agent d'entretien", "Chef d'équipe", "Technicien spécialisé", "Superviseur qualité", "Commercial / Développement", "Candidature spontanée"]),
        ("select", "Expérience", ["Débutant·e motivé·e", "1 à 3 ans", "3 à 5 ans", "Plus de 5 ans"]),
        ("select", "Disponibilité", ["Immédiate", "Sous 2 semaines", "Sous 1 mois", "À convenir"]),
        ("text", "Zone / quartier", "Ex. Cotonou, Calavi, Akpakpa…"),
    ]
    ff = ""
    for f in fields:
        if f[0] == "select":
            _, flab, opts = f
            o = '<option value="">Choisir…</option>' + "".join("<option>%s</option>" % x for x in opts)
            ff += '<label class="nx-config-field"><span>%s</span><select data-field data-label="%s">%s</select></label>' % (flab, flab, o)
        else:
            _, flab, ph = f
            ff += '<label class="nx-config-field"><span>%s</span><input type="text" data-field data-label="%s" placeholder="%s"></label>' % (flab, flab, ph)
    config = """<section id="postuler" class="section">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Postuler</span>
      <h2 class="section-title">Déposez votre candidature en 30 secondes</h2>
      <p class="section-copy">Renseignez l'essentiel : nous générons un message WhatsApp pré-rempli. Vous l'envoyez, notre équipe RH vous recontacte. Pensez à joindre votre CV dans la conversation.</p>
    </div></div>
    <div class="svc-config-wrap reveal">
      <div class="svc-tool">
        <div class="svc-tool-head"><span class="nx-ico is-navy">%s</span><h3>Pourquoi postuler chez nous ?</h3></div>
        <ul class="nx-list" style="margin-top:4px">
          <li>%s<span>Un employeur de droit béninois, structuré et fiable</span></li>
          <li>%s<span>Formation, encadrement et matériel professionnel</span></li>
          <li>%s<span>Des perspectives d'évolution au mérite</span></li>
        </ul>
      </div>
      <form class="nx-config" data-service="Candidature" data-wa="%s" data-wa-intro="Je souhaite déposer ma candidature chez NEXUS DKS GROUP." data-wa-outro="Merci de me recontacter pour la suite du recrutement.">
        <div class="nx-config-grid">%s</div>
        <div class="nx-config-actions">
          <button type="button" class="btn-lime" data-wa-build>%s Envoyer ma candidature par WhatsApp</button>
          <a class="btn-secondary" href="contact.html">%s Nous écrire</a>
        </div>
        <p class="form-note">Aucun engagement : votre message s'ouvre dans WhatsApp, vous l'envoyez si vous le souhaitez.</p>
      </form>
    </div>
  </div>
</section>""" % (ico("heart"), ico("check"), ico("check"), ico("check"), SITE["wa"], ff, ico("message"), ico("send"))

    body = hero + why + roles + config + cta(title="Envie de rejoindre l'aventure NEXUS&nbsp;?",
        text="Postulez dès maintenant, ou téléchargez notre brochure de présentation pour mieux nous connaître.")
    title = "Carrières & recrutement | NEXUS DKS GROUP — Cotonou (Bénin)"
    desc = "Rejoignez NEXUS DKS GROUP, entreprise de droit béninois d'entretien professionnel à Cotonou : agents, chefs d'équipe, techniciens, superviseurs. Postulez par WhatsApp."
    write("carrieres.html", head(title, desc, "carrieres.html", "page-carrieres") + header("") + body + footer())


# ============================================================ 404
def build_404():
    body = """<section class="page-banner" style="--banner-image:url('img/services/bandeau-supplies.jpg')">
  <div class="container"><div class="banner-shell reveal">
    <span class="nx-eyebrow">Erreur 404</span>
    <h1>Cette page a disparu au grand nettoyage</h1>
    <p class="lead">La page demandée n'existe pas ou a été déplacée. Retrouvez l'essentiel ci-dessous.</p>
    <div class="nx-hero-cta"><a class="btn-lime" href="index.html">Retour à l'accueil</a><a class="btn-secondary" href="nos-services.html">Nos services</a><a class="btn-secondary" href="contact.html">Contact</a></div>
  </div></div>
  <span class="nx-banner-rule"></span>
</section>"""
    title = "Page introuvable (404) | NEXUS DKS GROUP"
    desc = "Page introuvable. Revenez à l'accueil de NEXUS DKS GROUP — entretien professionnel à Cotonou."
    write("404.html", head(title, desc, "404.html", "page-404") + header("") + body + footer())


# ============================================================ PAGES SERVICES (détail)
# Image dédiée + contenu technique (≈60%) + outil-métier wow + configurateur WhatsApp.
SVC_IMG = {
    "entreprises-bureaux": "svc-bureaux.jpg", "fin-de-chantier": "svc-fin-chantier.jpg",
    "residences": "svc-residences.jpg", "restaurants-lounges": "svc-restaurants.jpg",
    "espaces-specifiques": "svc-espaces.jpg", "textiles-surfaces": "svc-textiles.jpg",
}

SERVICES_DETAIL = {
 "entreprises-bureaux": {
  "eyebrow": "Tertiaire · B2B · Institutions",
  "accroche": "Un plan de propreté piloté pour des bureaux sains, valorisants et propices à la performance.",
  "intro": [
   "L'entretien tertiaire ne s'improvise pas : il se pilote. Nous établissons un <strong>plan de propreté</strong> contractuel qui cartographie vos zones — open-spaces, salles de réunion, sanitaires, circulations, points de restauration — et leur affecte une fréquence d'intervention proportionnée au trafic et au risque sanitaire.",
   "Nos protocoles combinent <strong>bionettoyage</strong> des surfaces, <strong>désinfection ciblée des points de contact</strong> à fort passage (poignées, interrupteurs, ascenseurs, sanitaires) et traçabilité des passages. Microfibre code-couleur pour éliminer les transferts microbiens, dosage maîtrisé, produits adaptés à chaque support.",
  ],
  "points": [
   ("clipboard", "Plan de propreté", "Cartographie des zones, fréquences et niveaux de prestation formalisés dans un cahier des charges."),
   ("spray", "Bionettoyage", "Nettoyage et désinfection en un geste sur les surfaces et points de contact sensibles."),
   ("droplet", "Microfibre code-couleur", "Une couleur par zone (sanitaires, bureaux, cuisine) — zéro contamination croisée."),
   ("clipboard", "Traçabilité", "Fiches de passage et contrôle qualité après chaque intervention."),
  ],
  "reco": ("Fréquence recommandée selon votre trafic", "Niveau de fréquentation", [
   ("Faible — petite équipe", "Recommandé : 1 à 2 passages par semaine."),
   ("Modéré — bureaux classiques", "Recommandé : 3 passages par semaine."),
   ("Intense — accueil public", "Recommandé : passage quotidien (5j/7)."),
   ("Très intense — fort flux", "Recommandé : quotidien + repasse en milieu de journée."),
  ]),
  "fields": [
   ("select", "Type de locaux", ["Bureaux cloisonnés", "Open-space", "Plateau mixte", "Cabinet / clinique", "Coworking"]),
   ("select", "Surface approximative", ["Moins de 100 m²", "100 à 300 m²", "300 à 800 m²", "Plus de 800 m²"]),
   ("select", "Occupants", ["Moins de 10", "10 à 30", "30 à 80", "Plus de 80"]),
   ("text", "Contraintes horaires", "Ex. avant 8h, après 18h, week-end…"),
  ],
  "targets": ["PME & sièges sociaux", "Cabinets (conseil, médical, juridique)", "Institutions & administrations", "Coworkings & incubateurs", "Banques & assurances"],
 },
 "fin-de-chantier": {
  "eyebrow": "BTP · Livraison · Remise en état",
  "accroche": "La remise en état post-travaux qui transforme un chantier livré en espace prêt à occuper — sans la moindre trace.",
  "intro": [
   "Le nettoyage de fin de chantier est une <strong>prestation technique à part entière</strong>, distincte de l'entretien courant. Il s'attaque aux résidus de construction : laitance de ciment, traces de peinture et d'enduit, colles, films de protection, poussières fines incrustées dans les menuiseries et les VMC.",
   "Nous opérons en <strong>plusieurs passes</strong> : dégrossissage et évacuation des gravats, décollage et décapage des salissures adhérentes, puis finition fine des vitrages, sols et surfaces. Objectif : une réception <strong>« prête à occuper »</strong>, contrôlée poste par poste avant remise des clés.",
  ],
  "points": [
   ("droplet", "Décapage laitance", "Élimination des voiles de ciment et résidus minéraux sur sols et faïences."),
   ("sparkle", "Décollage de films", "Retrait des films de protection, adhésifs et traces de peinture sans rayer."),
   ("sparkle", "Vitrages sans trace", "Vitres, châssis et menuiseries, en intérieur et extérieur accessible."),
   ("wind", "Dépoussiérage fin", "Poussières incrustées : VMC, plinthes, gaines, luminaires, interstices."),
  ],
  "checklist": ("Checklist de réception « prêt à occuper »", [
   "Gravats & déchets évacués", "Films de protection & adhésifs retirés", "Laitance & traces de ciment décapées",
   "Vitrages & menuiseries nettoyés", "Sols lavés et protégés", "Sanitaires désinfectés",
   "Poussières fines (VMC, plinthes, luminaires)", "Contrôle final poste par poste",
  ]),
  "fields": [
   ("select", "Type de chantier", ["Construction neuve", "Rénovation", "Extension", "Local commercial"]),
   ("select", "Surface approximative", ["Moins de 100 m²", "100 à 300 m²", "300 à 1000 m²", "Plus de 1000 m²"]),
   ("select", "Niveaux", ["Plain-pied", "2 niveaux", "3 niveaux et plus"]),
   ("text", "Échéance souhaitée", "Ex. livraison le 30/06, urgent…"),
  ],
  "targets": ["Entreprises du BTP", "Promoteurs immobiliers", "Architectes & maîtres d'œuvre", "Agences immobilières", "Particuliers en fin de travaux"],
 },
 "residences": {
  "eyebrow": "Particuliers · B2C · Confort",
  "accroche": "Votre intérieur soigné comme il le mérite — la sérénité d'un refuge impeccable, sans y penser.",
  "intro": [
   "Du <strong>grand ménage de remise à neuf</strong> à l'entretien récurrent, nous adaptons la prestation au rythme de votre refuge. Chaque intervention suit une logique <strong>du plus propre au plus sale</strong> et <strong>du haut vers le bas</strong> pour ne jamais re-salir une zone déjà traitée.",
   "Cuisine dégraissée, sanitaires détartrés et désinfectés, sols adaptés à chaque revêtement (carrelage, parquet, marbre), vitrerie intérieure : un protocole complet, des produits adaptés aux matériaux et une discrétion totale.",
  ],
  "points": [
   ("sparkle", "Grand ménage", "Remise à neuf en profondeur : idéal avant emménagement ou après événement."),
   ("refresh", "Entretien récurrent", "Passages planifiés (hebdo, bi-mensuel, mensuel) selon votre rythme."),
   ("shield", "Soin des matériaux", "Gestes et produits adaptés : parquet, marbre, inox, surfaces fragiles."),
   ("smile", "Discrétion & confiance", "Personnel encadré, ponctuel et respectueux de votre intimité."),
  ],
  "reco": ("Quelle formule pour vous ?", "Votre objectif", [
   ("Remise à neuf ponctuelle", "Recommandé : grand ménage en profondeur, intervention unique."),
   ("Entretien régulier", "Recommandé : abonnement récurrent au rythme choisi."),
   ("Avant état des lieux", "Recommandé : nettoyage complet de restitution, finitions garanties."),
  ]),
  "fields": [
   ("select", "Type de logement", ["Studio", "Appartement", "Maison", "Duplex / Villa"]),
   ("select", "Nombre de pièces", ["1 à 2", "3 à 4", "5 à 6", "7 et plus"]),
   ("select", "Rythme souhaité", ["Ponctuel", "Hebdomadaire", "Bi-mensuel", "Mensuel"]),
   ("text", "Date souhaitée", "Ex. samedi matin, dès que possible…"),
  ],
  "targets": ["Particuliers & familles", "Expatriés & cadres", "Locations meublées & Airbnb", "Syndics & gestionnaires", "Résidences de standing"],
 },
 "restaurants-lounges": {
  "eyebrow": "CHR · Hygiène · Réputation",
  "accroche": "L'hygiène irréprochable qui protège votre réputation et celle de vos clients.",
  "intro": [
   "En restauration, la propreté est un <strong>enjeu sanitaire et réputationnel</strong>. Nos protocoles s'alignent sur les <strong>bonnes pratiques d'hygiène (HACCP)</strong> : dégraissage des plans, équipements et hottes, désinfection des surfaces en contact alimentaire, traitement des sols antidérapants et gestion des zones froides.",
   "Nous intervenons <strong>en horaires décalés</strong> — la nuit, après le service ou avant l'ouverture — pour ne jamais perturber votre exploitation. Microfibre code-couleur, dégraissants alimentaires et un soin particulier aux espaces d'accueil qui font votre image.",
  ],
  "points": [
   ("shield", "Conforme HACCP", "Protocoles alignés sur les bonnes pratiques d'hygiène alimentaire."),
   ("flask", "Dégraissage cuisine", "Plans, équipements, crédences et hottes : la graisse n'a aucune chance."),
   ("disc", "Sols antidérapants", "Traitement adapté aux sols techniques de cuisine et zones humides."),
   ("clock", "Horaires décalés", "Nuit, après-service, avant-ouverture : zéro impact sur votre activité."),
  ],
  "checklist": ("Planifiez votre intervention hors-service — zones à couvrir", [
   "Cuisine & plonge", "Salle & bar", "Terrasse / extérieur", "Sanitaires clients", "Réserves & chambres froides", "Vitrines & accueil",
  ]),
  "fields": [
   ("select", "Type d'établissement", ["Restaurant", "Lounge / bar", "Fast-food", "Traiteur", "Hôtel-restaurant"]),
   ("select", "Surface approximative", ["Moins de 80 m²", "80 à 200 m²", "200 à 500 m²", "Plus de 500 m²"]),
   ("reco", "Créneau d'intervention", [
     ("Nuit (après fermeture)", "Intervention nocturne : locaux opérationnels dès l'ouverture."),
     ("Après-service", "Remise en état immédiate après le dernier couvert."),
     ("Avant-ouverture", "Mise en propreté juste avant l'accueil des clients."),
   ]),
   ("select", "Fréquence", ["Quotidienne", "Plusieurs fois/semaine", "Hebdomadaire", "Ponctuelle"]),
  ],
  "targets": ["Restaurants & brasseries", "Lounges & bars", "Hôtels & resorts", "Traiteurs & food-courts", "Franchises CHR"],
 },
 "espaces-specifiques": {
  "eyebrow": "ERP · Événementiel · Forte affluence",
  "accroche": "Des lieux à forte fréquentation entretenus avec des protocoles dédiés : confort, sécurité et image.",
  "intro": [
   "Salles de cinéma, de conférence, de spectacle, espaces événementiels : ces <strong>établissements recevant du public (ERP)</strong> imposent des contraintes de <strong>forte fréquentation</strong> et de <strong>rotation rapide</strong>. Nous y répondons par des protocoles dédiés et une logistique de <strong>remise en état express entre deux événements</strong>.",
   "Désinfection des sièges et points de contact, gestion des déchets en volume, nettoyage des sols techniques et des grandes surfaces vitrées, traitement des sanitaires à fort passage : tout est calibré pour la sécurité et le confort du public.",
  ],
  "points": [
   ("shield", "Protocoles ERP", "Conformes aux exigences des établissements recevant du public."),
   ("refresh", "Remise en état express", "Rotation rapide entre deux séances ou événements."),
   ("broom", "Gestion de volume", "Déchets, grandes surfaces, fort passage : logistique dimensionnée."),
   ("sofa", "Désinfection sièges", "Points de contact et assises traités à chaque rotation."),
  ],
  "reco": ("Estimez votre rotation entre événements", "Type d'établissement", [
   ("Salle de cinéma", "Remise en état express : ~20 à 40 min entre deux séances selon la capacité."),
   ("Salle de conférence", "Réagencement + désinfection : prévoir ~30 à 60 min entre deux sessions."),
   ("Salle de fête / réception", "Remise à blanc complète : ~2 à 4 h selon la surface et l'affluence."),
   ("Espace événementiel", "Logistique sur mesure : équipe dimensionnée selon le programme."),
  ]),
  "fields": [
   ("select", "Capacité d'accueil", ["Moins de 100", "100 à 300", "300 à 800", "Plus de 800"]),
   ("select", "Fréquence d'événements", ["Quotidienne", "Hebdomadaire", "Mensuelle", "Ponctuelle"]),
   ("select", "Grandes surfaces vitrées", ["Oui, importantes", "Modérées", "Peu / pas"]),
   ("text", "Prochaine échéance", "Ex. événement le 15/07…"),
  ],
  "targets": ["Cinémas & lieux culturels", "Centres de conférence", "Salles de fête & réception", "Organisateurs d'événements", "Établissements ERP"],
 },
 "textiles-surfaces": {
  "eyebrow": "Traitement technique · Profondeur",
  "accroche": "La technicité du nettoyage en profondeur : redonner éclat et hygiène à vos textiles et revêtements.",
  "intro": [
   "Le traitement des textiles et surfaces dures relève d'une <strong>expertise machine</strong>. Selon le support, le protocole change : <strong>injection-extraction</strong> pour les moquettes et tapis, <strong>shampouinage</strong> et détachage pour canapés et fauteuils, <strong>désinfection vapeur</strong> pour les matelas, <strong>cristallisation</strong> et lustrage pour les sols durs.",
   "Chaque fibre et chaque revêtement a sa chimie : nous sélectionnons le détergent, la température et la mécanique adaptés pour un résultat profond, sans agresser le matériau.",
  ],
  "points": [
   ("droplet", "Injection-extraction", "Moquettes : pulvérisation d'une solution puis extraction immédiate des salissures."),
   ("sofa", "Shampouinage textile", "Canapés, fauteuils, sièges : détachage et ravivage des fibres."),
   ("shield", "Désinfection matelas", "Traitement anti-acariens et assainissement en profondeur."),
   ("disc", "Cristallisation", "Sols durs (marbre, granito) : brillance et protection durables."),
  ],
  "reco": ("Diagnostic express : quel protocole pour votre support ?", "Votre support", [
   ("Moquette / Tapis", "Protocole : injection-extraction — pulvérisation détergente puis extraction des salissures et de l'humidité."),
   ("Canapé / fauteuil tissu", "Protocole : shampouinage + détachage — ravivage des fibres, séchage maîtrisé."),
   ("Canapé / siège cuir", "Protocole : nettoyage doux + nourrissage du cuir, sans dessécher la matière."),
   ("Matelas", "Protocole : aspiration profonde + désinfection vapeur, traitement anti-acariens."),
   ("Sol dur (marbre / granito)", "Protocole : cristallisation + lustrage — brillance et protection durables."),
   ("Carrelage & joints", "Protocole : décapage + protection des joints — éclat et hygiène retrouvés."),
  ]),
  "fields": [
   ("select", "Quantité / surface", ["1 pièce / petit", "2 à 3 pièces", "Surface importante", "Lot / volume pro"]),
   ("select", "Niveau d'encrassement", ["Léger", "Moyen", "Très encrassé"]),
   ("text", "Précisions", "Ex. taches, matière, accès…"),
  ],
  "targets": ["Hôtels & résidences", "Bureaux & institutions", "Salles de réception", "Particuliers", "Syndics & gestionnaires"],
 },
}

# Précision technique par déclinaison (alignée sur l'ordre des bullets de CATS).
# Enrichit la liste sur la page dédiée sans alourdir la carte de nos-services.
SVC_TECH = {
 "entreprises-bureaux": [
  "Détergent-désinfectant virucide, temps de contact respecté, microfibre dédiée par zone.",
  "Poignées, interrupteurs, ascenseurs : zones à fort risque tracées à chaque passage.",
  "Détartrage et désinfection des sanitaires, réassort papier et savon planifié.",
  "Cahier des charges, fréquences contractuelles et contrôle qualité après intervention.",
 ],
 "fin-de-chantier": [
  "Tri et évacuation des gravats, emballages et chutes de chantier.",
  "Décapage de la laitance ciment et retrait des adhésifs sans rayer les supports.",
  "Raclette professionnelle, finition vitrages sans trace, dépoussiérage des menuiseries.",
  "Contrôle poste par poste et levée des réserves avant remise des clés.",
 ],
 "residences": [
  "Remise à neuf en profondeur, du haut vers le bas, sans re-salissure.",
  "Passages planifiés (hebdo, bi-mensuel, mensuel) au rythme du refuge.",
  "Produits adaptés à chaque support : parquet, marbre, inox, faïence.",
  "Prise de rendez-vous rapide par téléphone ou WhatsApp.",
 ],
 "restaurants-lounges": [
  "Dégraissants alimentaires sur plans, crédences, équipements et hottes.",
  "Surfaces d'accueil, mobilier et vitrines soignés pour votre image.",
  "Méthodes alignées sur les bonnes pratiques d'hygiène (HACCP).",
  "Nuit, après-service ou avant-ouverture : zéro impact sur l'exploitation.",
 ],
 "espaces-specifiques": [
  "Désinfection des sièges et points de contact à chaque rotation.",
  "Remise à blanc des grandes surfaces et gestion des déchets en volume.",
  "Conformité aux exigences des établissements recevant du public (ERP).",
  "Logistique dimensionnée pour une rotation rapide entre deux événements.",
 ],
 "textiles-surfaces": [
  "Injection de shampooing, détachage et ravivage des fibres, séchage maîtrisé.",
  "Pulvérisation détergente puis extraction des salissures et de l'humidité.",
  "Aspiration profonde et désinfection vapeur, traitement anti-acariens.",
  "Cristallisation et lustrage du marbre : brillance et protection durables.",
 ],
}

def build_service_pages():
    slugs = list(SERVICES_DETAIL.keys())
    for idx, slug in enumerate(slugs):
        D = SERVICES_DETAIL[slug]
        _, label, icon, desc, bullets = CATMAP[slug]
        img = SVC_IMG[slug]

        hero = """<section class="svc-hero">
  <img class="svc-hero-bg" src="../img/services/%s" alt="" aria-hidden="true">
  <div class="container">
    <nav class="svc-crumb" aria-label="Fil d'Ariane"><a href="../index.html">Accueil</a><span>/</span><a href="../nos-services.html">Services</a><span>/</span><b>%s</b></nav>
    <span class="nx-eyebrow">%s</span>
    <h1>%s</h1>
    <p class="lead">%s</p>
    <div class="nx-hero-cta"><a class="btn-lime" href="#config">%s Configurer ma demande</a><a class="btn-secondary" href="https://wa.me/%s" target="_blank" rel="noopener noreferrer">%s WhatsApp</a></div>
  </div>
</section>""" % (img, label, D["eyebrow"], label, D["accroche"], ico("send"), SITE["wa"], ico("message"))

        pts = "".join('<article class="nx-feature reveal%s"><span class="nx-ico is-lime">%s</span><div><h3>%s</h3><p>%s</p></div></article>' % (" d%d" % (k % 3) if k % 3 else "", ico(ic), t, d) for k, (ic, t, d) in enumerate(D["points"]))
        intro = "".join('<p class="section-copy">%s</p>' % p for p in D["intro"])
        expertise = """<section class="section">
  <div class="container">
    <div class="svc-split">
      <div class="reveal">
        <span class="nx-eyebrow">Expertise technique</span>
        <h2 class="section-title">%s</h2>
        %s
      </div>
      <div class="nx-feature-list reveal d1">%s</div>
    </div>
  </div>
</section>""" % (D["accroche"], intro, pts)

        techs = SVC_TECH.get(slug, [])
        bl = ""
        for k, b in enumerate(bullets):
            t = techs[k] if k < len(techs) else ""
            if t:
                bl += '<li>%s<div class="nx-list-rich"><strong>%s</strong><em>%s</em></div></li>' % (ico("check"), b, t)
            else:
                bl += "<li>%s<span>%s</span></li>" % (ico("check"), b)
        presta = """<section class="section section-soft">
  <div class="container">
    <div class="svc-presta">
      <div class="reveal">
        <span class="nx-eyebrow">Ce que nous prenons en charge</span>
        <h2 class="section-title">Prestations &amp; protocoles</h2>
        <p class="section-copy">%s</p>
        <ul class="nx-list">%s</ul>
      </div>
      <figure class="svc-presta-media reveal d1"><img src="../img/services/%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>
    </div>
  </div>
</section>""" % (desc, bl, img, label, label)

        # outil-métier : reco (select → résultat) ou checklist (cases + progression)
        tool = ""
        if "reco" in D:
            rtitle, rlabel, ropts = D["reco"]
            o = '<option value="">Choisir…</option>' + "".join('<option data-out="%s">%s</option>' % (out, lab) for lab, out in ropts)
            tool = """<div class="svc-tool reveal" data-reco>
  <div class="svc-tool-head"><span class="nx-ico is-navy">%s</span><h3>%s</h3></div>
  <label class="nx-config-field"><span>%s</span><select class="nx-reco-select" data-field data-label="%s">%s</select></label>
  <div class="nx-reco-out" hidden></div>
</div>""" % (ico("target"), rtitle, rlabel, rlabel, o)
        elif "checklist" in D:
            ctitle, citems = D["checklist"]
            checks = "".join('<label class="nx-check"><input type="checkbox" data-check data-group="%s" value="%s"><span>%s</span></label>' % (ctitle, it, it) for it in citems)
            tool = """<div class="svc-tool reveal" data-checklist>
  <div class="svc-tool-head"><span class="nx-ico is-navy">%s</span><h3>%s</h3></div>
  <div class="nx-config-progress"><div class="nx-config-progress-bar"></div><span class="nx-config-progress-label">0 / %d</span></div>
  <div class="nx-checks">%s</div>
</div>""" % (ico("clipboard"), ctitle, len(citems), checks)

        # configurateur → WhatsApp
        ff = ""
        for f in D["fields"]:
            if f[0] == "select":
                _, flab, opts = f
                o = '<option value="">Choisir…</option>' + "".join("<option>%s</option>" % x for x in opts)
                ff += '<label class="nx-config-field"><span>%s</span><select data-field data-label="%s">%s</select></label>' % (flab, flab, o)
            elif f[0] == "text":
                _, flab, ph = f
                ff += '<label class="nx-config-field"><span>%s</span><input type="text" data-field data-label="%s" placeholder="%s"></label>' % (flab, flab, ph)
            elif f[0] == "reco":
                _, flab, ropts = f
                o = '<option value="">Choisir…</option>' + "".join('<option data-out="%s">%s</option>' % (out, lab) for lab, out in ropts)
                ff += '<label class="nx-config-field"><span>%s</span><select class="nx-reco-select" data-field data-label="%s">%s</select></label>' % (flab, flab, o)
        config = """<section id="config" class="section">
  <div class="container">
    <div class="section-header reveal"><div class="section-heading">
      <span class="nx-eyebrow">Configurateur express</span>
      <h2 class="section-title">Préparez votre demande en 30 secondes</h2>
      <p class="section-copy">Renseignez l'essentiel : nous générons un message WhatsApp pré-rempli. Vous validez, nous revenons vers vous avec un devis ferme en FCFA sous 24&nbsp;h.</p>
    </div></div>
    <div class="svc-config-wrap reveal">
      %s
      <form class="nx-config" data-service="%s" data-wa="%s">
        <div class="nx-config-grid">%s</div>
        <div class="nx-reco-out" hidden></div>
        <div class="nx-config-actions">
          <button type="button" class="btn-lime" data-wa-build>%s Préparer ma demande WhatsApp</button>
          <a class="btn-secondary" href="../contact.html">%s Formulaire complet</a>
        </div>
        <p class="form-note">Aucun engagement : votre message s'ouvre dans WhatsApp, vous l'envoyez si vous le souhaitez.</p>
      </form>
    </div>
  </div>
</section>""" % (tool, label, SITE["wa"], ff, ico("message"), ico("send"))

        tg = "".join('<li>%s<span>%s</span></li>' % (ico("badge"), t) for t in D["targets"])
        # services connexes
        others = ""
        for j in (1, 2, 3):
            os_ = slugs[(idx + j) % len(slugs)]
            others += '<a class="svc-related-card" href="%s.html"><img src="../img/services/%s" alt="" loading="lazy"><span>%s %s</span></a>' % (os_, SVC_IMG[os_], CATMAP[os_][1], ico("arrow"))
        target = """<section class="section section-soft">
  <div class="container">
    <div class="svc-split">
      <div class="reveal">
        <span class="nx-eyebrow">À qui s'adresse ce service</span>
        <h2 class="section-title">Pensé pour vos enjeux</h2>
        <p class="section-copy">Nous adaptons protocoles, fréquences et horaires à votre réalité — du particulier exigeant à l'institution la plus structurée.</p>
        <ul class="nx-list nx-list-target">%s</ul>
      </div>
      <div class="reveal d1">
        <h3 class="svc-related-title">Autres expertises</h3>
        <div class="svc-related">%s</div>
      </div>
    </div>
  </div>
</section>""" % (tg, others)

        body = hero + expertise + presta + config + target \
            + cta(prefix="../", title="Un projet d'entretien %s ?" % label.lower(),
                  text="Décrivez votre besoin : diagnostic, protocole sur mesure et devis clair en FCFA sous 24&nbsp;heures.")
        title = "%s — Entretien professionnel | NEXUS DKS GROUP Cotonou" % label
        meta = "%s à Cotonou : %s" % (label, desc[:120])
        write("services/%s.html" % slug, head(title, meta, "services/%s.html" % slug, "page-service", prefix="../") + header("services", prefix="../") + body + footer(prefix="../"))


# ============================================================ MAIN
if __name__ == "__main__":
    build_home()
    build_services()
    build_service_pages()
    build_offre()
    build_about()
    build_blog()
    build_articles()
    build_contact()
    build_carrieres()
    build_404()
    print("\n✅ Site NEXUS DKS GROUP — ENTRETIEN régénéré.")
