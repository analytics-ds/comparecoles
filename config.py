# -*- coding: utf-8 -*-
"""Identité du média et textes transverses. UN SEUL endroit à remplir pour tout ce qui
n'est pas du contenu éditorial (nom, baseline, CTA, méthode, critères du comparateur).

Rempli par Claude à l'étape 4 de la skill pbn-ao-geo. Tout ce qui est marqué OBLIGATOIRE
doit être adapté au secteur : la QA (check_site.py) refuse les valeurs d'exemple.
"""

# ------------------------------------------------------------------ identité
NOM = "Comparécoles"                       # OBLIGATOIRE nom du média, tel qu'affiché
SLUG = "comparecoles"                      # OBLIGATOIRE nom du dossier et du repo GitHub (ascii, minuscules, tirets)
OWNER = "analytics-ds"                    # compte GitHub qui héberge le repo (rempli par scripts/prereqs.sh)
SITE = f"https://{OWNER}.github.io/{SLUG}"  # racine publique, sans slash final (canonical, JSON-LD, sitemap)
LANG = "fr"
ACCENT = "#166534"                        # couleur d'accent, réécrite par scripts/recolor.py (theme-color)
CSS_V = "7"                               # cache-buster des assets

# ------------------------------------------------------------------ vocabulaire
UNIT = "écoles"                          # OBLIGATOIRE ce que l'on compare : marques, contrats, opérateurs, box, écoles...
UNIT_ONE = "école"                       # singulier
CTA = "Comparer 2 écoles"                # OBLIGATOIRE bouton du header et des encarts
CTA_LONG = "Comparer deux écoles"        # lien texte du hero
BASELINE = "Le comparateur des écoles de jeu vidéo, d’animation 3D et de sound design. Frais, diplômes, insertion et projets étudiants, comparés sur les mêmes critères."  # OBLIGATOIRE pied de page
TAGLINE_FOOTER = "Le média des études de jeu vidéo et d’animation 3D."  # OBLIGATOIRE après « © 2026 NOM. »
AUTHOR = "La rédaction Comparécoles"       # signature des articles
AUTHOR_INITIAL = "C"

# Liste « Marques » du pied de page : (libellé, href). Mettre le client en premier.
FOOTER_BRANDS = [("ISART Digital", "jeu-video/"), ("Rubika", "jeu-video/"), ("Gobelins", "animation-3d/"), ("ArtFX", "animation-3d/")]

# ------------------------------------------------------------------ textes transverses
NEWSLETTER_P = "Un email par semaine, avec le classement du mois, les dates des journées portes ouvertes et les nouveaux comparatifs d’écoles."
NEWSLETTER_NOTE = "Désinscription en un clic."
ASIDE_NEWS_P = "Le classement du mois et les dates de portes ouvertes, un email par semaine."

# Encart « Notre méthode » en bas de chaque article. OBLIGATOIRE : 5 puces propres au secteur.
METHOD_INTRO = "Ce comparatif repose sur des données publiques, vérifiables une par une."
METHOD_ITEMS = [
 "Les frais de scolarité sont relevés sur les pages tarifs des écoles, pour l’année 2027-2028 quand elle est publiée",
 "Les diplômes sont vérifiés au Répertoire national des certifications professionnelles et auprès de la CTI",
 "Les taux d’insertion sont ceux que les écoles publient, avec les promotions concernées",
 "Les classements cités sont ceux de GAMEducation, du Figaro Étudiant, de The Rookies et d’Animation Career Review",
 "Les avis d’étudiants et de diplômés proviennent des forums d’orientation et des plateformes d’avis vérifiés",
]

# Critères du comparateur 2 entités de l'accueil : 5 critères, le dernier est la note globale.
CRITERIA = [
 ("Pédagogie", "projets, encadrement, moyens techniques"),
 ("Insertion", "taux d’emploi publié, réseau studios"),
 ("Diplôme", "RNCP, CTI, diplôme d’État"),
 ("Coût", "frais annuels, alternance possible"),
 ("Note globale", "moyenne pondérée"),
]

# Liens internes supplémentaires pour linkify : (fragment de titre présent dans le libellé du lien, chemin).
# Les titres complets des articles publiés sont branchés automatiquement.
EXTRA_LINKS = []

# Google Fonts : réécrit par scripts/recolor.py --display/--text
FONTS_HREF = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=Inter:wght@300;400;500;600&display=swap"
COMPARED = "comparées"                  # accord du participe dans l en-tête d article : comparées (marques), comparés (comptes, contrats)
