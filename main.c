#include <stdio.h>

int main() {
  FILE *file = fopen("dados.txt", "r");
  FILE *output = fopen("dados_formatados.csv", "w");

  if (file == NULL) {
    printf("Erro ao abrir o arquivo.\n");
    return 1;
  }

  for(char c = fgetc(file); c != EOF; c = fgetc(file)) {
    if (c == ',') {
      fputc('.', output);
    } else if (c == ' ') {
      char next = fgetc(file);
      if (next == ' ') {
        fputc(',', output);
      } else {
        fputc(c, output);
        if (next != EOF) {
          fputc(next, output);
        }
      }
    } else {
      fputc(c, output);
    }
  }
  // save the output only with the columns 1,2,3 and 4
  for (int i = 0; i < 4; i++) {
    char buffer[256];
    if (fgets(buffer, sizeof(buffer), output) != NULL) {
      fputs(buffer, stdout);
    }
  }
  fclose(output);
  fclose(file);
  return 0;
}
