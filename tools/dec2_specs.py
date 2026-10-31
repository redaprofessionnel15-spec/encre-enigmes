# Décembre 2026, créneau de 19 h : un 2e Short de Noël/hiver par jour, voix Guillaume.
# Chaque segment : (tts, scène, humeur du hibou)
def V(claim, stamp, on): return {"type": "verdict", "claim": claim, "stamp": stamp, "stamp_on": on}
def S(big, line): return {"type": "scroll", "big": big, "line": line}
def Y(year, place, on): return {"type": "year", "year": year, "from": 2026, "place": place, "land_on": on}
def C(value, unit, label, on): return {"type": "counter", "value": value, "unit": unit, "label": label, "from": 0, "slam_on": on}
def Q(title, sign): return {"type": "quote", "title": title, "sign": sign}
def CTA(big, tts): return (tts, {"type": "cta", "big": big, "sub_on": "Abonne", "like_on": "laisse"}, None)
D = lambda d: f"2026-12-{d:02d}T19:00:00+01:00"
GIFT, CANE, LANT = "gift", "candy_cane", "lantern"
AL = "Abonne-toi et laisse un like !"

SHORTS = [
 ("096-calendrier-avent", D(1), "🎄 Le calendrier de l'Avent est né d'une maman", GIFT,
  ["Wikipedia, Advent calendar (Gerhard Lang)"], [
  ("Le calendrier de l'Avent a été inventé grâce à une maman qui en avait marre qu'on lui demande : c'est quand, Noël ?", V("Inventé par un magasin ?", "MAMAN", "maman"), "smug"),
  ("En Allemagne, à la fin du dix-neuvième siècle, le petit Gerhard Lang n'arrête pas de demander combien de jours il reste avant Noël.", S("C'EST QUAND ?", "demande le petit Gerhard"), "curious"),
  ("Alors sa mère colle vingt-quatre petits gâteaux sur un carton. Un par jour, jusqu'à Noël.", C(24, "GÂTEAUX", "SUR UN CARTON", "vingt"), "happy"),
  ("Devenu adulte, Gerhard travaille dans une imprimerie à Munich. Et vers 1908, il imprime les premiers calendriers de l'Avent.", Y(1908, "MUNICH", "1908"), "serious"),
  ("Les petites portes à ouvrir arrivent un peu plus tard. Et le chocolat encore après.", S("LES PORTES", "puis le chocolat"), "surprised"),
  ("Aujourd'hui, on en vend des millions chaque année, avec des bonbons, des jouets, et même du fromage.", V("Seulement du chocolat ?", "FROMAGE", "fromage"), "happy"),
  CTA("1ER DÉCEMBRE", f"Toi, tu as déjà ouvert la première case ? {AL}")]),

 ("097-rudolph", D(2), "🎄 Le renne au nez rouge vient d'une pub", CANE,
  ["Wikipedia, Rudolph the Red-Nosed Reindeer", "Wikipedia, Robert L. May"], [
  ("Rudolph, le renne au nez rouge, n'est pas une vieille légende. C'est une publicité.", V("Une vieille légende ?", "PUB", "publicité"), "smug"),
  ("En 1939, aux États-Unis, le grand magasin Montgomery Ward veut offrir un petit livre aux enfants pour Noël.", Y(1939, "CHICAGO", "1939"), "curious"),
  ("Un employé, Robert May, invente l'histoire d'un renne moqué à cause de son nez qui brille.", S("UN NEZ QUI BRILLE", "et tout le monde se moque"), "worried"),
  ("Jusqu'au soir où le brouillard est si épais que le Père Noël a besoin de lui pour guider le traîneau.", V("Le renne raté ?", "HÉROS", "traîneau"), "happy"),
  ("Cette année-là, le magasin distribue plus de deux millions de livres.", C(2, "MILLIONS", "DE LIVRES OFFERTS", "millions"), "surprised"),
  ("En 1949, le beau-frère de Robert May en fait une chanson. Elle devient l'un des plus grands tubes de Noël de l'histoire.", S("UN TUBE", "chanté par Gene Autry"), "happy"),
  CTA("NEZ ROUGE", f"Tu connaissais l'origine de Rudolph ? {AL}")]),

 ("098-guirlandes-argent", D(3), "🎄 Les premières guirlandes étaient en vrai argent", GIFT,
  ["Wikipedia, Tinsel"], [
  ("Les premières guirlandes de Noël étaient faites en vrai argent.", V("En plastique ?", "ARGENT", "argent"), "smug"),
  ("Selon la tradition, elles apparaissent vers 1610, à Nuremberg, en Allemagne.", Y(1610, "NUREMBERG", "1610"), "curious"),
  ("Des artisans écrasent de l'argent en fils très fins, pour faire briller les sapins à la lueur des bougies.", S("DES FILS D'ARGENT", "pour refléter les bougies"), "happy"),
  ("Mais il y a un problème : la fumée des bougies noircit l'argent. Très vite, les guirlandes deviennent toutes ternes.", V("Elles brillent longtemps ?", "NOIRCIES", "noircit"), "worried"),
  ("Alors on essaie d'autres métaux. Plus tard, on en fabrique même en plomb. Ce qui n'est pas une très bonne idée.", S("DU PLOMB", "pas une très bonne idée"), "shocked"),
  ("Aujourd'hui, nos guirlandes sont en plastique brillant. Moins précieuses, mais beaucoup plus sûres.", S("DU PLASTIQUE", "moins précieux, plus sûr"), "serious"),
  CTA("TEAM GUIRLANDES", f"Chez toi, guirlandes ou pas ? {AL}")]),

 ("099-sainte-barbe", D(4), "🎄 Le 4 décembre, on sème du blé dans une soucoupe", GIFT,
  ["Wikipedia, Blé de la Sainte-Barbe", "Wikipedia, Sainte Barbe"], [
  ("Aujourd'hui, en Provence, on sème du blé dans des soucoupes. Pour savoir si l'année sera bonne.", V("Juste pour décorer ?", "PRÉSAGE", "bonne"), "curious"),
  ("C'est le blé de la Sainte-Barbe. Le 4 décembre, on pose des grains sur du coton mouillé, dans trois petites coupelles.", S("SAINTE-BARBE", "le 4 décembre"), "happy"),
  ("Si le blé pousse bien vert et bien droit pour Noël, la récolte sera bonne. S'il jaunit… mauvais signe.", V("Le blé jaunit ?", "MAUVAIS", "jaunit"), "worried"),
  ("Et sainte Barbe, c'est qui ? Selon la légende, son père l'enferme dans une tour, puis la tue parce qu'elle est chrétienne.", S("UNE TOUR", "et un père terrible"), "serious"),
  ("Juste après, il est frappé par la foudre. Voilà pourquoi elle protège tous ceux qui travaillent avec le feu.", V("Le père s'en sort ?", "FOUDROYÉ", "foudre"), "shocked"),
  ("Aujourd'hui, elle est la patronne des pompiers, des mineurs et des artificiers.", S("LES POMPIERS", "les mineurs, les artificiers"), "serious"),
  CTA("BLÉ DE NOËL", f"Tu vas essayer cette année ? {AL}")]),

 ("100-marche-strasbourg", D(5), "🎄 Le marché de Noël qui a remplacé saint Nicolas", GIFT,
  ["Strasbourg.eu, Histoire du Christkindelsmärik", "Wikipedia, Marché de Noël de Strasbourg"], [
  ("Le marché de Noël de Strasbourg existe depuis plus de quatre cent cinquante ans. Et il est né d'une dispute religieuse.", V("Une idée de commerçants ?", "RELIGION", "religieuse"), "curious"),
  ("Avant, à Strasbourg, il y avait un marché de la Saint-Nicolas, au début du mois de décembre.", S("SAINT-NICOLAS", "le marché d'avant"), "serious"),
  ("Mais la ville est devenue protestante. Et les protestants n'aiment pas trop qu'on fête les saints.", S("PROTESTANTS", "pas de fête des saints"), "angry"),
  ("Alors, en 1570, le marché est déplacé juste avant Noël. Et rebaptisé : le marché de l'Enfant Jésus.", Y(1570, "STRASBOURG", "1570"), "happy"),
  ("En alsacien, ça se dit Christkindelsmärik. C'est l'un des plus vieux marchés de Noël de France.", Q("CHRISTKINDELSMÄRIK", "— le marché de l'Enfant Jésus"), "smug"),
  ("Aujourd'hui, il attire des millions de visiteurs chaque hiver. Entre le vin chaud et les bredele.", S("DES MILLIONS", "de visiteurs chaque hiver"), "happy"),
  CTA("VIN CHAUD ?", f"Tu y es déjà allé ? {AL}")]),

 ("101-treize-desserts", D(6), "🎄 Pourquoi 13 desserts à Noël en Provence ?", CANE,
  ["Wikipedia, Treize desserts"], [
  ("En Provence, le soir de Noël, on ne mange pas un dessert. On en mange treize.", C(13, "DESSERTS", "LE SOIR DE NOËL", "treize"), "surprised"),
  ("Treize, comme Jésus et ses douze apôtres, réunis autour de la table.", S("JÉSUS + 12", "autour de la table"), "serious"),
  ("Parmi eux, les quatre mendiants : figues, amandes, raisins secs et noix. Leurs couleurs rappellent les robes de quatre ordres de moines.", S("4 MENDIANTS", "figues, amandes, raisins, noix"), "curious"),
  ("Il y a aussi le nougat blanc et le nougat noir, et la pompe à l'huile. Une brioche qu'il faut rompre avec les mains, jamais avec un couteau.", V("Avec un couteau ?", "INTERDIT", "couteau"), "smug"),
  ("Et on ne débarrasse pas la table tout de suite. La tradition veut qu'on laisse les desserts trois jours.", C(3, "JOURS", "SUR LA TABLE", "trois"), "happy"),
  ("Petite surprise : le chiffre treize ne s'est vraiment fixé qu'au début du vingtième siècle.", V("Une tradition millénaire ?", "RÉCENT", "vingtième"), "surprised"),
  CTA("13 DESSERTS", f"Toi, tu en manges combien ? {AL}")]),

 ("102-yule-lads", D(7), "🎄 En Islande, 13 trolls viennent à Noël", LANT,
  ["Wikipedia, Yule Lads", "Wikipedia, Grýla"], [
  ("En Islande, ce n'est pas un Père Noël qui passe. Ce sont treize trolls.", C(13, "TROLLS", "POUR NOËL", "treize"), "shocked"),
  ("On les appelle les Jólasveinar : les gars de Noël. Ils sont les fils de Grýla, une ogresse qui mange les enfants pas sages.", S("GRÝLA", "l'ogresse des montagnes"), "worried"),
  ("À partir du 12 décembre, ils descendent des montagnes, un par nuit. Et chacun a sa spécialité.", S("UN PAR NUIT", "à partir du 12 décembre"), "curious"),
  ("Il y a le lécheur de cuillères, le claqueur de portes, le voleur de saucisses. Et même celui qui renifle aux portes.", S("LE VOLEUR", "de saucisses"), "happy"),
  ("Les enfants posent une chaussure sur le rebord de la fenêtre. S'ils ont été sages, ils trouvent un bonbon. Sinon… une pomme de terre.", V("Toujours un bonbon ?", "PATATE", "pomme"), "smug"),
  ("Autrefois, ils faisaient vraiment peur. Aujourd'hui, ils portent souvent un costume rouge. Comme le Père Noël.", S("EN ROUGE", "comme le Père Noël"), "surprised"),
  CTA("13 TROLLS", f"Toi, tu aurais eu le bonbon ou la patate ? {AL}")]),

 ("103-fete-lumieres", D(8), "🎄 La fête des Lumières est née d'une averse", LANT,
  ["Wikipedia, Fête des Lumières", "Ville de Lyon, histoire de la fête du 8 décembre"], [
  ("La fête des Lumières de Lyon est née à cause de la pluie.", V("Prévue à l'avance ?", "LA PLUIE", "pluie"), "smug"),
  ("On est en 1852. Lyon doit inaugurer une statue de la Vierge Marie sur la colline de Fourvière.", Y(1852, "LYON", "1852"), "serious"),
  ("Mais le jour prévu, un violent orage éclate. La cérémonie est annulée, les feux d'artifice aussi.", V("La fête a lieu ?", "ANNULÉE", "annulée"), "worried"),
  ("Le soir, le ciel se dégage. Et spontanément, les Lyonnais posent des bougies sur le bord de leurs fenêtres.", S("DES BOUGIES", "à toutes les fenêtres"), "happy"),
  ("Toute la ville s'illumine. Et chaque 8 décembre, la tradition recommence.", S("8 DÉCEMBRE", "la ville s'illumine"), "happy"),
  ("Aujourd'hui, la fête attire jusqu'à deux millions de visiteurs. Mais beaucoup de Lyonnais mettent encore des lumignons à leurs fenêtres.", S("LES LUMIGNONS", "toujours aux fenêtres"), "curious"),
  CTA("LYON BRILLE", f"Ce soir, tu allumes une bougie ? {AL}")]),

 ("104-halifax", D(9), "🎄 Pourquoi le Canada offre un sapin à Boston", GIFT,
  ["Wikipedia, Halifax Explosion", "Government of Nova Scotia, Tree for Boston"], [
  ("Chaque année, le Canada offre un énorme sapin de Noël à la ville de Boston. Pour dire merci.", V("Un simple cadeau ?", "MERCI", "merci"), "curious"),
  ("Le 6 décembre 1917, dans le port d'Halifax, un cargo français chargé d'explosifs, le Mont-Blanc, entre en collision avec un autre navire.", Y(1917, "HALIFAX", "1917"), "serious"),
  ("Il prend feu. Puis il explose. C'est l'une des plus grosses explosions jamais provoquées par l'homme avant la bombe atomique.", V("Un simple incendie ?", "EXPLOSION", "explose"), "shocked"),
  ("Une partie de la ville est rasée. Environ deux mille morts, et des milliers de blessés.", C(2000, "MORTS", "À HALIFAX", "mille"), "worried"),
  ("Boston envoie aussitôt un train rempli de médecins, d'infirmières et de matériel, en pleine tempête de neige.", S("UN TRAIN", "de médecins et d'infirmières"), "serious"),
  ("L'année suivante, Halifax envoie un sapin pour remercier Boston. Et depuis 1971, c'est devenu une tradition chaque Noël.", S("UN SAPIN", "chaque année depuis 1971"), "happy"),
  CTA("MERCI BOSTON", f"Une belle histoire, non ? {AL}")]),

 ("105-rockefeller", D(10), "🎄 Le sapin le plus célèbre du monde est né sur un chantier", CANE,
  ["Rockefeller Center, History of the Christmas Tree", "Wikipedia, Rockefeller Center Christmas Tree"], [
  ("Le sapin de Noël le plus célèbre du monde, à New York, a été installé la première fois par des ouvriers. Sur un chantier.", V("Par la mairie ?", "OUVRIERS", "ouvriers"), "smug"),
  ("On est en 1931, en pleine crise économique. Des millions d'Américains ont perdu leur travail.", Y(1931, "NEW YORK", "1931"), "worried"),
  ("Sur le chantier du Rockefeller Center, les ouvriers ont au moins un emploi. Alors ils se cotisent pour acheter un sapin.", S("ILS SE COTISENT", "pour un sapin de chantier"), "happy"),
  ("Pas de boules de verre : ils le décorent avec des guirlandes en papier, des canneberges, et même des boîtes de conserve.", S("DES CONSERVES", "et des guirlandes en papier"), "surprised"),
  ("Deux ans plus tard, en 1933, le centre décide d'installer un sapin officiel. Et la tradition est lancée.", S("OFFICIEL", "depuis 1933"), "serious"),
  ("Aujourd'hui, il mesure souvent plus de vingt mètres, avec des dizaines de milliers de lumières. Et des millions de visiteurs viennent le voir.", C(20, "MÈTRES", "ET PLUS", "vingt"), "happy"),
  CTA("NEW YORK", f"Tu aimerais le voir en vrai ? {AL}")]),

 ("106-carte-noel", D(11), "🎄 La première carte de Noël a fait scandale", GIFT,
  ["Wikipedia, Christmas card (Henry Cole, 1843)"], [
  ("La toute première carte de Noël a fait scandale. À cause d'un enfant qui boit du vin.", V("Une carte sage ?", "SCANDALE", "scandale"), "smug"),
  ("On est à Londres, en 1843. Henry Cole a trop de lettres à écrire pour les fêtes.", Y(1843, "LONDRES", "1843"), "curious"),
  ("Alors il a une idée : faire imprimer une carte avec un message déjà écrit. Joyeux Noël et bonne année.", S("JOYEUX NOËL", "déjà imprimé"), "happy"),
  ("Un ami peintre dessine une famille qui lève son verre. Mais au milieu, un petit enfant boit lui aussi du vin.", V("Un enfant boit du vin ?", "CHOQUANT", "vin"), "shocked"),
  ("Certains sont choqués. Mais l'idée plaît. Environ mille cartes sont imprimées.", C(1000, "CARTES", "IMPRIMÉES", "mille"), "surprised"),
  ("Aujourd'hui, une de ces premières cartes peut se vendre plusieurs milliers d'euros aux enchères.", S("DES MILLIERS", "d'euros aux enchères"), "happy"),
  CTA("CARTE OU SMS ?", f"Toi, tu envoies encore des cartes ? {AL}")]),

 ("107-smog-londres", D(12), "🎄 Le brouillard qui a tué des milliers de Londoniens", LANT,
  ["Wikipedia, Great Smog of London", "Met Office, The Great Smog of 1952"], [
  ("En décembre 1952, un brouillard s'installe sur Londres. Et il va tuer des milliers de personnes.", V("Un simple brouillard ?", "MORTEL", "tuer"), "shocked"),
  ("Il fait froid. Tout le monde brûle du charbon pour se chauffer. Et il n'y a pas de vent.", S("DU CHARBON", "et pas un souffle de vent"), "worried"),
  ("La fumée reste coincée au-dessus de la ville. Un brouillard jaune et épais, qui sent le soufre.", Y(1952, "LONDRES", "fumée"), "serious"),
  ("On ne voit plus ses pieds. Les bus roulent guidés par des hommes à pied avec des torches. Dans les cinémas, on ne voit même plus l'écran.", S("ZÉRO VISIBILITÉ", "même dans les cinémas"), "surprised"),
  ("En cinq jours, au moins quatre mille personnes meurent. Et selon des études récentes, peut-être bien plus.", C(4000, "MORTS", "AU MOINS", "mille"), "worried"),
  ("Ce drame pousse le pays à voter une grande loi pour un air plus propre, en 1956.", S("AIR PROPRE", "loi de 1956"), "serious"),
  CTA("LE GRAND SMOG", f"Tu connaissais cette histoire ? {AL}")]),

 ("108-crackers", D(13), "🎄 Les crackers anglais sont nés à Paris", GIFT,
  ["Wikipedia, Christmas cracker (Tom Smith)"], [
  ("Les crackers de Noël, ces papillotes qui font pan chez les Anglais, ont été inspirés par… des bonbons français.", V("Une idée anglaise ?", "FRANÇAISE", "français"), "smug"),
  ("Dans les années 1840, un confiseur londonien, Tom Smith, visite Paris. Et il découvre des bonbons emballés dans du papier qu'on tortille.", Y(1840, "PARIS", "1840"), "curious"),
  ("De retour à Londres, il les vend avec un petit mot d'amour à l'intérieur. Ça marche bien. Mais il veut plus.", S("UN MOT D'AMOUR", "dans chaque papillote"), "happy"),
  ("Un soir, en entendant crépiter une bûche dans la cheminée, il a une idée : ajouter un petit pétard.", V("Juste un bonbon ?", "PAN !", "pétard"), "surprised"),
  ("Quand on tire à deux sur le papier, ça claque. Et le bonbon est bientôt remplacé par un petit cadeau et une couronne en papier.", S("UNE COURONNE", "en papier sur la tête"), "happy"),
  ("Aujourd'hui, au Royaume-Uni, on en ouvre des dizaines de millions chaque Noël.", S("DES MILLIONS", "chaque Noël au Royaume-Uni"), "curious"),
  CTA("PAN !", f"Tu as déjà ouvert un cracker ? {AL}")]),

 ("109-retraite-russie", D(14), "🎄 L'hiver qui a détruit l'armée de Napoléon", LANT,
  ["Wikipedia, Retraite de Russie", "Wikipedia, Campagne de Russie"], [
  ("En décembre 1812, l'hiver russe a presque entièrement détruit la plus grande armée d'Europe.", V("Vaincus au combat ?", "LE FROID", "russe"), "serious"),
  ("Napoléon est entré en Russie avec environ six cent mille hommes. Il a pris Moscou… mais la ville est vide, puis elle brûle.", C(600000, "SOLDATS", "ENTRÉS EN RUSSIE", "mille"), "worried"),
  ("Alors il ordonne la retraite. Et le froid arrive. Parfois moins trente degrés.", S("-30 °C", "pendant la retraite"), "shocked"),
  ("Les soldats n'ont plus de nourriture. Les chevaux meurent. Des hommes s'endorment dans la neige… et ne se réveillent pas.", V("Ils tiennent le coup ?", "GELÉS", "neige"), "worried"),
  ("Le 5 décembre, Napoléon quitte ce qui reste de son armée, et file vers Paris en traîneau.", Y(1812, "RUSSIE", "décembre"), "angry"),
  ("De cette immense armée, seules quelques dizaines de milliers d'hommes reviendront.", S("QUELQUES MILLIERS", "reviennent de Russie"), "serious"),
  CTA("HIVER 1812", f"Tu aurais survécu ? {AL}")]),

 ("110-pere-noel-magasin", D(15), "🎄 Le premier Père Noël de magasin", CANE,
  ["Wikipedia, James Edgar (Santa Claus)", "Old Colony History Museum, James Edgar"], [
  ("Le premier Père Noël de grand magasin, c'était un commerçant écossais. Qui avait juste envie de faire rire les enfants.", V("Un acteur payé ?", "LE PATRON", "commerçant"), "smug"),
  ("On est en 1890, à Brockton, près de Boston. James Edgar possède un grand magasin.", Y(1890, "BROCKTON", "1890"), "curious"),
  ("Pour Noël, il se fabrique un costume rouge, avec une grande barbe blanche, et il se promène dans son magasin.", S("BARBE BLANCHE", "et costume rouge"), "happy"),
  ("Les enfants n'en reviennent pas. Le Père Noël est là, en vrai ! Ils viennent de toute la région pour le voir.", V("Quelques curieux ?", "LA FOULE", "région"), "surprised"),
  ("Les autres magasins comprennent vite. Et partout, des Pères Noël s'installent dans les rayons.", S("PARTOUT", "des Pères Noël en magasin"), "happy"),
  ("Aujourd'hui, se faire prendre en photo sur ses genoux, c'est devenu une tradition dans le monde entier.", S("LA PHOTO", "sur les genoux du Père Noël"), "happy"),
  CTA("PHOTO ?", f"Toi, tu as une photo avec le Père Noël ? {AL}")]),

 ("111-beethoven", D(16), "🎄 Personne ne connaît l'anniversaire de Beethoven", LANT,
  ["Wikipedia, Ludwig van Beethoven", "Beethoven-Haus Bonn"], [
  ("Le jour de naissance de Beethoven ? Personne ne le connaît vraiment.", V("On connaît la date ?", "INCONNUE", "personne"), "curious"),
  ("Ce qu'on sait, c'est qu'il a été baptisé à Bonn, le 17 décembre 1770.", Y(1770, "BONN", "1770"), "serious"),
  ("À l'époque, on baptisait les bébés le lendemain de leur naissance. Alors on pense qu'il est né le 16 décembre. Mais aucune preuve.", S("16 DÉCEMBRE ?", "sans aucune preuve"), "curious"),
  ("Et le plus étrange : pendant longtemps, Beethoven lui-même pensait être né en 1772. Deux ans plus tard.", V("Il connaît son âge ?", "FAUX", "1772"), "surprised"),
  ("Selon certains biographes, son père l'aurait rajeuni pour le faire passer pour un enfant prodige, comme Mozart.", S("ENFANT PRODIGE", "comme Mozart"), "smug"),
  ("Plus tard, il devient sourd. Et il compose quand même certaines des plus grandes musiques de l'histoire.", S("SOURD", "et génial"), "serious"),
  CTA("BEETHOVEN", f"Tu connaissais ce mystère ? {AL}")]),

 ("112-freres-wright", D(17), "🎄 Le premier vol a duré 12 secondes", GIFT,
  ["Wikipedia, Wright Flyer", "Smithsonian National Air and Space Museum, 1903 Wright Flyer"], [
  ("Le premier vol d'un avion à moteur a duré douze secondes.", C(12, "SECONDES", "DE VOL", "douze"), "surprised"),
  ("Le 17 décembre 1903, aux États-Unis, sur une plage venteuse de Caroline du Nord.", Y(1903, "KITTY HAWK", "1903"), "curious"),
  ("Les frères Wright ne sont pas ingénieurs. Ils réparent… des vélos.", V("Des ingénieurs ?", "VÉLOS", "vélos"), "smug"),
  ("Orville s'allonge sur l'aile. L'avion décolle, et parcourt environ trente-six mètres. Moins que la longueur d'un avion de ligne aujourd'hui.", S("36 MÈTRES", "moins qu'un avion de ligne"), "surprised"),
  ("Ce jour-là, ils font quatre vols. Le dernier dure presque une minute.", S("4 VOLS", "le dernier, presque 1 minute"), "happy"),
  ("Soixante-six ans plus tard, des hommes marchent sur la Lune. Et un petit morceau de cet avion voyage avec eux.", V("Il est resté au musée ?", "LA LUNE", "lune"), "shocked"),
  CTA("DÉCOLLAGE", f"Tu aurais osé monter dedans ? {AL}")]),

 ("113-dickens", D(18), "🎄 Le conte de Noël écrit en six semaines", CANE,
  ["Wikipedia, A Christmas Carol", "Charles Dickens Museum, A Christmas Carol"], [
  ("L'histoire de Noël la plus célèbre du monde a été écrite en seulement six semaines. Par un auteur fauché.", V("Un auteur riche ?", "FAUCHÉ", "fauché"), "smug"),
  ("En 1843, Charles Dickens a des dettes. Son dernier livre se vend mal.", Y(1843, "LONDRES", "1843"), "worried"),
  ("Alors il écrit vite, très vite, l'histoire de Scrooge, un vieil avare visité par trois fantômes la nuit de Noël.", S("TROIS FANTÔMES", "et un vieil avare"), "curious"),
  ("Dickens paie lui-même l'impression. Avec une belle couverture, des dorures, des illustrations en couleur.", S("À SES FRAIS", "dorures et couleurs"), "serious"),
  ("Le livre sort le 19 décembre. Les six mille exemplaires sont vendus avant le soir de Noël.", C(6000, "EXEMPLAIRES", "VENDUS EN 5 JOURS", "mille"), "happy"),
  ("Mais le livre coûtait tellement cher à fabriquer que Dickens gagne beaucoup moins que prévu. Un vrai conte de Noël… à l'envers.", V("Il devient riche ?", "DÉÇU", "moins"), "surprised"),
  CTA("SCROOGE", f"Tu as déjà lu ou vu ce conte ? {AL}")]),

 ("114-couronnes-noel", D(19), "🎄 Les rois couronnés le jour de Noël", GIFT,
  ["Wikipedia, Couronnement de Charlemagne", "Wikipedia, Guillaume le Conquérant", "Wikipedia, Baptême de Clovis"], [
  ("Plusieurs grands rois ont été couronnés le jour de Noël. Et l'un d'eux a fini dans les flammes.", V("Une fête tranquille ?", "FLAMMES", "flammes"), "curious"),
  ("D'abord Clovis, roi des Francs, baptisé à Reims un jour de Noël. L'année exacte reste discutée.", S("CLOVIS", "baptisé à Reims, un 25 décembre"), "serious"),
  ("Puis Charlemagne. Le 25 décembre de l'an 800, à Rome, le pape le couronne empereur.", Y(800, "ROME", "800"), "smug"),
  ("Et le 25 décembre 1066, Guillaume le Conquérant est couronné roi d'Angleterre, à Westminster.", Y(1066, "WESTMINSTER", "1066"), "serious"),
  ("Mais pendant la cérémonie, on entend des cris de joie. Ses soldats normands croient à une attaque. Et ils mettent le feu aux maisons autour.", V("Une attaque ?", "PANIQUE", "attaque"), "shocked"),
  ("Les invités fuient l'église en plein couronnement. Un Noël qu'on n'oublie pas.", S("SAUVE QUI PEUT", "en plein couronnement"), "surprised"),
  CTA("COURONNÉS", f"Tu connaissais ces Noëls royaux ? {AL}")]),

 ("115-giotto-comete", D(20), "🎄 L'étoile de Noël peinte comme une comète", LANT,
  ["Wikipedia, Adoration des mages (Giotto)", "ESA, Giotto mission"], [
  ("Sur l'une des plus célèbres peintures de Noël, l'étoile des Rois mages est une comète.", V("Une étoile ?", "COMÈTE", "comète"), "curious"),
  ("Vers 1305, le peintre Giotto décore une chapelle à Padoue, en Italie. Et il peint l'adoration des mages.", Y(1305, "PADOUE", "1305"), "serious"),
  ("Au-dessus de l'étable, il ne peint pas une petite étoile. Mais une boule de feu avec une longue queue.", S("UNE QUEUE DE FEU", "au-dessus de l'étable"), "surprised"),
  ("Pourquoi ? Quelques années plus tôt, en 1301, une comète très brillante est passée dans le ciel. La comète de Halley.", S("HALLEY", "passée en 1301"), "smug"),
  ("Giotto l'a sûrement vue de ses propres yeux. Et elle l'a tellement marqué qu'il l'a peinte.", S("TÉMOIN", "Giotto l'a sans doute vue"), "happy"),
  ("En 1986, l'Europe envoie une sonde spatiale vers cette même comète. Son nom : Giotto.", V("Un nom au hasard ?", "GIOTTO", "nom"), "happy"),
  CTA("COMÈTE !", f"Tu as déjà vu une comète ? {AL}")]),

 ("116-tempete-1999", D(21), "🎄 La tempête qui a gâché le Noël 1999", LANT,
  ["Wikipedia, Tempêtes de fin décembre 1999", "Château de Versailles, la tempête de 1999"], [
  ("Juste après Noël 1999, deux tempêtes ont frappé la France en deux jours.", C(2, "TEMPÊTES", "EN DEUX JOURS", "deux"), "shocked"),
  ("Le 26 décembre, la tempête Lothar traverse le nord du pays. Le lendemain, la tempête Martin frappe le sud.", Y(1999, "FRANCE", "décembre"), "worried"),
  ("Des vents à plus de cent cinquante kilomètres heure. Des toits arrachés, des forêts entières couchées.", S("150 KM/H", "et parfois bien plus"), "shocked"),
  ("Des millions de foyers se retrouvent sans électricité. Certains pendant des semaines, en plein hiver.", V("Courant coupé une heure ?", "SEMAINES", "semaines"), "worried"),
  ("À Versailles, le parc du château perd plus de dix mille arbres. Certains plantés à l'époque des rois.", C(10000, "ARBRES", "PERDUS À VERSAILLES", "mille"), "serious"),
  ("Au total, quatre-vingt-douze morts en France. L'une des pires catastrophes naturelles du pays.", S("92 MORTS", "en France"), "serious"),
  CTA("DÉCEMBRE 1999", f"Tes parents s'en souviennent ? {AL}")]),

 ("117-amundsen", D(22), "🎄 La course au pôle Sud, perdue de 34 jours", LANT,
  ["Wikipedia, Expédition Amundsen", "Wikipedia, Expédition Terra Nova"], [
  ("En décembre 1911, une course mortelle se joue au pôle Sud. Et le perdant arrive trente-quatre jours trop tard.", C(34, "JOURS", "DE RETARD", "trente"), "serious"),
  ("D'un côté, le Norvégien Roald Amundsen, avec des chiens de traîneau. De l'autre, le Britannique Robert Scott, avec des poneys.", S("CHIENS / PONEYS", "Amundsen contre Scott"), "curious"),
  ("Le 14 décembre 1911, Amundsen atteint le pôle Sud. Il plante le drapeau norvégien, et laisse une tente.", Y(1911, "PÔLE SUD", "1911"), "happy"),
  ("Un mois plus tard, Scott arrive enfin. Et il découvre la tente, avec une lettre d'Amundsen.", V("Scott est premier ?", "DEUXIÈME", "tente"), "worried"),
  ("Le retour est terrible. Scott et ses quatre compagnons meurent dans le froid, à quelques kilomètres d'un dépôt de vivres.", S("À 18 KM", "d'un dépôt de vivres"), "shocked"),
  ("On retrouvera son journal. Ses derniers mots : pour l'amour de Dieu, prenez soin des nôtres.", Q("PRENEZ SOIN DES NÔTRES", "— Robert Scott, 1912"), "serious"),
  CTA("PÔLE SUD", f"Tu aurais choisi les chiens ou les poneys ? {AL}")]),

 ("118-animaux-parlent", D(23), "🎄 La nuit de Noël, les animaux parlent", LANT,
  ["Wikipedia, Christmas folklore (talking animals)", "Paul Sébillot, Le Folk-lore de France"], [
  ("Selon une vieille croyance, la nuit de Noël, à minuit, les animaux se mettent à parler.", V("Ils restent muets ?", "PARLENT", "parler"), "curious"),
  ("Dans les campagnes de France et d'Europe, on racontait qu'au moment de la messe de minuit, les bœufs et les ânes discutent dans l'étable.", S("MINUIT", "les bêtes discutent"), "happy"),
  ("Pourquoi eux ? Parce que, selon la tradition, un bœuf et un âne ont réchauffé l'Enfant Jésus dans la crèche.", S("LE BŒUF ET L'ÂNE", "les témoins de la crèche"), "serious"),
  ("Mais attention : il ne fallait surtout pas les écouter.", V("On peut écouter ?", "INTERDIT", "écouter"), "worried"),
  ("Une légende raconte l'histoire d'un fermier qui se cache dans l'étable. Et il entend ses bêtes dire qu'elles porteront bientôt son cercueil.", S("SON CERCUEIL", "porté par ses propres bêtes"), "shocked"),
  ("Alors cette nuit-là, on laissait les animaux tranquilles. Et on leur donnait même une ration en plus.", S("DOUBLE RATION", "pour la nuit de Noël"), "happy"),
  CTA("CHUT…", f"Toi, tu oserais écouter ton chat ? {AL}")]),

 ("119-mot-noel", D(24), "🎄 D'où vient le mot Noël ?", GIFT,
  ["CNRTL, étymologie de Noël", "Wikipedia, Noël"], [
  ("Le mot Noël, on le dit tous. Mais d'où vient-il vraiment ?", V("Un mot inventé ?", "LATIN", "vient"), "curious"),
  ("Il vient du latin natalis, qui veut dire : de la naissance. Le jour de la naissance de Jésus.", Q("NATALIS", "— de la naissance"), "serious"),
  ("Au Moyen Âge, Noël n'est pas seulement une fête. C'est aussi un cri de joie.", S("UN CRI DE JOIE", "au Moyen Âge"), "happy"),
  ("Quand un roi entre dans une ville, ou quand un prince naît, la foule crie : Noël ! Noël !", V("Pour Noël seulement ?", "PARTOUT", "foule"), "surprised"),
  ("Et dans d'autres langues, le nom est complètement différent. En anglais, Christmas, la messe du Christ. En allemand, Weihnachten, les nuits sacrées.", S("CHRISTMAS", "la messe du Christ"), "curious"),
  ("Ce soir, des millions de familles vont le dire. Joyeux Noël à toi, et à tous ceux que tu aimes.", S("JOYEUX NOËL", "à toi et aux tiens"), "happy"),
  CTA("JOYEUX NOËL", f"Joyeux réveillon ! {AL}")]),

 ("120-newton", D(25), "🎄 Isaac Newton est né le jour de Noël… ou pas", GIFT,
  ["Wikipedia, Isaac Newton", "Wikipedia, Calendrier julien"], [
  ("Isaac Newton est né le jour de Noël. Enfin… presque.", V("Né à Noël ?", "PRESQUE", "presque"), "smug"),
  ("Sur son acte, c'est écrit : 25 décembre 1642. En Angleterre.", Y(1642, "ANGLETERRE", "1642"), "curious"),
  ("Mais à l'époque, l'Angleterre utilise encore un vieux calendrier, le calendrier julien. Avec dix jours de décalage.", S("10 JOURS", "de décalage"), "serious"),
  ("Avec notre calendrier à nous, il est né le 4 janvier 1643. Pas à Noël, et même pas la même année.", V("Même année ?", "1643", "1643"), "surprised"),
  ("Et il a failli ne pas survivre. Il est né si petit que sa mère disait qu'il tenait dans un pot d'un litre.", S("UN POT", "d'un litre"), "worried"),
  ("Ce bébé fragile deviendra l'un des plus grands savants de l'histoire. Celui qui a expliqué la gravité.", S("LA GRAVITÉ", "et la lumière"), "happy"),
  CTA("JOYEUX NOËL", f"Joyeux Noël, Isaac ! {AL}")]),

 ("121-boxing-day", D(26), "🎄 Pourquoi les Anglais fêtent Boxing Day", GIFT,
  ["Wikipedia, Boxing Day"], [
  ("Le lendemain de Noël, les Anglais fêtent Boxing Day. Et ça n'a rien à voir avec la boxe.", V("Un jour de boxe ?", "NON", "boxe"), "smug"),
  ("Box, en anglais, ça veut dire boîte. Le jour des boîtes.", Q("BOX = BOÎTE", "— le jour des boîtes"), "curious"),
  ("Au dix-neuvième siècle, les domestiques travaillent le jour de Noël pour servir le repas de leurs maîtres.", S("DOMESTIQUES", "au travail le 25"), "serious"),
  ("Alors le 26, ils ont leur jour de congé. Et les maîtres leur donnent une boîte avec des cadeaux, de l'argent, des restes du repas.", S("UNE BOÎTE", "de cadeaux et de restes"), "happy"),
  ("Une autre explication : les boîtes des églises, où l'on récoltait des dons pour les pauvres, ouvertes juste après Noël.", S("LES DONS", "pour les pauvres"), "curious"),
  ("Aujourd'hui, c'est surtout un jour de soldes et de matchs de football.", V("Et les boîtes ?", "SOLDES", "soldes"), "surprised"),
  CTA("BOXING DAY", f"Toi, tu fais quoi le lendemain de Noël ? {AL}")]),

 ("122-pasteur", D(27), "🎄 Le garçon sauvé par Pasteur", CANE,
  ["Institut Pasteur, Joseph Meister", "Wikipedia, Louis Pasteur"], [
  ("Le 27 décembre 1822 naît Louis Pasteur. Et un jour, il va sauver un petit garçon que tout le monde croyait condamné.", Y(1822, "DOLE", "1822"), "serious"),
  ("En 1885, Joseph Meister, neuf ans, est mordu par un chien enragé. À l'époque, la rage tue presque à coup sûr.", V("Il peut guérir ?", "CONDAMNÉ", "rage"), "worried"),
  ("Sa mère l'emmène à Paris, chez Pasteur. Il travaille sur un vaccin, mais il ne l'a jamais testé sur un humain.", S("JAMAIS TESTÉ", "sur un humain"), "worried"),
  ("Pasteur prend le risque. Pendant dix jours, l'enfant reçoit des injections.", C(10, "JOURS", "D'INJECTIONS", "dix"), "serious"),
  ("Et Joseph survit. Le premier humain sauvé de la rage par un vaccin.", V("Il survit ?", "SAUVÉ", "survit"), "happy"),
  ("Devenu adulte, Joseph Meister travaillera toute sa vie à l'Institut Pasteur. Comme gardien.", S("GARDIEN", "de l'Institut Pasteur"), "happy"),
  CTA("MERCI PASTEUR", f"Tu connaissais cette histoire ? {AL}")]),

 ("123-cinema-lumiere", D(28), "🎄 La première séance de cinéma : 33 spectateurs", GIFT,
  ["Institut Lumière, la séance du 28 décembre 1895", "Wikipedia, L'Arrivée d'un train en gare de La Ciotat"], [
  ("Le 28 décembre 1895, a lieu la première séance de cinéma payante de l'histoire. Il y a seulement trente-trois spectateurs.", C(33, "SPECTATEURS", "SEULEMENT", "trente"), "surprised"),
  ("C'est à Paris, dans le sous-sol d'un café, boulevard des Capucines. Les frères Lumière présentent leur cinématographe.", Y(1895, "PARIS", "Paris"), "curious"),
  ("L'entrée coûte un franc. Au programme : dix petits films de moins d'une minute.", S("1 FRANC", "pour 10 petits films"), "happy"),
  ("On raconte que les spectateurs se sont enfuis en voyant un train arriver vers eux. Mais ce film n'était même pas au programme ce soir-là.", V("Ils ont fui le train ?", "LÉGENDE", "train"), "smug"),
  ("Le bouche-à-oreille fonctionne : quelques semaines plus tard, il y a des files d'attente dans la rue.", S("FILE D'ATTENTE", "devant le café"), "happy"),
  ("Pourtant, Louis Lumière aurait dit que le cinéma était une invention sans avenir.", Q("SANS AVENIR", "— attribué à Louis Lumière"), "surprised"),
  CTA("MOTEUR !", f"Toi, c'est quoi ton film de Noël préféré ? {AL}")]),

 ("124-sapin-electrique", D(29), "🎄 Le premier sapin électrique", CANE,
  ["Wikipedia, Christmas lights (Edward H. Johnson)"], [
  ("Avant l'électricité, on mettait de vraies bougies allumées dans les sapins. Et ça finissait parfois très mal.", V("Sans danger ?", "INCENDIE", "mal"), "worried"),
  ("En 1882, à New York, Edward Johnson travaille avec l'inventeur Thomas Edison.", Y(1882, "NEW YORK", "1882"), "curious"),
  ("Il a une idée folle : brancher des ampoules électriques sur son sapin. Quatre-vingts ampoules rouges, blanches et bleues, câblées à la main.", C(80, "AMPOULES", "CÂBLÉES À LA MAIN", "quatre"), "happy"),
  ("Et en plus, son sapin tourne sur lui-même grâce à un moteur.", V("Il reste immobile ?", "IL TOURNE", "tourne"), "surprised"),
  ("Un journaliste vient le voir, et en parle dans le journal. Mais pendant longtemps, les guirlandes électriques restent très chères.", S("TRÈS CHER", "réservé aux riches"), "serious"),
  ("Il faut attendre le vingtième siècle pour qu'elles entrent dans toutes les maisons. Et que les bougies quittent enfin les sapins.", S("ADIEU BOUGIES", "bonjour guirlandes"), "happy"),
  CTA("ÇA BRILLE", f"Chez toi, guirlande qui clignote ou fixe ? {AL}")]),

 ("125-raspoutine", D(30), "🎄 Raspoutine, l'homme qui ne voulait pas mourir", LANT,
  ["Wikipedia, Grigori Raspoutine", "Wikipedia, Félix Ioussoupov"], [
  ("Dans la nuit du 29 au 30 décembre 1916, des princes russes tentent d'assassiner Raspoutine. Et selon la légende, il ne veut pas mourir.", Y(1916, "PETROGRAD", "1916"), "serious"),
  ("Raspoutine est un moine mystérieux, très proche de la famille du tsar. Beaucoup le détestent.", S("RASPOUTINE", "le moine du tsar"), "curious"),
  ("Le prince Félix Ioussoupov l'invite chez lui. Il lui sert des gâteaux et du vin, empoisonnés au cyanure.", V("Le poison agit ?", "RIEN", "cyanure"), "shocked"),
  ("Selon le récit du prince, il ne se passe rien. Alors on lui tire dessus. Il tombe… puis il se relève et s'enfuit dans la cour.", S("IL SE RELÈVE", "selon le prince"), "shocked"),
  ("Il est abattu à nouveau, puis jeté dans le fleuve gelé.", V("Il est mort ?", "LE FLEUVE", "fleuve"), "worried"),
  ("Mais attention : l'autopsie n'aurait trouvé aucune trace de poison. Le prince a peut-être enjolivé son histoire.", S("AUCUN POISON ?", "selon l'autopsie"), "smug"),
  CTA("RASPOUTINE", f"Toi, tu crois la légende ? {AL}")]),

 ("126-bug-an-2000", D(31), "🎄 Le bug de l'an 2000 : la fin du monde qui n'est pas venue", GIFT,
  ["Wikipedia, Bug de l'an 2000"], [
  ("Le 31 décembre 1999, le monde entier avait peur que les ordinateurs s'arrêtent à minuit.", V("Une fête tranquille ?", "PANIQUE", "peur"), "worried"),
  ("Le problème : pour gagner de la place, beaucoup d'ordinateurs ne notaient l'année qu'avec deux chiffres. 99 pour 1999.", S("99 = 1999", "deux chiffres seulement"), "curious"),
  ("Alors à minuit, 99 devient 00. Et l'ordinateur risque de croire qu'on est revenu en 1900.", Y(1900, "RETOUR EN", "1900"), "surprised"),
  ("On imagine des avions qui tombent, des banques qui bloquent, des centrales en panne. Certains font même des réserves de nourriture.", S("DES RÉSERVES", "au cas où"), "worried"),
  ("Dans le monde, on dépense des centaines de milliards pour corriger les programmes.", S("DES MILLIARDS", "pour corriger le bug"), "serious"),
  ("Et à minuit… presque rien. Quelques petites pannes. Le travail avait payé.", V("Le chaos ?", "RIEN", "rien"), "happy"),
  CTA("BONNE ANNÉE", f"Bonne année à toi ! {AL}")]),
]
