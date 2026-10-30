# Série de Noël, décembre 2026 : un Short par jour, voix Guillaume.
# Chaque segment : (tts, scène, humeur du hibou[, act])
def V(claim, stamp, on): return {"type": "verdict", "claim": claim, "stamp": stamp, "stamp_on": on}
def S(big, line): return {"type": "scroll", "big": big, "line": line}
def Y(year, place, on): return {"type": "year", "year": year, "from": 2026, "place": place, "land_on": on}
def C(value, unit, label, on): return {"type": "counter", "value": value, "unit": unit, "label": label, "from": 0, "slam_on": on}
def Q(title, sign): return {"type": "quote", "title": title, "sign": sign}
def CTA(big, tts): return (tts, {"type": "cta", "big": big, "sub_on": "Abonne", "like_on": "laisse"}, None)

GIFT, CANE, LANT = "gift", "candy_cane", "lantern"

SHORTS = [
 ("024-saturnales", 1, "🎄 Avant Noël, les esclaves donnaient les ordres", GIFT,
  ["Wikipedia, Saturnalia", "Catulle, poème 14", "Wikipedia, Christmas (Chronographe de 354)"], [
  ("Avant Noël, à Rome, il y avait une fête où les esclaves donnaient des ordres à leurs maîtres.", V("Les maîtres commandent ?", "INVERSÉ", "maîtres"), "smug"),
  ("Ce sont les Saturnales, en l'honneur du dieu Saturne. Fin décembre, pendant plusieurs jours.", S("SATURNALES", "fin décembre, à Rome"), "curious"),
  ("Les écoles ferment, on fait la fête dans les rues, on joue aux dés, et on s'offre des petits cadeaux.", S("DES CADEAUX", "et la fête dans les rues"), "happy"),
  ("Et les maîtres servent le repas à leurs esclaves. Le monde est à l'envers.", V("Qui sert le repas ?", "LES MAÎTRES", "envers"), "surprised"),
  ("Le poète Catulle disait même que c'était le meilleur des jours.", Q("LE MEILLEUR DES JOURS", "— Catulle"), "serious"),
  ("Au quatrième siècle, à Rome, on fête Noël le 25 décembre. Juste après les Saturnales. Simple hasard ? Les historiens en débattent encore.", Y(336, "ROME", "quatrième"), "curious"),
  CTA("ROME EN FÊTE", "Et toi, tu aurais aimé fêter les Saturnales ? Abonne-toi et laisse un like !")]),

 ("025-selestat", 2, "🎄 Le premier sapin de Noël est… français", GIFT,
  ["Ville de Sélestat, exposition 1521 aux origines du sapin de Noël", "Paris.fr, Petites et grandes histoires du sapin de Noël"], [
  ("La plus vieille trace écrite d'un sapin de Noël n'est pas en Allemagne. Elle est en France.", V("En Allemagne ?", "EN FRANCE", "france"), "smug"),
  ("On est en 1521, à Sélestat, en Alsace.", Y(1521, "SÉLESTAT", "1521"), "curious"),
  ("Dans un livre de comptes de la ville, une ligne toute simple : quatre schillings pour faire surveiller les sapins, à partir du 21 décembre.", S("4 SCHILLINGS", "pour garder les sapins"), "serious"),
  ("Pourquoi les surveiller ? Parce que les habitants venaient en couper en douce, pour décorer leur maison.", V("Coupés en douce ?", "VOLÉS", "douce"), "surprised"),
  ("Selon la tradition, on les décorait avec des pommes rouges, des hosties et des petits gâteaux.", S("DES POMMES ROUGES", "et des petits gâteaux"), "happy"),
  ("Et une légende raconte qu'en 1858, faute de pommes, des souffleurs de verre de Lorraine les ont remplacées par des boules en verre.", S("BOULES EN VERRE", "Lorraine, 1858 (légende)"), "curious"),
  CTA("TEAM SAPIN ?", "Ton sapin, il est déjà prêt ? Abonne-toi et laisse un like !")]),

 ("026-dijon", 3, "🎄 Le jour où la France a brûlé le Père Noël", LANT,
  ["Claude Lévi-Strauss, Le Père Noël supplicié (1952)", "macommune.info, Il y a 70 ans le clergé brûlait le Père Noël à Dijon"], [
  ("En 1951, en France, on a brûlé le Père Noël. En public. Devant une cathédrale.", V("Le Père Noël ?", "BRÛLÉ", "brûlé"), "shocked", {"on": "brûlé", "pose": "recoil", "mood": "shocked", "hold": 1.0}),
  ("C'est le 23 décembre, à Dijon, devant la cathédrale Saint-Bénigne.", Y(1951, "DIJON", "dijon"), "serious"),
  ("Des membres du clergé l'accusent de faire oublier Jésus, et d'être une invention païenne venue d'Amérique.", S("ACCUSÉ", "d'être un païen venu d'Amérique"), "angry"),
  ("Alors, devant environ deux cent cinquante enfants, ils accrochent un mannequin du Père Noël aux grilles. Et ils y mettent le feu.", C(250, "ENFANTS", "DEVANT LE BÛCHER", "cinquante"), "worried"),
  ("Le lendemain soir, la mairie réplique : le Père Noël réapparaît, bien vivant, sur le toit de l'hôtel de ville.", V("Mort ?", "VIVANT", "vivant"), "happy", {"on": "vivant", "pose": "cheer", "hold": 1.0}),
  ("L'affaire fait tellement de bruit que l'anthropologue Claude Lévi-Strauss y consacre un texte : Le Père Noël supplicié.", Q("LE PÈRE NOËL SUPPLICIÉ", "— Claude Lévi-Strauss, 1952"), "serious"),
  CTA("TEAM PÈRE NOËL ?", "Team Père Noël ou team clergé ? Abonne-toi et laisse un like !")]),

 ("027-chat-de-noel", 4, "🎄 Le chat géant qui mange les enfants à Noël", LANT,
  ["Wikipedia, Yule Cat (Jólakötturinn)", "Iceland Monitor, The Christmas Cat"], [
  ("En Islande, à Noël, un chat géant dévore ceux qui n'ont pas reçu de vêtements neufs.", V("Un simple chat ?", "GÉANT", "géant"), "shocked", {"on": "dévore", "pose": "recoil", "mood": "shocked", "hold": 1.0}),
  ("Il s'appelle Jólakötturinn : le chat de Noël. Selon la légende, il est plus grand qu'une maison.", S("LE CHAT DE NOËL", "plus grand qu'une maison"), "worried"),
  ("La nuit de Noël, il rôde dans la neige, et il regarde par les fenêtres.", S("IL RÔDE", "la nuit de Noël"), "worried"),
  ("Si un enfant n'a pas de vêtement neuf… il le mange. Et son repas de Noël avec.", V("Pas de vêtement neuf ?", "DÉVORÉ", "mange"), "shocked"),
  ("Pourquoi une histoire aussi cruelle ? Autrefois, il fallait finir de travailler la laine avant Noël. Ceux qui avaient bien travaillé recevaient un vêtement neuf.", S("LA LAINE", "à finir avant Noël"), "serious"),
  ("Les autres risquaient de finir dans le ventre du chat. Une façon très efficace de motiver tout le monde.", V("Motivant ?", "TRÈS", "efficace"), "smug"),
  CTA("PULL NEUF ?", "Et toi, tu as eu un pull neuf cette année ? Abonne-toi et laisse un like !")]),

 ("028-krampus", 5, "🎄 Ce soir, le Krampus punit les enfants", LANT,
  ["Wikipedia, Krampus", "National Geographic, Who is Krampus?"], [
  ("Ce soir, dans les Alpes, des démons à cornes courent dans les rues pour punir les enfants.", V("Le Père Noël ?", "KRAMPUS", "démons"), "shocked", {"on": "démons", "pose": "recoil", "mood": "shocked", "hold": 1.0}),
  ("C'est le Krampus. Moitié chèvre, moitié démon, avec de grandes cornes et une longue langue.", S("LE KRAMPUS", "moitié chèvre, moitié démon"), "worried"),
  ("Le 5 décembre, la veille de la Saint-Nicolas, c'est la Krampusnacht : la nuit du Krampus.", S("5 DÉCEMBRE", "la nuit du Krampus"), "serious"),
  ("Saint Nicolas récompense les enfants sages. Le Krampus, lui, s'occupe des autres, avec des chaînes et des branches de bouleau.", V("Pas sage ?", "PUNI", "autres"), "angry"),
  ("Selon la légende, il pouvait même emporter les plus méchants dans un sac. Direction : son repaire.", S("DANS UN SAC", "direction son repaire"), "worried"),
  ("Dans les années 1930, l'Autriche a même essayé d'interdire le Krampus. Raté : aujourd'hui, des milliers de gens se déguisent en démon chaque année.", V("Interdit ?", "RATÉ", "raté"), "smug"),
  CTA("SOIS SAGE !", "Alors ce soir, sois sage ! Abonne-toi et laisse un like !")]),

 ("029-saint-nicolas", 6, "🎄 La légende terrifiante de saint Nicolas", GIFT,
  ["Wikipedia, La Légende de saint Nicolas (chanson)", "Wikipedia, Nicolas de Myre"], [
  ("La légende de saint Nicolas commence par un crime horrible : un boucher qui tue trois enfants.", V("Une jolie légende ?", "HORRIBLE", "horrible"), "shocked"),
  ("Trois petits enfants se perdent en allant glaner aux champs. La nuit tombe. Ils frappent chez un boucher.", S("TROIS ENFANTS", "perdus dans la nuit"), "worried"),
  ("Le boucher les fait entrer… et les cache dans son saloir, comme du petit salé.", S("LE SALOIR", "chez le boucher"), "worried"),
  ("Sept ans plus tard, saint Nicolas passe par là. Et il demande du petit salé.", C(7, "ANS", "PLUS TARD", "sept"), "serious"),
  ("Le boucher panique. Saint Nicolas étend trois doigts au-dessus du saloir… et les trois enfants se relèvent, vivants.", V("Perdus ?", "VIVANTS", "vivants"), "happy", {"on": "vivants", "pose": "cheer", "hold": 1.0}),
  ("Voilà pourquoi saint Nicolas protège les enfants. Et pourquoi, chaque 6 décembre, en Lorraine et en Belgique, il leur apporte des cadeaux.", S("6 DÉCEMBRE", "Lorraine, Belgique"), "happy"),
  CTA("SAINT-NICOLAS !", "Bonne Saint-Nicolas ! Abonne-toi et laisse un like !")]),

 ("030-pere-fouettard", 7, "🎄 Le Père Fouettard serait né d'une blague", LANT,
  ["Wikipedia, Père Fouettard", "Atlas Obscura, Beware the Christmas Cannibal of France"], [
  ("Le Père Fouettard, celui qui punit les enfants pas sages, serait né d'une moquerie contre un empereur.", V("Un monstre ?", "UNE MOQUERIE", "moquerie"), "smug"),
  ("On est en 1552. L'empereur Charles Quint assiège la ville de Metz.", Y(1552, "METZ", "1552"), "serious"),
  ("Mais l'hiver est terrible, son armée est malade, et il doit abandonner le siège.", V("Metz tombe ?", "ÉCHEC", "abandonner"), "smug"),
  ("Selon une tradition de Metz, les habitants fabriquent alors un mannequin de l'empereur, et le promènent dans les rues.", S("UN MANNEQUIN", "de Charles Quint"), "happy"),
  ("Ce personnage sombre et grimaçant serait devenu le Père Fouettard, le compagnon de saint Nicolas.", S("PÈRE FOUETTARD", "selon la tradition de Metz"), "curious"),
  ("Mais attention, d'autres versions existent. Dans la plus connue, c'est le boucher de la légende, condamné à suivre saint Nicolas pour toujours.", V("Une seule origine ?", "MYSTÈRE", "versions"), "serious"),
  CTA("PEUR ?", "Toi, il t'a déjà fait peur, le Père Fouettard ? Abonne-toi et laisse un like !")]),

 ("031-gui", 8, "🎄 S'embrasser sous le gui : une idée gauloise", CANE,
  ["Pline l'Ancien, Histoire naturelle, XVI, 95", "Wikipedia, Gui (plante) et Mistletoe"], [
  ("S'embrasser sous le gui, c'est une tradition qui remonte aux Gaulois.", V("Une idée romantique ?", "GAULOISE", "gaulois"), "smug"),
  ("Le Romain Pline l'Ancien raconte une cérémonie étonnante chez les druides.", Q("LA CUEILLETTE DU GUI", "— Pline l'Ancien"), "serious"),
  ("Un druide vêtu de blanc grimpe dans un chêne, et coupe le gui avec une serpe d'or.", S("UNE SERPE D'OR", "un druide dans un chêne"), "curious"),
  ("Pour eux, le gui qui pousse sur un chêne est très rare. Et il guérirait tout.", V("Une simple plante ?", "SACRÉE", "guérirait"), "surprised"),
  ("Bien plus tard, en Angleterre, on accroche du gui dans les maisons. Et celui qui passe dessous… doit donner un baiser.", S("UN BAISER", "sous le gui"), "happy"),
  ("Mais attention : les baies de gui sont toxiques. À regarder, pas à manger.", V("Ça se mange ?", "TOXIQUE", "toxiques"), "serious"),
  CTA("BISOU ?", "Tu as déjà eu un bisou sous le gui ? Abonne-toi et laisse un like !")]),

 ("032-noel-interdit", 9, "🎄 Quand fêter Noël était interdit", LANT,
  ["Wikipedia, Puritan Christmas ban (Massachusetts, 1659-1681)", "History.com, When Christmas Was Banned"], [
  ("Pendant plus de vingt ans, fêter Noël était interdit. Et puni d'une amende.", V("Fêter Noël ?", "INTERDIT", "interdit"), "shocked"),
  ("On est en 1659, dans la colonie du Massachusetts, en Amérique.", Y(1659, "BOSTON", "1659"), "serious"),
  ("Les puritains qui dirigent la colonie trouvent que Noël, c'est trop de fête, trop d'alcool. Et ce n'est pas dans la Bible.", S("TROP DE FÊTE", "et pas dans la Bible"), "angry"),
  ("La loi est claire : celui qui fête Noël paie cinq shillings d'amende.", C(5, "SHILLINGS", "D'AMENDE", "cinq"), "serious"),
  ("En Angleterre aussi, sous Cromwell, Noël a été aboli. Les boutiques devaient rester ouvertes le 25 décembre.", S("CROMWELL", "les boutiques restent ouvertes"), "worried"),
  ("Au Massachusetts, la loi est annulée en 1681. Mais pendant longtemps encore, Noël reste mal vu à Boston.", V("Fini ?", "EN 1681", "annulée"), "curious"),
  CTA("L'AMENDE ?", "Toi, tu aurais payé l'amende ? Abonne-toi et laisse un like !")]),

 ("033-bonshommes-bruxelles", 10, "🎄 Bruxelles envahie par 110 bonshommes de neige", CANE,
  ["Wikipedia, The Miracle of 1511", "Herman Pleij, De sneeuwpoppen van 1511"], [
  ("En 1511, Bruxelles a été envahie par plus de cent bonshommes de neige.", V("Une invasion ?", "DE NEIGE", "neige"), "smug"),
  ("Cet hiver-là, il fait si froid qu'on l'appelle l'hiver de la mort. Il gèle pendant des semaines.", S("HIVER DE LA MORT", "Bruxelles, 1511"), "worried"),
  ("Alors, les habitants sortent, et transforment toute la ville en musée de neige.", S("UN MUSÉE DE NEIGE", "dans toute la ville"), "happy"),
  ("Plus d'une centaine de sculptures : des chevaliers, des sirènes, des animaux… et même des personnages pas très sages.", C(110, "SCULPTURES", "DE NEIGE", "centaine"), "surprised"),
  ("Certaines se moquent même des puissants. Et un poète de la ville, Jan Smeken, a tout raconté dans un long poème.", Q("LE MIRACLE DE 1511", "— Jan Smeken, poète de Bruxelles"), "serious"),
  ("Et au dégel, tout disparaît. Il ne reste que le poème.", V("Il en reste quoi ?", "UN POÈME", "poème"), "sad"),
  CTA("TON BONHOMME ?", "Et toi, il ressemble à quoi, ton bonhomme de neige ? Abonne-toi et laisse un like !")]),

 ("034-pere-noel-rouge", 11, "🎄 Non, Coca-Cola n'a pas habillé le Père Noël en rouge", GIFT,
  ["Wikipedia, Santa Claus (Thomas Nast)", "Snopes, Did Coca-Cola Invent Santa Claus?"], [
  ("Non, ce n'est pas Coca-Cola qui a habillé le Père Noël en rouge.", V("Coca-Cola ?", "FAUX", "rouge"), "smug"),
  ("En 1863, un dessinateur américain, Thomas Nast, commence à le dessiner pour un journal. Un petit bonhomme joyeux, avec une barbe blanche.", Y(1863, "NEW YORK", "1863"), "curious"),
  ("Dans les années suivantes, il est souvent habillé de rouge, avec de la fourrure blanche. Des cartes postales le montrent déjà comme ça vers 1900.", S("DÉJÀ EN ROUGE", "cartes postales, vers 1900"), "happy"),
  ("Les publicités de Coca-Cola, dessinées par Haddon Sundblom, arrivent seulement en 1931.", V("Les premiers ?", "EN RETARD", "seulement"), "smug"),
  ("Mais elles sont partout, pendant des décennies. Et elles fixent son image : gros, souriant, rouge et blanc.", S("L'IMAGE FIXÉE", "gros, souriant, rouge et blanc"), "serious"),
  ("Coca-Cola ne l'a pas inventé. Mais l'a rendu célèbre dans le monde entier.", V("Inventé ?", "NON", "célèbre"), "curious"),
  CTA("TU LE SAVAIS ?", "Tu le savais ? Abonne-toi et laisse un like !")]),

 ("035-lettres-pere-noel", 12, "🎄 Qui répond vraiment aux lettres au Père Noël ?", GIFT,
  ["La Poste, Le secrétariat du Père Noël", "CIDJ, Depuis longtemps la lettre au Père Noël enchante les fêtes", "Connexion France, Letters from Santa: a French idea"], [
  ("En France, chaque lettre au Père Noël reçoit une réponse. Et la toute première a été écrite par une célèbre psychanalyste.", V("Une réponse ?", "TOUJOURS", "réponse"), "smug"),
  ("Au début des années 1960, des milliers d'enfants écrivent au Père Noël. Mais la Poste ne sait pas quoi faire de toutes ces lettres.", S("DES MILLIERS", "de lettres sans réponse"), "worried"),
  ("Alors, en 1962, la Poste crée le secrétariat du Père Noël.", Y(1962, "FRANCE", "1962"), "happy"),
  ("Et pour écrire la première réponse, on fait appel à Françoise Dolto, la célèbre spécialiste des enfants.", Q("FRANÇOISE DOLTO", "— psychanalyste"), "curious"),
  ("Aujourd'hui, le secrétariat est à Libourne, près de Bordeaux. Et il reçoit plus d'un million de lettres chaque année.", C(1, "MILLION", "DE LETTRES PAR AN", "million"), "surprised"),
  ("La règle : écrire avant le 20 décembre, à l'adresse Père Noël. Pas besoin de timbre. Et le Père Noël répond.", V("Un timbre ?", "INUTILE", "timbre"), "happy"),
  CTA("TA LETTRE ?", "Et toi, tu lui demandes quoi cette année ? Abonne-toi et laisse un like !")]),

 ("036-sainte-lucie", 13, "🎄 La nuit où les Suédoises portent du feu sur la tête", LANT,
  ["Wikipedia, Saint Lucy's Day", "Sweden.se, Lucia"], [
  ("En Suède, le 13 décembre, des jeunes filles portent une couronne de bougies allumées sur la tête.", V("Dangereux ?", "TRADITION", "bougies"), "surprised"),
  ("C'est la Sainte-Lucie. Lucie, ça vient du latin lux : la lumière.", S("LUX", "la lumière"), "curious"),
  ("Avec l'ancien calendrier, la nuit du 13 décembre était considérée comme la plus longue de l'année.", C(13, "DÉCEMBRE", "LA NUIT LA PLUS LONGUE", "13"), "serious"),
  ("Selon les vieilles croyances, cette nuit-là, des esprits et des créatures rôdaient dehors. Mieux valait rester éveillé.", S("DES ESPRITS", "rôdent dans la nuit"), "worried"),
  ("Alors, au petit matin, une jeune fille en blanc apporte la lumière, du café, et des petits pains au safran.", S("PAINS AU SAFRAN", "et du café, à l'aube"), "happy"),
  ("Aujourd'hui, dans les écoles et les villes, il y a même une Lucie de l'année. Avec de vraies bougies… ou électriques, c'est plus prudent.", V("De vraies bougies ?", "PARFOIS", "électriques"), "smug"),
  CTA("LUMIÈRE !", "Tu aimerais voir ça ? Abonne-toi et laisse un like !")]),

 ("037-papillotes", 14, "🎄 Les papillotes, nées d'un amour secret", CANE,
  ["Wikipedia, Papillote (confiserie)", "Office du tourisme de Lyon, La papillote lyonnaise"], [
  ("Les papillotes de Noël seraient nées d'une histoire d'amour secrète, à Lyon.", V("Un simple bonbon ?", "UN SECRET", "secrète"), "smug"),
  ("Au dix-huitième siècle, un confiseur lyonnais nommé Papillot a un apprenti. Et cet apprenti est amoureux.", S("PAPILLOT", "confiseur à Lyon"), "happy"),
  ("Pour séduire une jeune fille, il enveloppe des chocolats dans des petits mots d'amour.", S("DES MOTS D'AMOUR", "autour des chocolats"), "happy"),
  ("Mais le patron découvre que ses chocolats disparaissent. Et il renvoie l'apprenti.", V("Découvert ?", "RENVOYÉ", "renvoie"), "shocked"),
  ("Puis il a une idée : vendre des chocolats enveloppés de papier, avec un petit texte à l'intérieur.", S("LA PAPILLOTE", "un chocolat, un petit texte"), "curious"),
  ("Voilà ce que dit la légende. Vraie ou pas, chaque Noël, des millions de papillotes sont encore déballées en France.", V("Vraie histoire ?", "LÉGENDE", "légende"), "smug"),
  CTA("TEAM PAPILLOTE", "Ta dernière papillote, elle disait quoi ? Abonne-toi et laisse un like !")]),

 ("038-buche", 15, "🎄 Avant d'être un gâteau, la bûche brûlait pendant des jours", LANT,
  ["Wikipedia, Bûche de Noël", "Wikipedia, Yule log"], [
  ("La bûche de Noël, avant d'être un gâteau, c'était une vraie bûche. Qu'on faisait brûler pendant des jours.", V("Un gâteau ?", "DU BOIS", "vraie"), "smug"),
  ("Dans les campagnes, la veille de Noël, on choisit une énorme bûche, souvent d'arbre fruitier.", S("UNE ÉNORME BÛCHE", "choisie pour Noël"), "curious"),
  ("On la bénit, parfois avec du sel ou de l'eau bénite, puis on l'allume dans la cheminée.", S("BÉNIE", "puis allumée dans la cheminée"), "serious"),
  ("Elle doit brûler très longtemps. Dans certaines régions, jusqu'à douze jours.", C(12, "JOURS", "DE FEU", "douze"), "surprised"),
  ("Ses cendres étaient précieuses : on les gardait pour protéger la maison de la foudre et des maladies.", V("Des cendres ?", "PROTECTION", "foudre"), "curious"),
  ("Puis les grandes cheminées disparaissent. Et au dix-neuvième siècle, des pâtissiers ont l'idée de la transformer en gâteau.", S("UN GÂTEAU", "pâtissiers, XIXe siècle"), "happy"),
  CTA("TEAM CHOCOLAT ?", "Team chocolat ou team glacée ? Abonne-toi et laisse un like !")]),

 ("039-gemini-ovni", 16, "🎄 Le jour où des astronautes ont vu le Père Noël", GIFT,
  ["Smithsonian, Bells and Harmonica, Gemini 6", "Smithsonian Magazine, The Day Two Astronauts Said They Saw a U.F.O. Wearing a Red Suit"], [
  ("Le 16 décembre 1965, des astronautes signalent un objet volant non identifié. En orbite.", V("Un OVNI ?", "SIGNALÉ", "orbite"), "shocked"),
  ("Ils sont à bord de la capsule Gemini 6 : Wally Schirra et Tom Stafford.", S("GEMINI 6", "Schirra et Stafford"), "serious"),
  ("À la radio, Stafford annonce un objet qui va du nord vers le sud. Avec un pilote… en costume rouge.", Q("UN PILOTE EN ROUGE", "— Tom Stafford, 1965"), "surprised"),
  ("Au sol, silence total. Puis, on entend de la musique.", V("Une menace ?", "UNE MUSIQUE", "musique"), "curious"),
  ("Les astronautes avaient caché un petit harmonica et des clochettes à bord. Et ils jouent Jingle Bells.", S("JINGLE BELLS", "un harmonica, des clochettes"), "happy", {"on": "jouent", "pose": "cheer", "hold": 1.0}),
  ("C'était une blague. Mais c'est aussi la première musique jouée dans l'espace. L'harmonica est aujourd'hui dans un musée, à Washington.", V("Un vrai OVNI ?", "UNE BLAGUE", "blague"), "smug"),
  CTA("VU DE L'ESPACE", "Le Père Noël, vu de l'espace. Abonne-toi et laisse un like !")]),

 ("040-norad", 17, "🎄 Un enfant appelle l'armée… pour parler au Père Noël", GIFT,
  ["NORAD Tracks Santa, History", "Wikipedia, NORAD Tracks Santa"], [
  ("En 1955, un enfant appelle l'armée américaine pour parler au Père Noël. Et l'armée répond.", V("L'armée ?", "ALLÔ ?", "répond"), "smug"),
  ("Une publicité dans un journal de Colorado Springs invite les enfants à appeler le Père Noël. Mais le numéro est faux.", S("UN NUMÉRO FAUX", "dans une publicité"), "surprised"),
  ("Ce numéro, c'est une ligne secrète de la défense aérienne. Le colonel Harry Shoup décroche.", S("LIGNE SECRÈTE", "défense aérienne"), "serious"),
  ("Au bout du fil, une petite voix : c'est vraiment toi, le Père Noël ?", Q("PÈRE NOËL ?", "— un enfant, 1955"), "curious"),
  ("Le colonel joue le jeu. Et son équipe commence à donner aux enfants la position du traîneau sur les radars.", V("Il raccroche ?", "IL JOUE", "jeu"), "happy"),
  ("Soixante-dix ans plus tard, la tradition continue. Chaque 24 décembre, le NORAD suit le Père Noël en direct pour des millions d'enfants.", C(70, "ANS", "DE SUIVI RADAR", "soixante"), "happy"),
  CTA("SUR LE RADAR", "Le 24 décembre, regarde le radar ! Abonne-toi et laisse un like !")]),

 ("041-greccio", 18, "🎄 La toute première crèche était vivante", GIFT,
  ["Wikipedia, Crèche de Noël (Greccio, 1223)", "Thomas de Celano, Vie de saint François"], [
  ("La toute première crèche de Noël avait un vrai bœuf et un vrai âne. Et elle était dans une grotte.", V("Des santons ?", "VIVANTE", "vrai"), "smug"),
  ("On est en 1223, à Greccio, un petit village d'Italie.", Y(1223, "GRECCIO", "1223"), "curious"),
  ("François d'Assise veut que les gens voient de leurs yeux comment Jésus est né : dans la pauvreté.", S("FRANÇOIS D'ASSISE", "voir de ses propres yeux"), "serious"),
  ("Alors, dans une grotte, il installe une mangeoire avec du foin, un bœuf et un âne.", S("UNE MANGEOIRE", "du foin, un bœuf, un âne"), "happy"),
  ("La nuit de Noël, les villageois arrivent avec des torches. Et la messe est célébrée là, au milieu des animaux.", V("Dans une église ?", "UNE GROTTE", "animaux"), "surprised"),
  ("L'idée plaît tellement qu'elle se répand partout. Huit cents ans plus tard, on fait encore des crèches dans le monde entier.", C(800, "ANS", "DE CRÈCHES", "huit"), "happy"),
  CTA("TA CRÈCHE ?", "Chez toi, crèche ou pas crèche ? Abonne-toi et laisse un like !")]),

 ("042-douce-nuit", 19, "🎄 Le chant de Noël né d'un orgue en panne", LANT,
  ["Wikipedia, Silent Night", "Stille Nacht Gesellschaft, history"], [
  ("Le chant de Noël le plus célèbre du monde serait né à cause d'un orgue en panne.", V("Une grande idée ?", "UNE PANNE", "panne"), "smug"),
  ("On est le 24 décembre 1818, à Oberndorf, un village d'Autriche.", Y(1818, "OBERNDORF", "1818"), "curious"),
  ("Selon la tradition, l'orgue de l'église ne marche plus. Certains accusent même des souris d'avoir rongé le soufflet.", S("DES SOURIS ?", "l'orgue ne marche plus"), "surprised"),
  ("Le prêtre, Joseph Mohr, a écrit un poème. Il demande à l'instituteur, Franz Xaver Gruber, d'en faire une mélodie. Pour guitare.", S("POUR GUITARE", "Mohr et Gruber"), "serious"),
  ("Le soir même, ils chantent Stille Nacht pour la première fois. En français : Douce nuit.", Q("STILLE NACHT", "— Oberndorf, 24 décembre 1818"), "happy"),
  ("Aujourd'hui, ce chant serait traduit dans plus de trois cents langues et dialectes.", C(300, "LANGUES", "ET DIALECTES", "trois"), "surprised"),
  CTA("DOUCE NUIT", "Tu la connais par cœur ? Abonne-toi et laisse un like !")]),

 ("043-mari-lwyd", 20, "🎄 À Noël, un crâne de cheval frappe à ta porte", LANT,
  ["Wikipedia, Mari Lwyd", "Museum Wales, The Mari Lwyd"], [
  ("Au pays de Galles, à Noël, un crâne de cheval peut venir frapper à ta porte.", V("Le Père Noël ?", "UN CRÂNE", "crâne"), "shocked", {"on": "crâne", "pose": "recoil", "mood": "shocked", "hold": 1.0}),
  ("C'est la Mari Lwyd : un vrai crâne de cheval, sur un bâton, caché sous un drap blanc avec des rubans.", S("MARI LWYD", "un crâne de cheval sous un drap"), "worried"),
  ("Elle se promène de maison en maison avec sa troupe, entre Noël et le Nouvel An.", S("DE PORTE EN PORTE", "entre Noël et le Nouvel An"), "curious"),
  ("À la porte commence une bataille de chansons : la troupe chante des moqueries en rimes, et les habitants doivent répondre.", S("UN DUEL CHANTÉ", "des moqueries en rimes"), "smug"),
  ("Si les habitants perdent, la Mari Lwyd entre dans la maison, mange, boit, et sème la pagaille.", V("Ils perdent ?", "ELLE ENTRE", "entre"), "surprised"),
  ("La tradition a failli disparaître. Mais aujourd'hui, elle revient dans plusieurs villages gallois.", V("Disparue ?", "DE RETOUR", "revient"), "happy"),
  CTA("TU OUVRES ?", "Toi, tu lui ouvres la porte ? Abonne-toi et laisse un like !")]),

 ("044-newgrange", 21, "🎄 La tombe qui s'illumine un seul jour par an", LANT,
  ["Wikipedia, Newgrange", "World Heritage Ireland, Newgrange winter solstice"], [
  ("En Irlande, une tombe plus vieille que les pyramides s'illumine quelques minutes par an. Et c'est aujourd'hui.", V("Une simple tombe ?", "ILLUMINÉE", "illumine"), "surprised"),
  ("C'est Newgrange. Elle a été construite il y a plus de cinq mille ans.", C(5000, "ANS", "AVANT LES PYRAMIDES", "cinq"), "serious"),
  ("Au-dessus de l'entrée, ses bâtisseurs ont laissé une petite ouverture : une boîte à lumière.", S("BOÎTE À LUMIÈRE", "au-dessus de l'entrée"), "curious"),
  ("Au solstice d'hiver, à l'aube, le soleil entre par cette ouverture et remonte un couloir de dix-neuf mètres.", C(19, "MÈTRES", "DE COULOIR", "dix"), "curious"),
  ("Pendant environ dix-sept minutes, la chambre au fond de la tombe est éclairée. Puis tout redevient noir.", V("Combien de temps ?", "17 MINUTES", "minutes"), "surprised"),
  ("Chaque année, des milliers de personnes participent à un tirage au sort pour avoir une place à l'intérieur.", S("TIRAGE AU SORT", "pour une place à l'intérieur"), "happy"),
  CTA("SOLSTICE", "Le jour le plus court de l'année. Abonne-toi et laisse un like !")]),

 ("045-chaplin", 22, "🎄 Le cercueil volé de Charlie Chaplin", LANT,
  ["Wikipedia, Charlie Chaplin (death)", "BBC, The bizarre theft of Charlie Chaplin's body"], [
  ("Charlie Chaplin est mort le jour de Noël. Et deux mois plus tard, son cercueil a disparu.", V("Repose en paix ?", "VOLÉ", "disparu"), "shocked"),
  ("Il meurt le 25 décembre 1977, en Suisse, à Corsier-sur-Vevey.", Y(1977, "SUISSE", "1977"), "sad"),
  ("Début mars 1978, on découvre sa tombe vide. Le cercueil a été déterré pendant la nuit.", S("TOMBE VIDE", "mars 1978"), "shocked"),
  ("Les voleurs appellent sa veuve, Oona. Ils réclament une rançon de six cent mille francs suisses.", C(600, "MILLE FRANCS", "DE RANÇON", "six"), "angry"),
  ("La famille refuse de payer. La police surveille son téléphone, et plus de deux cents cabines téléphoniques.", S("200 CABINES", "sur écoute"), "serious"),
  ("Les voleurs sont arrêtés. Le cercueil était enterré dans un champ, pas très loin. Chaplin est enterré à nouveau. Cette fois, sous du béton.", V("Retrouvé ?", "SOUS LE BÉTON", "béton"), "smug"),
  CTA("INCROYABLE ?", "Tu connaissais cette histoire ? Abonne-toi et laisse un like !")]),

 ("046-washington-noel", 23, "🎄 L'attaque surprise du soir de Noël 1776", LANT,
  ["Wikipedia, Washington's crossing of the Delaware River", "Wikipedia, Battle of Trenton"], [
  ("Le soir de Noël 1776, George Washington lance une attaque surprise. En pleine tempête de neige.", V("Une trêve ?", "ATTAQUE", "attaque"), "serious"),
  ("La guerre d'indépendance américaine va mal. L'armée de Washington est épuisée, et beaucoup de soldats vont bientôt rentrer chez eux.", S("TOUT VA MAL", "une armée épuisée"), "worried"),
  ("La nuit du 25 décembre, il fait traverser le fleuve Delaware, plein de glace, à environ deux mille quatre cents hommes.", C(2400, "SOLDATS", "À TRAVERS LE FLEUVE", "deux"), "serious"),
  ("Le mot de passe de la nuit : victoire ou mort.", Q("VICTOIRE OU MORT", "— mot de passe, 1776"), "angry"),
  ("Au petit matin, ils tombent sur les soldats hessois de Trenton, qui ne s'attendent à rien.", S("TRENTON", "26 décembre 1776, à l'aube"), "surprised"),
  ("En à peine une heure, près de neuf cents soldats ennemis sont faits prisonniers.", C(900, "PRISONNIERS", "EN UNE MATINÉE", "neuf"), "shocked"),
  CTA("QUEL NOËL !", "Un Noël qui a changé l'histoire. Abonne-toi et laisse un like !")]),

 ("047-treve-1914", 24, "🎄 Noël 1914 : les ennemis ont arrêté la guerre", LANT,
  ["Wikipedia, Christmas truce", "Imperial War Museums, The real story of the Christmas truce"], [
  ("Le soir de Noël 1914, en pleine guerre, des soldats ennemis ont arrêté de se tirer dessus. Pour chanter ensemble.", V("La guerre continue ?", "TRÊVE", "chanter"), "surprised"),
  ("Sur le front, en Belgique, des soldats allemands posent des petits sapins avec des bougies sur leurs tranchées.", S("DES BOUGIES", "sur les tranchées"), "curious"),
  ("Puis ils chantent des chants de Noël. En face, les Britanniques répondent en chantant aussi.", S("DES CHANTS", "d'une tranchée à l'autre"), "happy"),
  ("Le lendemain, des soldats sortent sans armes. Ils se serrent la main, échangent du tabac et des boutons.", V("Des ennemis ?", "SANS ARMES", "armes"), "happy"),
  ("Ensemble, ils enterrent aussi leurs morts. Et selon plusieurs témoignages, certains jouent même au football.", S("UN MATCH ?", "selon plusieurs témoignages"), "sad"),
  ("Les généraux sont furieux. Les années suivantes, ce genre de trêve est interdit. Elle ne se répétera jamais à cette échelle.", V("Encore en 1915 ?", "INTERDIT", "interdit"), "serious"),
  CTA("JOYEUX NOËL", "Joyeux Noël à toi. Abonne-toi et laisse un like !")]),

 ("048-apollo-8", 25, "🎄 Le Noël passé autour de la Lune", GIFT,
  ["NASA, Apollo 8: Christmas at the Moon", "Wikipedia, Earthrise"], [
  ("Le soir de Noël 1968, trois hommes fêtent Noël autour de la Lune.", V("Un Noël normal ?", "EN ORBITE", "lune"), "surprised"),
  ("C'est la mission Apollo 8. Pour la première fois, des humains font le tour de la Lune.", S("APOLLO 8", "Borman, Lovell, Anders"), "curious"),
  ("Le 24 décembre, en sortant de derrière la Lune, ils voient la Terre se lever à l'horizon.", S("LEVER DE TERRE", "24 décembre 1968"), "surprised"),
  ("Bill Anders attrape un appareil photo, et prend une des photos les plus célèbres de l'histoire.", V("Une simple photo ?", "LÉGENDAIRE", "célèbres"), "happy"),
  ("Ce soir-là, ils lisent un texte en direct à la télévision. Le monde entier les écoute.", S("EN DIRECT", "depuis la Lune, le soir de Noël"), "serious"),
  ("Sur Terre, 1968 a été une année terrible. Un télégramme leur dira : merci, vous avez sauvé 1968.", Q("VOUS AVEZ SAUVÉ 1968", "— un télégramme reçu par Frank Borman"), "happy"),
  CTA("DEPUIS LA LUNE", "Joyeux Noël depuis la Lune ! Abonne-toi et laisse un like !")]),

 ("049-flannan", 26, "🎄 Les trois gardiens de phare disparus", LANT,
  ["Wikipedia, Flannan Isles Lighthouse", "Northern Lighthouse Board, Flannan Isles"], [
  ("Le 26 décembre 1900, un bateau arrive sur une île écossaise. Les trois gardiens du phare ont disparu.", V("Personne ?", "DISPARUS", "disparu"), "shocked"),
  ("Nous sommes aux îles Flannan, au large de l'Écosse. Le phare n'a même pas un an.", Y(1900, "ÎLES FLANNAN", "flannan"), "serious"),
  ("Le bateau de relève approche. Pas de drapeau, pas de signal. Personne ne vient l'accueillir.", S("AUCUN SIGNAL", "26 décembre 1900"), "worried"),
  ("Dans le phare, tout est en ordre. Les lits sont faits. Mais l'horloge est arrêtée.", S("HORLOGE ARRÊTÉE", "les lits sont faits"), "worried"),
  ("Seul indice : deux cirés ont disparu. Le troisième est toujours là. Comme si un homme était sorti en manches de chemise.", C(2, "CIRÉS", "SUR TROIS ONT DISPARU", "deux"), "curious"),
  ("L'enquête pense qu'une vague géante les a emportés. Mais personne ne sait pourquoi le troisième est sorti. Et on ne les a jamais retrouvés.", V("Une vague ?", "MYSTÈRE", "jamais"), "serious"),
  CTA("TA THÉORIE ?", "Et toi, tu as une théorie ? Abonne-toi et laisse un like !")]),

 ("050-befana", 27, "🎄 En Italie, c'est une sorcière qui apporte les cadeaux", CANE,
  ["Wikipedia, Befana", "Italia.it, La Befana"], [
  ("En Italie, les cadeaux ne sont pas apportés par le Père Noël. Mais par une sorcière.", V("Le Père Noël ?", "UNE SORCIÈRE", "sorcière"), "smug"),
  ("Elle s'appelle la Befana. Elle vole sur un balai, avec un vieux châle et des chaussures trouées.", S("LA BEFANA", "sur son balai"), "happy"),
  ("Selon la légende, les Rois mages frappent à sa porte, et lui demandent de les accompagner pour voir l'Enfant Jésus.", S("LES ROIS MAGES", "frappent à sa porte"), "curious"),
  ("Elle refuse : elle a trop de ménage. Puis elle regrette… mais trop tard, ils sont partis.", V("Elle les suit ?", "TROP TARD", "tard"), "sad"),
  ("Depuis, elle cherche l'enfant. Dans la nuit du 5 au 6 janvier, elle passe dans chaque maison, par la cheminée.", S("5 AU 6 JANVIER", "par la cheminée"), "curious"),
  ("Les enfants sages reçoivent des bonbons. Les autres… du charbon. Mais souvent, c'est du charbon en sucre.", V("Du charbon ?", "EN SUCRE", "sucre"), "smug"),
  CTA("CHARBON ?", "Toi, tu mérites bonbons ou charbon ? Abonne-toi et laisse un like !")]),

 ("051-musee-mexico", 28, "🎄 Le casse du réveillon au musée de Mexico", LANT,
  ["Wikipedia, 1985 Museo Nacional de Antropología robbery", "Los Angeles Times, 1989, recovery of the stolen artifacts"], [
  ("La nuit de Noël 1985, pendant que tout le monde fait la fête, un musée de Mexico est cambriolé.", V("Une nuit calme ?", "CAMBRIOLÉ", "cambriolé"), "shocked"),
  ("C'est le Musée national d'anthropologie. Il garde les plus grands trésors de l'histoire du Mexique.", S("MEXICO", "musée national d'anthropologie"), "serious"),
  ("Les gardiens fêtent le réveillon. Les voleurs entrent par un conduit d'aération.", S("UN CONDUIT", "pendant le réveillon"), "worried"),
  ("Le matin, il manque plus de cent vingt objets anciens. Des masques, des bijoux, des trésors mayas et aztèques.", C(120, "OBJETS", "VOLÉS EN UNE NUIT", "cent"), "shocked"),
  ("On imagine un gang international. Mais pendant des années, la police ne trouve rien.", V("Un gang ?", "RIEN", "rien"), "worried"),
  ("En 1989, la vérité tombe : les voleurs sont deux anciens étudiants vétérinaires. Ils gardaient presque tout dans une armoire.", V("Des pros ?", "DES ÉTUDIANTS", "étudiants"), "surprised"),
  CTA("UN FILM !", "Cette histoire a même inspiré un film. Abonne-toi et laisse un like !")]),

 ("052-ecosse-noel", 29, "🎄 En Écosse, Noël n'était pas férié avant 1958", GIFT,
  ["Wikipedia, Christmas in Scotland", "Wikipedia, Hogmanay"], [
  ("En Écosse, Noël n'est devenu un jour férié qu'en 1958.", V("Noël, férié ?", "EN 1958", "1958"), "surprised"),
  ("Tout commence en 1640. Le Parlement écossais interdit de fêter Yule, le vieux nom de Noël.", Y(1640, "ÉCOSSE", "1640"), "serious"),
  ("Pour l'Église d'Écosse, Noël n'est pas dans la Bible. Et cette fête rappelle trop les vieilles fêtes païennes.", S("TROP PAÏEN", "selon l'Église d'Écosse"), "angry"),
  ("Pendant des siècles, beaucoup d'Écossais travaillent le 25 décembre, comme un jour normal.", V("Un jour de fête ?", "AU TRAVAIL", "travaillent"), "worried"),
  ("Alors, la grande fête de l'hiver devient le Nouvel An. En Écosse, on l'appelle Hogmanay.", S("HOGMANAY", "le Nouvel An écossais"), "happy"),
  ("Et la tradition dit qu'il faut être le premier à franchir la porte d'une maison après minuit, avec un cadeau. Ça porte bonheur.", S("LE PREMIER PAS", "après minuit, avec un cadeau"), "happy"),
  CTA("TON CAMP ?", "Toi, tu préfères Noël ou le Nouvel An ? Abonne-toi et laisse un like !")]),

 ("053-douze-raisins", 30, "🎄 Douze raisins à minuit pile", CANE,
  ["Wikipedia, Twelve Grapes", "El País, El origen de las uvas de Nochevieja"], [
  ("En Espagne, à minuit pile, le 31 décembre, tout le monde avale douze raisins. Un à chaque coup de cloche.", V("Du champagne ?", "12 RAISINS", "raisins"), "smug"),
  ("Si tu les manges tous à temps, l'année sera bonne. Douze raisins, douze mois de chance.", C(12, "RAISINS", "12 MOIS DE CHANCE", "douze"), "happy"),
  ("D'où ça vient ? L'histoire la plus connue parle de 1909.", Y(1909, "ESPAGNE", "1909"), "curious"),
  ("Cette année-là, la récolte est énorme. Les vignerons d'Alicante ont des tonnes de raisins à vendre.", S("TROP DE RAISINS", "Alicante, 1909"), "surprised"),
  ("Mais des journaux de Madrid en parlent déjà dans les années 1880. Des bourgeois qui imitaient les Français et leur champagne.", S("MADRID, 1880", "déjà dans les journaux"), "serious"),
  ("Le vrai défi : les coups sonnent toutes les trois secondes. Avec les pépins. Bonne chance.", V("Facile ?", "DÉFI", "défi"), "smug"),
  CTA("TU TENTES ?", "Tu tentes cette année ? Abonne-toi et laisse un like !")]),

 ("054-nouvel-an", 31, "🎄 Pourquoi l'année commence le 1er janvier", GIFT,
  ["Wikipedia, Édit de Roussillon", "Wikipedia, Poisson d'avril"], [
  ("Avant 1564, en France, la nouvelle année ne commençait pas le premier janvier.", V("Le 1er janvier ?", "PAS AVANT", "janvier"), "smug"),
  ("Selon les régions, elle commençait à Noël, le 25 mars, ou même à Pâques. Une date qui change chaque année !", S("À PÂQUES ?", "ou à Noël, ou le 25 mars"), "surprised"),
  ("Résultat : un vrai casse-tête pour dater les contrats et les lettres.", V("Pratique ?", "LE CHAOS", "casse"), "worried"),
  ("En 1564, le jeune roi Charles IX fait le tour de la France. Et au château de Roussillon, il signe un édit.", Y(1564, "ROUSSILLON", "1564"), "serious"),
  ("Désormais, dans tout le royaume, l'année commencera le premier janvier.", S("1ER JANVIER", "édit de Roussillon, 1564"), "happy"),
  ("Une légende dit que ceux qui fêtaient encore l'ancienne date, au printemps, recevaient de faux cadeaux pour rire. Ce serait l'origine du poisson d'avril.", V("Le poisson d'avril ?", "PEUT-ÊTRE", "avril"), "curious"),
  CTA("BONNE ANNÉE !", "Bonne année à toi ! Abonne-toi et laisse un like !")]),
]
