# Droit et utilisateurs
# Changement de permission

```
chmod o+rw nom_ fichier
```
# Types de droits
```
r = read = lire / afficher = 4
w = write = mofifier / écrire = 2
x = execute / accés = 1
```

# Différents groupes :
```
u = owner user
g = groupe
o = others
```
# chmod ugo+rwx exemple.txt
```
accorde les droits de lecture, de modification et d'exécution aux users, groups et autres sur le fichier exemple.txt.
```

# chmod go-rwx exemple.txt
```
enlève les droits de lecture, de modification et d'exécution aux groups et autres sur le fichier exemple.txt.
```

# plusieurs commande pour les utilisateurs et groupes uniquement sur ROOT (à privilégier) ou avec sudo
# commande adduser jean

```
créer un nouvel utilisateur "jean".
```
# commande addgroup linux

```
créer un nouveau groupe "linux"
```

# commande deluser jean

```
efface l'utilisateur "jean".
```
# commande delgroup linux

```
efface le groupe "linux"
```

# Création d'utilisateur et groupe 

```
-Créez un utilisateur nommé bill
su -

adduser bill

-Ajoutez le dans un groupe nommé microsoft

addgroup microsoft

-Créez un utilisateur nommé steve

adduser steve

-Ajoutez le dans un groupe nommé apple

adduser steve apple

-Créez un utilisateur nommé linus et un autre nommé ian

adduser linus
adduser ian

-Les ajouter au groupe linux.

adduser linus linux
adduser ian linus

-Quels sont les rôles des fichiers /etc/group, /etc/passwd et /etc/shadow ?

/etc/group : liste les groupes et leurs membres.
/etc/passwd : liste des dossier home des utilisateurs.
/etc/shadow : contient les mot de passe codé des utilisateurs.

-Connectez-vous en tant que ian avec la commande su et créez un fichier nommé je-suis-su.txt. Déconnectez-vous

su ian
touch je-suis-su.txt


-Connectez-vous en tant que ian avec la commande su - et créez un fichier nommé je-suis-su-tiret.txt. Déconnectez-vous

su - ian
touch je-suis-su-tiret.txt
exit

-Qu’observez-vous ? Où sont les deux fichiers créés ?

su ian : Il se trouve dans le dossier /home/user
su - ian : le fichier se trouve dans le dossier /home/ian

-Utilisez la commande suivante: sudo -u ian echo Bonjour >> fichier-ian.txt. À qui appartient ce fichier ? Réessayer en mettant la cible dans /tmp (/tmp/fichier----ian.txt) puis dans /home/ian.

pour chacune de ces commandes : voila l'erreur affichée : erreur : ian n'est pas dans le fichier des sudoers.

-Utilisez la commande suivante: sudo -u ian cp fichier-ian.txt copie-ian.txt. À qui appartient ce nouveau fichier ? Essayer de faire ces opérations dans le répertoire /home/ian.

erreur : ian n'est pas dans le fichier des sudoers
```

# remplacer un mot de passe

```
-Modifiez le mot de passe de linus et mettez: "8chats+caiLLou".

passwd linus
puis on rentre le nouveau mot de passe à la lettre (8chats+caiLLou).

-Désactivez l’utilisateur linus (il doit exister sur le système mais toute tentative de connexion en l’utilisant doit échouer).

usermod -L linus

-Réactivez l’utilisateur linus.

usermod -U linus

-Ajoutez-le au groupe des sudoers.

sudo usermod -aG sudo linus
Puis c'est ainsi que beaucoup de commande, notemment avec sudo, sont désormais possible chez ian.

-À quoi correspond la clef de salage ?

Cela permet de codé les mot de passe choisis pour qu'il devienne presque impossible pour les hackers de le déchiffrer.

-Utilisez ce résultat pour remplacer le mot de passe de linus dans le fichier /etc/shadow. Vérifiez que vous pouvez vous connecter.

une fois que nous sommes sur que les copies des fichiers /etc/shadows sont fais :
openssl passwd -6 "8chats+caiLLou" (par exemple)
pour vérifier le chagement : sudo nano /etc/shadow
```

# L'ACLs

```
-Mettez les droits correspondants aux groupes définis précédemment et correspondant à ces répertoires (le groupe apple n’a pas le droit d’aller lire ni écrire dans le répertoire windows par exemple).

dossier linux : appartient au groupe linux
dossier mac : appartient au groupe apple
dossier windows : appartient au groupe microsoft
il n’est pas demandé de changer le propriétaire du fichier (qui doit rester votre utilisateur par défaut)
setfacl -m g:linux:rwx linux
setfacl -m g:apple:rwx mac
setfacl -m g:microsoft:rwx windows

-Utiliser la commande setfacl pour permettre à linus (et uniquement lui) de lire et écrire dans le répertoire mac et ses sous-répertoires.

setfacl -R -m u:linus:rwx mac

-Utilisez la commande getfacl pour vérifier les droits affectés au fichier informatique/mac/sources/init.c

getfacl informatique/mac/sources/init.c

-Taper la commande sudo -u linus touch mac/sources/init.c. Que signifie cette commande ?

En tant que linus, on créer u fichier appelé init.c dans le dossier source du dossier mac.

-Taper la commande sudo -u bill touch mac/sources/init.c. Est-ce que le résultat est normal ?

résultat : permission non acordée
normal ? Oui car bill est dans le groupe microsoft, or se groupe n'as aucune permission sur le dossier mac.

-Taper la commande setfacl -Rb mac puis essayer à nouveau sudo -u linus touch mac/sources/init.c. Que s’est-il passé ?

la commande setfacl -Rb mac a remis les droits UNIX du dossier mac à zéro, rendant se dossier modifiable, exécutable et lisible pour tous.
Mais cela ne change pas le fait que linus ne peut n'as pas de permission dessus car il n'est pas du groupe apple ccar malgré cette commande, apple est toujours le propriétaire du dossier mac.

-Taper la commande setfacl -Rm u:linus:rwX mac puis créer le répertoire mac/bin. Quels sont les autorisations associées à ce dossier ? Est-ce normal ? Est-ce souhaité ?

Ici, Linus doit avoir tous les droits sur le dossier mac grâce à "setfacl -Rm u:linus:rwX mac". Mais si on garde le contexte que c'est le groupe apple doit toujours être proptiétaire de ce dossier, non ce n'est pas normal, mais si c'était volontaire, alors oui le résultat est tout à fait normal.

-Taper la commande setfacl -Rdm u:linus:rwX mac puis créer le répertoire mac/partage. Observer les autorisations associées à ce dossier. Que peut-on en conclure ?

setfacl -Rdm u:linus:rwX mac
mkdir mac/partage
getfacl mac/partage/
on constate que les droits "default" ont été créer et les permissions sont similaires à celles que nous avons apporté précédement.
Pour finir, supprimer les ACLs de tous les dossiers (mac, linux, windows).
sudo setfacl -Rb informatique/linux
sudo setfacl -Rb informatique/mac
sudo setfacl -Rb informatique/windows
```

# gestion des droits INUX

```
-Lancer la commande suivante: chmod 755 mac. Vérifier ses effets.

le dossier mac a bien comme permissions :
user = rwx
group = r-x
others = r-x
pour vérifier : getfacl mac

-Taper la commande sudo -u linus touch mac/jesuislinus. Que se passe-t-il ?

une erreur de permission se produit.

-Taper la commande sudo -u linus touch linux/jesuislinus. Que se passe-t-il ?

cela va créer un fichier jesuislinus dans le dossier linux. Se qui est normal car dans se dossier, linux a désormais les permissions les permissions.

-Taper la commande sudo -u linus touch windows/jesuislinus. Que se passe-t-il ?

une errer de permission se produit encore. se qui est encore normal.

-Créer le fichier windows/USER avec la commande touch windows/USER. Est-ce normal que le fichier existe ?

touch windows/mathis
oui parce qu'après avoir taper getfacl windows, j'ai remarqué que mathis a bien les droits pour cela.

-Supprimer le fichier windows/USER.

rm windows/mathis

-Taper la commande chown bill windows puis la commande touch windows/USER. Que se passe-t-il ? Est-ce normal ?

chown bill windows == bill devient le propriétaire du dossier windows.

Impossible de créer un nouveau fichier, ce qui est normal car maintenant c'est bill le main user du dossier wondows.

-Taper la commande chown linus linux.

-Taper la commande chown steve mac.

-Tenter de créer les fichiers windows/USER, mac/USER et linux/USER.

Cela est impossible par manque de permission.

-Ajouter USER au groupe linux et retenter de créer linux/USER.

adduser mathis linux
touch linux/mathis
impossible toujours par manque de permission.

-Ajouter USER au groupe mac (je pense apple au final car le groupe mac n'éxiste pas) et retenter de créer windows/USER, mac/USER et linux/USER.

adduser mathis mac
touch windows/mathis
touch mac/mathis
touch linux/mathis
les 3 créations de fichier ne fonctionnent pas encore par manque de permission.

-Ajouter USER au groupe microsoft et retenter de créer windows/USER.

adduser mathis microsoft
touch windows/mathis
Encore une fois, cela n'as pas marché à cause du même problème.

-Taper la commande sudo chmod g+w windows et retenter de créer windows/USER. Est-ce normal ?

sudo chmod g+w windows
touch windows/mathis
Oui c'est normal car le chmod taper a ajouter la possibilité de modifier/écrire pour les groupe dans le dossier windows.

-Déconnectez vous et retenter de créer windows/USER. Que s’est-il passé ? Dans quel autre cas avez-vous déjà dû vous déconnecter pour observer le changement de groupe effectif ?

lorsqu'on se reconnecte à nouveau, le fait que mathis fasse partie d'un certain groupe s'applique à cet instant là seulement et dans certain cas, cela peut petre possible lorsqu'on modifie simplement les droits d'un fichier/dossier.
```
