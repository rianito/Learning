#include <stdio.h>

int main(void) {
  int notas[10];
  for(int i = 0; i < 10; i++){
    printf("Digite a nota do aluno %i: ",i);
    scanf("%i",&notas[i]);
  }
  
  for(int i = 0; i < 10; i++){
    if(notas[i] >= 5){
      printf("O aluno %i passou de ano.\n", i);
    }else{
      printf("O aluno %i não passou de ano.\n", i);
    }
  }
  return 0;
}