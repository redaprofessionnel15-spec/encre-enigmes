# Du 14 au 30 novembre 2026 : 2 Shorts par jour (16 h et 19 h). Histoire insolite et mystères.
from xmas_specs import V, S, Y, C, Q, CTA

DET = {"hat": "detective", "coat": "brown", "accessory": "magnifier"}
NAVY = {"hat": "bicorne", "coat": "navy", "accessory": "spyglass"}
DARK = {"hat": "tricorne", "coat": "black", "accessory": "lantern"}
GREEN = {"hat": "tricorne", "coat": "green", "accessory": "spyglass"}
RED = {"hat": "beret", "coat": "red", "accessory": "magnifier"}
WHITE = {"hat": "headphones", "coat": "white", "accessory": "radio"}
def at(day, h): return f"2026-11-{day:02d}T{h}:00:00+01:00"

SHORTS = [
 ("068-louvre-2025", at(14, 19), "Le casse du Louvre en moins de 8 minutes", DET,
  ["Euronews, Cerveau du casse du Louvre (13/07/2026)", "Franceinfo, Cambriolage au musée du Louvre"], [
  ("Un dimanche matin, en plein jour, des voleurs ont pillé le Louvre en moins de huit minutes.", V("Impossible ?", "8 MINUTES", "minutes"), "shocked"),
  ("Le 19 octobre 2025, vers neuf heures et demie, un camion avec une nacelle se gare au pied du musée. Comme pour des travaux.", Y(2025, "LE LOUVRE", "2025"), "serious"),
  ("Les voleurs montent jusqu'à une fenêtre de la galerie d'Apollon, et découpent les vitrines avec des disqueuses.", S("GALERIE D'APOLLON", "les vitrines découpées"), "worried"),
  ("Ils emportent huit bijoux de la Couronne de France, ayant appartenu à des reines et des impératrices.", C(8, "BIJOUX", "DE LA COURONNE", "huit"), "shocked"),
  ("Valeur estimée : environ quatre-vingt-huit millions d'euros. Dans leur fuite, ils font même tomber la couronne de l'impératrice Eugénie.", C(88, "MILLIONS D'EUROS", "ESTIMÉS", "quatre"), "surprised"),
  ("Des suspects ont été arrêtés. Mais selon eux, le reste du butin a été remis à un commanditaire, toujours inconnu.", V("Affaire résolue ?", "EN COURS", "inconnu"), "serious"),
  CTA("CASSE DU SIÈCLE", "Tu penses qu'on retrouvera les bijoux ? Abonne-toi et laisse un like !")]),

 ("069-rennes-le-chateau", at(15, 19), "Le trésor caché du curé de Rennes-le-Château", DARK,
  ["Wikipedia, Bérenger Saunière", "Wikipedia, Affaire de Rennes-le-Château"], [
  ("Un curé d'un tout petit village est devenu riche du jour au lendemain. Et personne ne sait vraiment comment.", V("Un curé pauvre ?", "RICHE", "riche"), "curious"),
  ("En 1885, l'abbé Bérenger Saunière arrive à Rennes-le-Château, un village perché dans l'Aude.", Y(1885, "AUDE", "1885"), "serious"),
  ("Selon la légende, en restaurant son église, il découvre de mystérieux parchemins cachés dans un pilier.", S("DES PARCHEMINS", "cachés dans un pilier"), "surprised"),
  ("Peu après, il dépense des sommes énormes : une villa, une tour, des jardins. Bien plus qu'un curé de campagne.", S("LA TOUR MAGDALA", "une folie de curé"), "surprised"),
  ("Un trésor caché ? Les enquêtes de l'époque montrent surtout un trafic de messes : il en vendait beaucoup trop.", V("Un trésor ?", "DES MESSES", "messes"), "smug"),
  ("Mais la légende a explosé. Aujourd'hui encore, des chasseurs de trésor viennent creuser en cachette. Pourtant, c'est interdit.", V("Fouilles permises ?", "INTERDITES", "interdit"), "serious"),
  CTA("TON AVIS ?", "Trésor ou arnaque, à ton avis ? Abonne-toi et laisse un like !")]),

 ("070-mur-de-berlin", at(16, 19), "Le mur de Berlin est tombé à cause d'une erreur", NAVY,
  ["Wikipedia, Günter Schabowski", "Wikipedia, Chute du mur de Berlin"], [
  ("Le mur de Berlin est tombé à cause d'une petite phrase mal préparée. En direct à la télévision.", V("Un plan ?", "ERREUR", "phrase"), "surprised"),
  ("Le 9 novembre 1989, Günter Schabowski, un dirigeant de l'Allemagne de l'Est, donne une conférence de presse.", Y(1989, "BERLIN", "1989"), "serious"),
  ("On lui a passé une note sur une nouvelle règle pour voyager. Mais il ne l'a pas vraiment lue avant.", S("UNE NOTE", "qu'il n'a pas lue"), "worried"),
  ("Un journaliste demande : quand est-ce que ça commence ? Il cherche dans ses papiers, et répond : immédiatement.", Q("IMMÉDIATEMENT", "— Günter Schabowski, 1989"), "curious"),
  ("Le soir même, des milliers de Berlinois se pressent devant les postes-frontières.", C(1000, "BERLINOIS", "ET BIEN PLUS", "milliers"), "surprised"),
  ("Les gardes n'ont aucun ordre. Peu avant minuit, ils ouvrent les barrières. Le mur vient de tomber.", V("Ils tirent ?", "OUVERT", "ouvrent"), "happy", {"on": "ouvrent", "pose": "cheer", "hold": 1.0}),
  CTA("QUELLE ERREUR !", "La meilleure erreur de l'histoire ? Abonne-toi et laisse un like !")]),

 ("071-canon-paris", at(17, 19), "Le canon qui bombardait Paris à 120 km", NAVY,
  ["Wikipedia, Paris Gun (Pariser Kanonen)", "Wikipedia, Bombardement de Paris (1918)"], [
  ("En 1918, des obus tombent sur Paris. Mais l'ennemi est à plus de cent kilomètres.", V("Un avion ?", "UN CANON", "kilomètres"), "shocked"),
  ("Le 23 mars 1918, des explosions secouent la ville. Il n'y a aucun avion dans le ciel. Personne ne comprend.", Y(1918, "PARIS", "1918"), "worried"),
  ("En fait, l'Allemagne a construit un canon géant : le canon de Paris. Son tube mesure plus de trente mètres.", C(30, "MÈTRES", "DE CANON", "trente"), "surprised"),
  ("Il tire à environ cent vingt kilomètres. Ses obus montent jusqu'à quarante kilomètres d'altitude.", C(120, "KILOMÈTRES", "DE PORTÉE", "cent"), "shocked"),
  ("Ils font environ trois minutes de vol avant de retomber sur Paris.", S("3 MINUTES", "de vol pour chaque obus"), "curious"),
  ("À la fin de la guerre, les Allemands détruisent le canon. On n'en a jamais retrouvé un seul exemplaire.", V("Retrouvé ?", "JAMAIS", "jamais"), "serious"),
  CTA("INCROYABLE ?", "Tu connaissais ce canon ? Abonne-toi et laisse un like !")]),

 ("072-tour-eiffel-sauvee", at(18, 19), "La tour Eiffel devait être démolie", RED,
  ["Wikipedia, Tour Eiffel", "Site officiel de la tour Eiffel, histoire"], [
  ("La tour Eiffel devait être démolie après vingt ans. Elle a été sauvée par une antenne.", V("Pour toujours ?", "20 ANS", "vingt"), "surprised"),
  ("Elle est construite pour l'Exposition universelle de 1889. Et beaucoup de Parisiens la détestent.", Y(1889, "PARIS", "1889"), "curious"),
  ("Des artistes signent une lettre contre cette tour inutile et monstrueuse.", Q("INUTILE ET MONSTRUEUSE", "— lettre des artistes, 1887"), "angry"),
  ("Et l'autorisation n'est que de vingt ans. En 1909, elle doit être démontée.", S("1909", "date prévue de démolition"), "worried"),
  ("Mais Gustave Eiffel a une idée : en faire un laboratoire. Et surtout, une antenne de radio militaire.", S("UNE ANTENNE", "pour l'armée"), "smug"),
  ("Pendant la Première Guerre mondiale, elle intercepte même des messages ennemis. Plus personne n'ose la démolir.", V("Démolie ?", "SAUVÉE", "démolir"), "happy", {"on": "démolir", "pose": "cheer", "hold": 1.0}),
  CTA("TEAM TOUR EIFFEL", "Heureusement qu'elle est restée ! Abonne-toi et laisse un like !")]),

 ("073-liberte-francaise", at(19, 19), "La statue de la Liberté est française", RED,
  ["Wikipedia, Statue de la Liberté", "National Park Service, Statue of Liberty history"], [
  ("La statue de la Liberté, symbole de l'Amérique, a été construite à Paris. En pleine rue.", V("Américaine ?", "FRANÇAISE", "paris"), "smug"),
  ("Elle est imaginée par le sculpteur français Bartholdi, comme un cadeau de la France aux États-Unis.", S("BARTHOLDI", "un cadeau de la France"), "happy"),
  ("Et à l'intérieur, la structure en fer est conçue par… Gustave Eiffel.", S("GUSTAVE EIFFEL", "le squelette en fer"), "surprised"),
  ("Elle est d'abord assemblée à Paris. Pendant un moment, elle domine les toits du dix-septième arrondissement.", S("À PARIS", "dans le 17e arrondissement"), "curious"),
  ("Puis on la démonte, et on l'envoie en bateau dans plus de deux cents caisses.", C(200, "CAISSES", "EN BATEAU", "deux"), "surprised"),
  ("Et elle n'était pas verte. Elle était couleur cuivre, et c'est l'oxydation qui l'a rendue verte.", V("Verte ?", "CUIVRÉE", "verte"), "smug"),
  CTA("TU SAVAIS ?", "Tu le savais ? Abonne-toi et laisse un like !")]),

 ("074-vasa", at(20, 16), "Le navire qui a coulé au bout de 1 300 mètres", NAVY,
  ["Vasamuseet, The ship", "Wikipedia, Vasa (navire)"], [
  ("Le navire de guerre le plus puissant de son époque a coulé… au bout de mille trois cents mètres.", V("Puissant ?", "COULÉ", "coulé"), "shocked"),
  ("On est en 1628, à Stockholm. Le Vasa, fierté du roi de Suède, part pour son premier voyage.", Y(1628, "STOCKHOLM", "1628"), "happy"),
  ("Il est magnifique : des centaines de sculptures, et soixante-quatre canons.", C(64, "CANONS", "À BORD", "soixante"), "surprised"),
  ("Mais il est trop haut, et pas assez lesté. Au premier coup de vent, il penche.", V("Stable ?", "TROP HAUT", "penche"), "worried"),
  ("L'eau entre par les sabords des canons. Et devant la foule, le Vasa coule dans le port.", S("DEVANT LA FOULE", "dans le port de Stockholm"), "sad"),
  ("En 1961, on le remonte presque intact. Aujourd'hui, il est exposé dans son propre musée.", S("REMONTÉ", "en 1961, presque intact"), "happy"),
  CTA("QUEL FLOP !", "Le pire premier voyage de l'histoire ? Abonne-toi et laisse un like !")]),

 ("075-alcatraz", at(20, 19), "L'évasion d'Alcatraz : sont-ils vivants ?", DARK,
  ["FBI, Alcatraz Escape", "Wikipedia, June 1962 Alcatraz escape attempt"], [
  ("En 1962, trois hommes se sont évadés d'Alcatraz, la prison dont on ne s'évade pas. On ne les a jamais retrouvés.", V("Impossible ?", "ÉVADÉS", "évadés"), "shocked"),
  ("Frank Morris et les frères Anglin creusent les murs de leur cellule pendant des mois, avec des cuillères.", S("DES CUILLÈRES", "des mois à creuser"), "curious"),
  ("Pour tromper les gardiens, ils fabriquent de fausses têtes en papier mâché, avec de vrais cheveux.", S("FAUSSES TÊTES", "en papier mâché"), "smug"),
  ("Le 11 juin 1962, la nuit, ils montent sur le toit et partent sur un radeau fait de cirés.", Y(1962, "ALCATRAZ", "1962"), "worried"),
  ("Le FBI conclut qu'ils se sont sûrement noyés. Mais on n'a jamais retrouvé leurs corps.", V("Noyés ?", "INTROUVÉS", "corps"), "serious"),
  ("Et des années plus tard, des proches ont affirmé avoir reçu des nouvelles. Le mystère reste ouvert.", V("Fin de l'histoire ?", "MYSTÈRE", "mystère"), "curious"),
  CTA("VIVANTS ?", "Pour toi, ils ont survécu ? Abonne-toi et laisse un like !")]),

 ("076-spaggiari", at(21, 16), "Le casse du siècle par les égouts de Nice", DET,
  ["Wikipedia, Albert Spaggiari", "Wikipedia, Casse de la Société générale de Nice"], [
  ("En 1976, des voleurs ont creusé un tunnel depuis les égouts jusqu'au coffre d'une banque, à Nice.", V("Par la porte ?", "ÉGOUTS", "égouts"), "smug"),
  ("Pendant des semaines, ils creusent huit mètres de tunnel, sous la Société générale.", C(8, "MÈTRES", "DE TUNNEL", "huit"), "curious"),
  ("Un week-end de juillet, ils entrent dans la salle des coffres. Et ils prennent tout leur temps.", Y(1976, "NICE", "juillet"), "serious"),
  ("Ils ouvrent des centaines de coffres, pique-niquent sur place, et repartent avec des millions.", S("UN PIQUE-NIQUE", "dans la salle des coffres"), "happy"),
  ("Sur le mur, ils laissent un message : sans armes, ni haine, ni violence.", Q("SANS ARMES NI HAINE", "— message sur le mur"), "smug"),
  ("Le cerveau présumé, Albert Spaggiari, est arrêté. Mais pendant son interrogatoire, il saute par une fenêtre et s'enfuit. On ne l'a jamais repris.", V("Repris ?", "JAMAIS", "jamais"), "surprised", {"on": "saute", "pose": "recoil", "mood": "shocked", "hold": 1.0}),
  CTA("LE CASSE DU SIÈCLE", "Tu connaissais ce casse ? Abonne-toi et laisse un like !")]),

 ("077-mata-hari", at(21, 19), "Mata Hari : espionne ou bouc émissaire ?", DARK,
  ["Wikipedia, Mata Hari", "Archives nationales, procès de Mata Hari (1917)"], [
  ("La plus célèbre espionne de l'histoire était peut-être une très mauvaise espionne.", V("Une super espionne ?", "PAS SÛR", "mauvaise"), "curious"),
  ("Elle s'appelle Margaretha Zelle, elle est néerlandaise. Mais à Paris, elle devient Mata Hari, une danseuse célèbre.", S("MATA HARI", "danseuse à Paris"), "happy"),
  ("Pendant la Première Guerre mondiale, elle voyage, rencontre des officiers de tous les camps.", S("TOUS LES CAMPS", "pendant la guerre"), "serious"),
  ("En 1917, la France l'arrête. On l'accuse d'avoir livré des secrets à l'Allemagne.", Y(1917, "PARIS", "1917"), "worried"),
  ("Après un procès très rapide, elle est condamnée et fusillée à Vincennes.", V("Coupable ?", "FUSILLÉE", "fusillée"), "sad"),
  ("Mais beaucoup d'historiens pensent que les preuves étaient faibles. En pleine année noire, la France cherchait un coupable.", S("UN COUPABLE IDÉAL", "selon des historiens"), "serious"),
  CTA("TON AVIS ?", "Coupable ou pas, à ton avis ? Abonne-toi et laisse un like !")]),

 ("078-champollion", at(22, 16), "Je tiens l'affaire : Champollion et les hiéroglyphes", GREEN,
  ["Wikipedia, Jean-François Champollion", "British Museum, The Rosetta Stone"], [
  ("Un Français a crié je tiens l'affaire, puis il s'est évanoui. Il venait de déchiffrer les hiéroglyphes.", V("Un exploit ?", "ÉVANOUI", "évanoui"), "surprised", {"on": "évanoui", "pose": "recoil", "mood": "shocked", "hold": 1.0}),
  ("Pendant des siècles, plus personne ne sait lire l'écriture des pharaons.", S("HIÉROGLYPHES", "illisibles depuis des siècles"), "curious"),
  ("En 1799, des soldats de Napoléon trouvent en Égypte une pierre avec trois écritures. La pierre de Rosette.", Y(1799, "ROSETTE", "1799"), "serious"),
  ("Le même texte en grec, en démotique, et en hiéroglyphes. Une vraie clé.", C(3, "ÉCRITURES", "UN SEUL TEXTE", "même"), "happy"),
  ("Jean-François Champollion y travaille pendant des années. Il comprend que les signes notent aussi des sons.", S("DES SONS", "pas seulement des images"), "curious"),
  ("En 1822, il court voir son frère, crie je tiens l'affaire, et tombe évanoui. Il a réussi.", Q("JE TIENS L'AFFAIRE !", "— Champollion, 1822"), "happy"),
  CTA("GÉNIE !", "Respect, Champollion. Abonne-toi et laisse un like !")]),

 ("079-voynich", at(22, 19), "Le livre que personne n'arrive à lire", DET,
  ["Wikipedia, Manuscrit de Voynich", "Université Yale, Beinecke Library MS 408"], [
  ("Il existe un livre de plus de deux cents pages que personne au monde n'arrive à lire.", V("Personne ?", "PERSONNE", "personne"), "curious"),
  ("C'est le manuscrit de Voynich. Le parchemin date du début du quinzième siècle.", S("MANUSCRIT DE VOYNICH", "XVe siècle"), "serious"),
  ("Il est écrit dans un alphabet inconnu, qui n'existe nulle part ailleurs.", S("ALPHABET INCONNU", "nulle part ailleurs"), "surprised"),
  ("Et il est rempli de dessins étranges : des plantes qui n'existent pas, des étoiles, des femmes dans des bassins.", S("PLANTES INCONNUES", "et des dessins étranges"), "curious"),
  ("Des cryptographes de l'armée, des linguistes, et même des intelligences artificielles ont essayé. Sans succès.", V("Déchiffré ?", "ÉCHEC", "succès"), "smug"),
  ("Langue perdue, code secret, ou canular génial ? Il est aujourd'hui conservé à l'université Yale, et il résiste toujours.", S("UNIVERSITÉ YALE", "il résiste toujours"), "serious"),
  CTA("TA THÉORIE ?", "Code, langue ou canular ? Abonne-toi et laisse un like !")]),

 ("080-loch-ness", at(23, 16), "La photo du monstre du Loch Ness était un jouet", DET,
  ["Wikipedia, Surgeon's photograph", "Wikipedia, Monstre du Loch Ness"], [
  ("La photo la plus célèbre du monstre du Loch Ness était un jouet de trente centimètres.", V("Le monstre ?", "UN JOUET", "jouet"), "smug"),
  ("En 1934, un chirurgien londonien publie une photo : un long cou qui sort de l'eau, en Écosse.", Y(1934, "LOCH NESS", "1934"), "surprised"),
  ("Un chirurgien, c'est sérieux. Pendant soixante ans, la photo fait le tour du monde.", C(60, "ANS", "DE MYSTÈRE", "soixante"), "curious"),
  ("Mais en 1994, on révèle les aveux d'un complice : c'était un faux.", V("Authentique ?", "UN FAUX", "faux"), "shocked"),
  ("Le monstre était un petit sous-marin jouet, avec une tête et un cou en bois.", S("UN SOUS-MARIN JOUET", "et un cou en bois"), "smug"),
  ("Et pourtant, chaque année, des gens fouillent encore le lac. Une étude d'ADN en 2018 n'y a trouvé que… beaucoup d'anguilles.", S("DES ANGUILLES", "étude ADN, 2018"), "happy"),
  CTA("TU Y CROIS ?", "Nessie, tu y crois encore ? Abonne-toi et laisse un like !")]),

 ("081-bermudes", at(23, 19), "Le triangle des Bermudes est-il vraiment maudit ?", NAVY,
  ["NOAA Ocean Service, What is the Bermuda Triangle?", "Wikipedia, Triangle des Bermudes"], [
  ("Le triangle des Bermudes ferait disparaître des avions et des bateaux. Mais il y a un problème.", V("Maudit ?", "PROBLÈME", "problème"), "curious"),
  ("C'est une zone de l'Atlantique, entre la Floride, Porto Rico et les Bermudes.", S("ATLANTIQUE", "Floride, Porto Rico, Bermudes"), "serious"),
  ("En 1945, cinq avions de l'armée américaine disparaissent pendant un entraînement. Le Vol 19.", Y(1945, "VOL 19", "1945"), "worried"),
  ("Dans les années 1970, des livres en font une zone maudite : extraterrestres, Atlantide, champs magnétiques.", S("LA LÉGENDE", "née dans les années 1970"), "surprised"),
  ("Sauf que c'est une des zones les plus fréquentées du monde. Et les disparitions n'y sont pas plus nombreuses qu'ailleurs.", V("Plus d'accidents ?", "NON", "nombreuses"), "smug"),
  ("Les assurances maritimes ne font même pas payer plus cher pour la traverser.", S("MÊME PRIX", "pour les assurances"), "smug"),
  CTA("DÉÇU ?", "Déçu ou rassuré ? Abonne-toi et laisse un like !")]),

 ("082-nazca", at(24, 16), "Les dessins géants du désert de Nazca", GREEN,
  ["Wikipedia, Lignes de Nazca", "UNESCO, Lines and Geoglyphs of Nasca"], [
  ("Dans un désert du Pérou, il y a des dessins si grands qu'on ne peut les voir que du ciel.", V("Du sol ?", "DU CIEL", "ciel"), "surprised"),
  ("Ce sont les lignes de Nazca. Un singe, une araignée, un colibri. Certains font des centaines de mètres.", S("LIGNES DE NAZCA", "un singe, une araignée, un colibri"), "curious"),
  ("Ils ont été tracés il y a environ deux mille ans, par le peuple Nazca.", C(2000, "ANS", "ENVIRON", "deux"), "serious"),
  ("Comment ? En retirant les cailloux sombres, pour laisser apparaître le sol plus clair en dessous.", S("DES CAILLOUX", "retirés un par un"), "curious"),
  ("Et grâce au désert, l'un des plus secs du monde, ils sont restés presque intacts.", V("Effacés ?", "INTACTS", "intacts"), "happy"),
  ("Pourquoi ? Rituels pour l'eau, chemins sacrés… Et en 2024, grâce à l'IA, on en a découvert plus de trois cents nouveaux.", C(300, "NOUVEAUX DESSINS", "DÉCOUVERTS EN 2024", "trois"), "surprised"),
  CTA("FASCINANT ?", "Tu aimerais les voir d'avion ? Abonne-toi et laisse un like !")]),

 ("083-moai", at(24, 19), "Les statues de l'île de Pâques auraient marché", GREEN,
  ["Hunt et Lipo, Journal of Archaeological Science, 2013", "Wikipedia, Moaï"], [
  ("Selon la légende, les statues géantes de l'île de Pâques ont marché. Et c'est peut-être vrai.", V("Une légende ?", "PEUT-ÊTRE", "marché"), "smug"),
  ("Il y a près de mille moaï sur l'île. Certains pèsent des dizaines de tonnes.", C(1000, "MOAÏ", "SUR L'ÎLE", "mille"), "surprised"),
  ("Mais il n'y a ni roues, ni gros animaux. Alors, comment les déplacer sur des kilomètres ?", S("SANS ROUES", "ni animaux de trait"), "curious"),
  ("Les habitants disaient qu'elles marchaient toutes seules jusqu'à leur place.", Q("ELLES ONT MARCHÉ", "— tradition de l'île"), "serious"),
  ("En 2012, des chercheurs testent une idée : avec des cordes, une équipe fait basculer une réplique à gauche, puis à droite.", S("DES CORDES", "à gauche, puis à droite"), "curious"),
  ("Et la statue avance, comme si elle marchait. Une vingtaine de personnes suffit.", V("Ça marche ?", "OUI !", "avance"), "happy", {"on": "avance", "pose": "cheer", "hold": 1.0}),
  CTA("INCROYABLE !", "Des statues qui marchent ! Abonne-toi et laisse un like !")]),

 ("084-stonehenge", at(25, 16), "La pierre de Stonehenge venue d'Écosse", GREEN,
  ["Clarke et al., Nature, 2024", "English Heritage, Stonehenge"], [
  ("Une des pierres de Stonehenge vient d'Écosse. À plus de sept cents kilomètres.", V("Du coin ?", "D'ÉCOSSE", "vient"), "surprised"),
  ("Stonehenge, en Angleterre, a été construit il y a environ cinq mille ans.", C(5000, "ANS", "ENVIRON", "cinq"), "serious"),
  ("On savait déjà que certaines pierres venaient du pays de Galles, à plus de deux cents kilomètres.", S("PAYS DE GALLES", "à plus de 200 km"), "curious"),
  ("Mais en 2024, des chercheurs analysent la Pierre de l'autel, au centre. Elle pèse environ six tonnes.", S("LA PIERRE DE L'AUTEL", "environ 6 tonnes"), "curious"),
  ("Résultat : elle vient du nord-est de l'Écosse. Environ sept cent cinquante kilomètres de voyage.", C(750, "KILOMÈTRES", "DE VOYAGE", "sept"), "shocked"),
  ("Sans roues, sans chevaux. Par la terre, ou par la mer ? Personne ne sait encore comment.", V("Expliqué ?", "MYSTÈRE", "comment"), "serious"),
  CTA("TA THÉORIE ?", "Toi, tu ferais comment ? Abonne-toi et laisse un like !")]),

 ("085-violet-jessop", at(25, 19), "La femme qui a survécu à trois naufrages", NAVY,
  ["Wikipedia, Violet Jessop", "Encyclopedia Titanica, Violet Jessop"], [
  ("Une femme était à bord du Titanic. Et ce n'était même pas son pire voyage.", V("Le pire ?", "PAS LE PIRE", "pire"), "surprised"),
  ("Elle s'appelle Violet Jessop. Elle est hôtesse sur les grands paquebots.", S("VIOLET JESSOP", "hôtesse sur les paquebots"), "happy"),
  ("En 1911, elle est à bord de l'Olympic, quand il percute un navire de guerre. Elle s'en sort.", Y(1911, "OLYMPIC", "1911"), "worried"),
  ("En 1912, elle est sur le Titanic. Elle monte dans un canot de sauvetage. Et elle survit.", S("TITANIC", "1912, canot numéro 16"), "sad"),
  ("En 1916, pendant la guerre, elle est infirmière sur le Britannic. Il heurte une mine et coule. Elle survit encore.", C(3, "NAUFRAGES", "ET TOUJOURS VIVANTE", "survit"), "shocked"),
  ("On l'a surnommée Miss Insubmersible. Elle a continué à naviguer pendant des années.", V("Elle arrête ?", "JAMAIS", "continué"), "happy"),
  CTA("QUELLE CHANCE !", "Chanceuse ou malchanceuse ? Abonne-toi et laisse un like !")]),

 ("086-wojtek", at(26, 16), "L'ours qui est devenu soldat", GREEN,
  ["Wikipedia, Wojtek (ours)", "BBC, Wojtek the bear"], [
  ("Pendant la Seconde Guerre mondiale, un ours brun a été soldat dans l'armée polonaise.", V("Un ours ?", "SOLDAT", "soldat"), "surprised"),
  ("En 1942, des soldats polonais adoptent un petit ourson orphelin en Iran. Ils l'appellent Wojtek.", Y(1942, "IRAN", "1942"), "happy"),
  ("Il grandit avec eux. Il boit dans un biberon, lutte pour jouer, et adore les cigarettes. Il les mange.", S("WOJTEK", "l'ours de la compagnie"), "happy"),
  ("Pour qu'il puisse monter dans les bateaux, l'armée l'inscrit officiellement comme soldat. Avec un grade.", V("Officiel ?", "ENRÔLÉ", "officiellement"), "smug"),
  ("Selon ses camarades, pendant la bataille du Mont-Cassin, il aidait à porter des caisses d'obus.", S("MONT-CASSIN", "il porte des caisses d'obus"), "surprised"),
  ("Après la guerre, il finit ses jours au zoo d'Édimbourg. Et il a aujourd'hui des statues en Pologne et en Écosse.", S("UN HÉROS", "statues en Pologne et en Écosse"), "happy"),
  CTA("TEAM WOJTEK", "Le meilleur soldat de l'histoire ? Abonne-toi et laisse un like !")]),

 ("087-mammouths", at(26, 19), "Des mammouths vivaient encore à l'époque des pyramides", WHITE,
  ["Wikipedia, Île Wrangel (mammouths)", "Dehasque et al., Cell, 2024"], [
  ("Quand les Égyptiens construisaient les pyramides, il y avait encore des mammouths vivants.", V("Disparus avant ?", "VIVANTS", "vivants"), "shocked"),
  ("La plupart des mammouths ont disparu il y a environ dix mille ans.", C(10000, "ANS", "LA PLUPART DISPARUS", "dix"), "serious"),
  ("Mais un petit groupe a survécu sur une île isolée, au nord de la Sibérie : l'île Wrangel.", S("ÎLE WRANGEL", "au nord de la Sibérie"), "curious"),
  ("Ils y ont vécu jusqu'à il y a environ quatre mille ans.", C(4000, "ANS", "LES DERNIERS", "quatre"), "surprised"),
  ("La grande pyramide de Gizeh, elle, a environ quatre mille cinq cents ans. Les deux ont existé en même temps.", V("En même temps ?", "OUI", "temps"), "smug"),
  ("Pourquoi ont-ils fini par disparaître ? Peut-être un événement brutal. Les scientifiques cherchent encore.", S("UN MYSTÈRE", "la fin des derniers mammouths"), "sad"),
  CTA("FOU, NON ?", "Ça te paraît fou ? Abonne-toi et laisse un like !")]),

 ("088-cleopatre", at(27, 16), "Cléopâtre est plus proche de nous que des pyramides", RED,
  ["Wikipedia, Cléopâtre VII", "Wikipedia, Pyramide de Khéops"], [
  ("Cléopâtre a vécu plus près de nous… que de la construction des pyramides.", V("Impossible ?", "VRAI", "pyramides"), "smug"),
  ("La grande pyramide de Khéops est construite vers 2560 avant Jésus-Christ.", S("KHÉOPS", "vers 2560 av. J.-C."), "serious"),
  ("Cléopâtre, elle, meurt en l'an 30 avant Jésus-Christ. Environ deux mille cinq cents ans plus tard.", C(2500, "ANS", "APRÈS LES PYRAMIDES", "deux"), "surprised"),
  ("Et les premiers pas sur la Lune, en 1969 ? Environ deux mille ans après Cléopâtre.", C(2000, "ANS", "AVANT LA LUNE", "deux"), "curious"),
  ("Donc oui : Cléopâtre est plus proche des astronautes que des bâtisseurs de pyramides.", V("Plus proche ?", "DE LA LUNE", "astronautes"), "shocked"),
  ("Pour elle, les pyramides étaient déjà des monuments très, très anciens.", S("DÉJÀ ANCIENNES", "pour Cléopâtre"), "happy"),
  CTA("ÇA RETOURNE ?", "Ça te retourne le cerveau ? Abonne-toi et laisse un like !")]),

 ("089-napoleon-taille", at(27, 19), "Napoléon n'était pas petit", NAVY,
  ["Wikipedia, Napoléon Ier (taille)", "Fondation Napoléon, La taille de Napoléon"], [
  ("Napoléon n'était pas petit. C'est une erreur de mesure… et un peu de propagande.", V("Petit ?", "FAUX", "petit"), "smug"),
  ("À sa mort, on le mesure : cinq pieds, deux pouces. Ça a l'air minuscule.", S("5 PIEDS 2 POUCES", "à sa mort, en 1821"), "surprised"),
  ("Mais ce sont des pieds français, plus grands que les pieds anglais. En réalité, il mesure environ un mètre soixante-neuf.", C(169, "CENTIMÈTRES", "ENVIRON", "soixante"), "curious"),
  ("C'est même un peu plus que la moyenne des Français de l'époque.", V("Petit ?", "MOYEN", "moyenne"), "happy"),
  ("Mais les caricaturistes anglais le dessinent tout petit et colérique. Une image qui reste.", S("CARICATURES", "made in England"), "angry"),
  ("Et on l'appelle le petit caporal. Un surnom affectueux de ses soldats, pas une question de taille.", Q("LE PETIT CAPORAL", "— surnom donné par ses soldats"), "smug"),
  CTA("TU SAVAIS ?", "Tu le croyais petit ? Abonne-toi et laisse un like !")]),

 ("090-grande-puanteur", at(28, 16), "L'été où Londres a pué si fort que le Parlement a fui", DET,
  ["Wikipedia, Great Stink", "Wikipedia, Joseph Bazalgette"], [
  ("En 1858, Londres a tellement pué que le Parlement a failli déménager.", V("Une odeur ?", "INFECTE", "pué"), "shocked"),
  ("À l'époque, les égouts de la ville se jettent directement dans la Tamise.", S("LA TAMISE", "le grand égout de Londres"), "worried"),
  ("Et cet été-là, il fait très chaud. Le fleuve se met à fermenter.", Y(1858, "LONDRES", "été"), "worried"),
  ("Au Parlement, au bord de l'eau, on accroche des rideaux trempés dans de la chaux pour couvrir l'odeur.", S("RIDEAUX À LA CHAUX", "contre l'odeur"), "surprised"),
  ("Les députés n'en peuvent plus. En quelques semaines, ils votent un énorme projet d'égouts.", V("Ils agissent ?", "VITE", "semaines"), "smug"),
  ("L'ingénieur Joseph Bazalgette construit des centaines de kilomètres de tunnels. Une partie est encore utilisée aujourd'hui.", S("BAZALGETTE", "des égouts toujours utilisés"), "happy"),
  CTA("BEURK !", "Tu aurais tenu combien de temps ? Abonne-toi et laisse un like !")]),

 ("091-zouave", at(28, 19), "Le zouave qui mesure les crues de Paris", RED,
  ["Wikipedia, Zouave du pont de l'Alma", "Wikipedia, Crue de la Seine de 1910"], [
  ("À Paris, une statue de soldat sert à mesurer les inondations. Et en 1910, l'eau lui arrive aux épaules.", V("Une décoration ?", "MESURE", "mesurer"), "curious"),
  ("C'est le zouave du pont de l'Alma, une statue d'un soldat de l'armée française.", S("LE ZOUAVE", "pont de l'Alma"), "serious"),
  ("Les Parisiens regardent jusqu'où monte l'eau sur lui pour savoir si la Seine déborde.", S("LES PIEDS ?", "la Seine monte"), "worried"),
  ("En janvier 1910, c'est la grande crue. Le métro est inondé, des rues deviennent des canaux.", Y(1910, "PARIS", "1910"), "shocked"),
  ("L'eau monte jusqu'aux épaules du zouave. Plus de huit mètres au-dessus de la normale.", C(8, "MÈTRES", "AU-DESSUS DE LA NORMALE", "huit"), "shocked"),
  ("Aujourd'hui, les experts disent qu'une crue comme celle-là reviendra un jour. La question, c'est quand.", V("Plus jamais ?", "UN JOUR", "reviendra"), "serious"),
  CTA("TU CONNAISSAIS ?", "Tu connaissais le zouave ? Abonne-toi et laisse un like !")]),

 ("092-pompei-graffitis", at(29, 16), "Les graffitis de Pompéi", RED,
  ["Wikipedia, Pompéi (graffitis)", "Parc archéologique de Pompéi"], [
  ("À Pompéi, les murs sont couverts de graffitis. Et certains ressemblent à des messages d'aujourd'hui.", V("Des Romains sérieux ?", "GRAFFITIS", "graffitis"), "smug"),
  ("En l'an 79, le Vésuve ensevelit la ville. Et les cendres conservent tout, même les murs.", Y(79, "POMPÉI", "79"), "serious"),
  ("On y trouve des pubs électorales : votez pour untel, c'est un homme honnête.", Q("VOTEZ POUR LUI", "— affiche électorale, Pompéi"), "happy"),
  ("Des déclarations d'amour, des insultes entre voisins, et des avis sur les tavernes.", S("DES AVIS", "sur les tavernes"), "happy"),
  ("Et un passant a même écrit : je m'étonne, ô mur, que tu ne te sois pas effondré sous tant de bêtises.", Q("Ô MUR…", "— graffiti de Pompéi"), "smug"),
  ("Deux mille ans plus tard, on écrit toujours sur les murs. Les humains n'ont pas tant changé.", V("Si différents ?", "PAREILS", "changé"), "happy"),
  CTA("TU ÉCRIRAIS QUOI ?", "Toi, tu écrirais quoi sur un mur ? Abonne-toi et laisse un like !")]),

 ("093-premier-selfie", at(29, 19), "Le premier selfie de l'histoire date de 1839", WHITE,
  ["Library of Congress, Robert Cornelius self-portrait", "Wikipedia, Robert Cornelius"], [
  ("Le premier selfie de l'histoire a été pris en 1839. Et il a fallu ne pas bouger pendant plusieurs minutes.", V("Avec un téléphone ?", "EN 1839", "1839"), "smug"),
  ("Robert Cornelius est un jeune Américain passionné par une nouvelle invention : la photographie.", S("ROBERT CORNELIUS", "Philadelphie"), "curious"),
  ("Il installe son appareil devant le magasin de sa famille, retire le cache de l'objectif, et court se placer devant.", S("IL COURT", "se placer devant l'objectif"), "happy"),
  ("Il reste immobile pendant de longues minutes. Puis il remet le cache.", C(3, "MINUTES", "OU PLUS, IMMOBILE", "minutes"), "serious"),
  ("Résultat : un portrait un peu flou, les cheveux en bataille, les bras croisés.", S("CHEVEUX EN BATAILLE", "un peu flou"), "happy"),
  ("Au dos, il écrit : la première photo de lumière jamais prise. C'est l'un des plus vieux portraits photographiques connus.", Q("LA PREMIÈRE PHOTO", "— Robert Cornelius, 1839"), "surprised"),
  CTA("PRENDS UN SELFIE", "Ton prochain selfie, pense à lui. Abonne-toi et laisse un like !")]),

 ("094-atlantide", at(30, 16), "L'Atlantide : la vraie origine du mythe", DET,
  ["Platon, Timée et Critias", "Wikipedia, Atlantide"], [
  ("Tout ce qu'on sait sur l'Atlantide vient d'un seul homme. Et ce n'était pas un explorateur.", V("Une vraie cité ?", "UN SEUL", "homme"), "curious"),
  ("C'est le philosophe grec Platon, il y a environ deux mille quatre cents ans.", C(2400, "ANS", "ENVIRON", "deux"), "serious"),
  ("Dans deux de ses livres, il décrit une île puissante, au-delà des colonnes d'Hercule.", S("AU-DELÀ D'HERCULE", "une île immense"), "curious"),
  ("Un peuple riche et orgueilleux, qui veut conquérir le monde. Jusqu'à ce que, en un jour et une nuit, l'île soit engloutie.", Q("UN JOUR ET UNE NUIT", "— Platon"), "worried"),
  ("Aucune autre source ancienne n'en parle avant lui. Pour la plupart des historiens, c'est une fable pour faire réfléchir.", V("Réelle ?", "UNE FABLE", "fable"), "smug"),
  ("Mais certains y voient le souvenir d'une vraie catastrophe : l'éruption de Santorin, il y a plus de trois mille ans.", S("SANTORIN", "une éruption géante"), "surprised"),
  CTA("TU Y CROIS ?", "L'Atlantide, mythe ou souvenir ? Abonne-toi et laisse un like !")]),

 ("095-hiver-1709", at(30, 19), "L'hiver où le vin gelait sur la table du roi", WHITE,
  ["Wikipedia, Grand Hiver de 1709", "Marcel Lachiver, Les Années de misère"], [
  ("En 1709, il faisait si froid à Versailles que le vin gelait sur la table du roi.", V("À Versailles ?", "GELÉ", "gelait"), "shocked"),
  ("Dans la nuit du 5 au 6 janvier, les températures s'effondrent dans toute l'Europe.", Y(1709, "VERSAILLES", "janvier"), "worried"),
  ("À Paris, on mesure moins quinze degrés, et parfois bien moins encore. Pendant des semaines.", C(15, "DEGRÉS", "SOUS ZÉRO", "quinze"), "worried"),
  ("Les rivières gèlent, les arbres éclatent sous le froid, et la mer gèle même près des côtes.", S("LES ARBRES ÉCLATENT", "et la mer gèle"), "shocked"),
  ("Et le pire vient après : les récoltes sont détruites. Le pain manque, et c'est la famine.", V("Fini au printemps ?", "LA FAMINE", "famine"), "sad"),
  ("On l'a appelé le Grand Hiver. C'est l'un des plus terribles de l'histoire de France.", S("LE GRAND HIVER", "1709"), "serious"),
  CTA("TU AS FROID ?", "Ça donne froid, non ? Abonne-toi et laisse un like !")]),
]
