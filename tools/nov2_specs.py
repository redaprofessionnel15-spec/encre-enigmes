# 2e créneau quotidien (19 h) du 1er au 13 novembre 2026 : Halloween du 1er au 9, puis histoire insolite.
from xmas_specs import V, S, Y, C, Q, CTA

HALLO = {"hat": "tricorne", "coat": "black", "accessory": "lantern"}

SHORTS = [
 ("055-catacombes", "2026-11-01T19:00:00+01:00", "🎃 Six millions de morts sous Paris", HALLO,
  ["Paris Musées, Les Catacombes de Paris", "Wikipedia, Philibert Aspairt"], [
  ("Sous les rues de Paris, il y a plus de morts que de vivants au-dessus.", V("Juste des tunnels ?", "DES MORTS", "morts"), "shocked", {"on": "morts", "pose": "recoil", "mood": "shocked", "hold": 1.0}),
  ("À la fin du dix-huitième siècle, les cimetières de Paris débordent. Celui des Innocents empeste tout le quartier.", S("CIMETIÈRES PLEINS", "Paris, XVIIIe siècle"), "worried"),
  ("Alors, à partir de 1785, on déplace les ossements, la nuit, vers d'anciennes carrières sous la ville.", Y(1785, "PARIS", "1785"), "serious"),
  ("Les restes d'environ six millions de personnes y sont rangés. Des murs entiers de crânes et d'os.", C(6, "MILLIONS", "DE PARISIENS", "six"), "shocked"),
  ("Et en 1793, un portier, Philibert Aspairt, descend dans les galeries avec une bougie. Il ne remonte jamais.", S("PHILIBERT ASPAIRT", "disparu en 1793"), "worried"),
  ("On le retrouve onze ans plus tard. À quelques mètres seulement d'une sortie.", V("Si loin ?", "SI PRÈS", "mètres"), "sad"),
  CTA("TU DESCENDS ?", "Toi, tu oserais descendre ? Abonne-toi et laisse un like !")]),

 ("056-ankou", "2026-11-02T19:00:00+01:00", "🎃 L'Ankou, le faucheur de Bretagne", HALLO,
  ["Wikipedia, Ankou", "Anatole Le Braz, La Légende de la mort chez les Bretons armoricains"], [
  ("En Bretagne, si tu entends grincer une charrette la nuit, ne te retourne pas. C'est peut-être l'Ankou.", V("Une charrette ?", "L'ANKOU", "peut"), "worried"),
  ("L'Ankou, c'est le serviteur de la Mort. Un grand squelette, avec une faux, et un chapeau à larges bords.", S("L'ANKOU", "le serviteur de la Mort"), "serious"),
  ("Il passe dans les villages avec sa charrette, et il ramasse les âmes de ceux qui vont mourir.", S("SA CHARRETTE", "grince dans la nuit"), "worried"),
  ("Et qui devient l'Ankou ? Selon la légende, le dernier mort de l'année, dans chaque paroisse.", V("Qui le remplace ?", "LE DERNIER", "dernier"), "shocked"),
  ("Pendant un an, il fait la tournée. Puis il passe la faux au suivant.", C(1, "AN", "DE TOURNÉE", "an"), "serious"),
  ("Aujourd'hui encore, on peut voir l'Ankou sculpté dans de vieilles églises bretonnes. En ce jour des morts, il veille.", S("2 NOVEMBRE", "le jour des morts"), "curious"),
  CTA("NE TE RETOURNE PAS", "Tu connaissais l'Ankou ? Abonne-toi et laisse un like !")]),

 ("057-golem", "2026-11-03T19:00:00+01:00", "🎃 Le Golem de Prague dort-il encore au grenier ?", HALLO,
  ["Wikipedia, Golem de Prague", "Prague.eu, The Legend of the Golem"], [
  ("Dans le grenier d'une synagogue de Prague, une créature d'argile dormirait encore.", V("Une légende ?", "PEUT-ÊTRE", "dormirait"), "worried"),
  ("Au seizième siècle, selon la légende, le rabbin Loew veut protéger les habitants du quartier juif.", S("LE RABBIN LOEW", "Prague, XVIe siècle"), "serious"),
  ("Avec de l'argile de la rivière, il façonne un géant. Puis il lui donne vie avec un mot sacré : emet, la vérité.", S("EMET", "la vérité"), "curious"),
  ("Le Golem est fort, obéissant. Mais un jour, il devient incontrôlable et sème la destruction.", V("Toujours obéissant ?", "DÉCHAÎNÉ", "incontrôlable"), "shocked", {"on": "incontrôlable", "pose": "recoil", "mood": "shocked", "hold": 1.0}),
  ("Alors le rabbin efface une seule lettre. Emet devient met : la mort. Et le Golem retombe en poussière.", S("MET", "la mort"), "serious"),
  ("On dit que ses restes sont cachés dans le grenier de la synagogue Vieille-Nouvelle. Et que l'escalier a été retiré.", V("On peut monter ?", "INTERDIT", "retiré"), "worried"),
  CTA("TU MONTES ?", "Toi, tu monterais au grenier ? Abonne-toi et laisse un like !")]),

 ("058-toutankhamon", "2026-11-04T19:00:00+01:00", "🎃 La malédiction de Toutânkhamon", HALLO,
  ["Wikipedia, Curse of the pharaohs", "Wikipedia, Discovery of the tomb of Tutankhamun"], [
  ("Le 4 novembre 1922, en Égypte, on découvre une marche. Et cette marche mène au tombeau de Toutânkhamon.", Y(1922, "ÉGYPTE", "1922"), "surprised"),
  ("L'archéologue Howard Carter et son mécène, Lord Carnarvon, découvrent des trésors incroyables.", S("DES TRÉSORS", "Carter et Carnarvon"), "happy"),
  ("Mais quelques mois plus tard, Carnarvon meurt. Une piqûre de moustique infectée.", V("Un hasard ?", "MAUDIT ?", "meurt"), "shocked"),
  ("Les journaux s'emballent : c'est la malédiction du pharaon ! Ceux qui ouvrent le tombeau vont mourir.", S("LA MALÉDICTION", "selon les journaux"), "worried"),
  ("Sauf que Howard Carter, celui qui a ouvert le tombeau, a vécu encore seize ans.", C(16, "ANS", "DE PLUS POUR CARTER", "seize"), "smug"),
  ("La malédiction a surtout servi à vendre des journaux. Mais on en parle encore cent ans plus tard.", V("Une vraie malédiction ?", "INVENTÉE", "journaux"), "smug"),
  CTA("TU Y CROIS ?", "Et toi, tu y crois ? Abonne-toi et laisse un like !")]),

 ("059-enterres-vivants", "2026-11-05T19:00:00+01:00", "🎃 Les cercueils avec une cloche", HALLO,
  ["Wikipedia, Safety coffin", "Wikipedia, Premature burial"], [
  ("Au dix-neuvième siècle, des gens se faisaient enterrer avec une cloche. Au cas où ils se réveilleraient.", V("Une cloche ?", "AU CAS OÙ", "réveilleraient"), "shocked"),
  ("À l'époque, la peur d'être enterré vivant est partout. Les médecins ne savent pas toujours bien constater la mort.", S("ENTERRÉ VIVANT", "la grande peur du XIXe"), "worried"),
  ("Alors, des inventeurs déposent des brevets pour des cercueils de sécurité.", S("DES BREVETS", "cercueils de sécurité"), "curious"),
  ("Une ficelle relie la main du défunt à une cloche, au-dessus de la tombe. S'il bouge, la cloche sonne.", S("UNE FICELLE", "reliée à une cloche"), "surprised"),
  ("Certains modèles avaient même un tube pour respirer, ou une petite fenêtre.", V("Pour respirer ?", "UN TUBE", "tube"), "shocked"),
  ("Et non : l'expression sauvé par le gong ne vient pas de là. Elle vient de la boxe.", V("Le cimetière ?", "LA BOXE", "boxe"), "smug"),
  CTA("FLIPPANT ?", "Ça te fait flipper ? Abonne-toi et laisse un like !")]),

 ("060-dyatlov", "2026-11-06T19:00:00+01:00", "🎃 Le mystère du col Dyatlov", HALLO,
  ["Wikipedia, Dyatlov Pass incident", "Gaume et Puzrin, Communications Earth & Environment, 2021"], [
  ("En 1959, neuf randonneurs fuient leur tente en pleine nuit. Par moins vingt-cinq degrés. Certains pieds nus.", Y(1959, "OURAL", "1959"), "worried"),
  ("Ce sont des étudiants expérimentés, menés par Igor Dyatlov, dans les montagnes de l'Oural, en Russie.", S("IGOR DYATLOV", "monts Oural"), "serious"),
  ("Quand les secours arrivent, la tente est vide. Et elle a été découpée… de l'intérieur.", V("Ouverte normalement ?", "DÉCOUPÉE", "découpée"), "shocked"),
  ("Aucun d'eux n'a survécu. Pendant des décennies, on parle d'animaux, d'armes secrètes, et même d'extraterrestres.", S("TOUTES LES THÉORIES", "pendant 60 ans"), "sad"),
  ("En 2021, des scientifiques proposent une explication : une petite avalanche de plaque, tombée sur la tente.", S("UNE AVALANCHE", "selon une étude de 2021"), "curious"),
  ("Une explication solide. Mais certains détails restent troublants, et l'affaire divise encore.", V("Résolu ?", "PAS SÛR", "divise"), "serious"),
  CTA("TA THÉORIE ?", "Et toi, tu penses quoi ? Abonne-toi et laisse un like !")]),

 ("061-momies-chats", "2026-11-07T19:00:00+01:00", "🎃 Des momies de chats transformées en engrais", HALLO,
  ["Wikipedia, Animal mummy", "Liverpool Museums, Mummified cat (Beni Hasan)"], [
  ("En 1888, des milliers de momies de chats ont fini… dans des champs anglais. Comme engrais.", V("Au musée ?", "EN ENGRAIS", "engrais"), "shocked"),
  ("Tout commence en Égypte, à Beni Hassan. Un paysan creuse, et tombe sur un immense cimetière de chats.", S("BENI HASSAN", "Égypte, 1888"), "surprised"),
  ("Les Égyptiens anciens momifiaient des chats par milliers, en offrande à la déesse Bastet.", S("BASTET", "déesse à tête de chat"), "curious"),
  ("Mais en 1888, personne ne les protège. On en charge environ dix-neuf tonnes sur un bateau, direction Liverpool.", C(19, "TONNES", "DE CHATS MOMIFIÉS", "dix"), "shocked"),
  ("Là-bas, elles sont vendues aux enchères, broyées, et répandues dans les champs.", V("Conservées ?", "BROYÉES", "broyées"), "sad"),
  ("Seules quelques-unes ont été sauvées. On peut encore en voir dans des musées anglais.", S("QUELQUES-UNES", "sauvées dans des musées"), "serious"),
  CTA("TEAM CHAT ?", "Les chats méritaient mieux. Abonne-toi et laisse un like !")]),

 ("062-hollandais-volant", "2026-11-08T19:00:00+01:00", "🎃 Le Hollandais volant, le navire fantôme", HALLO,
  ["Wikipedia, Flying Dutchman", "The Cruise of HMS Bacchante, 1879-1882"], [
  ("Un futur roi d'Angleterre a noté dans un journal de bord qu'il avait vu un navire fantôme.", V("Un roi ?", "FANTÔME", "fantôme"), "surprised"),
  ("Ce navire, c'est le Hollandais volant. Selon la légende, il ne peut jamais rentrer au port.", S("HOLLANDAIS VOLANT", "le navire maudit"), "worried"),
  ("Son capitaine aurait juré de passer le cap de Bonne-Espérance, même s'il devait naviguer jusqu'au jugement dernier.", S("BONNE-ESPÉRANCE", "le serment du capitaine"), "angry"),
  ("Résultat : il est condamné à errer sur les mers. Pour toujours.", V("Rentré au port ?", "JAMAIS", "toujours"), "serious"),
  ("En 1881, à bord d'un navire de la Marine, le jeune prince George écrit qu'à quatre heures du matin, le Hollandais volant a croisé leur route.", Y(1881, "EN MER", "1881"), "surprised"),
  ("Pour les marins, le voir annonce un malheur. Et justement, ce jour-là, un matelot est tombé du mât.", V("Une coïncidence ?", "MALHEUR", "tombé"), "shocked"),
  CTA("TU Y CROIS ?", "Les navires fantômes, tu y crois ? Abonne-toi et laisse un like !")]),

 ("063-saint-germain", "2026-11-09T19:00:00+01:00", "🎃 Le comte qui se disait immortel", HALLO,
  ["Wikipedia, Comte de Saint-Germain", "Mémoires de Madame de Hausset"], [
  ("À la cour de Louis XV, un homme mystérieux laissait entendre qu'il avait plusieurs siècles.", V("Un simple noble ?", "IMMORTEL ?", "siècles"), "curious"),
  ("On l'appelle le comte de Saint-Germain. Personne ne sait d'où il vient, ni quel est son vrai nom.", S("SAINT-GERMAIN", "un comte sans passé"), "serious"),
  ("Il parle une dizaine de langues, joue du violon, et raconte des scènes d'histoire comme s'il les avait vécues.", S("COMME S'IL Y ÉTAIT", "des siècles de souvenirs"), "surprised"),
  ("On dit qu'il ne mange jamais en public, et qu'il connaît le secret de l'élixir de longue vie.", V("Il mange ?", "JAMAIS", "jamais"), "smug"),
  ("Il meurt officiellement en 1784, en Allemagne.", Y(1784, "ALLEMAGNE", "1784"), "sad"),
  ("Mais pendant des années, des témoins affirment l'avoir revu. Bien vivant.", V("Mort ?", "REVU", "revu"), "shocked", {"on": "vivant", "pose": "recoil", "mood": "shocked", "hold": 1.0}),
  CTA("IMMORTEL ?", "Fin d'Halloween ! Abonne-toi et laisse un like !")]),

 ("064-truie-falaise", "2026-11-10T19:00:00+01:00", "Le cochon condamné à mort par un tribunal", {"hat": "detective", "coat": "brown", "accessory": "magnifier"},
  ["Michel Pastoureau, Le Cochon, histoire d'un cousin mal aimé", "Wikipedia, Procès d'animaux"], [
  ("En 1386, en Normandie, une truie a été jugée par un tribunal. Et condamnée à mort.", V("Un procès ?", "COUPABLE", "condamnée"), "shocked"),
  ("Ça se passe à Falaise. La truie est accusée d'avoir blessé mortellement un bébé.", Y(1386, "FALAISE", "falaise"), "serious"),
  ("Il y a un vrai procès, avec un juge. Et elle est déclarée coupable.", S("UN VRAI PROCÈS", "avec un juge"), "serious"),
  ("Pour l'exécution, on l'habille avec des vêtements humains : une veste, des culottes, et des gants.", V("Une truie ?", "HABILLÉE", "vêtements"), "surprised"),
  ("Au Moyen Âge, ce n'est pas un cas isolé. Les historiens ont retrouvé des dizaines de procès d'animaux en Europe.", S("DES DIZAINES", "de procès d'animaux"), "curious"),
  ("Des cochons, des chiens, et même des insectes. Ils avaient parfois droit à un avocat.", V("Un avocat ?", "OUI", "avocat"), "smug"),
  CTA("JUSTICE ?", "Tu trouves ça juste ? Abonne-toi et laisse un like !")]),

 ("065-trebuchon", "2026-11-11T19:00:00+01:00", "Le dernier soldat français mort, 15 minutes avant la paix", {"hat": "tricorne", "coat": "navy", "accessory": "lantern"},
  ["Gouvernement français, Qui était Augustin Trébuchon ?", "Western Front Association, 11 November 1918"], [
  ("Le 11 novembre 1918, la guerre doit s'arrêter à onze heures. Augustin Trébuchon meurt à dix heures quarante-cinq.", V("La paix ?", "15 MINUTES", "quarante"), "sad"),
  ("L'armistice est signé à l'aube. Mais le cessez-le-feu n'est prévu qu'à onze heures. Les combats continuent.", S("ONZE HEURES", "11 novembre 1918"), "serious"),
  ("Augustin est berger en Lozère. Soldat de première classe, il est estafette : il porte les messages.", S("AUGUSTIN TRÉBUCHON", "berger de Lozère"), "serious"),
  ("Ce matin-là, près de Vrigne-Meuse, il court porter un message aux soldats. Le message dit : soupe à onze heures trente.", Q("SOUPE À 11 H 30", "— le dernier message"), "sad"),
  ("Il est touché par une balle. Il meurt quinze minutes avant la fin de la guerre.", C(15, "MINUTES", "AVANT L'ARMISTICE", "quinze"), "sad"),
  ("Plus tard, sur sa tombe, on écrira le 10 novembre. Comme si l'armée ne voulait pas avouer des morts le jour de la paix.", V("Le 11 ?", "LE 10", "novembre"), "serious"),
  CTA("NE PAS OUBLIER", "Aujourd'hui, on se souvient. Abonne-toi et laisse un like pour ne pas oublier.")]),

 ("066-louis-xix", "2026-11-12T19:00:00+01:00", "Le roi de France qui a régné 20 minutes", {"hat": "crown", "coat": "navy", "accessory": "spyglass"},
  ["Wikipedia, Louis-Antoine d'Artois (Louis XIX)", "Wikipedia, Révolution de Juillet"], [
  ("La France aurait eu un roi qui a régné vingt minutes. Il s'appelait Louis dix-neuf.", V("Un vrai règne ?", "20 MINUTES", "vingt"), "smug"),
  ("On est en 1830. Paris se soulève : c'est la révolution de Juillet.", Y(1830, "PARIS", "1830"), "serious"),
  ("Le roi Charles dix comprend qu'il a perdu. Le 2 août, il signe son abdication.", S("CHARLES X", "abdique le 2 août"), "sad"),
  ("Son fils, Louis-Antoine, devient alors roi, en théorie. Mais il hésite.", S("LOUIS-ANTOINE", "roi en théorie"), "worried"),
  ("Une vingtaine de minutes plus tard, il signe à son tour. Il renonce au trône.", C(20, "MINUTES", "DE RÈGNE", "vingtaine"), "surprised"),
  ("Alors, a-t-il vraiment été roi ? Les historiens en débattent encore. Mais ses partisans l'ont toujours appelé Louis dix-neuf.", V("Un vrai roi ?", "DÉBAT", "débattent"), "curious"),
  CTA("ROI OU PAS ?", "Pour toi, roi ou pas roi ? Abonne-toi et laisse un like !")]),

 ("067-facteur-cheval", "2026-11-13T19:00:00+01:00", "Le facteur qui a construit un palais avec des cailloux", {"hat": "beret", "coat": "green", "accessory": "lantern"},
  ["Palais idéal du facteur Cheval, histoire", "Wikipedia, Palais idéal du facteur Cheval"], [
  ("Un facteur français a construit un palais entier, tout seul, avec des cailloux ramassés pendant sa tournée.", V("Tout seul ?", "33 ANS", "seul"), "surprised"),
  ("Il s'appelle Ferdinand Cheval. Il est facteur dans la Drôme, et fait trente kilomètres à pied par jour.", S("FERDINAND CHEVAL", "facteur dans la Drôme"), "curious"),
  ("En 1879, il trébuche sur une pierre à la forme étrange. Et il a une idée folle.", Y(1879, "HAUTERIVES", "1879"), "surprised"),
  ("Chaque jour, il ramasse des pierres pendant sa tournée. Le soir, il construit. À la lueur d'une lampe.", S("LA NUIT", "à la lueur d'une lampe"), "serious"),
  ("Les voisins se moquent de lui. Ils le prennent pour un fou.", V("Un génie ?", "UN FOU ?", "fou"), "sad"),
  ("Trente-trois ans plus tard, son Palais idéal est terminé. Aujourd'hui, c'est un monument historique, visité par des milliers de gens.", C(33, "ANS", "DE TRAVAIL", "trente"), "happy", {"on": "terminé", "pose": "cheer", "hold": 1.0}),
  CTA("RESPECT", "Respect au facteur Cheval. Abonne-toi et laisse un like !")]),
]
