lines_info = ['Bienvenue dans le jeu MOTUS !', 'Règles du jeu :','Tout d'+"'"+'abord, votre adversaire entrera un mot à l'  +
 "'" + 'endroit prévu, vous allez devoir deviner ce mot par la suite . Ce mot ne doit pas contenir de chiffre, ou tout autre caractère n'+"'" +'étant pas une lettre' ,
'Une fois ce mot choisi, il vous sera impossible de le changer', 'Pour tester un mot, entrez celui-ci dans l'+"'" + 'espace dédié à coté du boutton, et cliquez sur ce même boutton ' +"'" + 'Tester le mot' +"'",
'Une fois le mot entré, celui-ci s'+"'" +'affichera dans la grille', 'Si la case contenant une lettre devient rouge, c'+"'" +'est que cette lettre est juste et à la bonne place !',
'Si celle-ci devient jaune, cette lettre est bien dans le mot, mais mal placée ! Vous êtes proche du but ! ', 'Si au contraire, cette lettre reste blanche, c'+"'" +
'est que celle-ci n'+"'" +'est pas dans le mot recherché, dommage !','Vous avez 6 essais pour retrouver le mot de votre adversaire, sans quoi la défaite est imminente.','Bon Jeu !' ]
messagebox.showinfo("Règles du jeu", "\n\n".join(lines_info))