#include <stdio.h>
#include <stdlib.h>
#include <string.h>









int main(int argc, char const *argv[])
{
	FILE *dico;

	dico=fopen("french","r");
	if(dico==NULL){
		printf("Erreur d'ouverture du fichier");
		exit(1);
	}

	char mot[50];

	do{
		fscanf(dico,"%s",mot);
		printf("%s\n",mot );
	}while(!feof(dico));



	return 0;
}

/*

b d f k l m n p s t v z g ɲ(gn) r ʃ(ch) ʒ(je) 

a e i o u ø(eu) é ɑ(en) ɔ(on) ɛ(un)

*/